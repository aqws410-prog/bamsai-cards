"""밤사이 릴스 공통 라이브러리 — 스타일(CSS), 말풍선·내레이션·효과음 글자 등 부품.

장면 파일(posts/<날짜>/reel/scenes.py)에서 `from lib import *` 로 가져다 쓴다.
좌표계는 1080x1920 기준이며, page()가 내용 전체를 인스타 안전 영역(가로 60~919, 세로 240~1520)으로 줄여 배치한다."""
import pathlib, random
from chars import mascot, chip, mini, p_card, p_paper, p_mag, p_tablet, L

HERE = pathlib.Path(__file__).parent
FONT = (HERE / "fonts").resolve().as_uri()

CSS = f"""
@font-face{{font-family:'Jua';src:url('{FONT}/Jua-Regular.ttf')}}
html,body{{margin:0;padding:0}}
body{{width:1080px;height:1920px;overflow:hidden;word-break:keep-all;font-family:'Jua','Noto Sans CJK KR',sans-serif;color:{L};-webkit-font-smoothing:antialiased}}
.stage{{position:relative;width:1080px;height:1920px;overflow:hidden}}
.safe{{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:0 0;transform:translate(21.5px,136.75px) scale(.875)}}
.abs{{position:absolute}}
.head{{position:absolute;left:44px;right:54px;top:118px;display:flex;justify-content:space-between;align-items:center;font-size:34px}}
.head .dot{{display:inline-block;width:16px;height:16px;border-radius:8px;background:#FFB27F;margin-right:12px;vertical-align:middle}}
.prog{{display:flex;gap:8px}}.prog i{{display:block;width:30px;height:8px;border-radius:4px;background:currentColor;opacity:.25}}.prog i.on{{opacity:1;background:#FFB27F}}
.hook{{line-height:1.2;letter-spacing:-0.01em}}
.panel{{position:absolute;border:5px solid {L};border-radius:34px;overflow:hidden;box-shadow:0 8px 0 rgba(0,0,0,.18)}}
.nar{{position:absolute;background:#FFF0B3;border:4px solid {L};padding:10px 22px;border-radius:16px;font-size:38px;line-height:1.35}}
.bub{{position:absolute;background:#fff;border:4px solid {L};border-radius:44px;padding:20px 30px;font-size:42px;line-height:1.3;text-align:center}}
.bub b{{color:#E8590C;font-weight:400}} .nar b{{color:#E8590C;font-weight:400}}
.tail{{position:absolute;width:26px;height:26px;background:inherit;border-right:4px solid {L};border-bottom:4px solid {L}}}
.t-down{{bottom:-17px;transform:rotate(45deg)}} .t-up{{top:-17px;transform:rotate(-135deg)}}
.t-left{{left:-17px;transform:rotate(135deg)}} .t-right{{right:-17px;transform:rotate(-45deg)}}
.think{{position:absolute;background:#fff;border:4px solid {L};border-radius:70px;padding:22px 32px;font-size:40px;line-height:1.3;text-align:center}}
.sfx{{position:absolute;color:#fff;-webkit-text-stroke:9px {L};paint-order:stroke fill}}
.tag{{position:absolute;background:{L};color:#FFF6EA;font-size:30px;padding:6px 18px;border-radius:999px}}
.num{{position:absolute;background:#fff;border:4px solid {L};border-radius:24px;padding:12px 24px;box-shadow:0 5px 0 rgba(0,0,0,.15)}}
.num .k{{font-size:30px}} .num .v{{font-size:56px;color:#2F6BD8}}
.src{{position:absolute;left:44px;right:54px;font-family:'Noto Sans CJK KR',sans-serif;font-size:23px;line-height:1.5;opacity:.85}}
.wave{{transform-box:fill-box;transform-origin:20% 90%;animation:wave .7s ease-in-out infinite alternate}}
@keyframes pop{{0%{{opacity:0;transform:scale(.5)}}70%{{opacity:1;transform:scale(1.05)}}100%{{opacity:1;transform:scale(1)}}}}
@keyframes rise{{0%{{opacity:0;transform:translateY(50px)}}100%{{opacity:1;transform:none}}}}
@keyframes fade{{0%{{opacity:0}}100%{{opacity:1}}}}
@keyframes slideL{{0%{{opacity:0;transform:translateX(-160px)}}100%{{opacity:1;transform:none}}}}
@keyframes slideR{{0%{{opacity:0;transform:translateX(160px)}}100%{{opacity:1;transform:none}}}}
@keyframes drop{{0%{{opacity:0;transform:translateY(-70px)}}70%{{opacity:1;transform:translateY(6px)}}100%{{opacity:1;transform:none}}}}
@keyframes squish{{0%,100%{{transform:scale(1,1)}}50%{{transform:scale(1.04,.95)}}}}
@keyframes hop{{0%,100%{{transform:translateY(0) scale(1,1)}}15%{{transform:translateY(0) scale(1.06,.92)}}45%{{transform:translateY(-36px) scale(.96,1.05)}}75%{{transform:translateY(0) scale(1.04,.95)}}}}
@keyframes wave{{from{{transform:rotate(-14deg)}}to{{transform:rotate(18deg)}}}}
@keyframes shiver{{0%,100%{{transform:translateX(0)}}25%{{transform:translateX(-7px)}}75%{{transform:translateX(7px)}}}}
@keyframes stamp{{0%{{opacity:0;transform:scale(2.2) rotate(var(--r,-8deg))}}60%{{opacity:1;transform:scale(.92) rotate(var(--r,-8deg))}}100%{{opacity:1;transform:scale(1) rotate(var(--r,-8deg))}}}}
@keyframes zzz{{0%{{opacity:0;transform:translate(0,0) scale(.6)}}30%{{opacity:1}}100%{{opacity:0;transform:translate(36px,-100px) scale(1.15)}}}}
@keyframes draw{{from{{stroke-dashoffset:var(--len)}}to{{stroke-dashoffset:0}}}}
@keyframes run{{from{{transform:translateX(0)}}to{{transform:translateX(var(--dx))}}}}
@keyframes jog{{0%,100%{{transform:translateY(0) rotate(-3deg)}}50%{{transform:translateY(-14px) rotate(3deg)}}}}
@keyframes sunrise{{from{{transform:translateY(240px)}}to{{transform:translateY(0)}}}}
@keyframes twinkle{{0%,100%{{opacity:.3}}50%{{opacity:1}}}}
.a-pop{{animation:pop .5s cubic-bezier(.2,1.4,.4,1) both;animation-delay:var(--d,0s)}}
.a-rise{{animation:rise .5s cubic-bezier(.2,.9,.3,1) both;animation-delay:var(--d,0s)}}
.a-fade{{animation:fade .45s ease both;animation-delay:var(--d,0s)}}
.a-sl{{animation:slideL .55s cubic-bezier(.2,1.2,.4,1) both;animation-delay:var(--d,0s)}}
.a-sr{{animation:slideR .55s cubic-bezier(.2,1.2,.4,1) both;animation-delay:var(--d,0s)}}
.a-drop{{animation:drop .5s ease-out both;animation-delay:var(--d,0s)}}
.a-stamp{{animation:stamp .45s ease-out both;animation-delay:var(--d,0s)}}
.squish{{transform-origin:50% 100%;animation:squish 1.6s ease-in-out infinite}}
.squish2{{transform-origin:50% 100%;animation:squish 1.4s ease-in-out .5s infinite}}
.hop{{transform-origin:50% 100%;animation:hop .9s ease-in-out infinite}}
.shiver{{animation:shiver .35s ease-in-out infinite}}
.jog{{animation:jog .35s ease-in-out infinite}}
.star{{animation:twinkle 2.4s ease-in-out infinite}}
"""

