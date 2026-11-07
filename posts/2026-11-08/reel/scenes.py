"""형식: 밤사이 일기예보 v4 (검수 전 · 2026-11-08 일요일판) — 밤톨이 기상캐스터, 솜부엉 예보관, 별콩이 시청자.
장면 1 새 구도: 고드름 달린 '한파 특보' 바 + 초대형 ▼11.71% + 결론 리본 '코스피, 한 주 새 한파' + 일기도(뉴욕→서울로 그어지는 한랭전선, 서울 위 눈송이) + 놀란 캐스터 클로즈업(오른쪽).
흐름: 1 결론 먼저 → 2 지수별 날씨 카드 5장(미국은 비, 한국은 눈보라) → 3 주간 날씨 달력(목·금 눈폭풍, 금요일 서킷브레이커)
→ 4 주말 날씨: 중동에 번개 한 번(소규모 공습) + "대화 중" → 5 다음 주 예보(일정 3 + 체크 3) → 6 마침.
핵심 비유: 미국에서 불어온 찬 바람(AI 데이터센터 규제 걱정)이 서울에선 한파가 됐다(한랭전선).
숫자는 2026-11-08 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes flash{0%{opacity:0}8%{opacity:.8}20%{opacity:.1}30%{opacity:.55}100%{opacity:0}}
@keyframes drift{0%,100%{transform:translateX(0)}50%{transform:translateX(16px)}}
@keyframes snowfall{from{transform:translateY(-40px) rotate(0)}to{transform:translateY(420px) rotate(200deg)}}
@keyframes bolt{0%,100%{opacity:0}5%,15%{opacity:1}10%{opacity:.2}}
@keyframes icicle{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.12)}}
.drift{animation:drift 2.2s ease-in-out infinite}
.flake{position:absolute;animation:snowfall 1.8s linear infinite}
.icy{transform-origin:50% 0;animation:icicle 1.2s ease-in-out infinite}
</style>"""

def flake_svg(s=40, c="#FFFFFF"):
    arms = "".join(f'<path d="M20 4 V36 M14 9 L20 14 L26 9 M14 31 L20 26 L26 31" transform="rotate({a} 20 20)"/>' for a in (0, 60, 120))
    return f'<svg viewBox="0 0 40 40" width="{s}" height="{s}"><g stroke="{c}" stroke-width="3.4" stroke-linecap="round" fill="none">{arms}</g></svg>'

def snow(n, x0, x1, top, seed, s=(26, 44)):
    import random
    r = random.Random(seed)
    return "".join(f'<div class="flake" style="left:{r.randint(x0, x1)}px;top:{top}px;animation-delay:-{r.random()*1.8:.2f}s">{flake_svg(r.randint(*s))}</div>' for _ in range(n))

def snow_icon(s=120):
    """눈구름 아이콘 (wx_icon과 같은 비율)."""
    fl = "".join(f'<g transform="translate({x} 82) scale(.42)"><g stroke="#5B8DEF" stroke-width="7" stroke-linecap="round" fill="none"><path d="M0 -14 V14"/><path d="M-12 -7 L12 7"/><path d="M-12 7 L12 -7"/></g></g>' for x in (34, 52, 70))
    cloud = f'<path d="M24 66 a16 16 0 0 1 4 -31 a22 22 0 0 1 41 -6 a17 17 0 0 1 9 37 z" fill="#EAF2FF" stroke="{L}" stroke-width="4" stroke-linejoin="round"/>'
    return f'<svg viewBox="0 0 100 110" width="{s}" height="{s*1.1:.0f}" overflow="visible">{cloud}{fl}</svg>'

def icon(kind, s):
    return snow_icon(s) if kind == "snow" else wx_icon(kind, s)

