"""형식: 밤사이 일기예보 v3 (검수 전 · 2026-11-01 일요일판) — 밤톨이 기상캐스터, 솜부엉 예보관, 별콩이 시청자.
장면 1 새 구도: '주간 증시 날씨' 바 + 초대형 ▲3.25% + 결론 리본 '소나기 맞고도 한 주는 맑음' + 회전하는 기상 레이더 화면 + 놀란 캐스터 클로즈업(오른쪽).
흐름: 1 결론 먼저 → 2 지수별 날씨 카드 5장(미국은 비, 코스피만 해) → 3 땡볕(28일 ▲6.63%) vs 소나기(금요일 3%대 급락)
→ 4 주말 날씨: 중동 하늘 짙은 안개(재공격 '아직 결정 안 해') → 5 다음 주 예보(일정 3 + 체크 3) → 6 마침.
숫자는 2026-11-01 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes flash{0%{opacity:0}8%{opacity:.8}20%{opacity:.1}30%{opacity:.55}100%{opacity:0}}
@keyframes drift{0%,100%{transform:translateX(0)}50%{transform:translateX(16px)}}
@keyframes radar{from{transform:rotate(0)}to{transform:rotate(360deg)}}
@keyframes fogmove{0%,100%{transform:translateX(-30px)}50%{transform:translateX(30px)}}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes sunspin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
.drift{animation:drift 2.2s ease-in-out infinite}
.sweep{transform-origin:50% 50%;animation:radar 1.6s linear infinite}
.fog{animation:fogmove 3s ease-in-out infinite}
.sunspin{animation:sunspin 6s linear infinite}
</style>"""

