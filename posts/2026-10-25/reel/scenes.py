"""형식: 밤사이 일기예보 v2 (검수 전 · 2026-10-25 일요일판) — 밤톨이 기상캐스터, 솜부엉 예보관, 별콩이 시청자.
장면 1 새 구도: '주간 증시 날씨' 바 + 초대형 ▼2.08% + 결론 리본 '사흘 내리 3%대 널뛰기' + 들쭉날쭉 일교차 그래프(요일별 날씨 아이콘) + 놀란 캐스터 클로즈업.
흐름: 1 결론 먼저 → 2 지난주 기온계(지수별 온도계) → 3 왜 널뛰었나(찬 바람·뜨거운 바람) → 4 주말 날씨(중동 태풍 주의보·기름값)
→ 5 다음 주 예보(일정 3 + 체크 3) → 6 마침. 숫자는 2026-10-25 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes flash{0%{opacity:0}8%{opacity:.8}20%{opacity:.1}30%{opacity:.55}100%{opacity:0}}
@keyframes drift{0%,100%{transform:translateX(0)}50%{transform:translateX(16px)}}
@keyframes spin{from{transform:rotate(0)}to{transform:rotate(-360deg)}}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes blow{0%{opacity:0;transform:translateX(var(--bx))}100%{opacity:1;transform:none}}
@keyframes wobble{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
.drift{animation:drift 2.2s ease-in-out infinite}
.spin{animation:spin 2.4s linear infinite}
.grow{transform-origin:50% 100%;animation:grow .5s cubic-bezier(.2,1.2,.4,1) both;animation-delay:var(--d,0s)}
.growd{transform-origin:50% 0%;animation:grow .5s cubic-bezier(.2,1.2,.4,1) both;animation-delay:var(--d,0s)}
.blow{animation:blow .55s cubic-bezier(.2,1.1,.4,1) both;animation-delay:var(--d,0s)}
.wob{animation:wobble .8s ease-in-out infinite}
</style>"""

