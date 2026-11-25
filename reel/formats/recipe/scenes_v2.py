"""2026-11-26 릴스 · 요리 레시피(recipe) v2 — '결론 먼저' 훅, 장면 1 '가스레인지 클로즈업 — 끓어 넘치는 냄비(장중 ▼4.6% 딱지) + 찬물 한 컵 붓기 + 주방 타이머' 새 구도 (검수 전).
그날 상황: PCE 발표·나스닥 장중 ▼4.6% 급변 → 첫 칸 1순위 news(11-25)·2순위 talkshow(11-24) 모두 최근 3일 사용 → 다음 칸.
          '원인 찾기' 칸은 원인이 하나로 모이지 않아 해당 없음 → '원인 여러 개가 섞인 결과' 1순위 recipe(마지막 10-28, 최근 3일 11-23 chat·11-24 talkshow·11-25 news 미사용).
흐름: 1 결론(나스닥 ▼0.62%, '낙폭 대부분 되찾았다!') → 2 재료 셋(뜨거운 물가 · 관세 · AI 걱정) → 냄비가 끓어 넘침(장중 ▼4.6%, 다우 1,100포인트↓)
      → 3 찬물 한 컵(연휴 앞 저가 매수) → 완성 접시 3대 지수 → 4 한국 식탁(25일 코스피 ▼6.16%, 반등 전에 마감 · 반찬: 관세 15% 유지안)
      → 5 체크 3 → 6 다음 메뉴(오늘 금통위·미국 휴장, 27일 조기 폐장).
숫자·사실은 posts/2026-11-26 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes steam{0%{transform:translateY(0) scaleX(1);opacity:0}25%{opacity:.9}100%{transform:translateY(-120px) scaleX(1.3);opacity:0}}
@keyframes intoPot{0%{opacity:0;transform:translate(0,-60px) rotate(-8deg)}60%{opacity:1;transform:translate(0,8px) rotate(4deg)}100%{opacity:1;transform:none}}
@keyframes flame{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.86)}}
@keyframes boil{0%,100%{transform:scale(1,1)}50%{transform:scale(1.04,.96)}}
@keyframes foam{0%{transform:scaleY(1)}55%{transform:scaleY(1.25)}100%{transform:scaleY(.25)}}
@keyframes drip{0%{transform:scaleY(1)}55%{transform:scaleY(1.3)}100%{transform:scaleY(.2);opacity:.2}}
@keyframes pour{0%{transform:rotate(0)}100%{transform:rotate(-60deg)}}
@keyframes stream{0%{transform:scaleY(0)}100%{transform:scaleY(1)}}
@keyframes tick{from{transform:rotate(0)}to{transform:rotate(360deg)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:.25}}
@keyframes rise3{0%{transform:translateY(0)}100%{transform:translateY(var(--dy))}}
.steam{animation:steam 1.2s ease-out infinite}
.into{animation:intoPot .5s cubic-bezier(.3,1.3,.5,1) var(--d,0s) both}
.boil{transform-origin:50% 100%;animation:boil .3s ease-in-out infinite}
.blink{animation:blink .7s steps(1) infinite}
</style>"""

# 셰프 모자 (밤톨이 좌표계)
HAT = (f'<rect x="102" y="70" width="96" height="34" rx="8" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<circle cx="114" cy="56" r="26" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<circle cx="186" cy="56" r="26" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<circle cx="150" cy="40" r="32" fill="#fff" stroke="{L}" stroke-width="3.6"/>'
       f'<rect x="105" y="72" width="90" height="22" fill="#fff"/>')

