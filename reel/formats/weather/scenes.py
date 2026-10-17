"""형식: 밤사이 일기예보 (검수 전 · 예시 내용 2026-10-18 일요일판 — 새 날짜에는 구조만 참고) — 밤톨이 기상캐스터, 솜부엉 예보관, 별콩이 시청자.
원칙(2026-10-17 훅 규칙): 장면 1에 결론(코스피 주간 ▼14.46% + '한 주 새 폭풍우')을 0초부터 크게 → 2 지수별 날씨 카드 → 3 왜 폭풍이 됐나(먹구름 3개)
→ 4 한국 날씨(구름 사이 햇살) → 5 다음 주 예보(체크) → 6 마침. 시그니처: 하늘색 '주간 증시 날씨' 바 + 날씨 지도 + 번개 번쩍·천둥(thunder)·예보 차임(forecast).
숫자는 2026-10-18 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes punch{0%{transform:scale(1)}12%{transform:scale(1.15)}24%{transform:scale(.96)}34%{transform:scale(1.04)}46%,100%{transform:scale(1)}}
@keyframes jolt{0%,100%{transform:translateX(0)}20%{transform:translateX(-16px)}40%{transform:translateX(14px)}60%{transform:translateX(-9px)}80%{transform:translateX(5px)}}
@keyframes flash{0%{opacity:0}8%{opacity:.85}20%{opacity:.1}30%{opacity:.6}100%{opacity:0}}
@keyframes fall{from{transform:translateY(-80px)}to{transform:translateY(520px)}}
@keyframes boltin{0%,100%{opacity:0}10%,30%{opacity:1}20%{opacity:.2}}
@keyframes drift{0%,100%{transform:translateX(0)}50%{transform:translateX(16px)}}
@keyframes merge{from{transform:translate(var(--mx),0) scale(1)}to{transform:translate(0,0) scale(.9)}}
@keyframes sweep{from{transform:rotate(-30deg)}to{transform:rotate(30deg)}}
.punch2{display:inline-block;transform-origin:50% 60%;animation:punch 1.1s ease-out var(--d,0s) both, jolt .45s ease-out calc(var(--d,0s) + .05s) both}
.drift{animation:drift 2.2s ease-in-out infinite}
.drop{position:absolute;width:8px;height:34px;border-radius:4px;background:#8EC5FF;animation:fall .7s linear infinite}
</style>"""

def rain(n, x0, x1, top, seed, color="#8EC5FF"):
    import random
    r = random.Random(seed)
    return "".join(f'<div class="drop" style="left:{r.randint(x0, x1)}px;top:{top}px;background:{color};animation-delay:-{r.random()*.7:.2f}s"></div>' for _ in range(n))

def wxbar(text, top=186):
    """일기예보 시그니처 — 하늘색 방송 바 (0초부터 보임)."""
    return (f'<div class="abs" style="left:44px;top:{top}px;width:982px;height:104px;box-sizing:border-box;background:linear-gradient(90deg,#4F8EF0,#7FC3FF);'
            f'border:6px solid {L};border-radius:22px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;gap:18px;color:#fff">'
            f'<div style="flex:none;width:96px;height:96px;margin-top:-6px">{wx_icon("partly", 86)}</div>'
            f'<div style="font-size:60px;-webkit-text-stroke:6px {L};paint-order:stroke fill">{text}</div></div>')