def coldbar(text, top=186):
    """한파 특보 바 — 하늘색 방송 바 + 고드름 (0초부터 보임)."""
    ic = "".join(f'<div class="abs icy" style="left:{x}px;top:96px;width:0;height:0;border-left:{w}px solid transparent;border-right:{w}px solid transparent;border-top:{h}px solid #DFF1FF;animation-delay:-{i*.17:.2f}s"></div>'
                 for i, (x, w, h) in enumerate([(60, 12, 46), (150, 9, 30), (250, 14, 56), (420, 10, 36), (600, 13, 50), (760, 9, 28), (880, 12, 44)]))
    return (f'<div class="abs" style="left:44px;top:{top}px;width:982px;height:104px;box-sizing:border-box;background:linear-gradient(90deg,#3D7BE0,#8FD0FF);'
            f'border:6px solid {L};border-radius:22px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;gap:18px;color:#fff">'
            f'<div style="flex:none">{flake_svg(70)}</div>'
            f'<div style="font-size:62px;-webkit-text-stroke:6px {L};paint-order:stroke fill">한파 특보 · {text}</div>'
            f'<div style="flex:none">{flake_svg(70)}</div>{ic}</div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·캐스터·일기도가 모두 보인다
# 한랭전선: 뉴욕(왼쪽 아래) → 서울(오른쪽 위)로 그어지는 파란 선 + 삼각형 표시
front_path = "M70 430 C 170 330, 260 380, 340 270 S 470 160, 560 150"
tris = "".join(f'<path d="M{x} {y} l18 -6 l-4 20 z" fill="#3D7BE0" stroke="{L}" stroke-width="3" class="a-pop" style="--d:{d}s;transform-box:fill-box;transform-origin:center"/>'
               for x, y, d in [(150, 352, .62), (255, 352, .72), (340, 262, .82), (440, 190, .92)])
wmap = (f'<div class="abs" style="left:24px;top:24px;width:600px;height:532px;border-radius:26px;background:#CFE6F5;border:5px solid {L};box-sizing:border-box;overflow:hidden">'
        f'<div class="abs" style="left:-60px;top:360px;width:300px;height:240px;border-radius:50%;background:#B9D8A6;border:5px solid {L}"></div>'
        f'<div class="abs" style="left:440px;top:50px;width:120px;height:200px;border-radius:45% 55% 50% 50%;background:#B9D8A6;border:5px solid {L};transform:rotate(14deg)"></div>'
        f'<div class="abs" style="left:24px;top:470px;font-size:38px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill">● 뉴욕</div>'
        f'<div class="abs" style="left:420px;top:250px;font-size:38px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill">● 서울</div>'
        f'<svg class="abs" style="left:0;top:0;overflow:visible" width="600" height="532"><path d="{front_path}" fill="none" stroke="#3D7BE0" stroke-width="10" stroke-linecap="round" '
        f'style="stroke-dasharray:640;stroke-dashoffset:640;animation:draw .45s ease-out .55s both;--len:640"/>{tris}</svg>'
        f'{snow(9, 380, 580, -20, 11)}'
        f'<div class="abs a-pop" style="left:20px;top:20px;--d:.95s;background:{L};color:#BFE3FF;border-radius:999px;padding:4px 18px;font-size:32px">한랭전선</div>'
        f'</div>')
S[1] = (1, page(FX + f'''
{stars(12, 41, 0, 180)}
{head("밤사이 날씨 · 11.08 SUN", 1, "#F6EEE4")}
{coldbar("주간 증시")}
<div class="abs" style="left:0;width:1080px;top:330px;text-align:center;font-size:50px;color:#C9D6FF">코스피 · 지난주(11/2~6)</div>
<div class="abs" style="left:0;width:1080px;top:398px;text-align:center"><span class="punch" style="--d:0s;font-size:200px;line-height:1;color:#7DBBFF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼11.71%</span></div>
<div class="abs" style="left:44px;top:646px;width:982px;height:124px;box-sizing:border-box;background:#EAF6FF;border:6px solid {L};border-radius:62px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;font-size:76px">
  코스피, 한 주 새 <span style="color:{BLUE};margin-left:14px">한파</span>
</div>
{stamp("특보", 834, 286, .35, 12)}
<div class="panel" style="left:44px;top:800px;width:982px;height:580px;background:#2E3570">
  {wmap}
  <div class="abs" style="left:600px;top:170px;width:300px"><div class="shiver">{mascot("bamtol", "surprised", "point")}</div></div>
</div>
<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#fff;pointer-events:none;animation:flash .5s ease-out .3s both"></div>
{sfx("부르르!", 660, 830, 76, .7, 8, "#BFE3FF")}
''', "#262B55"))

# 2 ── 지수별 날씨 카드 5장
def card5(i, kind, name, val, color, d):
    w, gap = 166, 18
    x = P + i * (w + gap)
    return (f'<div class="abs a-pop" style="left:{x}px;top:300px;width:{w}px;height:390px;box-sizing:border-box;--d:{d}s;background:#fff;border:5px solid {L};border-radius:26px;text-align:center;padding-top:18px">'
            f'<div style="display:flex;justify-content:center">{icon(kind, 120)}</div>'
            f'<div style="font-size:40px;line-height:1.2;margin-top:10px">{name}</div>'
            f'<div style="font-size:38px;line-height:1.2;margin-top:12px;color:{color}">{val}</div></div>')
S[2] = (1, page(FX + f'''
{head("지난주 날씨 카드", 2, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#E8F2FF">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:88px;line-height:1.15"><span class="punch" style="--d:.05s">미국은 <span style="color:#5B8DEF">비</span>,<br>한국은 <span style="color:{BLUE}">눈보라</span></span></div>
  {card5(0, "cloud", "다우", "▼0.94%", BLUE, .3)}{card5(1, "rain", "S&amp;P", "▼2.68%", BLUE, .45)}{card5(2, "rain", "나스닥", "▼3.37%", BLUE, .6)}{card5(3, "snow", "코스피", "▼11.71%", BLUE, .9)}{card5(4, "snow", "코스닥", "▼11.06%", BLUE, 1.1)}
  <div class="abs" style="left:0;right:0;top:720px;text-align:center;font-size:34px;color:#55607A">한 주 등락 · 10월 30일 종가 대비</div>
  {ch(mascot("star", "teary", "down"), 40, 820, 260, 1.5, "a-sl", "shiver")}
  {bub("미국의 찬 바람이<br>서울에선 <b>눈보라</b>로!", 330, 880, 1.7, "t-left", style="font-size:50px")}
</div>
''', "#2B3060"))

# 3 ── 주간 날씨 달력: 목·금 눈폭풍
def day(i, dname, kind, val, color, d, hi=False):
    w, gap = 166, 18
    x = P + i * (w + gap)
    bg = "#DCEBFF" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:330px;width:{w}px;height:360px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:26px;text-align:center;padding-top:14px">'
            f'<div style="font-size:42px">{dname}</div>'
            f'<div style="display:flex;justify-content:center;margin-top:4px">{icon(kind, 116)}</div>'
            f'<div style="font-size:38px;line-height:1.2;margin-top:8px;color:{color}">{val}</div></div>')
