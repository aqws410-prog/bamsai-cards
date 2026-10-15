#!/usr/bin/env python3
"""밤사이 릴스 제작기.

사용법:
  python3 reel/make_reel.py posts/2026-10-15                # posts/2026-10-15/reel/scenes.py → posts/2026-10-15/reel.mp4
  python3 reel/make_reel.py posts/2026-10-15 --sheet /tmp/reel_sheet.jpg --stills /tmp/reel_stills.jpg   # + 검수용(UI 표시) / 보고용(깨끗한) 시트
  python3 reel/make_reel.py reel/formats/news --out /tmp/news.mp4          # 기준 예시 다시 만들기

scenes.py 가 정의할 것: S[n] = (아무 숫자, page(...)), PLAN[n] = (화면 길이 초, 재생 배속), CUES = [(장면, 시각, 효과음, 볼륨), ...]
- 장면 길이 합계에서 전환(0.25초 × 장면 수-1)을 뺀 것이 영상 길이.
- CUES의 시각은 HTML 애니메이션 delay와 같은 기준(배속 적용 전). 배속은 자동으로 반영된다.
"""
import argparse, importlib.util, pathlib, shutil, subprocess, sys, tempfile
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from audio import SFX, theme, write, SR, sfx_steps, sfx_snore, sfx_check  # noqa: E402

FPS, XF = 30, 0.25

SPECIAL = {"SNORE": lambda: sfx_snore(1.6), "SNORE_SHORT": lambda: sfx_snore(1.4),
           "STEPS_SLOW": lambda: sfx_steps(2.4, 8), "STEPS_FAST": lambda: sfx_steps(2.0, 12),
           "CHECK1": lambda: sfx_check(76), "CHECK2": lambda: sfx_check(79), "CHECK3": lambda: sfx_check(84)}

def load_scenes(folder):
    f = folder / "reel" / "scenes.py"
    if not f.exists():
        f = folder / "scenes.py"
    spec = importlib.util.spec_from_file_location("scenes", f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    keys = sorted(m.S)
    return [m.S[k][1] for k in keys], [m.PLAN[k] for k in keys], m.CUES

def render_video(htmls, plan, work):
    from playwright.sync_api import sync_playwright
    clips = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for n, (html, (dur, k)) in enumerate(zip(htmls, plan), 1):
            hf = work / f"{n}.html"; hf.write_text(html, encoding="utf-8")
            fd = work / f"f{n}"; fd.mkdir()
            pg.goto(hf.as_uri()); pg.wait_for_load_state("load"); pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150); pg.evaluate("seek(0)")
            for i in range(int(round(dur * FPS))):
                pg.evaluate(f"seek({i / FPS * k})")
                pg.screenshot(path=str(fd / f"{i:04d}.jpg"), type="jpeg", quality=92)
            clip = work / f"{n}.mp4"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(fd / "%04d.jpg"),
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", str(clip)], check=True)
            clips.append((clip, dur)); print(f"장면 {n}: {dur}초")
        b.close()
    inputs, filt, last, off = [], [], "0:v", 0.0
    for c, _ in clips: inputs += ["-i", str(c)]
    for i in range(1, len(clips)):
        off += clips[i - 1][1] - XF
        filt.append(f"[{last}][{i}:v]xfade=transition=slideleft:duration={XF}:offset={off:.3f}[v{i}]"); last = f"v{i}"
    out = work / "silent.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(filt), "-map", f"[{last}]",
                    "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "22", "-r", str(FPS),
                    "-g", "60", "-maxrate", "4M", "-bufsize", "8M", str(out)], check=True)
    return out

def build_audio(plan, cues):
    dur = [d for d, _ in plan]; K = [k for _, k in plan]
    start = [sum(dur[:i]) - XF * i for i in range(len(dur))]
    total = sum(dur) - XF * (len(dur) - 1); n = int(total * SR)
    music = theme(total)[:n]; fx = np.zeros(n)
    for sc, t, name, g in cues:
        x = (SPECIAL[name]() if name in SPECIAL else SFX[name]()) * g
        f = min(len(x), int(.004 * SR)); x[:f] *= np.linspace(0, 1, f)
        i = int((start[sc - 1] + t / K[sc - 1]) * SR)
        if i >= n: continue
        j = min(n, i + len(x)); fx[i:j] += x[:j - i]
    envf = np.convolve(np.abs(fx), np.ones(2205) / 2205, mode="same")
    mix = music * .55 * (1 - .45 * np.clip(envf / .08, 0, 1)) + fx * .8
    peak = np.max(np.abs(mix))
    return mix / peak * .89 if peak > .89 else mix