def wxcard(kind, name, val, col, top, d, color, h=300):
    x, w = col
    return (f'<div class="wx a-pop" style="left:{x}px;top:{top}px;width:{w}px;height:{h}px;box-sizing:border-box;--d:{d}s;padding:10px 6px">'
            f'<div style="display:flex;justify-content:center">{wx_icon(kind, 110)}</div>'
            f'<div style="font-size:40px;line-height:1.1">{name}</div>'
            f'<div style="font-size:60px;line-height:1.15;color:{color}">{val}</div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·캐스터·폭풍 지도가 모두 보인다
storm_big = f'<div class="abs" style="left:540px;top:40px;width:330px"><div class="drift">{wx_icon("storm", 300)}</div></div>'
S[1] = (1, page(FX + f'''
{stars(12, 51, 0, 180)}
{head("밤사이 날씨 · 10.18 SUN", 1, "#F6EEE4")}
{wxbar("주간 증시 날씨")}
<div class="abs" style="left:0;width:1080px;top:316px;text-align:center;font-size:50px;color:#C9D6FF">코스피 · 지난주(12~16일)</div>
<div class="abs" style="left:0;width:1080px;top:376px;text-align:center"><span class="punch2" style="--d:0s;font-size:220px;line-height:1;color:#7DBBFF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼14.46%</span></div>
<div class="abs" style="left:44px;top:630px;width:982px;height:140px;box-sizing:border-box;background:#6A3FB5;border:6px solid {L};border-radius:26px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;overflow:hidden">
  <div style="flex:none;height:100%;width:170px;background:#E8484A;border-right:6px solid {L};color:#fff;font-size:56px;line-height:1.05;display:flex;align-items:center;justify-content:center;text-align:center">기상<br>특보</div>
  <div style="flex:1;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">한 주 새 <span style="color:#FFE36E">폭풍우</span></div>
</div>
<div class="panel" style="left:44px;top:800px;width:982px;height:580px;background:#3C4485">
  <div class="abs" style="left:420px;top:330px;width:620px;height:320px;border-radius:50%;background:#5E9E6E;border:5px solid {L}"></div>
  <div class="abs" style="left:640px;top:410px;font-size:44px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill">● 서울</div>
  {storm_big}
  {rain(16, 560, 860, 300, 7)}
  <div class="abs" style="left:-30px;top:110px;width:520px"><div class="shiver">{mascot("bamtol", "surprised", "point")}</div></div>
</div>
<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#fff;pointer-events:none;animation:flash .5s ease-out .3s both"></div>
{sfx("우르릉 쾅!", 560, 760, 96, .35, -8, "#FFE36E")}
<div class="abs" style="left:530px;top:1210px;--d:.7s" ><div class="a-pop" style="--d:.7s;background:#fff;border:4px solid {L};border-radius:999px;padding:6px 22px;font-size:40px">다우만 <span style="color:{RED}">▲</span> 맑음</div></div>
''', "#262B55"))

# 2 ── 지난주 날씨 지도 (지수별 날씨 카드)
S[2] = (1, page(FX + f'''
{head("지난주 날씨 지도", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E8F2FF;--d:0s">
  <div class="abs" style="left:0;right:0;top:30px;text-align:center;font-size:80px"><span class="punch2" style="--d:.1s">미국은 <span style="color:{BLUE}">흐림</span>, 한국은 <span style="color:#7B3FC4">폭풍</span></span></div>
  <div class="abs" style="left:0;right:0;top:130px;text-align:center;font-size:36px;color:#55607A">한 주 등락 · 16일 종가 기준</div>
  {wxcard("sun", "다우", "▲0.67%", COL3[0], 200, .4, RED)}
  {wxcard("cloud", "S&amp;P500", "▼1.95%", COL3[1], 200, .7, BLUE)}
  {wxcard("rain", "나스닥", "▼4.48%", COL3[2], 200, 1.0, BLUE)}
  {wxcard("storm", "코스피", "▼14.46%", COL2[0], 540, 1.5, BLUE)}
  {wxcard("storm", "코스닥", "▼10.93%", COL2[1], 540, 1.8, BLUE)}
  {ch(mascot("star", "teary", "down"), 60, 880, 270, 2.2, "a-sl", "shiver")}
  {bub("한국만 <b>폭풍</b>이<br>몰아쳤네요…", 350, 930, 2.5, "t-left", style="font-size:46px")}
</div>
''', "#2B3060"))

# 3 ── 왜 폭풍이 됐나: 먹구름 3개가 한꺼번에
def cloudbox(i, t, col, d):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:250px;width:{w}px;--d:{d}s;text-align:center">'
            f'<div style="display:flex;justify-content:center">{wx_icon("rain", 150)}</div>'
            f'<div style="margin-top:6px;background:#fff;border:4px solid {L};border-radius:22px;padding:10px 6px;font-size:38px;line-height:1.25">'
            f'<span style="color:#E8590C">{i}</span> {t}</div></div>')