S[3] = (1, page(FX + f'''
{head("지난주 날씨 달력", 3, "#EDEAF8")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#EEE9FF">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:92px;line-height:1.15"><span class="punch" style="--d:.05s">목·금 이틀<br><span style="color:{BLUE}">눈폭풍</span></span></div>
  {day(0, "2일 월", "sun", "▲2.24%", RED, .3)}{day(1, "3일 화", "rain", "▼3.59%", BLUE, .45)}{day(2, "4일 수", "partly", "▲0.62%", RED, .6)}{day(3, "5일 목", "snow", "▼5.28%", BLUE, .85, True)}{day(4, "6일 금", "snow", "▼6.02%", BLUE, 1.05, True)}
  <div class="abs" style="left:0;right:0;top:720px;text-align:center;font-size:34px;color:#55607A">코스피 하루 등락</div>
  {ch(mascot("owl", "worried", "point"), P, 820, 280, 1.3, "a-sl", "squish")}
  {bub("금요일엔 <b>서킷브레이커</b><br>(거래 잠깐 멈춤)까지!", 340, 880, 1.5, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 주말 날씨: 중동에 번개 한 번
S[4] = (1, page(FX + f'''
{head("주말 날씨", 4, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#2F3570">
  <div class="abs" style="left:0;top:0;width:982px;height:1200px;background:#fff;animation:bolt 1.6s linear .3s infinite;pointer-events:none;mix-blend-mode:overlay"></div>
  <div class="abs" style="left:0;right:0;top:34px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="punch" style="--d:.05s">중동에 <span style="color:#FFE36E">번개</span> 한 번</span></div>
  <div class="abs" style="left:371px;top:150px;width:240px"><div class="drift">{wx_icon("storm", 230)}</div></div>
  <div class="abs a-sl" style="left:{P}px;top:430px;width:{IW}px;--d:.4s;box-sizing:border-box;background:#fff;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">6일(현지) 미국, 이란 <b style="color:#E8590C;font-weight:400">"소규모" 공습</b></div>
  <div class="abs a-sr" style="left:{P}px;top:545px;width:{IW}px;--d:.8s;box-sizing:border-box;background:#E6F0FF;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">트럼프 <b style="color:{BLUE};font-weight:400">"이란과 대화 중"</b></div>
  {numbox("브렌트유 (6일)", "▲0.03%", COL2[0], 680, 1.2, RED)}
  {numbox("원/달러 1,356.6원 (6일)", "▲14.5원", COL2[1], 680, 1.4, RED)}
  {ch(mascot("bamtol", "worried", "point"), P, 900, 270, 1.8, "a-sl", "squish2")}
  {bub("번개가 또 칠지,<br><b>구름이 걷힐지</b> 지켜봐요", 340, 950, 2.0, "t-left", style="font-size:46px")}
</div>
''', "#4A3E78"))

# 5 ── 다음 주 예보 (일정 3 + 체크 3)
def drow(i, date, dayname, t, d, hi=False):
    bg = "#FFD84D" if hi else "#fff"
    tag = f'<span style="margin-left:14px;font-size:28px;background:{L};color:#FFE59A;border-radius:999px;padding:2px 14px;vertical-align:middle">한국 영향 1순위</span>' if hi else ""
    return (f'<div class="abs a-sl" style="left:{P}px;top:{170+i*150}px;width:{IW}px;height:130px;box-sizing:border-box;--d:{d}s;background:{bg};border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:24px;padding:0 24px">'
            f'<div style="flex:none;width:150px;text-align:center"><div style="font-size:56px;line-height:1">{date}</div><div style="font-size:28px;color:#6B5A50">{dayname}</div></div>'
            f'<div style="font-size:44px;line-height:1.15">{t}{tag}</div></div>')
def chk(i, t, d):
    x, w = COL3[i]
    return (f'<div class="abs a-pop" style="left:{x}px;top:690px;width:{w}px;height:170px;box-sizing:border-box;--d:{d}s;background:#FFB27F;border:4px solid {L};border-radius:24px;text-align:center;padding-top:16px">'
            f'<div style="font-size:36px">체크 {i+1}</div><div style="font-size:42px;line-height:1.15;margin-top:6px">{t}</div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("다음 주 예보", 5, L)}
<div class="panel" style="left:44px;top:200px;width:982px;height:1080px;background:#FFFDF6">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:84px"><span class="punch" style="--d:.05s">다음 주 <span style="color:#E8590C">예보</span></span></div>
  {drow(0, "10", "화요일 밤", "미국 10월 CPI(물가)", .3)}
  {drow(1, "11", "수요일 아침", "코어위브 실적", .6, True)}
  {drow(2, "12", "목요일", "옵션 만기일", .9)}
  {chk(0, "코어위브<br>AI 투자", 1.4)}{chk(1, "미국<br>물가", 1.75)}{chk(2, "이란<br>공습·협상", 2.1)}
  {cbub("한파가 풀릴지는<br><b>AI 실적·물가</b>에 달렸어요", 915, 2.5, "t-up", style="font-size:44px")}
</div>
<div class="src a-fade" style="top:1300px;color:#6B5A50;--d:2.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 아주경제, 연합인포맥스, 이투데이, 코어위브 공시, 미 노동통계국</div>
''', "#FFE1CC"))

# 6 ── 마침: 내일 예보 + 팔로우
S[6] = (1, page(FX + f'''
{head("밤사이 날씨 · 마침", 6, L)}
<div class="panel" style="left:44px;top:200px;width:982px;height:1000px;background:#FFE9C2">
  <div class="abs" style="left:271px;top:600px;width:440px;height:440px;border-radius:50%;background:#FFC46B;border:6px solid {L};box-sizing:border-box;animation:sunrise .9s cubic-bezier(.2,.9,.3,1) both"></div>
  <div class="abs a-pop" style="left:0;right:0;top:60px;--d:.2s;text-align:center;font-size:44px">내일(월) 아침 예보</div>
  <div class="abs a-pop" style="left:0;right:0;top:130px;--d:.3s;text-align:center;font-size:90px;line-height:1.15">아침 8시<br>주말 시장 반응</div>
  <div class="abs a-rise" style="left:0;right:0;top:370px;--d:.5s;text-align:center;font-size:42px">미국 지수 선물 <span style="color:#E8590C">월요일 아침 8시</span> 거래 시작</div>
  {ch(mascot("owl", "happy", "wave"), 40, 640, 260, .5, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 680, 610, 270, .6, "a-sr", "hop")}
  {cbub("추운 한 주였죠,<br><b>예보</b> 챙겨 보세요!", 480, .8, "t-down", style="font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1250px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1390px;color:#6B5A50;--d:1.1s">출처: AP, 뉴스핌, 이투데이, 아주경제, 서울경제, 한국일보, 파이낸셜뉴스, 뉴스1<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.6), 3: (3.6, 1.6), 4: (4.0, 1.6), 5: (4.4, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "forecast", .9), (1, .05, "thud", .8), (1, .3, "sparkle", .6), (1, .35, "thud", .9),
 (1, .55, "whoosh", .6), (1, .7, "boing", .5), (1, .95, "pop", .6),
 (2, .05, "thud", .7), (2, .3, "blip_down", .5), (2, .45, "rain", .4), (2, .6, "blip_down", .6), (2, .9, "slidedown", .6), (2, 1.1, "blip_down", .6), (2, 1.5, "sad", .5), (2, 1.7, "pop", .8),
 (3, .05, "thud", .7), (3, .3, "sunrise", .5), (3, .45, "blip_down", .5), (3, .6, "pop", .5), (3, .85, "slidedown", .6), (3, 1.05, "blip_down", .6), (3, 1.3, "boing", .6), (3, 1.5, "pop", .8),
 (4, .05, "thud", .6), (4, .3, "thunder", .8), (4, .4, "whoosh", .5), (4, .8, "whoosh", .5), (4, 1.2, "pop", .6), (4, 1.4, "pop", .6), (4, 1.8, "boing", .5), (4, 2.0, "pop", .8),
 (5, .05, "forecast", .7), (5, .3, "whoosh", .5), (5, .6, "whoosh", .5), (5, .9, "whoosh", .5), (5, 1.4, "CHECK1", 1), (5, 1.75, "CHECK2", 1), (5, 2.1, "CHECK3", 1), (5, 2.5, "pop", .8),
 (6, .0, "sunrise", .8), (6, .3, "pop", .6), (6, .5, "boing", .6), (6, .8, "pop", .8), (6, 1.0, "jingle", .9),
]
