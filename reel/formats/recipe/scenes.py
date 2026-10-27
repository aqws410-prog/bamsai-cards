"""형식: 밤사이 요리 레시피 (처음 제작 · 검수 전 · 2026-10-28 수요일판) — 오늘의 요리 '나스닥 ▲1.18%', 재료는 둘.
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(나스닥 ▲1.18%, '두 재료로 또 올랐다!')을 0초부터 크게.
시그니처: 요리 스튜디오(레시피 카드 · 김 나는 냄비 · 재료 태그가 냄비로 쏙) + 셰프 모자 밤톨이 + 지글지글(sizzle).
흐름: 1 오늘의 요리(결론) → 2 재료 ① AI 반도체 → 3 재료 ② 유가 하락(불 조절) → 4 완성 접시(3대 지수)·탄 재료(보잉) → 5 한국 식탁·체크 3 → 6 다음 메뉴·마무리.
숫자는 2026-10-28 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes steam{0%{transform:translateY(0) scaleX(1);opacity:0}25%{opacity:.9}100%{transform:translateY(-120px) scaleX(1.3);opacity:0}}
@keyframes intoPot{0%{opacity:0;transform:translate(0,-60px) rotate(-8deg)}60%{opacity:1;transform:translate(0,8px) rotate(4deg)}100%{opacity:1;transform:none}}
@keyframes flame{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.86)}}
@keyframes shrink{from{transform:scale(1.35)}to{transform:scale(.7)}}
@keyframes knob{from{transform:rotate(0)}to{transform:rotate(-110deg)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:.25}}
.steam{animation:steam 1.2s ease-out infinite}
.into{animation:intoPot .5s cubic-bezier(.3,1.3,.5,1) var(--d,0s) both}
.blink{animation:blink .7s steps(1) infinite}
</style>"""

# 셰프 모자 (밤톨이 좌표계)
HAT = (f'<rect x="102" y="70" width="96" height="34" rx="8" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<circle cx="114" cy="56" r="26" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<circle cx="186" cy="56" r="26" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<circle cx="150" cy="40" r="32" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<rect x="105" y="72" width="90" height="22" fill="#fff"/>')

def pot(w=380, label="나스닥"):
    puffs = "".join(f'<path class="steam" d="M{x} 70 q-14 -20 0 -40 q14 -20 0 -40" fill="none" stroke="#B9B0D6" stroke-width="9" stroke-linecap="round" '
                    f'style="animation-delay:{dl}s;transform-box:fill-box;transform-origin:50% 100%"/>' for x, dl in ((120, 0), (190, .4), (260, .8)))
    return (f'<svg viewBox="0 0 380 300" width="{w}" height="{w*300/380:.0f}" overflow="visible">{puffs}'
            f'<rect x="40" y="96" width="300" height="26" rx="13" fill="#7A6A9C" stroke="{L}" stroke-width="6"/>'
            f'<path d="M58 122 h264 v110 q0 50 -50 50 h-164 q-50 0 -50 -50 z" fill="#9C8CC4" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M58 150 h-34 M322 150 h34" stroke="{L}" stroke-width="12" stroke-linecap="round"/>'
            f'<rect x="120" y="170" width="140" height="58" rx="12" fill="#FFF6EA" stroke="{L}" stroke-width="4"/>'
            f'<text x="190" y="212" text-anchor="middle" font-size="36" font-family="Jua" fill="{L}">{label}</text></svg>')

def tag(text, x, y, d, bg):
    return (f'<div class="abs into" style="left:{x}px;top:{y}px;--d:{d}s;background:{bg};border:5px solid {L};border-radius:20px;'
            f'padding:8px 22px;font-size:46px;box-shadow:0 6px 0 rgba(0,0,0,.18)">{text}</div>')

