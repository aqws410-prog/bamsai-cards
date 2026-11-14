"""형식: 밤사이 일기예보 v5 (검수 전 · 2026-11-15 일요일판) — 밤톨이 기상캐스터, 솜부엉 예보관, 별콩이 시청자.
장면 1 새 구도: 왼쪽 세로 대형 온도계(수은주가 0~1초에 쭉 올라감) + 오른쪽 초대형 ▲4.56% + 결론 '한 주 새 날이 풀렸다' + '해빙' 도장 + 녹는 눈사람 옆 캐스터 클로즈업.
흐름: 1 결론 먼저 → 2 지수별 날씨 카드 5장(모두 맑음) → 3 주간 날씨 달력(화·수 쨍쨍, 목·금 흐림 — 젠슨 황 사임 소식)
→ 4 주말: 세 바람이 선전으로(미·중·러 첫 3자 회담 19일, 핵무기 감축) → 5 다음 주 예보(일정 3 + 체크 3) → 6 마침.
핵심 비유: 지난주 한파 뒤 온도계가 올라 눈이 녹았다(해빙) / 세 나라 바람이 한곳으로 모인다.
숫자는 2026-11-15 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes merc{from{height:22%}to{height:78%}}
@keyframes drip{0%{transform:translateY(0);opacity:1}100%{transform:translateY(60px);opacity:0}}
@keyframes melt{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.94)}}
@keyframes rays{from{transform:rotate(0)}to{transform:rotate(360deg)}}
@keyframes flash{0%{opacity:0}10%{opacity:.7}100%{opacity:0}}
@keyframes gather{from{transform:translate(var(--fx),var(--fy)) scale(.8)}to{transform:none}}
@keyframes drift{0%,100%{transform:translateX(0)}50%{transform:translateX(14px)}}
.drip{position:absolute;width:14px;height:22px;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;background:#9FD3FF;border:3px solid #3a2a1f;animation:drip .8s ease-in infinite}
.melt{transform-origin:50% 100%;animation:melt 1.1s ease-in-out infinite}
.rays{animation:rays 6s linear infinite}
.drift{animation:drift 2.2s ease-in-out infinite}
</style>"""

def thermo(x, top, h):
    """세로 온도계: 수은주가 0초부터 올라간다(0.05~0.95초)."""
    ticks = "".join(f'<div class="abs" style="left:116px;top:{40 + i*(h-260)//8}px;width:{40 if i%2==0 else 26}px;height:8px;border-radius:4px;background:{L}"></div>' for i in range(9))
    return (f'<div class="abs" style="left:{x}px;top:{top}px;width:180px;height:{h}px">'
            f'<div class="abs" style="left:40px;top:0;width:76px;height:{h-120}px;box-sizing:border-box;background:#fff;border:7px solid {L};border-radius:38px;overflow:hidden">'
            f'<div class="abs" style="left:10px;right:10px;bottom:0;background:#FF5A5F;border-radius:24px;animation:merc .9s cubic-bezier(.2,.9,.3,1) .05s both"></div></div>'
            f'<div class="abs" style="left:8px;top:{h-170}px;width:140px;height:140px;border-radius:50%;background:#FF5A5F;border:7px solid {L};box-sizing:border-box"></div>'
            f'{ticks}</div>')

def snowman(x, y):
    drips = "".join(f'<div class="drip" style="left:{dx}px;top:{dy}px;animation-delay:-{i*.27:.2f}s"></div>' for i, (dx, dy) in enumerate([(30, 150), (150, 170), (90, 250)]))
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:200px;height:300px"><div class="melt abs" style="left:0;top:0;width:200px;height:300px">'
            f'<div class="abs" style="left:10px;top:120px;width:180px;height:160px;border-radius:50% 50% 46% 46%/60% 60% 40% 40%;background:#fff;border:6px solid {L};box-sizing:border-box"></div>'
            f'<div class="abs" style="left:45px;top:30px;width:110px;height:104px;border-radius:50%;background:#fff;border:6px solid {L};box-sizing:border-box"></div>'
            f'<div class="abs" style="left:72px;top:68px;width:12px;height:12px;border-radius:50%;background:{L}"></div><div class="abs" style="left:112px;top:68px;width:12px;height:12px;border-radius:50%;background:{L}"></div>'
            f'<div class="abs" style="left:92px;top:88px;width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:30px solid #FF8A3D"></div>'
            f'</div>{drips}</div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·캐스터·온도계가 모두 보인다