S[3] = (1, page(FX + f'''
{head("왜 폭풍이 됐을까?", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#EEE9FF;--d:0s">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:100px;line-height:1.1"><span class="punch2" style="--d:.1s">먹구름 <span style="color:#7B3FC4">3개</span>가<br>한꺼번에</span></div>
  {cloudbox("①", "외국인<br>대규모 매도", COL3[0], .5)}
  {cloudbox("②", "AI 투자<br>의구심", COL3[1], .8)}
  {cloudbox("③", "뜨거운<br>미국 물가", COL3[2], 1.1)}
  <div class="abs a-pop" style="left:0;right:0;top:640px;--d:1.6s;text-align:center;font-size:84px">＝ <span style="display:inline-block;vertical-align:middle">{wx_icon("storm", 130)}</span> <span style="color:#7B3FC4">폭풍</span></div>
  {sfx("번쩍!", 680, 600, 90, 1.7, 8, "#FFE36E")}
  {ch(mascot("owl", "normal", "point"), P, 860, 280, 2.1, "a-sl", "squish")}
  {bub("구름 하나면 비,<br><b>셋이 겹치면 폭풍</b>이에요", 340, 920, 2.4, "t-left", style="font-size:44px")}
</div>
''', "#30366E"))

# 4 ── 한국 날씨: 금요일, 구름 사이 햇살
sun_peek = (f'<div class="abs" style="left:300px;top:40px;width:380px;height:380px">'
            f'<div class="abs" style="left:0;top:0;width:380px;height:380px;border-radius:50%;background:#FFD84D;border:6px solid {L};box-sizing:border-box;animation:sunrise .9s cubic-bezier(.2,.9,.3,1) .1s both"></div></div>')
S[4] = (1, page(FX + f'''
{head("한국 날씨", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFF4D9;--d:0s">
  {sun_peek}
  <div class="abs" style="left:150px;top:230px;width:330px"><div class="drift">{wx_icon("cloud", 300)}</div></div>
  <div class="abs" style="left:560px;top:250px;width:300px"><div class="drift" style="animation-delay:-1s">{wx_icon("cloud", 260)}</div></div>
  <div class="abs" style="left:0;right:0;top:470px;text-align:center;font-size:92px;line-height:1.1"><span class="punch2" style="--d:.5s">금요일, <span style="color:#E8590C">구름 사이 햇살</span></span></div>
  <div class="abs a-pop" style="left:0;right:0;top:590px;--d:.9s;text-align:center;font-size:52px">16일 외국인 <span style="color:{RED}">순매수</span>로 돌아섰어요</div>
  {ch(mascot("star", "happy", "up"), P, 700, 280, 1.3, "a-sl", "hop")}
  {bub("해 뜨는 거예요?", 330, 740, 1.5, "t-left", style="font-size:44px")}
  {ch(mascot("bamtol", "worried", "point"), 660, 700, 260, 1.9, "a-sr", "squish2")}
  {bub("아직은 <b>구름 많음</b>!", 300, 870, 2.2, "t-right", style="font-size:44px")}
  {numbox("원/달러 1,331.4원 (16일) · 2년여 만에 최저", "▼13.2원", (P, IW), 1010, 2.6, BLUE)}
</div>
''', "#4A3E78"))