def page(body, bg):
    return (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body><div class="stage" style="background:{bg}"><div class="safe">{body}</div></div>'
            '<script>window.seek=t=>{document.body.offsetHeight;document.getAnimations().forEach(a=>{a.pause();a.currentTime=t*1000})};</script></body></html>')

def head(label, n, color):
    prog = "".join(f'<i class="{"on" if i == n else ""}"></i>' for i in range(1, 7))
    return f'<div class="head" style="color:{color}"><div><span class="dot"></span>{label}</div><div class="prog">{prog}</div></div>'

def ch(svg, x, y, w, d=0, anim="a-pop", inner="squish"):
    return f'<div class="abs {anim}" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s"><div class="{inner}">{svg}</div></div>'

def bub(text, x, y, d, tail="t-down", tx="50%", style="", cls="bub"):
    tpos = f"left:{tx};" if tail in ("t-down", "t-up") else "top:40%;"
    return (f'<div class="{cls} a-pop" style="left:{x}px;top:{y}px;--d:{d}s;{style}">{text}'
            f'<div class="tail {tail}" style="{tpos}"></div></div>')

def think(text, x, y, d, style=""):
    dots = ''.join(f'<div class="abs" style="left:{50+i*28}px;bottom:-{30+i*26}px;width:{26-i*7}px;height:{26-i*7}px;border-radius:50%;background:#fff;border:4px solid {L}"></div>' for i in range(3))
    return f'<div class="think a-pop" style="left:{x}px;top:{y}px;--d:{d}s;{style}">{text}{dots}</div>'