def pot(w=420, label="나스닥", foam_d=None):
    """끓어 넘치는 냄비. foam_d가 있으면 그 시각부터 거품이 부풀었다 가라앉는다."""
    fa = f"animation:foam 1.1s ease-in-out {foam_d}s both" if foam_d is not None else ""
    da = f"animation:drip 1.1s ease-in-out {foam_d}s both" if foam_d is not None else ""
    puffs = "".join(f'<path class="steam" d="M{x} 40 q-14 -20 0 -40 q14 -20 0 -40" fill="none" stroke="#C9C2E4" stroke-width="9" stroke-linecap="round" '
                    f'style="animation-delay:{dl}s;transform-box:fill-box;transform-origin:50% 100%"/>' for x, dl in ((120, 0), (190, .4), (260, .8)))
    foam = (f'<g style="transform-box:fill-box;transform-origin:50% 100%;{fa}">'
            f'<path d="M40 112 C40 70 80 60 100 76 C110 40 160 36 176 66 C196 34 250 40 258 74 C282 56 330 66 336 112 Z" fill="#FFFFFF" stroke="{L}" stroke-width="6" stroke-linejoin="round"/></g>')
    drips = "".join(f'<g style="transform-box:fill-box;transform-origin:50% 0;{da}"><path d="M{x} 118 q-8 {h} 0 {h + 16} q8 -{16} 0 -{h + 16}" fill="#FFFFFF" stroke="{L}" stroke-width="5"/></g>'
                    for x, h in ((70, 70), (300, 90), (220, 40)))
    return (f'<svg viewBox="0 0 380 300" width="{w}" height="{w*300/380:.0f}" overflow="visible">{puffs}{foam}'
            f'<rect x="40" y="96" width="300" height="26" rx="13" fill="#7A6A9C" stroke="{L}" stroke-width="6"/>'
            f'<path d="M58 122 h264 v110 q0 50 -50 50 h-164 q-50 0 -50 -50 z" fill="#9C8CC4" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M58 150 h-34 M322 150 h34" stroke="{L}" stroke-width="12" stroke-linecap="round"/>'
            f'<rect x="120" y="170" width="140" height="58" rx="12" fill="#FFF6EA" stroke="{L}" stroke-width="4"/>'
            f'<text x="190" y="212" text-anchor="middle" font-size="36" font-family="Jua" fill="{L}">{label}</text>{drips}</svg>')

def stove(x, y, w):
    fl = "".join(f'<path d="M{cx} 30 C{cx+18} 8 {cx+10} -8 {cx} -24 C{cx-10} -8 {cx-18} 8 {cx} 30 Z" fill="#5AA9FF" stroke="{L}" stroke-width="4" '
                 f'style="transform-box:fill-box;transform-origin:50% 100%;animation:flame .25s ease-in-out {i*.08:.2f}s infinite"/>' for i, cx in enumerate(range(80, w - 40, 70)))
    return (f'<svg class="abs" style="left:{x}px;top:{y}px" width="{w}" height="110" viewBox="0 -30 {w} 110" overflow="visible">{fl}'
            f'<rect x="0" y="30" width="{w}" height="50" rx="14" fill="#56607A" stroke="{L}" stroke-width="6"/></svg>')

def cup(x, y, d):
    """찬물 컵: d초에 기울어 물줄기를 붓는다."""
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:150px;height:170px">'
            f'<div class="abs" style="left:0;top:0;transform-origin:20px 150px;animation:pour .35s ease-out {d}s both">'
            f'<svg width="140" height="160" viewBox="0 0 140 160"><path d="M14 10 h112 l-12 140 h-88 z" fill="#DDF1FF" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M22 50 h96 l-8 94 h-80 z" fill="#74C0FC"/><text x="70" y="112" text-anchor="middle" font-size="30" font-family="Jua" fill="{L}">찬물</text></svg></div>'
            f'<div class="abs" style="left:-30px;top:120px;width:22px;height:230px;background:#74C0FC;border:4px solid {L};border-radius:11px;transform-origin:50% 0;'
            f'animation:stream .3s ease-out {d + .3:.2f}s both"></div></div>')

def timer(x, y, s=150):
    return (f'<svg class="abs" style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 100 100">'
            f'<circle cx="50" cy="54" r="40" fill="#FFE36E" stroke="{L}" stroke-width="5"/><rect x="42" y="4" width="16" height="12" rx="4" fill="{L}"/>'
            f'<g style="transform-origin:50px 54px;animation:tick 1.2s linear infinite"><path d="M50 54 V24" stroke="#E03131" stroke-width="6" stroke-linecap="round"/></g>'
            f'<circle cx="50" cy="54" r="5" fill="{L}"/></svg>')