# 5 ── 다음 주 예보 (일정 + 체크)
def daycard(day, date, t, col, d, hi=False):
    x, w = col
    bg = "#FFD84D" if hi else "#fff"
    tag = (f'<div style="margin-top:8px;font-size:26px;background:{L};color:#FFE59A;border-radius:999px;padding:2px 10px">한국 영향 1순위</div>' if hi else "")
    return (f'<div class="abs a-pop" style="left:{x}px;top:180px;width:{w}px;height:330px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};'
            f'border-radius:26px;box-shadow:0 6px 0 rgba(0,0,0,.15);text-align:center;padding:16px 10px">'
            f'<div style="font-size:34px;color:#6B5A50">{day}</div><div style="font-size:92px;line-height:1.05">{date}</div>'
            f'<div style="font-size:38px;line-height:1.2;margin-top:6px">{t}</div>{tag}</div>')
checks = [("외국인, 계속 살까", ""), ("AI 의구심 풀릴까", f"나스닥 주간 <span style='color:#1D4ED8'>▼4.48%</span>"),
          ("기름값과 금리", f"브렌트유 109.86달러 <span style='color:#C92A2A'>▲3.7%</span>")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{570+i*150}px;width:{IW}px;height:130px;box-sizing:border-box;--d:{1.6+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:46px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div><div style="font-size:48px">{t}</div>' + (f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">{s}</div>' if s else "") + '</div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("다음 주 예보", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:84px"><span class="punch2" style="--d:.1s">다음 주 <span style="color:#E8590C">예보 3</span></span></div>
  {daycard("월요일", "19", "중국<br>3분기 GDP", COL3[0], .4)}
  {daycard("목요일", "22", "한은<br>금리 결정", COL3[1], .7, True)}
  {daycard("미국 주중", "실적", "테슬라·<br>넷플릭스", COL3[2], 1.0)}
  {rows}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: AP, 로이터, 뉴스핌, 뉴스1, 서울경제, 한국경제, SBS</div>
''', "#FFE1CC"))

# 6 ── 마침: 내일 예보 + 팔로우
S[6] = (1, page(FX + f'''
{head("밤사이 날씨 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:40px;color:#FFC08A">내일(월) 아침 예보</div>
  <div class="abs" style="left:44px;top:100px;font-size:76px;line-height:1.2">아침 8시<br>주말 시장 반응</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.3s;font-size:42px">미국 선물 <span style="color:#FFC08A">월요일 아침 7시</span> 개장</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "happy", "wave"), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("우산 챙기고 오세요!<br><b>밤사이 날씨</b>였습니다", 280, 30, .65, "t-down", "75%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1395px;color:#6B5A50;--d:1.0s">출처: AP, 로이터, 뉴스핌, 뉴스1, 서울경제, 한국경제, CNBC<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.8, 1.3), 2: (4.0, 1.6), 3: (4.0, 1.6), 4: (3.8, 1.6), 5: (4.6, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "forecast", .9), (1, .05, "thud", .8), (1, .3, "thunder", 1), (1, .35, "thud", .9), (1, .1, "rain", .6), (1, .7, "pop", .8), (1, 1.2, "rain", .5),
 (2, .05, "whoosh", .5), (2, .1, "thud", .7), (2, .4, "sparkle", .6), (2, .7, "blip_down", .6), (2, 1.0, "blip_down", .7), (2, 1.5, "thud", .8), (2, 1.8, "thud", .8), (2, 2.2, "sad", .5), (2, 2.5, "pop", .8),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .5, "pop", .6), (3, .8, "pop", .6), (3, 1.1, "pop", .6), (3, 1.6, "thunder", .7), (3, 2.1, "boing", .6), (3, 2.4, "pop", .8),
 (4, .05, "whoosh", .5), (4, .1, "sunrise", .7), (4, .5, "sparkle", .7), (4, .9, "ding", .6), (4, 1.3, "yay", .5), (4, 1.5, "pop", .8), (4, 1.9, "boing", .5), (4, 2.2, "pop", .8), (4, 2.6, "blip_down", .8),
 (5, .05, "whoosh", .5), (5, .1, "forecast", .7), (5, .4, "pop", .6), (5, .7, "pop", .7), (5, 1.0, "pop", .6), (5, 1.6, "CHECK1", 1), (5, 2.05, "CHECK2", 1), (5, 2.5, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