def ui_sheet(htmls, plan, path):
    """각 장면 마지막 화면에 인스타 UI(상단·오른쪽 버튼·하단 캡션)를 얹어 가림 여부를 확인하는 미리보기."""
    from playwright.sync_api import sync_playwright
    from PIL import Image, ImageDraw
    work = pathlib.Path(tempfile.mkdtemp()); ims = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for n, (html, (dur, k)) in enumerate(zip(htmls, plan), 1):
            hf = work / f"{n}.html"; hf.write_text(html, encoding="utf-8")
            pg.goto(hf.as_uri()); pg.wait_for_load_state("load"); pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150); pg.evaluate("seek(0)"); pg.evaluate(f"seek({(dur - .1) * k})")
            png = work / f"{n}.png"; pg.screenshot(path=str(png))
            im = Image.open(png).convert("RGBA"); o = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(o)
            P = (255, 0, 80, 70)
            d.rectangle((0, 0, 1080, 230), fill=P)          # 상단: 뒤로가기·카메라
            d.rectangle((0, 0, 50, 1920), fill=P); d.rectangle((1030, 0, 1080, 1920), fill=P)  # 긴 화면에서 잘리는 양옆
            d.rectangle((920, 1110, 1030, 1680), fill=P)    # 오른쪽 좋아요·댓글·공유 버튼
            d.rectangle((0, 1560, 1080, 1920), fill=P)      # 하단: 아이디·캡션
            ims.append(Image.alpha_composite(im, o).convert("RGB"))
        b.close()
    w, h = 360, 640; sheet = Image.new("RGB", (w * 3, h * ((len(ims) + 2) // 3)), "white")
    for i, im in enumerate(ims): sheet.paste(im.resize((w, h)), ((i % 3) * w, (i // 3) * h))
    sheet.save(path, quality=88); shutil.rmtree(work, ignore_errors=True)
    print("검수 미리보기:", path, "(분홍 영역 = 인스타 UI가 덮는 곳. 글자·캐릭터가 들어가면 안 됨)")

def stills_sheet(htmls, plan, path):
    """장면별 마지막 화면을 UI 표시 없이 깨끗하게 모은 시트(사용자 보고용, 장면 번호 표기)."""
    from playwright.sync_api import sync_playwright
    from PIL import Image, ImageDraw, ImageFont
    work = pathlib.Path(tempfile.mkdtemp()); ims = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for n, (html, (dur, k)) in enumerate(zip(htmls, plan), 1):
            hf = work / f"{n}.html"; hf.write_text(html, encoding="utf-8")
            pg.goto(hf.as_uri()); pg.wait_for_load_state("load"); pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150); pg.evaluate("seek(0)"); pg.evaluate(f"seek({(dur - .1) * k})")
            png = work / f"{n}.png"; pg.screenshot(path=str(png)); ims.append(Image.open(png).convert("RGB"))
        b.close()
    F = ImageFont.truetype(str(HERE / "fonts/Jua-Regular.ttf"), 34)
    w, h, pad = 540, 960, 56; cols = 3; rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols + 1) * 16, rows * (h + pad) + 16), "#FFFBF4"); d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        x = 16 + (i % cols) * (w + 16); y = 16 + (i // cols) * (h + pad)
        d.text((x + 4, y + 6), f"장면 {i+1}", font=F, fill="#4A3838"); sheet.paste(im.resize((w, h)), (x, y + pad - 6))
    sheet.save(path, quality=90); shutil.rmtree(work, ignore_errors=True)
    print("정지 화면 시트:", path)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("--out"); ap.add_argument("--sheet")
    ap.add_argument("--sheet-only", action="store_true")
    ap.add_argument("--stills", help="장면별 깨끗한 정지 화면 시트 경로(사용자 보고용)")
    a = ap.parse_args()
    folder = pathlib.Path(a.folder).resolve()
    htmls, plan, cues = load_scenes(folder)
    if a.sheet: ui_sheet(htmls, plan, a.sheet)
    if a.stills: stills_sheet(htmls, plan, a.stills)
    if a.sheet_only: return
    out = pathlib.Path(a.out).resolve() if a.out else folder / "reel.mp4"
    work = pathlib.Path(tempfile.mkdtemp())
    try:
        silent = render_video(htmls, plan, work)
        wav = work / "mix.wav"; write(wav, build_audio(plan, cues))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent), "-i", str(wav), "-map", "0:v", "-map", "1:a",
                        "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "44100", "-c:a", "aac", "-b:a", "128k",
                        "-shortest", "-movflags", "+faststart", str(out)], check=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    size = out.stat().st_size / 1e6
    total = sum(d for d, _ in plan) - XF * (len(plan) - 1)
    print(f"완성: {out} ({total:.1f}초, {size:.1f}MB)")

if __name__ == "__main__":
    main()