def bar(text, right=""):
    return (f'<div class="abs" style="left:0;right:0;top:0;height:88px;background:#FFD9A8;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">{text}'
            f'<span style="position:absolute;right:30px;font-size:32px">{right}</span></div>')

def tag(text, x, y, d, bg, size=44):
    return (f'<div class="abs into" style="left:{x}px;top:{y}px;--d:{d}s;background:{bg};border:5px solid {L};border-radius:20px;'
            f'padding:8px 22px;font-size:{size}px;box-shadow:0 6px 0 rgba(0,0,0,.18)">{text}</div>')

# 1 ── 결론 먼저 (가스레인지 클로즈업): 0초에 숫자·결론·넘치는 냄비·놀란 셰프 밤톨이(클로즈업)가 모두 보인다
#      0~1초: 숫자 펀치(0) → '부글!' 쾅(.15) → '장중 ▼4.6%' 딱지 쾅(.35) → 찬물 붓기(.55~.9) → 거품 가라앉음(.55~1.6) → '휴~'(.95)
S[1] = (1, page(FX + f'''
{stars(14, 126, 0, 180)}
{head("오늘의 요리 · 11.26 THU", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:190px;text-align:center;font-size:46px;color:#FFE36E">🍳 나스닥 · 25일 마감</div>
<div class="abs" style="left:0;width:1080px;top:250px;text-align:center"><span class="punch" style="--d:0s;font-size:222px;line-height:1;color:#7DB0FF;-webkit-text-stroke:11px {L};paint-order:stroke fill">▼0.62%</span></div>
<div class="abs" style="left:0;width:1080px;top:500px;text-align:center;font-size:78px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">낙폭 <span style="color:#FFE36E">대부분 되찾았다!</span></div>
<div class="panel" style="left:44px;top:640px;width:982px;height:750px;background:#FFF3E2">
  <div class="abs" style="left:0;right:0;top:0;height:250px;background:repeating-linear-gradient(90deg,#FFE2C4 0 80px,#FFD6B0 80px 84px)"></div>
  {timer(40, 20, 110)}
  <div class="abs" style="left:200px;top:60px;font-size:36px;color:#7A5A44">장중엔 끓어 넘쳤는데…</div>
  {stove(40, 600, 560)}
  <div class="abs boil" style="left:90px;top:270px">{pot(460, "나스닥", .55)}</div>
  {stamp("장중 ▼4.6%", 50, 150, .35, -6)}
  {cup(540, 110, .55)}
  <div class="abs" style="left:520px;top:330px;width:400px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver">{mascot("bamtol", "surprised", "up", HAT)}</div></div>
  {sfx("휴~", 700, 40, 96, .95, 8, "#74C0FC")}
</div>
{sfx("부글!", 60, 560, 110, .15, -10, "#FFE36E")}
''', "#262B55"))

# 2 ── 재료 셋이 한꺼번에 → 냄비가 끓어 넘침 (장중 나스닥 ▼4.6%, 다우 1,100포인트↓)
S[2] = (1, page(FX + f'''
{head("재료 · 센 불 셋", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFFDF6;--d:0s">
  {bar("🔥 오늘 냄비에 들어간 재료", '<span class="blink" style="color:#E8484A">● 센 불</span>')}
  <div class="abs" style="left:0;right:0;top:118px;text-align:center;font-size:76px"><span class="punch" style="--d:.1s">걱정 <span style="color:#E8590C">세 숟갈</span>이 한꺼번에</span></div>
  {tag("🌡 뜨거운 물가", P, 250, .4, "#FFD3D3")}
  {tag("📦 관세안", 380, 250, .7, "#FFE36E")}
  {tag("🤖 AI 걱정", 640, 250, 1.0, "#D6E4FF")}
  <div class="abs a-fade" style="left:{P}px;top:350px;--d:.5s;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">근원 PCE 3.3% (예상 3.2%)</div>
  <div class="abs a-fade" style="left:380px;top:350px;--d:.8s;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">14개 경제권</div>
  <div class="abs a-fade" style="left:640px;top:350px;--d:1.1s;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">AI 투자 걱정</div>
  {stove(60, 860, 520)}
  <div class="abs boil" style="left:100px;top:520px">{pot(440, "나스닥")}</div>
  {numbox("나스닥 장중", "<span class='thump' style='--d:1.6s'>▼4.6%</span>", COL2[1], 520, 1.4, BLUE)}
  {numbox("다우 장중", "1,100p↓", COL2[1], 700, 1.7, BLUE)}
  {sfx("부글부글!", 120, 440, 90, 1.3, -8, "#FFE36E")}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), 600, 880, 220, 2.0, "a-sr", "shiver")}
  {bub("한때 <b>끓어 넘쳤어요!</b>", 140, 980, 2.2, "t-right", style="font-size:44px")}
</div>
''', "#2B3060"))

