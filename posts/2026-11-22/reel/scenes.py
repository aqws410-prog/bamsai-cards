"""형식: 밤사이 일기예보 v6 (검수 전 · 2026-11-22 일요일판) — 밤톨이 기상캐스터, 솜부엉 예보관, 별콩이 시청자.
장면 1 새 구도: 위쪽 초대형 ▼7.95% + 결론 'AI 태풍에 서울도 휘청' + '태풍 특보' 도장 + 아래 위성 화면(소용돌이 태풍이 돌고, 뉴욕→서울 진로선이 0.5~0.95초에 그려짐) + 번개 번쩍 + 캐스터 클로즈업.
흐름: 1 결론 먼저 → 2 지수별 날씨 카드 5장(모두 비, 나스닥 폭풍) → 3 코스피 주간 날씨 달력(월·화 비, 수·목 갬, 금 태풍)
→ 4 주말 중동 하늘(트럼프 '영구적인 합의' / 이란 F-16 주장 → 미군 '거짓') + 엔비디아 SEC 조사 → 5 다음 주 예보(금통위·PCE·추수감사절 + 체크 3) → 6 마침.
핵심 비유: 미국에서 생긴 AI 태풍이 서울까지 올라왔다 / 금요일이 태풍 상륙일.
숫자는 2026-11-22 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes spin{from{transform:rotate(0)}to{transform:rotate(-360deg)}}
@keyframes flash{0%{opacity:0}10%{opacity:.75}100%{opacity:0}}
@keyframes streak{from{transform:translate(0,-60px)}to{transform:translate(-40px,160px)}}
@keyframes blinkp{0%,49%{opacity:1}50%,100%{opacity:.3}}
@keyframes sway{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
.spin{animation:spin 1.6s linear infinite}
.rainl{position:absolute;width:5px;height:46px;border-radius:3px;background:rgba(190,215,255,.8);animation:streak .55s linear infinite}
.sway{animation:sway 1.4s ease-in-out infinite;transform-origin:50% 100%}
</style>"""

def typhoon(cx, cy, r):
    """소용돌이 태풍 (위성 사진 느낌, 계속 돈다)."""
    arms = "".join(f'<path d="M0 0 C {r*.35} {-r*.15}, {r*.7} {r*.1}, {r*.95} {r*.55}" stroke="#F4F7FF" stroke-width="{r*.2:.0f}" stroke-linecap="round" fill="none" opacity=".9" transform="rotate({a})"/>' for a in (0, 90, 180, 270))
    return (f'<div class="abs" style="left:{cx-r}px;top:{cy-r}px;width:{2*r}px;height:{2*r}px"><svg class="spin" width="{2*r}" height="{2*r}" viewBox="{-r} {-r} {2*r} {2*r}" overflow="visible">'
            f'<circle r="{r*.92:.0f}" fill="rgba(230,238,255,.35)"/>{arms}<circle r="{r*.16:.0f}" fill="#1E2A5A" stroke="#F4F7FF" stroke-width="6"/></svg></div>')

def rain(n, seed, x0, x1, y0, y1):
    import random
    rnd = random.Random(seed)
    return "".join(f'<div class="rainl" style="left:{rnd.randint(x0,x1)}px;top:{rnd.randint(y0,y1)}px;animation-delay:-{rnd.random()*.55:.2f}s"></div>' for _ in range(n))

def track(x1, y1, x2, y2, d):
    import math
    ln = int(math.hypot(x2 - x1, y2 - y1)) + 10
    return (f'<svg class="abs" style="left:0;top:0;overflow:visible" width="982" height="610"><path d="M{x1} {y1} Q {(x1+x2)//2} {min(y1,y2)-170} {x2} {y2}" stroke="#FF5A5F" stroke-width="12" stroke-linecap="round" fill="none" '
            f'style="stroke-dasharray:{ln+200};--len:{ln+200};stroke-dashoffset:{ln+200};animation:draw .45s ease-out both;animation-delay:{d}s"/></svg>')