def bar(text, right=""):
    return (f'<div class="abs" style="left:0;right:0;top:0;height:88px;background:#FFD9A8;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">{text}'
            f'<span style="position:absolute;right:30px;font-size:32px">{right}</span></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·레시피 카드(냄비)·놀란 셰프 밤톨이(클로즈업)가 모두 보인다
S[1] = (1, page(FX + f'''
{stars(14, 28, 0, 180)}
{head("오늘의 요리 · 10.28 WED", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:188px;text-align:center;font-size:44px;color:#C9D6FF">🍳 나스닥 · 27일 마감</div>
<div class="abs" style="left:0;width:1080px;top:246px;text-align:center"><span class="punch" style="--d:0s;font-size:220px;line-height:1;color:{RED};-webkit-text-stroke:10px {L};paint-order:stroke fill">▲1.18%</span></div>
<div class="abs" style="left:0;width:1080px;top:486px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">재료 둘로 <span style="color:#FFE36E">또 올랐다!</span></div>
<div class="panel" style="left:44px;top:630px;width:982px;height:760px;background:#FFFDF6">
  {bar("📖 오늘의 레시피", '<span class="blink" style="color:#E8484A">● 조리 중</span>')}
  <div class="abs" style="left:470px;top:330px">{pot(420)}</div>
  {tag("🤖 AI 반도체", 470, 130, .3, "#FFE36E")}
  {tag("🛢 유가 하락", 600, 220, .6, "#BFE3FF")}
  <div class="abs" style="left:-20px;top:300px;width:440px"><div class="shiver">{mascot("bamtol", "surprised", "up", HAT)}</div></div>
</div>
{sfx("지글!", 820, 580, 92, .0, 10, "#FFE36E")}
''', "#262B55"))

# 2 ── 재료 ①: AI 반도체 (앤트로픽 상장 기대, 하루 더)
S[2] = (1, page(FX + f'''
{head("재료 ① · AI 반도체", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFFDF6;--d:0s">
  {bar("🥄 재료 ① 손질")}
  <div class="abs" style="left:0;right:0;top:120px;text-align:center;font-size:80px;line-height:1.15"><span class="punch" style="--d:.1s">앤트로픽 기대, <span style="color:#7B3FC4">하루 더</span></span></div>
  <div class="abs a-drop" style="left:{P}px;top:250px;--d:.4s;width:{IW}px;box-sizing:border-box;background:#FFF2DC;border:4px solid {L};border-radius:24px;padding:26px 34px;font-size:42px;line-height:1.5">
    AI 회사 <span style="color:#7B3FC4">앤트로픽</span>이 전날 상장 신청<br>→ AI·반도체주가 <span style="color:{RED}">또 올랐다 ▲</span></div>
  {numbox("AMD", "▲5.45%", COL2[0], 500, .9, RED)}
  {numbox("반도체주", "일제히 ▲", COL2[1], 500, 1.2, RED)}
  {ch(mascot("owl", "happy", "point"), P, 740, 300, 1.5, "a-sl", "squish")}
  {bub("AI에 쏟는 돈 걱정이<br><b>또 한숨 돌렸어요</b>", 370, 790, 1.7, "t-left", style="font-size:44px")}
</div>
''', "#2B3060"))

# 3 ── 재료 ②: 유가 하락 = 불 조절 (기름값 ↓ → 물가 걱정 약불)
FLAME = (f'<svg viewBox="0 0 200 200" width="260" height="260" overflow="visible"><g style="transform-origin:100px 190px;animation:shrink 1s ease-out .5s both">'
         f'<g style="transform-origin:100px 190px;animation:flame .3s ease-in-out infinite">'
         f'<path d="M100 10 C150 70 170 110 160 150 C150 190 50 190 40 150 C30 110 60 80 100 10 Z" fill="#FF8A3D" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
         f'<path d="M100 80 C125 110 130 135 122 155 C112 178 88 178 78 155 C70 135 80 115 100 80 Z" fill="#FFE36E"/></g></g></svg>')
KNOB = (f'<svg viewBox="0 0 120 120" width="150" height="150"><circle cx="60" cy="60" r="52" fill="#fff" stroke="{L}" stroke-width="6"/>'
        f'<g style="transform-origin:60px 60px;animation:knob .8s ease-out .5s both"><rect x="52" y="12" width="16" height="50" rx="8" fill="{L}"/></g></svg>')
S[3] = (1, page(FX + f'''
{head("재료 ② · 불 조절", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {bar("🔥 재료 ② · 불 줄이기")}
  <div class="abs" style="left:0;right:0;top:120px;text-align:center;font-size:44px">국제유가(WTI) · 27일 마감</div>
  <div class="abs" style="left:0;right:0;top:180px;text-align:center;font-size:130px;line-height:1"><span class="punch" style="--d:.1s"><span style="color:{BLUE}">▼</span> 99.90달러</span></div>
  <div class="abs a-pop" style="left:0;right:0;top:340px;--d:.4s;text-align:center"><span style="display:inline-block;background:#fff;border:4px solid {L};border-radius:999px;padding:10px 36px;font-size:46px">이틀째 하락 · <span style="color:{BLUE}">100달러 아래</span></span></div>
  <div class="abs" style="left:110px;top:450px">{FLAME}</div>
  <div class="abs a-pop" style="left:560px;top:520px;--d:.3s;text-align:center">{KNOB}<div style="font-size:36px">약불로~</div></div>
  {ch(mascot("moon", "happy", "point"), P, 760, 300, 1.2, "a-sl", "squish")}
  {bub("기름값이 내리면<br><b>물가 걱정도 약불</b>", 380, 800, 1.5, "t-left", style="font-size:46px")}
  <div class="abs a-fade" style="left:380px;top:1020px;--d:1.8s;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#5B4F78">중동 긴장 완화 기대에 내렸어요</div>
</div>
''', "#30366E"))

# 4 ── 완성 접시: 3대 지수 + 탄 재료(보잉)
def plate(name, v, col, d, color, hi=False):
    x, w = col
    ring = "#FFE36E" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:250px;width:{w}px;--d:{d}s;text-align:center">'
            f'<div style="width:{w}px;height:{w}px;border-radius:50%;background:{ring};border:5px solid {L};box-sizing:border-box;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 6px 0 rgba(0,0,0,.15)">'
            f'<div style="font-size:36px">{name}</div><div style="font-size:54px;color:{color}">{v}</div></div></div>')