S[1] = (1, page(FX + f'''
{stars(10, 77, 0, 160)}
{head("밤사이 날씨 · 11.15 SUN", 1, "#F6EEE4")}
{thermo(40, 190, 1180)}
<div class="abs" style="left:240px;width:800px;top:200px;text-align:center;font-size:48px;color:#C9D6FF">코스피 · 지난주(11/9~13)</div>
<div class="abs" style="left:240px;width:800px;top:268px;text-align:center"><span class="punch" style="--d:0s;font-size:200px;line-height:1;color:#FF7A7F;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲4.56%</span></div>
<div class="abs" style="left:250px;top:514px;width:776px;height:210px;box-sizing:border-box;background:#FFF1D6;border:6px solid {L};border-radius:40px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;text-align:center;font-size:80px;line-height:1.15">
  <div>한 주 새<br>날이 <span style="color:{RED}">풀렸다</span></div>
</div>
{stamp("해빙", 870, 470, .35, 12)}
<div class="panel" style="left:250px;top:770px;width:776px;height:610px;background:#CFE9FF">
  <div class="abs rays" style="left:500px;top:-120px;width:300px;height:300px">{wx_icon("sun", 300)}</div>
  {snowman(40, 270)}
  <div class="abs" style="left:300px;top:150px;width:400px"><div class="hop" style="animation:hop .6s ease-out .6s 1 both">{mascot("bamtol", "surprised", "point")}</div></div>
</div>
<div class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#FFF3C4;pointer-events:none;animation:flash .5s ease-out .3s both"></div>
{sfx("사르르~", 280, 820, 72, .7, -8, "#BFE3FF")}
''', "#262B55"))

# 2 ── 지수별 날씨 카드 5장: 모두 맑음
def card5(i, kind, name, val, color, d):
    w, gap = 166, 18
    x = P + i * (w + gap)
    return (f'<div class="abs a-pop" style="left:{x}px;top:300px;width:{w}px;height:390px;box-sizing:border-box;--d:{d}s;background:#fff;border:5px solid {L};border-radius:26px;text-align:center;padding-top:18px">'
            f'<div style="display:flex;justify-content:center">{wx_icon(kind, 120)}</div>'
            f'<div style="font-size:40px;line-height:1.2;margin-top:10px">{name}</div>'
            f'<div style="font-size:38px;line-height:1.2;margin-top:12px;color:{color}">{val}</div></div>')
S[2] = (1, page(FX + f'''
{head("지난주 날씨 카드", 2, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#FFF6DA">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:88px;line-height:1.15"><span class="punch" style="--d:.05s">다섯 곳 모두<br><span style="color:#E8590C">맑음</span></span></div>
  {card5(0, "sun", "다우", "▲2.07%", RED, .3)}{card5(1, "sun", "S&amp;P", "▲2.51%", RED, .45)}{card5(2, "sun", "나스닥", "▲2.27%", RED, .6)}{card5(3, "sun", "코스피", "▲4.56%", RED, .85)}{card5(4, "sun", "코스닥", "▲8.60%", RED, 1.05)}
  <div class="abs" style="left:0;right:0;top:720px;text-align:center;font-size:34px;color:#6B5A50">한 주 등락 · 11월 6일 종가 대비</div>
  {ch(mascot("star", "happy", "up"), 40, 820, 260, 1.4, "a-sl", "hop")}
  {bub("코스닥은 한 주<br><b>▲8.60%</b>나 올랐어요!", 330, 880, 1.6, "t-left", style="font-size:50px")}
</div>
''', "#2B3060"))