def pin(label, x, y, c, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:{y}px;--d:{d}s;text-align:center">'
            f'<div style="display:inline-block;background:{c};border:5px solid {L};border-radius:999px;padding:4px 22px;font-size:40px">{label}</div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·캐스터·위성 화면이 모두 보인다
S[1] = (1, page(FX + f'''
{stars(10, 122, 0, 160)}
{head("밤사이 날씨 · 11.22 SUN", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:200px;text-align:center;font-size:48px;color:#C9D6FF">코스피 · 지난주(11/16~20)</div>
<div class="abs" style="left:0;width:1080px;top:268px;text-align:center"><span class="punch" style="--d:0s;font-size:210px;line-height:1;color:#7DB4FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼7.95%</span></div>
<div class="abs" style="left:44px;top:520px;width:982px;height:200px;box-sizing:border-box;background:#E3ECFF;border:6px solid {L};border-radius:40px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;text-align:center;font-size:84px;line-height:1.15">
  <div><span style="color:{BLUE}">AI 태풍</span>에 서울도 휘청</div>
</div>
{stamp("태풍 특보", 700, 455, .35, 10)}
<div class="panel" style="left:44px;top:770px;width:982px;height:610px;background:#1E2A5A;overflow:hidden">
  {rain(26, 7, 0, 960, -40, 560)}
  {typhoon(300, 300, 190)}
  {track(860, 150, 330, 300, .5)}
  {pin("뉴욕", 760, 60, "#FFD6D6", .05)}
  {pin("서울", 230, 470, "#FFE36E", .9)}
  <div class="abs" style="left:610px;top:180px;width:360px"><div class="hop" style="animation:hop .6s ease-out .6s 1 both">{mascot("bamtol", "surprised", "point")}</div></div>
</div>
<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#EAF2FF;pointer-events:none;animation:flash .45s ease-out .3s both"></div>
{sfx("우르릉 쾅!", 70, 800, 70, .32, -8, "#FFE36E")}
''', "#262B55"))

# 2 ── 지수별 날씨 카드 5장: 모두 비, 나스닥은 폭풍
def card5(i, kind, name, val, d, hi=False):
    w, gap = 166, 18
    x = P + i * (w + gap)
    bg = "#D9E4FF" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:300px;width:{w}px;height:390px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:26px;text-align:center;padding-top:18px">'
            f'<div style="display:flex;justify-content:center">{wx_icon(kind, 120)}</div>'
            f'<div style="font-size:40px;line-height:1.2;margin-top:10px">{name}</div>'
            f'<div style="font-size:36px;line-height:1.2;margin-top:12px;color:{BLUE}">{val}</div></div>')
S[2] = (1, page(FX + f'''
{head("지난주 날씨 카드", 2, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#EEF2FA">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:88px;line-height:1.15"><span class="punch" style="--d:.05s">다섯 곳 모두 <span style="color:{BLUE}">비</span>,<br>나스닥은 <span style="color:{BLUE}">폭풍</span></span></div>
  {card5(0, "rain", "다우", "▼8.02%", .3)}{card5(1, "rain", "S&amp;P", "▼8.61%", .45)}{card5(2, "storm", "나스닥", "▼10.02%", .6, True)}{card5(3, "rain", "코스피", "▼7.95%", .85)}{card5(4, "rain", "코스닥", "▼7.72%", 1.05)}
  <div class="abs" style="left:0;right:0;top:720px;text-align:center;font-size:34px;color:#55607A">한 주 등락 · 11월 13일 종가 대비</div>
  {ch(mascot("star", "teary", "down"), 40, 820, 260, 1.4, "a-sl", "squish")}
  {bub("나스닥은 한 주에<br><b>▼10.02%</b>나 빠졌어요", 330, 880, 1.6, "t-left", style="font-size:50px")}
</div>
''', "#2B3060"))

# 3 ── 코스피 주간 날씨 달력
def day(i, dname, kind, val, color, d, hi=False):
    w, gap = 166, 18
    x = P + i * (w + gap)
    bg = "#D9E4FF" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:330px;width:{w}px;height:360px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:26px;text-align:center;padding-top:14px">'
            f'<div style="font-size:42px">{dname}</div>'
            f'<div style="display:flex;justify-content:center;margin-top:4px">{wx_icon(kind, 116)}</div>'
            f'<div style="font-size:38px;line-height:1.2;margin-top:8px;color:{color}">{val}</div></div>')