S[4] = (1, page(FX + f'''
{head("완성 · 3대 지수", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFF6E8;--d:0s">
  {bar("🍽 완성! 27일 마감 접시")}
  <div class="abs" style="left:0;right:0;top:120px;text-align:center;font-size:80px"><span class="punch" style="--d:.1s">나스닥이 <span style="color:{RED}">제일 맛있게</span></span></div>
  {plate("다우", "▲0.03%", COL3[0], .4, RED)}
  {plate("S&amp;P500", "▲0.60%", COL3[1], .6, RED)}
  {plate("나스닥", "▲1.18%", COL3[2], .8, RED, True)}
  <div class="abs a-sl" style="left:{P}px;top:580px;--d:1.1s;width:{IW}px;height:200px;box-sizing:border-box;background:#3A3460;color:#fff;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px">
    <div style="font-size:90px">🔥</div><div><div style="font-size:38px;color:#FFC08A">탄 재료 · 보잉</div><div style="font-size:70px;line-height:1.1"><span style="color:#8EC5FF">▼</span> 10% 넘게 급락</div></div></div>
  {ch(mascot("star", "surprised", "up"), 640, 820, 280, 1.4, "a-sr", "shiver")}
  {bub("손실이 예상보다 컸고<br><b>737 증산도 늦어져요</b>", P, 840, 1.6, "t-right", style="font-size:42px")}
</div>
''', "#4A3E78"))

# 5 ── 한국 식탁 · 체크 3
checks = [("오늘 SK하이닉스 실적", "기대 넘으면 강세 연장, 못 미치면 차익 실현 가능성"),
          ("외국인, 이틀 연속 살까", "어제 외국인·기관 동반 순매수"),
          ("유가 100달러 아래", "내림세 이어지면 물가·금리 부담 덜 가능성")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{300+i*180}px;width:{IW}px;height:158px;box-sizing:border-box;--d:{.6+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:14px;background:#FFF6EA;border:4px solid {L};font-size:54px;line-height:70px;text-align:center;color:{RED}">✔</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("한국 식탁 · 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  {bar("🇰🇷 한국 식탁 · 오늘 한국장")}
  <div class="abs" style="left:0;right:0;top:120px;text-align:center;font-size:44px">어제 코스피 5,638.34</div>
  <div class="abs" style="left:0;right:0;top:170px;text-align:center;font-size:96px;line-height:1"><span class="punch" style="--d:.1s;color:{RED}">▲3.09%</span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point", HAT), 700, 830, 200, 2.0, "a-sr", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.2s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 로이터, 뉴스핌, 파이낸셜뉴스, 뉴스1, SBS, 한국경제</div>
''', "#FFE1CC"))

# 6 ── 다음 메뉴 · 마무리
def daycard(day, date, t, col, d, hi=False):
    x, w = col
    bg = "#FFD84D" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:{w}px;height:280px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};'
            f'border-radius:26px;box-shadow:0 6px 0 rgba(0,0,0,.15);text-align:center;padding:14px 8px;color:{L}">'
            f'<div style="font-size:32px;color:#6B5A50">{day}</div><div style="font-size:88px;line-height:1.05">{date}</div>'
            f'<div style="font-size:32px;line-height:1.2;margin-top:6px">{t}</div></div>')
S[6] = (1, page(FX + f'''
{head("다음 메뉴 · 마무리", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:30px;font-size:42px;color:#FFC08A">다음 메뉴 나오는 날</div>
  {daycard("오늘(수)", "28", "SK하이닉스<br>실적", COL3[0], .15, True)}
  {daycard("목 새벽", "29", "FOMC<br>금리 결정", COL3[1], .3, True)}
  {daycard("목요일", "29", "삼성전자<br>실적", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("bamtol", "happy", "wave", HAT), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("star", "happy", "wave"), 680, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 차려 드릴게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 로이터, 뉴스핌, 파이낸셜뉴스, 뉴스1, AP, SBS, 한국경제<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.2, 1.5), 3: (4.0, 1.5), 4: (4.0, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "sizzle", 1), (1, .05, "thud", .8), (1, .3, "thud", .9), (1, .6, "thud", .9), (1, .85, "ding", .6),
 (2, .05, "whoosh", .5), (2, .1, "boing", .6), (2, .4, "tick", .6), (2, .9, "pop", .7), (2, 1.2, "pop", .7), (2, 1.5, "boing", .5), (2, 1.7, "ding", .7),
 (3, .05, "whoosh", .5), (3, .1, "blip_down", .8), (3, .3, "pop", .6), (3, .4, "pop", .6), (3, .5, "sizzle", .6), (3, 1.2, "boing", .5), (3, 1.5, "pop", .7),
 (4, .05, "whoosh", .5), (4, .1, "thud", .7), (4, .4, "pop", .6), (4, .6, "pop", .6), (4, .8, "sparkle", .7), (4, 1.1, "slidedown", .7), (4, 1.4, "question", .5), (4, 1.6, "pop", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .6, "CHECK1", 1), (5, 1.05, "CHECK2", 1), (5, 1.5, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "pop", .5), (6, .9, "jingle", .9),
]