# 3 ── 찬물 한 컵(연휴 앞 저가 매수) → 완성 접시 3대 지수
def plate(name, v, col, d, color, hi=False):
    x, w = col
    ring = "#FFE36E" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:560px;width:{w}px;--d:{d}s;text-align:center">'
            f'<div style="width:{w}px;height:{w}px;border-radius:50%;background:{ring};border:5px solid {L};box-sizing:border-box;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 6px 0 rgba(0,0,0,.15)">'
            f'<div style="font-size:36px">{name}</div><div style="font-size:54px;color:{color}">{v}</div></div></div>')
S[3] = (1, page(FX + f'''
{head("찬물 한 컵 · 완성", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {bar("💧 불 끄고 찬물 한 컵")}
  <div class="abs" style="left:0;right:0;top:118px;text-align:center;font-size:74px"><span class="punch" style="--d:.1s">연휴 앞 <span style="color:#1F6FD1">저가 매수</span></span></div>
  {cup(120, 230, .3)}
  {cbub("많이 빠졌을 때 <b>싸게 사자</b>는 손님이<br>추수감사절 연휴 전에 몰렸어요", 260, .6, "t-left", style="font-size:40px", left=300, width=640)}
  {plate("다우", "▲0.33%", COL3[0], 1.2, RED, True)}
  {plate("S&amp;P500", "▼0.25%", COL3[1], 1.4, BLUE)}
  {plate("나스닥", "▼0.62%", COL3[2], 1.6, BLUE)}
  <div class="abs a-pop" style="left:{P}px;top:860px;--d:2.0s;width:{IW}px;box-sizing:border-box;background:#FFF8E1;border:4px solid {L};border-radius:24px;text-align:center;padding:14px 0;font-size:46px">다우는 <span style="color:{RED}">플러스</span>로 마감, 나머지는 살짝 ▼</div>
  {ch(mascot("moon", "happy", "point"), 600, 960, 200, 2.3, "a-sr", "squish")}
  {bub("간이 <b>딱 맞진</b> 않아도<br>타진 않았어요", 180, 990, 2.5, "t-right", style="font-size:40px")}
</div>
''', "#30366E"))

# 4 ── 한국 식탁: 25일 서울은 반등 전에 마감 · 반찬은 관세 15% 유지안
S[4] = (1, page(FX + f'''
{head("한국 식탁", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {bar("🇰🇷 한국 식탁은 하루 먼저")}
  {ch(mascot("star", "teary", "up"), P, 110, 230, .1, "a-sl", "squish")}
  {bub("어제 한국은<br><b>많이 빠졌던데요?</b>", 300, 150, .3, "t-left", style="font-size:44px")}
  <div class="abs a-pop" style="left:{P}px;top:380px;width:{IW}px;--d:.6s;text-align:center">
    <div style="font-size:40px">코스피 (25일 종가 4,697.51)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.8s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼6.16%</span></div></div>
  {numbox("삼성전자", "▼9.87%", COL2[0], 630, 1.1, BLUE)}
  {numbox("SK하이닉스", "▼11.05%", COL2[1], 630, 1.25, BLUE)}
  {nar("미국이 낙폭을 되찾은 건 <b>서울 장 끝난 뒤</b>", P, 830, 1.7, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  <div class="abs a-sl" style="left:{P}px;top:950px;--d:2.2s;width:800px;height:170px;box-sizing:border-box;background:#FFF8E1;border:5px solid {L};border-radius:26px;display:flex;align-items:center;gap:24px;padding:0 30px">
    <div style="font-size:80px">🍚</div><div><div style="font-size:34px;color:#8A5A3B">반찬 하나 · 미국 관세안</div><div style="font-size:58px;line-height:1.15">한국은 <span style="color:#E8590C">15% 유지</span> <span style="font-size:32px">(1월 확정)</span></div></div></div>
</div>
''', "#4A3E78"))