S[3] = (1, page(FX + f'''
{head("지난주 날씨 달력", 3, "#EDEAF8")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#EEE9FF">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:88px;line-height:1.15"><span class="punch" style="--d:.05s">잠깐 <span style="color:#E8590C">갰다가</span>,<br>금요일 <span style="color:{BLUE}">태풍 상륙</span></span></div>
  {day(0, "16일 월", "rain", "▼3.59%", BLUE, .3)}{day(1, "17일 화", "rain", "▼2.59%", BLUE, .45)}{day(2, "18일 수", "partly", "▲1.99%", RED, .6)}{day(3, "19일 목", "partly", "▲1.39%", RED, .85)}{day(4, "20일 금", "storm", "▼5.21%", BLUE, 1.05, True)}
  <div class="abs" style="left:0;right:0;top:720px;text-align:center;font-size:34px;color:#55607A">코스피 하루 등락</div>
  {ch(mascot("owl", "worried", "point"), P, 820, 280, 1.3, "a-sl", "squish")}
  {bub("금요일엔 <b>AI 투자 걱정</b>에<br>반도체가 크게 흔들렸어요", 340, 880, 1.5, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 주말: 중동 하늘 + 엔비디아 조사
def line(t, top, d, anim, bg):
    return (f'<div class="abs {anim}" style="left:{P}px;top:{top}px;width:{IW}px;--d:{d}s;box-sizing:border-box;background:{bg};border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center;line-height:1.25">{t}</div>')
S[4] = (1, page(FX + f'''
{head("주말 날씨", 4, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#2F3570">
  <div class="abs" style="left:0;right:0;top:34px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="punch" style="--d:.05s">중동엔 <span style="color:#FFE36E">말 바람</span></span></div>
  <div class="abs a-pop sway" style="left:390px;top:150px;--d:.15s">{wx_icon("cloud", 200)}</div>
  {line("트럼프: 이란과 <b style='color:#E8590C;font-weight:400'>영구적인 합의</b> 하겠다<br><span style='font-size:32px'>21일(현지) 인터뷰 · 이란 핵무기 보유를 막는 합의</span>", 390, .4, "a-sl", "#fff")}
  {line("이란: 미군 F-16 공격했다<br><span style='font-size:32px'>미군(중부사령부) 21일 반박</span>", 590, .8, "a-sr", "#E6F0FF")}
  {stamp("거짓", 760, 560, 1.15, 12)}
  {line("엔비디아 <b style='color:{BLUE};font-weight:400'>회계 조사</b> 보도 (로이터)<br><span style='font-size:32px'>싱가포르 매출 공시 방식 주목 · 위법 확정 아님</span>", 770, 1.5, "a-sl", "#fff")}
  {ch(mascot("bamtol", "normal", "point"), P, 960, 230, 1.9, "a-sl", "squish")}
  {bub("미국 지수 선물은<br><b>월요일 아침 8시</b> 열려요", 300, 1000, 2.1, "t-left", style="font-size:46px")}
</div>
''', "#4A3E78"))

# 5 ── 다음 주 예보 (일정 3 + 체크 3)
def drow(i, date, dayname, t, d, hi=False):
    bg = "#FFD84D" if hi else "#fff"
    tag = f'<span style="margin-left:14px;font-size:28px;background:{L};color:#FFE59A;border-radius:999px;padding:2px 14px;vertical-align:middle">한국 영향 1순위</span>' if hi else ""
    return (f'<div class="abs a-sl" style="left:{P}px;top:{170+i*150}px;width:{IW}px;height:130px;box-sizing:border-box;--d:{d}s;background:{bg};border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:24px;padding:0 24px">'
            f'<div style="flex:none;width:170px;text-align:center"><div style="font-size:52px;line-height:1">{date}</div><div style="font-size:26px;color:#6B5A50">{dayname}</div></div>'
            f'<div style="font-size:42px;line-height:1.15">{t}{tag}</div></div>')
def chk(i, t, d):
    x, w = COL3[i]
    return (f'<div class="abs a-pop" style="left:{x}px;top:690px;width:{w}px;height:170px;box-sizing:border-box;--d:{d}s;background:#FFB27F;border:4px solid {L};border-radius:24px;text-align:center;padding-top:16px">'
            f'<div style="font-size:36px">체크 {i+1}</div><div style="font-size:42px;line-height:1.15;margin-top:6px">{t}</div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("다음 주 예보", 5, L)}
<div class="panel" style="left:44px;top:200px;width:982px;height:1080px;background:#FFFDF6">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:84px"><span class="punch" style="--d:.05s">다음 주 <span style="color:#E8590C">예보</span></span></div>
  {drow(0, "26", "목요일", "한은 금통위<br><span style='font-size:30px'>3.00% → 3.25% 인상 전망</span>", .3, True)}
  {drow(1, "주중", "미국 현지", "미국 10월 PCE 물가<br><span style='font-size:30px'>(연준이 중시하는 물가)</span>", .6)}
  {drow(2, "26·27", "미국 현지", "추수감사절 휴장·<br>27일 조기 폐장", .9)}
  {chk(0, "반도체<br>흐름", 1.4)}{chk(1, "한은<br>금통위", 1.75)}{chk(2, "미국<br>물가", 2.1)}
  {cbub("한국엔 <b>26일 금통위</b>가<br>가장 큰 변수예요", 915, 2.5, "t-up", style="font-size:44px")}
</div>
<div class="src a-fade" style="top:1300px;color:#6B5A50;--d:2.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 이투데이, 뉴스웍스, 포인트데일리, 아주경제, 마켓잉크</div>
''', "#FFE1CC"))

# 6 ── 마침
S[6] = (1, page(FX + f'''
{head("밤사이 날씨 · 마침", 6, L)}
<div class="panel" style="left:44px;top:200px;width:982px;height:1000px;background:#FFE9C2">
  <div class="abs" style="left:271px;top:600px;width:440px;height:440px;border-radius:50%;background:#FFC46B;border:6px solid {L};box-sizing:border-box;animation:sunrise .9s cubic-bezier(.2,.9,.3,1) both"></div>
  <div class="abs a-pop" style="left:0;right:0;top:60px;--d:.2s;text-align:center;font-size:44px">내일(월) 아침 예보</div>
  <div class="abs a-pop" style="left:0;right:0;top:130px;--d:.3s;text-align:center;font-size:90px;line-height:1.15">아침 8시<br>주말 시장 반응</div>
  <div class="abs a-rise" style="left:0;right:0;top:370px;--d:.5s;text-align:center;font-size:42px">미국 지수 선물 <span style="color:#E8590C">월요일 아침 8시</span> 거래 시작</div>
  {ch(mascot("star", "happy", "wave"), 40, 640, 250, .5, "a-sl", "hop")}
  {ch(mascot("moon", "happy", "wave"), 690, 630, 250, .6, "a-sr", "squish")}
  {cbub("태풍 지나간 뒤,<br>다음 주 <b>예보</b>도 챙겨요!", 480, .8, "t-down", style="font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1250px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1390px;color:#6B5A50;--d:1.1s">출처: AP, 파이낸셜뉴스, 마켓잉크, 아주경제, 로이터, 이투데이<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.6), 3: (3.6, 1.6), 4: (4.4, 1.6), 5: (4.4, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "forecast", .9), (1, .05, "rain", .5), (1, .3, "thunder", .9), (1, .35, "thud", .8),
 (1, .5, "whoosh", .6), (1, .6, "boing", .6), (1, .9, "ding", .6),
 (2, .05, "thud", .7), (2, .3, "pop", .4), (2, .45, "pop", .4), (2, .6, "thunder", .5), (2, .85, "pop", .4), (2, 1.05, "pop", .5), (2, 1.4, "sad", .5), (2, 1.6, "pop", .8),
 (3, .05, "thud", .7), (3, .3, "rain", .4), (3, .6, "sparkle", .5), (3, .85, "sparkle", .4), (3, 1.05, "thunder", .6), (3, 1.3, "boing", .6), (3, 1.5, "pop", .8),
 (4, .05, "thud", .6), (4, .15, "whoosh", .5), (4, .4, "whoosh", .5), (4, .8, "whoosh", .5), (4, 1.15, "thud", .8), (4, 1.5, "whoosh", .5), (4, 1.9, "boing", .5), (4, 2.1, "pop", .8),
 (5, .05, "forecast", .7), (5, .3, "whoosh", .5), (5, .6, "whoosh", .5), (5, .9, "whoosh", .5), (5, 1.4, "CHECK1", 1), (5, 1.75, "CHECK2", 1), (5, 2.1, "CHECK3", 1), (5, 2.5, "pop", .8),
 (6, .0, "sunrise", .8), (6, .3, "pop", .6), (6, .5, "boing", .6), (6, .8, "pop", .8), (6, 1.0, "jingle", .9),
]