def sfx(text, x, y, size, d, rot=-8, color="#fff"):
    return f'<div class="sfx a-stamp" style="left:{x}px;top:{y}px;font-size:{size}px;--d:{d}s;--r:{rot}deg;color:{color}">{text}</div>'

def nar(text, x, y, d, style=""):
    return f'<div class="nar a-drop" style="left:{x}px;top:{y}px;--d:{d}s;{style}">{text}</div>'

def stars(n, seed, y0=0, y1=1920, x0=0, x1=1080):
    r = random.Random(seed)
    out = ""
    for _ in range(n):
        sz = r.choice([4, 5, 6, 8])
        out += (f'<div class="abs star" style="left:{r.randint(x0, x1)}px;top:{r.randint(y0, y1)}px;width:{sz}px;height:{sz}px;'
                f'border-radius:50%;background:#FFF6D6;animation-delay:{r.random()*2.4:.2f}s"></div>')
    return out

def moon(x, y, s=110):
    return (f'<svg class="abs" style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 100 100">'
            f'<path d="M60 8 a44 44 0 1 0 32 64 a36 36 0 1 1 -32 -64z" fill="#FFE7A8" stroke="{L}" stroke-width="4"/></svg>')

ICONS = {
    "chip": f'<svg viewBox="0 0 80 80" width="70"><rect x="14" y="14" width="52" height="52" rx="14" fill="#BFD3FF" stroke="{L}" stroke-width="4"/><path d="M26 6v8M40 6v8M54 6v8M26 66v8M40 66v8M54 66v8" stroke="{L}" stroke-width="4" stroke-linecap="round"/><path d="M28 46 l9 -10 l8 7 l10 -12" stroke="{L}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "won": f'<svg viewBox="0 0 80 80" width="70"><circle cx="40" cy="40" r="30" fill="#FFE59A" stroke="{L}" stroke-width="4"/><text x="40" y="53" text-anchor="middle" font-size="36" fill="{L}" font-family="Jua">$</text></svg>',
    "oil": f'<svg viewBox="0 0 80 80" width="70"><path d="M40 8 Q64 40 60 52 A20 20 0 0 1 20 52 Q16 40 40 8Z" fill="#8A7BC8" stroke="{L}" stroke-width="4"/><path d="M30 50 Q32 58 38 60" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/></svg>',
}
