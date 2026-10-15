"""밤사이 릴스 공통 라이브러리 — 스타일(CSS), 말풍선·내레이션·효과음 글자 등 부품.

장면 파일(posts/<날짜>/reel/scenes.py)에서 `from lib import *` 로 가져다 쓴다.
좌표계는 1080x1920 기준이며, page()가 내용 전체를 가운데 정렬로 줄여(0.82배) 인스타 안전 영역(가로 137~943, 세로 250~1450) 안에 배치한다.
세로로 긴 휴대폰은 영상 양옆을 약 50px씩 잘라 보여 주므로 좌우 여백을 같게 둔다."""
import pathlib, random
from chars import mascot, chip, mini, p_card, p_paper, p_mag, p_tablet, L

HERE = pathlib.Path(__file__).parent
FONT = (HERE / "fonts").resolve().as_uri()

CSS = f"""
@font-face{{font-family:'Jua';src:url('{FONT}/Jua-Regular.ttf')}}
html,body{{margin:0;padding:0}}
body{{width:1080px;height:1920px;overflow:hidden;word-break:keep-all;font-family:'Jua','Noto Sans CJK KR',sans-serif;color:{L};-webkit-font-smoothing:antialiased}}
.stage{{position:relative;width:1080px;height:1920px;overflow:hidden}}
.safe{{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:0 0;transform:translate(101.3px,153.2px) scale(.82)}}
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


# ═══════════════ 형식별 부품 (뉴스·퀴즈·단톡방·탐정·날씨) ═══════════════
CSS += f"""
@keyframes marquee{{from{{transform:translateX(0)}}to{{transform:translateX(-50%)}}}}
@keyframes blinkb{{0%,49%{{opacity:1}}50%,100%{{opacity:.25}}}}
@keyframes glow{{0%{{box-shadow:0 0 0 0 rgba(255,214,90,.0)}}40%{{box-shadow:0 0 0 18px rgba(255,214,90,.55)}}100%{{box-shadow:0 0 0 10px rgba(255,214,90,.35)}}}}
@keyframes dim{{to{{opacity:.28;filter:grayscale(1)}}}}
@keyframes dots{{0%,100%{{opacity:.25}}50%{{opacity:1}}}}
.ticker{{position:absolute;left:44px;width:982px;height:74px;background:#E8484A;border:5px solid {L};border-radius:18px;overflow:hidden;color:#fff;font-size:38px;line-height:66px;white-space:nowrap}}
.ticker .lab{{position:absolute;left:0;top:0;bottom:0;z-index:2;background:{L};color:#FFE59A;padding:0 22px}}
.ticker .run{{display:inline-block;padding-left:190px;animation:marquee 9s linear infinite}}
.live{{position:absolute;background:#E8484A;color:#fff;border:4px solid {L};border-radius:12px;padding:4px 16px;font-size:30px}}
.live i{{display:inline-block;width:14px;height:14px;border-radius:7px;background:#fff;margin-right:10px;vertical-align:2px;animation:blinkb 1s steps(1) infinite}}
.lower{{position:absolute;display:flex;border:5px solid {L};border-radius:16px;overflow:hidden;box-shadow:0 6px 0 rgba(0,0,0,.18)}}
.lower .n{{background:#FFB27F;padding:8px 22px;font-size:34px}} .lower .t{{background:#fff;padding:8px 22px;font-size:34px}}
.screen{{position:absolute;background:#1F2347;border:7px solid {L};border-radius:26px;overflow:hidden}}
.ox{{position:absolute;width:200px;height:200px;border-radius:50%;border:6px solid {L};display:flex;align-items:center;justify-content:center;font-size:150px;line-height:1}}
.ox.ok{{animation:glow .6s ease-out both;animation-delay:var(--r,99s)}} .ox.no{{animation:dim .4s ease-out both;animation-delay:var(--r,99s)}}
.qcard{{position:absolute;background:#fff;border:5px solid {L};border-radius:30px;padding:26px 32px;font-size:46px;line-height:1.35;box-shadow:0 8px 0 rgba(0,0,0,.18)}}
.qcard .no{{display:inline-block;background:#7B6FD6;color:#fff;border-radius:999px;padding:2px 18px;font-size:30px;margin-bottom:10px}}
.chat{{position:absolute;background:#BFD0E6;border:6px solid {L};border-radius:34px;overflow:hidden}}
.chat .top{{position:absolute;left:0;right:0;top:0;height:84px;background:#AFC2DC;border-bottom:4px solid {L};font-size:36px;line-height:84px;padding-left:30px}}
.msg{{position:absolute;display:flex;gap:14px;align-items:flex-start}}
.msg .av{{flex:none;width:86px;height:86px;border-radius:30px;background:#fff;border:4px solid {L};overflow:hidden}}
.msg .nm{{font-size:26px;margin:0 0 6px 4px;opacity:.75}}
.msg .tx{{background:#fff;border:4px solid {L};border-radius:26px;padding:14px 24px;font-size:38px;line-height:1.32;max-width:600px}}
.msg.r{{flex-direction:row-reverse}} .msg.r .tx{{background:#FFE36E}}
.tdots span{{display:inline-block;width:14px;height:14px;margin:0 4px;border-radius:7px;background:{L};animation:dots 1s ease-in-out infinite}}
.tdots span:nth-child(2){{animation-delay:.2s}} .tdots span:nth-child(3){{animation-delay:.4s}}
.cork{{position:absolute;border:7px solid #8A5A3B;border-radius:22px;overflow:hidden;background:#D9A877;
  background-image:radial-gradient(#C38E5D 2px,transparent 2.5px),radial-gradient(#E6BC8E 2px,transparent 2.5px);background-size:26px 26px,34px 34px;background-position:0 0,13px 17px}}
.pola{{position:absolute;background:#fff;border:4px solid {L};border-radius:8px;padding:12px 12px 6px;box-shadow:0 8px 0 rgba(0,0,0,.2);text-align:center;font-size:30px}}
.pin{{position:absolute;left:50%;top:-16px;width:26px;height:26px;margin-left:-13px;border-radius:50%;background:#E8484A;border:4px solid {L}}}
.stamp{{position:absolute;border:8px solid #E03131;color:#E03131;border-radius:16px;padding:4px 22px;font-size:72px;background:rgba(255,255,255,.7)}}
.wx{{position:absolute;background:#fff;border:5px solid {L};border-radius:28px;text-align:center;padding:16px 10px 18px;box-shadow:0 6px 0 rgba(0,0,0,.15)}}
.wx .l{{font-size:34px}} .wx .s{{font-family:'Noto Sans CJK KR',sans-serif;font-size:23px;color:#6B5A50;margin-top:4px;line-height:1.35}}
"""

def face_svg(kind, mood="normal"):
    """단톡방 프로필용 얼굴 클로즈업."""
    return mascot(kind, mood).replace('viewBox="30 40 240 260"', 'viewBox="72 122 156 156"')

def ticker(text, y, label="속보"):
    return (f'<div class="ticker" style="top:{y}px"><div class="lab">{label}</div>'
            f'<div class="run">{text}&nbsp;&nbsp;·&nbsp;&nbsp;{text}&nbsp;&nbsp;·&nbsp;&nbsp;</div></div>')

def live(x, y, text="LIVE", d=0):
    return f'<div class="live a-pop" style="left:{x}px;top:{y}px;--d:{d}s"><i></i>{text}</div>'

def lower_third(name, title, x, y, d):
    return f'<div class="lower a-sl" style="left:{x}px;top:{y}px;--d:{d}s"><div class="n">{name}</div><div class="t">{title}</div></div>'

def desk(x, y, w, label="밤사이 뉴스"):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:120px;background:#5B5FA8;border:5px solid {L};border-radius:18px 18px 0 0">'
            f'<div style="text-align:center;color:#FFE59A;font-size:40px;line-height:110px">🌙 {label}</div></div>')

def screen(inner, x, y, w, h, d, label=""):
    lab = f'<div class="abs" style="left:16px;top:12px;font-size:28px;color:#FFE59A">{label}</div>' if label else ""
    return f'<div class="screen a-pop" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;--d:{d}s">{lab}{inner}</div>'

def qcard(no, text, x, y, w, d):
    return f'<div class="qcard a-drop" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s"><div class="no">Q{no}</div><br>{text}</div>'

def ox(answer, x, y, d, reveal):
    """answer: 'O' 또는 'X'. reveal 초에 정답이 빛나고 오답이 흐려진다."""
    o_cls = "ok" if answer == "O" else "no"; x_cls = "ok" if answer == "X" else "no"
    return (f'<div class="ox {o_cls} a-pop" style="left:{x}px;top:{y}px;--d:{d}s;--r:{reveal}s;background:#DFF3FF;color:#2F6BD8">O</div>'
            f'<div class="ox {x_cls} a-pop" style="left:{x+250}px;top:{y}px;--d:{d+.1}s;--r:{reveal}s;background:#FFE3E3;color:#E03131">X</div>')

def oxs(answer, x, y, d, reveal):
    """ox()에 애니메이션 두 개(pop+glow)를 같이 거는 버전 — 바깥 div가 pop, 안쪽이 glow."""
    def one(ch, bg, col, cls, dx, dd):
        return (f'<div class="abs a-pop" style="left:{x+dx}px;top:{y}px;--d:{dd}s"><div class="ox {cls}" style="position:relative;--r:{reveal}s;background:{bg};color:{col}">{ch}</div></div>')
    return (one("O", "#DFF3FF", "#2F6BD8", "ok" if answer == "O" else "no", 0, d)
            + one("X", "#FFE3E3", "#E03131", "ok" if answer == "X" else "no", 250, d + .1))

def chat(title, x, y, w, h, d, inner):
    return (f'<div class="chat a-pop" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;--d:{d}s">'
            f'<div class="top">{title}</div>{inner}</div>')

NAMES = {"bamtol": "밤톨이", "star": "별콩이", "owl": "솜부엉", "moon": "달떡이"}
def msg(kind, text, y, d, side="l", mood="normal", x=24, name=True):
    av = f'<div class="av">{face_svg(kind, mood)}</div>'
    nm = f'<div class="nm">{NAMES.get(kind, kind)}</div>' if name and side == "l" else ""
    pos = f"left:{x}px;" if side == "l" else f"right:{x}px;"
    return f'<div class="msg {"r" if side == "r" else ""} a-rise" style="{pos}top:{y}px;--d:{d}s">{av}<div>{nm}<div class="tx">{text}</div></div></div>'

def msg_card(inner, y, d, side="l", x=124, w=560):
    pos = f"left:{x}px;" if side == "l" else f"right:{x}px;"
    return f'<div class="abs a-rise" style="{pos}top:{y}px;width:{w}px;--d:{d}s;background:#fff;border:4px solid {L};border-radius:24px;padding:16px 20px">{inner}</div>'

def typing(y, d, side="l", x=124, until=None):
    pos = f"left:{x}px;" if side == "l" else f"right:{x}px;"
    hide = f";animation:fade .3s ease both reverse;animation-delay:{until}s" if until else ""
    return (f'<div class="abs a-fade" style="{pos}top:{y}px;--d:{d}s"><div class="tdots" style="background:#fff;border:4px solid {L};border-radius:26px;padding:16px 22px{hide}">'
            f'<span></span><span></span><span></span></div></div>')

def cork(x, y, w, h, d):
    return f'<div class="cork a-pop" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;--d:{d}s"></div>'

def pola(inner, label, x, y, w, d, rot=-3):
    return (f'<div class="abs a-drop" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s"><div class="pola" style="position:relative;transform:rotate({rot}deg)">'
            f'<div class="pin"></div>{inner}<div style="margin-top:4px">{label}</div></div></div>')

def string(x1, y1, x2, y2, d, color="#E03131"):
    import math
    ln = int(math.hypot(x2 - x1, y2 - y1)) + 10
    return (f'<svg class="abs" style="left:0;top:0;overflow:visible" width="1080" height="1920"><path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="7" stroke-linecap="round" '
            f'style="stroke-dasharray:{ln};--len:{ln};stroke-dashoffset:{ln};animation:draw .45s ease-out both;animation-delay:{d}s"/></svg>')

def stamp(text, x, y, d, rot=-10):
    return f'<div class="stamp a-stamp" style="left:{x}px;top:{y}px;--d:{d}s;--r:{rot}deg">{text}</div>'

def wx_icon(kind, s=120):
    sun = f'<circle cx="50" cy="50" r="22" fill="#FFD84D" stroke="{L}" stroke-width="4"/>' + "".join(
        f'<path d="M50 14 v-10" stroke="{L}" stroke-width="5" stroke-linecap="round" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45))
    cloud = lambda c="#fff", dy=0: f'<path d="M24 {72+dy} a16 16 0 0 1 4 -31 a22 22 0 0 1 41 -6 a17 17 0 0 1 9 37 z" fill="{c}" stroke="{L}" stroke-width="4" stroke-linejoin="round"/>'
    drops = "".join(f'<path d="M{x} 84 l-5 12" stroke="#5B8DEF" stroke-width="5" stroke-linecap="round"/>' for x in (36, 52, 68))
    bolt = f'<path d="M54 74 l-12 16 h10 l-6 14 l18 -20 h-10 l6 -10z" fill="#FFD84D" stroke="{L}" stroke-width="3" stroke-linejoin="round"/>'
    body = {"sun": sun, "cloud": cloud(), "partly": f'<g transform="translate(14 -10) scale(.8)">{sun}</g>' + cloud(dy=6),
            "rain": cloud("#DDE3F0", -6) + drops, "storm": cloud("#B9C0D6", -6) + bolt}[kind]
    return f'<svg viewBox="0 0 100 110" width="{s}" height="{s*1.1:.0f}" overflow="visible">{body}</svg>'

def wx(kind, label, sub, x, y, w, d):
    return f'<div class="wx a-pop" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s">{wx_icon(kind)}<div class="l">{label}</div><div class="s">{sub}</div></div>'

def big(text, x, y, size, d, color="#F6EEE4", anim="a-rise"):
    return f'<div class="abs hook {anim}" style="left:{x}px;top:{y}px;font-size:{size}px;color:{color};--d:{d}s">{text}</div>'
