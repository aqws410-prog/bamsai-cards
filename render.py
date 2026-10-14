#!/usr/bin/env python3
"""밤사이 카드 렌더러.

사용법:
  python3 render.py posts/2026-10-15          # posts/2026-10-15/src/1~6.html → posts/2026-10-15/1~6.jpg
  python3 render.py template/example --out /tmp/preview   # 미리보기

- 각 HTML은 1080x1350(인스타 4:5 세로형), 폰트는 로컬(Noto Sans CJK KR)만 사용.
- 결과는 JPG(품질 88)로 저장해 저장소 용량을 줄인다.
"""
import argparse, pathlib, sys
from playwright.sync_api import sync_playwright

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--out")
    ap.add_argument("--sheet", help="6장을 이어 붙인 미리보기 저장 경로(커밋하지 말 것)")
    a = ap.parse_args()
    folder = pathlib.Path(a.folder).resolve()
    src = folder / "src" if (folder / "src").is_dir() else folder
    out = pathlib.Path(a.out).resolve() if a.out else folder
    out.mkdir(parents=True, exist_ok=True)
    pages = sorted(src.glob("[0-9].html"), key=lambda p: int(p.stem))
    if not pages:
        sys.exit(f"HTML 카드가 없습니다: {src}")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for f in pages:
            pg.goto(f.as_uri())
            pg.wait_for_load_state("networkidle")
            pg.evaluate("document.fonts.ready")
            dst = out / f"{f.stem}.jpg"
            pg.screenshot(path=str(dst), type="jpeg", quality=88,
                          clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            print(dst, dst.stat().st_size // 1024, "KB")
        b.close()
    if a.sheet:
        from PIL import Image
        ims = [Image.open(out / f"{f.stem}.jpg") for f in pages]
        w = 540
        h = int(w * 1350 / 1080)
        sheet = Image.new("RGB", (w * 3, h * ((len(ims) + 2) // 3)), "white")
        for k, im in enumerate(ims):
            sheet.paste(im.resize((w, h)), ((k % 3) * w, (k // 3) * h))
        sheet.save(a.sheet, quality=85)
        print("미리보기:", a.sheet)

if __name__ == "__main__":
    main()