def wxbar(text, top=186):
    """일기예보 시그니처 — 하늘색 방송 바 (0초부터 보임)."""
    return (f'<div class="abs" style="left:44px;top:{top}px;width:982px;height:104px;box-sizing:border-box;background:linear-gradient(90deg,#4F8EF0,#7FC3FF);'
            f'border:6px solid {L};border-radius:22px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;gap:18px;color:#fff">'
            f'<div style="flex:none;width:96px;height:96px;margin-top:-6px">{wx_icon("partly", 86)}</div>'
            f'<div style="font-size:60px;-webkit-text-stroke:6px {L};paint-order:stroke fill">{text}</div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·캐스터·레이더 화면이 모두 보인다
R = 210
blips = [(150, 110, RED, .5, 34), (290, 160, "#7DBBFF", .62, 22), (110, 270, "#7DBBFF", .74, 22), (300, 300, "#7DBBFF", .86, 22), (200, 210, "#FFE36E", .98, 26)]
blip_html = "".join(f'<div class="abs a-pop" style="left:{x-s//2}px;top:{y-s//2}px;width:{s}px;height:{s}px;border-radius:50%;background:{c};border:4px solid {L};--d:{d}s"></div>' for x, y, c, d, s in blips)
radar = (f'<div class="abs" style="left:40px;top:60px;width:{2*R}px;height:{2*R}px;border-radius:50%;background:#1F4A3A;border:8px solid {L};box-sizing:border-box;overflow:hidden">'
         f'<div class="abs" style="left:{R//2-8}px;top:{R//2-8}px;width:{R}px;height:{R}px;border-radius:50%;border:3px solid #4FA37A"></div>'
         f'<div class="abs" style="left:0;top:{R-8}px;width:{2*R}px;border-top:3px solid #4FA37A"></div>'
         f'<div class="abs" style="left:{R-8}px;top:0;height:{2*R}px;border-left:3px solid #4FA37A"></div>'
         f'<div class="abs sweep" style="left:0;top:0;width:{2*R-16}px;height:{2*R-16}px;background:conic-gradient(from 0deg,rgba(120,255,170,.55),rgba(120,255,170,0) 70deg,rgba(0,0,0,0) 360deg);border-radius:50%"></div>'
         f'{blip_html}</div>'
         f'<div class="abs" style="left:40px;top:500px;width:{2*R}px;text-align:center;font-size:36px;color:#C9D6FF">밤사이 기상 레이더</div>')
S[1] = (1, page(FX + f'''
{stars(12, 41, 0, 180)}
{head("밤사이 날씨 · 11.01 SUN", 1, "#F6EEE4")}
{wxbar("주간 증시 날씨")}
<div class="abs" style="left:0;width:1080px;top:316px;text-align:center;font-size:50px;color:#C9D6FF">코스피 · 지난주(26~30일)</div>
<div class="abs" style="left:0;width:1080px;top:376px;text-align:center"><span class="punch" style="--d:0s;font-size:230px;line-height:1;color:#FF6B6B;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲3.25%</span></div>
<div class="abs" style="left:44px;top:636px;width:982px;height:130px;box-sizing:border-box;background:#FFE36E;border:6px solid {L};border-radius:65px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;font-size:74px">
  소나기 맞고도 한 주는 <span style="color:{RED};margin-left:14px">맑음</span>
</div>
<div class="panel" style="left:44px;top:800px;width:982px;height:580px;background:#2E3570">
  {radar}
  <div class="abs" style="left:470px;top:60px;width:410px"><div class="shiver">{mascot("bamtol", "surprised", "point")}</div></div>
</div>
<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#fff;pointer-events:none;animation:flash .5s ease-out .3s both"></div>
{sfx("쨍!", 450, 830, 100, .35, -10, "#FFE36E")}
''', "#262B55"))

# 2 ── 지수별 날씨 카드 5장
def card5(i, kind, name, val, color, d):
    w, gap = 166, 18
    x = P + i * (w + gap)
    return (f'<div class="abs a-pop" style="left:{x}px;top:300px;width:{w}px;height:390px;box-sizing:border-box;--d:{d}s;background:#fff;border:5px solid {L};border-radius:26px;text-align:center;padding-top:18px">'
            f'<div style="display:flex;justify-content:center">{wx_icon(kind, 120)}</div>'
            f'<div style="font-size:40px;line-height:1.2;margin-top:10px">{name}</div>'
            f'<div style="font-size:40px;line-height:1.2;margin-top:12px;color:{color}">{val}</div></div>')
S[2] = (1, page(FX + f'''
{head("지난주 날씨 카드", 2, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#E8F2FF">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:88px;line-height:1.15"><span class="punch" style="--d:.05s">미국은 <span style="color:{BLUE}">비</span>,<br>코스피만 <span style="color:{RED}">해</span></span></div>
  {card5(0, "rain", "다우", "▼0.85%", BLUE, .3)}{card5(1, "rain", "S&amp;P", "▼0.57%", BLUE, .45)}{card5(2, "storm", "나스닥", "▼2.00%", BLUE, .6)}{card5(3, "sun", "코스피", "▲3.25%", RED, .9)}{card5(4, "rain", "코스닥", "▼3.63%", BLUE, 1.1)}
  <div class="abs" style="left:0;right:0;top:720px;text-align:center;font-size:34px;color:#55607A">한 주 등락 · 23일 종가 대비</div>
  {ch(mascot("star", "happy", "up"), 40, 820, 260, 1.5, "a-sl", "hop")}
  {bub("코스피만<br><b>해가 떴어요!</b>", 330, 880, 1.7, "t-left", style="font-size:50px")}
</div>
''', "#2B3060"))

# 3 ── 땡볕 vs 소나기
def tile(col, kind, day, word, val, color, bg, d):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:300px;width:{w}px;height:520px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:30px;text-align:center;padding-top:20px">'
            f'<div style="font-size:42px">{day}</div>'
            f'<div style="display:flex;justify-content:center;margin-top:6px"><div class="{"sunspin" if kind == "sun" else "drift"}">{wx_icon(kind, 170)}</div></div>'
            f'<div style="font-size:66px;line-height:1.1;margin-top:4px">{word}</div>'
            f'<div style="font-size:60px;line-height:1.2;margin-top:8px;color:{color}">{val}</div></div>')