# 3 ── 주간 날씨 달력: 화·수 쨍쨍, 목·금 흐림
def day(i, dname, kind, val, color, d, hi=False):
    w, gap = 166, 18
    x = P + i * (w + gap)
    bg = "#FFE9B0" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:330px;width:{w}px;height:360px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:26px;text-align:center;padding-top:14px">'
            f'<div style="font-size:42px">{dname}</div>'
            f'<div style="display:flex;justify-content:center;margin-top:4px">{wx_icon(kind, 116)}</div>'
            f'<div style="font-size:38px;line-height:1.2;margin-top:8px;color:{color}">{val}</div></div>')
S[3] = (1, page(FX + f'''
{head("지난주 날씨 달력", 3, "#EDEAF8")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#EEE9FF">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:88px;line-height:1.15"><span class="punch" style="--d:.05s">화·수 <span style="color:#E8590C">쨍쨍</span>,<br>목·금은 <span style="color:{BLUE}">흐림</span></span></div>
  {day(0, "9일 월", "cloud", "▼0.81%", BLUE, .3)}{day(1, "10일 화", "sun", "▲4.39%", RED, .45, True)}{day(2, "11일 수", "sun", "▲2.60%", RED, .6, True)}{day(3, "12일 목", "cloud", "▼0.61%", BLUE, .85)}{day(4, "13일 금", "rain", "▼0.98%", BLUE, 1.05)}
  <div class="abs" style="left:0;right:0;top:720px;text-align:center;font-size:34px;color:#55607A">코스피 하루 등락</div>
  {ch(mascot("owl", "worried", "point"), P, 820, 280, 1.3, "a-sl", "squish")}
  {bub("목·금엔 <b>젠슨 황 사임</b><br>소식에 구름이 꼈어요", 340, 880, 1.5, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 주말: 세 바람이 선전으로
def wind(label, x, y, fx, fy, d, c):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:200px;height:200px;animation:gather .7s cubic-bezier(.2,.9,.3,1) {d}s both;--fx:{fx}px;--fy:{fy}px">'
            f'<div class="drift" style="width:200px;height:200px;border-radius:50%;background:{c};border:5px solid {L};box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:52px">{label}</div></div>')
S[4] = (1, page(FX + f'''
{head("주말 날씨", 4, "#F6EEE4")}
<div class="panel" style="left:44px;top:200px;width:982px;height:1200px;background:#2F3570">
  <div class="abs" style="left:0;right:0;top:34px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="punch" style="--d:.05s">세 바람이 <span style="color:#FFE36E">한곳으로</span></span></div>
  {wind("미국", 120, 170, -120, 60, .2, "#FFD6D6")}{wind("중국", 391, 150, 0, -120, .3, "#FFE9A8")}{wind("러시아", 662, 170, 120, 60, .4, "#D6E6FF")}
  <div class="abs a-pop" style="left:341px;top:380px;width:300px;--d:.9s;text-align:center;background:#FFE36E;border:5px solid {L};border-radius:999px;font-size:46px;padding:6px 0">★ 19일 선전</div>
  <div class="abs a-sl" style="left:{P}px;top:480px;width:{IW}px;--d:1.1s;box-sizing:border-box;background:#fff;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">백악관: 미·중·러 <b style="color:#E8590C;font-weight:400">첫 3자 정상회담</b></div>
  <div class="abs a-sr" style="left:{P}px;top:595px;width:{IW}px;--d:1.4s;box-sizing:border-box;background:#E6F0FF;border:4px solid {L};border-radius:24px;padding:16px 26px;font-size:44px;text-align:center">핵심 의제는 <b style="color:{BLUE};font-weight:400">핵무기 감축</b></div>
  {numbox("브렌트유 95.84달러 (13일)", "▲0.02%", COL2[0], 730, 1.7, RED)}
  {numbox("원/달러 1,336.7원 (13일)", "▲6.0원", COL2[1], 730, 1.9, RED)}
  {ch(mascot("bamtol", "normal", "point"), P, 930, 260, 2.1, "a-sl", "squish2")}
  {bub("세 바람이 만나면<br>날씨가 <b>어떻게 바뀔지</b> 봐요", 330, 980, 2.3, "t-left", style="font-size:46px")}
</div>
''', "#4A3E78"))

# 5 ── 다음 주 예보 (일정 3 + 체크 3)
def drow(i, date, dayname, t, d, hi=False):
    bg = "#FFD84D" if hi else "#fff"
    tag = f'<span style="margin-left:14px;font-size:28px;background:{L};color:#FFE59A;border-radius:999px;padding:2px 14px;vertical-align:middle">한국 영향 1순위</span>' if hi else ""
    return (f'<div class="abs a-sl" style="left:{P}px;top:{170+i*150}px;width:{IW}px;height:130px;box-sizing:border-box;--d:{d}s;background:{bg};border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:24px;padding:0 24px">'
            f'<div style="flex:none;width:170px;text-align:center"><div style="font-size:56px;line-height:1">{date}</div><div style="font-size:26px;color:#6B5A50">{dayname}</div></div>'
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
  {drow(0, "18", "수요일 아침", "엔비디아 실적", .3, True)}
  {drow(1, "19", "목요일 새벽", "FOMC 의사록<br><span style='font-size:30px'>(연준 회의 기록)</span>", .6)}
  {drow(2, "19", "목요일(현지)", "앤트로픽 상장", .9)}
  {chk(0, "엔비디아<br>실적", 1.4)}{chk(1, "앤트로픽<br>상장", 1.75)}{chk(2, "연준<br>신호", 2.1)}
  {cbub("다음 주 첫 고비는<br><b>엔비디아 실적</b>이에요", 915, 2.5, "t-up", style="font-size:44px")}
</div>
<div class="src a-fade" style="top:1300px;color:#6B5A50;--d:2.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 엔비디아 공시, 한국경제, 아주경제, 데일리안, CNBC</div>
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
  {cbub("날이 풀린 한 주,<br>다음 주 <b>예보</b>도 챙겨요!", 480, .8, "t-down", style="font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1250px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1390px;color:#6B5A50;--d:1.1s">출처: AP, 이투데이, 한국경제, 아주경제, 아시아경제, 서울경제, 데일리안<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.6), 3: (3.6, 1.6), 4: (4.2, 1.6), 5: (4.4, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "forecast", .9), (1, .05, "sparkle", .7), (1, .35, "thud", .9),
 (1, .6, "boing", .6), (1, .7, "pop", .6), (1, .95, "ding", .5),
 (2, .05, "thud", .7), (2, .3, "sparkle", .4), (2, .45, "pop", .4), (2, .6, "pop", .4), (2, .85, "sparkle", .5), (2, 1.05, "sparkle", .6), (2, 1.4, "yay", .5), (2, 1.6, "pop", .8),
 (3, .05, "thud", .7), (3, .3, "pop", .4), (3, .45, "sunrise", .5), (3, .6, "sparkle", .5), (3, .85, "hmm", .5), (3, 1.05, "rain", .5), (3, 1.3, "boing", .6), (3, 1.5, "pop", .8),
 (4, .05, "thud", .6), (4, .2, "whoosh", .5), (4, .3, "whoosh", .5), (4, .4, "whoosh", .5), (4, .9, "sparkle", .6), (4, 1.1, "whoosh", .5), (4, 1.4, "whoosh", .5), (4, 1.7, "pop", .6), (4, 1.9, "pop", .6), (4, 2.1, "boing", .5), (4, 2.3, "pop", .8),
 (5, .05, "forecast", .7), (5, .3, "whoosh", .5), (5, .6, "whoosh", .5), (5, .9, "whoosh", .5), (5, 1.4, "CHECK1", 1), (5, 1.75, "CHECK2", 1), (5, 2.1, "CHECK3", 1), (5, 2.5, "pop", .8),
 (6, .0, "sunrise", .8), (6, .3, "pop", .6), (6, .5, "boing", .6), (6, .8, "pop", .8), (6, 1.0, "jingle", .9),
]