# 5 ── 오늘 체크 3 (복숭아빛)
checks = [("오늘 오전 한은 금통위", "연 3.00% → 3.25% 인상 전망 우세"),
          ("반도체, 미국 반등 따라갈까", "어제 코스피 <span style='color:#2F6BD8'>▼6.16%</span> 뒤 미국은 낙폭 회복"),
          ("관세 15% 유지안", "확정은 내년 1월 공청회 뒤")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{300+i*180}px;width:{IW}px;height:158px;box-sizing:border-box;--d:{.6+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:14px;background:#FFF6EA;border:4px solid {L};font-size:54px;line-height:70px;text-align:center;color:{RED}">✔</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  {bar("✅ 오늘 한국장, 세 가지만")}
  <div class="abs" style="left:0;right:0;top:130px;text-align:center;font-size:84px;line-height:1"><span class="punch" style="--d:.1s">맛볼 건 <span style="color:#E8590C">딱 셋</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point", HAT), 60, 830, 200, 2.0, "a-sl", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.2s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스1, 디지털타임스, 아시아경제, 데일리안, 아주경제, 이투데이</div>
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
  {daycard("오늘 오전", "26", "한은 금통위<br>미국 휴장", COL3[0], .15, True)}
  {daycard("금(현지)", "27", "미국장<br>조기 폐장", COL3[1], .3)}
  {daycard("일요일", "29", "OPEC+<br>회의", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("bamtol", "happy", "wave", HAT), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("star", "happy", "wave"), 680, 230, 260, .4, "a-sr", "squish")}
  {bub("금통위 결과는 내일 8시,<br><b>또 차려 드릴게요!</b>", 300, 40, .65, "t-down", "50%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 이투데이, 이코노미블록, 블록미디어, 아시아경제, 비즈니스코리아, 데일리안, MTN, 뉴스1<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.0, 1.55), 3: (4.4, 1.6), 4: (4.2, 1.6), 5: (3.3, 1.45), 6: (3.0, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "sizzle", 1), (1, .15, "thud", .9), (1, .35, "thud", .9), (1, .55, "whoosh", .6), (1, .85, "slidedown", .5), (1, .95, "ding", .6),
 (2, .05, "whoosh", .5), (2, .1, "thud", .7), (2, .4, "pop", .7), (2, .7, "pop", .7), (2, 1.0, "pop", .7), (2, 1.3, "sizzle", .8), (2, 1.4, "blip_down", .8), (2, 1.7, "blip_down", .8), (2, 2.0, "boing", .5), (2, 2.2, "pop", .8),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .3, "whoosh", .6), (3, .6, "pop", .8), (3, 1.2, "sparkle", .7), (3, 1.4, "pop", .6), (3, 1.6, "pop", .6), (3, 2.0, "ding", .6), (3, 2.3, "boing", .5), (3, 2.5, "pop", .8),
 (4, .05, "whoosh", .5), (4, .1, "boing", .5), (4, .3, "question", .7), (4, .6, "blip_down", .8), (4, 1.1, "pop", .6), (4, 1.25, "pop", .6), (4, 1.7, "tick", .8), (4, 2.2, "whoosh", .5), (4, 2.4, "ding", .6),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .6, "CHECK1", 1), (5, 1.05, "CHECK2", 1), (5, 1.5, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "pop", .5), (6, .9, "jingle", .9),
]