S[3] = (1, page(FX + f'''
{head("한 주에 땡볕과 소나기", 3, "#EDEAF8")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#EEE9FF">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:92px;line-height:1.15"><span class="punch" style="--d:.05s"><span style="color:#E8590C">땡볕</span>이 <span style="color:{BLUE}">소나기</span>보다<br>셌다</span></div>
  {tile(COL2[0], "sun", "28일(수)", "땡볕", "▲6.63%", RED, "#FFE3D6", .4)}
  {tile(COL2[1], "rain", "30일(금)", "소나기", "3%대 급락", BLUE, "#DCEBFF", .8)}
  {sfx("쏴아~", 640, 840, 76, 1.0, -6, "#BFD9FF")}
  {ch(mascot("owl", "normal", "point"), P, 860, 290, 1.3, "a-sl", "squish")}
  {bub("땡볕이 세서<br>한 주는 <b>플러스</b>!", 350, 930, 1.6, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 주말 날씨: 중동 하늘에 짙은 안개
def fogband(top, d, op, x=-60, w=1100):
    return f'<div class="abs fog" style="left:{x}px;top:{top}px;width:{w}px;height:56px;border-radius:28px;background:rgba(220,226,240,{op});animation-delay:-{d}s"></div>'
S[4] = (1, page(FX + f'''
{head("주말 날씨", 4, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#2F3570">
  <div class="abs" style="left:0;right:0;top:34px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="punch" style="--d:.05s">중동에 <span style="color:#C9D6FF">짙은 안개</span></span></div>
  {fogband(170, 0, .35, 120, 700)}{fogband(240, 1.2, .25, 260, 640)}{fogband(310, 2.1, .3, 60, 760)}
  <div class="abs a-sl" style="left:{P}px;top:400px;width:{IW}px;--d:.4s;box-sizing:border-box;background:#fff;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">이란 재공격 <b style="color:#E8590C;font-weight:400">"아직 결정 안 해"</b></div>
  <div class="abs a-sr" style="left:{P}px;top:515px;width:{IW}px;--d:.8s;box-sizing:border-box;background:#E6F0FF;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">카타르, <b style="color:{BLUE};font-weight:400">12시간 넘게</b> 중재 협상</div>
  {numbox("브렌트유 (30일)", "▲2.4%", COL2[0], 650, 1.2, RED)}
  {numbox("원/달러 1,334.3원 (30일)", "▼2.5원", COL2[1], 650, 1.4, BLUE)}
  {ch(mascot("bamtol", "worried", "point"), P, 880, 270, 1.8, "a-sl", "squish2")}
  {bub("안개가 짙어서<br><b>앞이 잘 안 보여요</b>", 340, 940, 2.0, "t-left", style="font-size:46px")}
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
    return (f'<div class="abs a-pop" style="left:{x}px;top:720px;width:{w}px;height:170px;box-sizing:border-box;--d:{d}s;background:#FFB27F;border:4px solid {L};border-radius:24px;text-align:center;padding-top:16px">'
            f'<div style="font-size:36px">체크 {i+1}</div><div style="font-size:42px;line-height:1.15;margin-top:6px">{t}</div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("다음 주 예보", 5, L)}
<div class="panel" style="left:44px;top:200px;width:982px;height:1080px;background:#FFFDF6">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:84px"><span class="punch" style="--d:.05s">다음 주 <span style="color:#E8590C">예보</span></span></div>
  {drow(0, "2", "월요일", "저PBR 기업 명단", .3)}
  {drow(1, "3", "화(미국)", "미국 중간선거", .6, True)}
  {drow(2, "6", "금(미국)", "10월 고용보고서", .9)}
  {chk(0, "선거 뒤<br>이란", 1.4)}{chk(1, "AI 투자<br>걱정", 1.75)}{chk(2, "외국인", 2.1)}
  {cbub("선거 뒤 <b>안개</b>가 걷힐지가 관건!", 925, 2.5, "t-up", style="font-size:44px")}
</div>
<div class="src a-fade" style="top:1300px;color:#6B5A50;--d:2.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 이투데이, 디지털타임스, 서울경제, 파이낸셜뉴스, 뉴스핌</div>
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
  {cbub("안개 낀 한 주,<br><b>예보</b> 챙겨 보세요!", 480, .8, "t-down", style="font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1250px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1390px;color:#6B5A50;--d:1.1s">출처: AP, 파이낸셜뉴스, 이투데이, 디지털타임스, 뉴스1, 로이터, 뉴스핌<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.6), 3: (3.6, 1.6), 4: (4.0, 1.6), 5: (4.4, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "forecast", .9), (1, .05, "thud", .8), (1, .3, "sparkle", .8), (1, .35, "thud", .9),
 (1, .5, "pop", .5), (1, .62, "pop", .5), (1, .74, "pop", .5), (1, .86, "pop", .5), (1, .98, "pop", .5),
 (2, .05, "thud", .7), (2, .3, "rain", .4), (2, .3, "blip_down", .5), (2, .45, "blip_down", .5), (2, .6, "blip_down", .6), (2, .9, "sparkle", .8), (2, 1.1, "blip_down", .6), (2, 1.5, "yay", .6), (2, 1.7, "pop", .8),
 (3, .05, "thud", .7), (3, .4, "sunrise", .6), (3, .8, "rain", .6), (3, 1.0, "slidedown", .6), (3, 1.3, "boing", .6), (3, 1.6, "ding", .7),
 (4, .05, "thud", .7), (4, .2, "tension", .6), (4, .4, "whoosh", .5), (4, .8, "whoosh", .5), (4, 1.2, "pop", .6), (4, 1.4, "pop", .6), (4, 1.8, "boing", .5), (4, 2.0, "pop", .8),
 (5, .05, "forecast", .7), (5, .3, "whoosh", .5), (5, .6, "whoosh", .5), (5, .9, "whoosh", .5), (5, 1.4, "CHECK1", 1), (5, 1.75, "CHECK2", 1), (5, 2.1, "CHECK3", 1), (5, 2.5, "pop", .8),
 (6, .0, "sunrise", .8), (6, .3, "pop", .6), (6, .5, "boing", .6), (6, .8, "pop", .8), (6, 1.0, "jingle", .9),
]