def wxbar(text, top=186):
    """일기예보 시그니처 — 하늘색 방송 바 (0초부터 보임)."""
    return (f'<div class="abs" style="left:44px;top:{top}px;width:982px;height:104px;box-sizing:border-box;background:linear-gradient(90deg,#4F8EF0,#7FC3FF);'
            f'border:6px solid {L};border-radius:22px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;gap:18px;color:#fff">'
            f'<div style="flex:none;width:96px;height:96px;margin-top:-6px">{wx_icon("partly", 86)}</div>'
            f'<div style="font-size:60px;-webkit-text-stroke:6px {L};paint-order:stroke fill">{text}</div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·캐스터·일교차 그래프 틀이 모두 보인다
days = [("19", "sun", 1.76), ("20", "storm", -3.73), ("21", "sun", 3.29), ("22", "storm", -3.52), ("23", "partly", 0.30)]
gx = [400, 520, 640, 760, 870]
gy = [int(300 - v * 34) for _, _, v in days]
pts = " ".join(f"{x},{y}" for x, y in zip(gx, gy))
import math
glen = int(sum(math.hypot(gx[i+1]-gx[i], gy[i+1]-gy[i]) for i in range(4))) + 20
icons = "".join(
    f'<div class="abs a-pop" style="left:{x-50}px;top:24px;width:100px;--d:{.5+i*.12:.2f}s">{wx_icon(k, 90)}</div>'
    f'<div class="abs" style="left:{x-40}px;top:476px;width:80px;text-align:center;font-size:36px;color:#fff">{dd}일</div>'
    for i, ((dd, k, v), x, y) in enumerate(zip(days, gx, gy)))
dots = "".join(f'<div class="abs a-pop" style="left:{x-15}px;top:{y-15}px;width:30px;height:30px;border-radius:50%;background:#FFE36E;border:5px solid {L};box-sizing:border-box;--d:{.55+i*.12:.2f}s"></div>' for i, (x, y) in enumerate(zip(gx, gy)))
S[1] = (1, page(FX + f'''
{stars(12, 25, 0, 180)}
{head("밤사이 날씨 · 10.25 SUN", 1, "#F6EEE4")}
{wxbar("주간 증시 날씨")}
<div class="abs" style="left:0;width:1080px;top:316px;text-align:center;font-size:50px;color:#C9D6FF">코스피 · 지난주(19~23일)</div>
<div class="abs" style="left:0;width:1080px;top:376px;text-align:center"><span class="punch" style="--d:0s;font-size:230px;line-height:1;color:#7DBBFF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼2.08%</span></div>
<div class="abs" style="left:44px;top:636px;width:982px;height:130px;box-sizing:border-box;background:#FFE36E;border:6px solid {L};border-radius:65px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;font-size:78px">
  사흘 내리 <span style="color:#E8590C;margin:0 14px">3%대</span> 널뛰기
</div>
<div class="panel" style="left:44px;top:800px;width:982px;height:560px;background:#3C4485">
  <div class="abs" style="left:360px;top:300px;width:590px;border-top:4px dashed #8F98D8"></div>
  <div class="abs" style="left:372px;top:306px;font-size:28px;color:#C9D6FF">0</div>
  <svg class="abs" style="left:0;top:0;overflow:visible" width="982" height="560"><polyline points="{pts}" fill="none" stroke="#FFE36E" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"
    style="stroke-dasharray:{glen};--len:{glen};stroke-dashoffset:{glen};animation:draw .7s ease-out .45s both"/></svg>
  {dots}{icons}
  <div class="abs" style="left:-40px;top:130px;width:450px"><div class="shiver">{mascot("bamtol", "surprised", "point")}</div></div>
</div>
<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#fff;pointer-events:none;animation:flash .5s ease-out .3s both"></div>
{sfx("들쭉날쭉!", 70, 815, 84, .35, -8, "#FFE36E")}
''', "#262B55"))

# 2 ── 지난주 기온계: 오르면 따뜻(빨강), 내리면 추움(파랑)
def thermo(i, name, v, d):
    w, gap = 150, 38
    x = P + i * (w + gap)
    zero, scale = 560, 55
    h = int(abs(v) * scale)
    up = v > 0
    col = RED if up else BLUE
    bar_top = zero - h if up else zero
    cls = "grow" if up else "growd"
    sign = "▲" if up else "▼"
    return (f'<div class="abs" style="left:{x}px;top:200px;width:{w}px;text-align:center;font-size:44px">{name}</div>'
            f'<div class="abs" style="left:{x+45}px;top:270px;width:60px;height:610px;border-radius:30px;background:#fff;border:5px solid {L};box-sizing:border-box"></div>'
            f'<div class="abs {cls}" style="left:{x+55}px;top:{bar_top}px;width:40px;height:{max(h,6)}px;border-radius:20px;background:{col};--d:{d}s"></div>'
            f'<div class="abs a-pop" style="left:{x-10}px;top:892px;width:{w+20}px;text-align:center;font-size:44px;color:{col};--d:{d+.3:.2f}s">{sign}{abs(v):.2f}%</div>')
S[2] = (1, page(FX + f'''
{head("지난주 기온계", 2, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#E8F2FF">
  <div class="abs" style="left:0;right:0;top:34px;text-align:center;font-size:84px"><span class="punch" style="--d:.05s"><span style="color:{BLUE}">코스닥</span>이 제일 추웠다</span></div>
  <div class="abs" style="left:0;right:0;top:140px;text-align:center;font-size:34px;color:#55607A">한 주 등락 · 16일 종가 대비</div>
  <div class="abs" style="left:{P}px;top:560px;width:{IW}px;border-top:4px dashed #8C98B8"></div>
  {thermo(0, "다우", 0.41, .3)}{thermo(1, "S&amp;P", -0.47, .5)}{thermo(2, "나스닥", -0.71, .7)}{thermo(3, "코스피", -2.08, 1.0)}{thermo(4, "코스닥", -5.42, 1.3)}
  {ch(mascot("star", "teary", "down"), 40, 960, 230, 1.8, "a-sl", "shiver")}
  {bub("코스닥 <b>▼5.42%</b>,<br>꽁꽁 얼었어요…", 300, 1010, 2.0, "t-left", style="font-size:46px")}
</div>
''', "#2B3060"))

# 3 ── 왜 널뛰었나: 찬 바람과 뜨거운 바람
def wind(color):
    return (f'<svg viewBox="0 0 200 80" width="200" height="80"><path d="M10 25 H140 a18 18 0 1 0 -18 -18 M10 50 H170 a16 16 0 1 1 -16 16" fill="none" stroke="{color}" stroke-width="9" stroke-linecap="round"/></svg>')
def front(x, w, bg, col, title, sub, bx, d):
    return (f'<div class="abs blow" style="left:{x}px;top:250px;width:{w}px;height:470px;--bx:{bx}px;--d:{d}s;box-sizing:border-box;background:{bg};border:5px solid {L};border-radius:30px;text-align:center;padding:26px 16px">'
            f'<div class="wob" style="display:flex;justify-content:center">{wind(col)}</div>'
            f'<div style="font-size:54px;line-height:1.2;margin-top:14px;color:{col}">{title}</div>'
            f'<div style="font-size:40px;line-height:1.3;margin-top:16px">{sub}</div></div>')
S[3] = (1, page(FX + f'''
{head("왜 널뛰었을까?", 3, "#EDEAF8")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#EEE9FF">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:96px;line-height:1.12"><span class="punch" style="--d:.05s">바람 <span style="color:#7B3FC4">두 개</span>가<br>번갈아 불었다</span></div>
  {front(COL2[0][0], COL2[0][1], "#DCEBFF", BLUE, "찬 바람", "AI 투자<br>비용 걱정<br><span style='font-size:32px;color:#55607A'>메타 현금흐름<br>마이너스</span>", -200, .5)}
  {front(COL2[1][0], COL2[1][1], "#FFE3D6", RED, "뜨거운 바람", "중동발<br>기름값<br><span style='font-size:32px;color:#55607A'>중동 긴장에<br>유가 급등</span>", 200, .9)}
  {sfx("휘잉~", 600, 740, 80, 1.2, -6, "#BFD9FF")}
  {ch(mascot("owl", "normal", "point"), P, 820, 300, 1.6, "a-sl", "squish")}
  {bub("두 바람이 오가니<br><b>일교차</b>가 컸던 거예요", 360, 900, 1.9, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 주말 날씨: 중동에 태풍 주의보
typhoon = (f'<svg viewBox="0 0 200 200" width="300" height="300"><g class="spin" style="transform-origin:100px 100px">'
           f'<path d="M100 100 m-12 0 a12 12 0 1 1 24 0 a40 40 0 0 1 -60 34 M100 100 m12 0 a40 40 0 0 1 60 -34 M100 100 m0 -12 a50 50 0 0 1 50 -48 M100 100 m0 12 a50 50 0 0 1 -50 48" '
           f'fill="none" stroke="#9AA6E8" stroke-width="16" stroke-linecap="round"/><circle cx="100" cy="100" r="16" fill="#FFF6EA" stroke="{L}" stroke-width="5"/></g></svg>')
S[4] = (1, page(FX + f'''
{head("주말 날씨", 4, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#2F3570">
  <div class="abs" style="left:0;right:0;top:34px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="punch" style="--d:.05s">중동에 <span style="color:#FFB27F">태풍 주의보</span></span></div>
  <div class="abs a-pop" style="left:340px;top:150px;width:300px;--d:.2s">{typhoon}</div>
  <div class="abs a-sl" style="left:{P}px;top:470px;width:{IW}px;--d:.6s;box-sizing:border-box;background:#fff;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">트럼프 <b style="color:#E8590C;font-weight:400">'재타격' 언급</b></div>
  <div class="abs a-sr" style="left:{P}px;top:585px;width:{IW}px;--d:1.0s;box-sizing:border-box;background:#FFE3E3;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">이란 <b style="color:{RED};font-weight:400">보복 경고로 맞불</b></div>
  {numbox("브렌트유 (23일)", "116.72달러 ▲3.1%", COL2[0], 720, 1.4, RED)}
  {numbox("WTI (23일)", "103.27달러 ▲3.8%", COL2[1], 720, 1.6, RED)}
  {ch(mascot("bamtol", "worried", "point"), P, 900, 270, 2.0, "a-sl", "squish2")}
  {bub("기름값 태풍,<br><b>진로</b>를 지켜봐야 해요", 340, 960, 2.2, "t-left", style="font-size:46px")}
</div>
''', "#4A3E78"))

# 5 ── 다음 주 예보 (일정 3 + 체크 3)
def drow(i, date, day, t, d, hi=False):
    bg = "#FFD84D" if hi else "#fff"
    tag = f'<span style="margin-left:14px;font-size:28px;background:{L};color:#FFE59A;border-radius:999px;padding:2px 14px;vertical-align:middle">한국 영향 1순위</span>' if hi else ""
    return (f'<div class="abs a-sl" style="left:{P}px;top:{170+i*150}px;width:{IW}px;height:130px;box-sizing:border-box;--d:{d}s;background:{bg};border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:24px;padding:0 24px">'
            f'<div style="flex:none;width:150px;text-align:center"><div style="font-size:56px;line-height:1">{date}</div><div style="font-size:28px;color:#6B5A50">{day}</div></div>'
            f'<div style="font-size:44px;line-height:1.15">{t}{tag}</div></div>')
def chk(i, t, d):
    x, w = COL3[i]
    return (f'<div class="abs a-pop" style="left:{x}px;top:720px;width:{w}px;height:150px;box-sizing:border-box;--d:{d}s;background:#FFB27F;border:4px solid {L};border-radius:24px;text-align:center;padding-top:14px">'
            f'<div style="font-size:38px">체크 {i+1}</div><div style="font-size:46px">{t}</div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("다음 주 예보", 5, L)}
<div class="panel" style="left:44px;top:200px;width:982px;height:1080px;background:#FFFDF6">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:84px"><span class="punch" style="--d:.05s">다음 주 <span style="color:#E8590C">예보</span></span></div>
  {drow(0, "28", "수요일", "SK하이닉스 실적", .3, True)}
  {drow(1, "29", "목요일", "삼성전자 실적 · FOMC 결과", .6)}
  {drow(2, "주중", "미국", "MS·알파벳·아마존 실적", .9)}
  {chk(0, "반도체 실적", 1.4)}{chk(1, "기름값", 1.75)}{chk(2, "외국인", 2.1)}
  {cbub("실적이 기대를 넘으면 <b>맑음</b> 가능성!", 910, 2.5, "t-up", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1300px;color:#6B5A50;--d:2.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스1, 서울경제, 삼성전자, 한국경제, 뉴스핌, 이데일리</div>
''', "#FFE1CC"))

# 6 ── 마침: 내일 예보 + 팔로우
S[6] = (1, page(FX + f'''
{head("밤사이 날씨 · 마침", 6, L)}
<div class="panel" style="left:44px;top:200px;width:982px;height:1000px;background:#FFE9C2">
  <div class="abs" style="left:271px;top:600px;width:440px;height:440px;border-radius:50%;background:#FFC46B;border:6px solid {L};box-sizing:border-box;animation:sunrise .9s cubic-bezier(.2,.9,.3,1) both"></div>
  <div class="abs a-pop" style="left:0;right:0;top:60px;--d:.2s;text-align:center;font-size:44px">내일(월) 아침 예보</div>
  <div class="abs a-pop" style="left:0;right:0;top:130px;--d:.3s;text-align:center;font-size:90px;line-height:1.15">아침 8시<br>주말 시장 반응</div>
  <div class="abs a-rise" style="left:0;right:0;top:370px;--d:.5s;text-align:center;font-size:42px">미국 지수 선물 <span style="color:#E8590C">월요일 아침 7시</span> 거래 시작</div>
  {ch(mascot("owl", "happy", "wave"), 40, 640, 260, .5, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 680, 610, 270, .6, "a-sr", "hop")}
  {cbub("일교차 큰 한 주,<br><b>겉옷</b> 챙기세요!", 480, .8, "t-down", style="font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1250px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1390px;color:#6B5A50;--d:1.1s">출처: AP, 뉴스핌, 뉴스1, 서울경제, 한국경제, 이데일리, 이투데이<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.9, 1.6), 3: (3.9, 1.6), 4: (4.0, 1.6), 5: (4.4, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "forecast", .9), (1, .05, "thud", .8), (1, .3, "thunder", .9), (1, .35, "thud", .9), (1, .45, "whoosh", .6),
 (1, .55, "pop", .5), (1, .67, "pop", .5), (1, .79, "pop", .5), (1, .91, "pop", .5), (1, 1.03, "pop", .5),
 (2, .05, "thud", .7), (2, .3, "sparkle", .5), (2, .5, "blip_down", .5), (2, .7, "blip_down", .6), (2, 1.0, "blip_down", .7), (2, 1.3, "slidedown", .8), (2, 1.8, "sad", .5), (2, 2.0, "pop", .8),
 (3, .05, "thud", .7), (3, .5, "whoosh", .7), (3, .9, "whoosh", .7), (3, 1.2, "thud", .7), (3, 1.6, "boing", .6), (3, 1.9, "ding", .7),
 (4, .05, "thud", .7), (4, .2, "tension", .6), (4, .6, "whoosh", .5), (4, 1.0, "whoosh", .5), (4, 1.4, "pop", .6), (4, 1.6, "pop", .6), (4, 2.0, "boing", .5), (4, 2.2, "pop", .8),
 (5, .05, "forecast", .7), (5, .3, "whoosh", .5), (5, .6, "whoosh", .5), (5, .9, "whoosh", .5), (5, 1.4, "CHECK1", 1), (5, 1.75, "CHECK2", 1), (5, 2.1, "CHECK3", 1), (5, 2.5, "pop", .8),
 (6, .0, "sunrise", .8), (6, .3, "pop", .6), (6, .5, "boing", .6), (6, .8, "pop", .8), (6, 1.0, "jingle", .9),
]
