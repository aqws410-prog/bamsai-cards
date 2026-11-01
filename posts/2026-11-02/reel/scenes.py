"""형식: 밤사이 단톡방 v3 (장면 1 '사진 공유 + 이모지 리액션' 새 구도 · 검수 전 · 2026-11-02 월요일판) — 솜부엉이 수출 성적표 사진을 올리고, 별콩이가 놀라고, 달떡이가 비유로 풀고, 밤톨이가 공지로 정리.
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(10월 수출 ▲93.7% + '수출 역대 2위, 근데 변수도')을 0초부터 크게. 시그니처: 찰칵 플래시 + 단톡방 사진(성적표) 공유 + 👍/😰 리액션 카운터 + 띵동(msg)·타닥(typing).
10-19(잠금화면 알림)·10-26(고정 투표판)과 다르게, 사진 메시지 + 리액션 구도로 새로 짰다.
흐름: 1 성적표 사진(결론) → 2 반도체 성적 공유·질문 → 3 비유(추석에 문 닫았던 가게와 비교) → 4 변수(트럼프 "10분" · 이란 "이틀") → 5 공지(오늘 체크 3) → 6 이번 주 일정·마무리.
숫자는 2026-11-02 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes punch2{0%{transform:scale(1)}12%{transform:scale(1.15)}24%{transform:scale(.96)}34%{transform:scale(1.04)}46%,100%{transform:scale(1)}}
@keyframes jolt2{0%,100%{transform:translateX(0)}20%{transform:translateX(-16px)}40%{transform:translateX(14px)}60%{transform:translateX(-9px)}80%{transform:translateX(5px)}}
@keyframes flash{0%{opacity:.45}100%{opacity:0}}
@keyframes cnt{0%{transform:scale(1)}30%{transform:scale(1.35)}100%{transform:scale(1)}}
@keyframes tilt{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(2deg)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:.25}}
@keyframes shut{from{height:0}to{height:var(--h)}}
.p2{display:inline-block;transform-origin:50% 60%;animation:punch2 1.1s ease-out var(--d,0s) both, jolt2 .45s ease-out calc(var(--d,0s) + .05s) both}
.flash{position:absolute;left:-200px;top:-200px;width:1480px;height:2400px;background:#fff;pointer-events:none;animation:flash .25s ease-out both}
.cnt{display:inline-block;animation:cnt .4s ease-out var(--d,0s) both}
.tilt{animation:tilt 1.4s ease-in-out infinite}
.blink{animation:blink .7s steps(1) infinite}
</style>"""

def react(icon, label, n, x, w, top, d, bg):
    return (f'<div class="abs a-pop" style="left:{x}px;top:{top}px;width:{w}px;height:96px;box-sizing:border-box;--d:{d}s;background:{bg};border:4px solid {L};border-radius:999px;'
            f'display:flex;align-items:center;justify-content:center;gap:12px;font-size:42px">'
            f'<span style="font-size:56px">{icon}</span><span class="cnt" style="--d:{d + .25:.2f}s">{label}</span></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·사진·놀란 별콩이가 모두 보인다 (찰칵 플래시)
report = (f'<div class="tilt" style="background:#FFFDF6;border:4px solid {L};border-radius:18px;padding:18px 24px;box-shadow:0 6px 0 rgba(0,0,0,.15)">'
          f'<div style="font-size:34px;color:#6B5A50">📄 10월 수출 성적표</div>'
          f'<div style="font-size:64px;line-height:1.15">1,152.8억달러</div>'
          f'<div style="font-size:34px;color:#6B5A50">1년 전보다 <span style="color:{RED}">▲93.7%</span></div></div>')
S[1] = (1, page(FX + f'''
{stars(14, 41, 0, 180)}
{head("밤사이 단톡방 · 11.02 MON", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:188px;text-align:center;font-size:44px;color:#C9D6FF">10월 수출 · 1년 전 대비 (1일 발표)</div>
<div class="abs" style="left:0;width:1080px;top:246px;text-align:center"><span class="p2" style="--d:0s;font-size:230px;line-height:1;color:{RED};-webkit-text-stroke:10px {L};paint-order:stroke fill">▲93.7%</span></div>
<div class="abs" style="left:0;width:1080px;top:490px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">수출 역대 2위, <span style="color:#FFE36E">근데 변수도</span></div>
<div class="chat" style="left:44px;top:630px;width:982px;height:760px">
  <div class="top">밤사이 단톡방 (4) <span class="blink" style="margin-left:10px;color:#E8484A">● 사진 1장</span></div>
  <div class="abs" style="left:24px;top:110px;width:86px;height:86px;border-radius:30px;background:#fff;border:4px solid {L};overflow:hidden">{face_svg("owl", "happy")}</div>
  <div class="abs" style="left:124px;top:104px;font-size:26px;opacity:.75">솜부엉</div>
  <div class="abs" style="left:124px;top:146px;width:520px">{report}</div>
  {stamp("역대 2위", 520, 120, .3, -12)}
  {react("👍", "수출", 3, P, 300, 470, .55, "#FFE3E3")}
  {react("😰", '"10분"', 2, P, 300, 586, .8, "#DDE6FF")}
  <div class="abs" style="left:470px;top:330px;width:440px"><div class="shiver">{mascot("star", "surprised", "up")}</div></div>
</div>
{sfx("찰칵!", 760, 600, 88, .0, 10, "#FFE36E")}
{sfx("띵동!", 360, 1060, 72, .45, -8, "#fff")}
<div class="flash"></div>
''', "#262B55"))

# 2 ── 반도체가 끌어올렸다
S[2] = (1, page(FX + f'''
{head("성적표 뜯어보기", 2, "#F6EEE4")}
{chat("밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("owl", "📌 1일 발표! 1등 공신은 이거", 110, .1, mood="happy")}
  <div class="abs a-rise" style="left:{P}px;top:260px;--d:.35s;width:{IW}px;height:430px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;text-align:center;padding-top:30px">
    <div style="font-size:48px">💾 10월 반도체 수출</div>
    <div style="font-size:150px;line-height:1.1"><span class="thump" style="--d:.7s">564.4억달러</span></div>
    <div style="font-size:72px;color:{RED}">1년 전보다 ▲259.4%</div></div>
  {stamp("역대 2위", 600, 640, 1.2, -8)}
  {typing(820, 1.5, "r", 24, 1.9)}
  {msg("star", "반도체가 다 끌어올렸네?!<br>근데 93.7%는 너무 큰데…🤔", 820, 1.95, "r", "surprised")}
""")}
''', "#2B3060"))

# 3 ── 비유: 작년 10월엔 추석에 문 닫은 가게
def shop(x, w, title, sign, days, sub, bg, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:250px;width:{w}px;height:430px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:28px;text-align:center;padding-top:22px">'
            f'<div style="font-size:42px">{title}</div><div style="font-size:120px;line-height:1.2">{sign}</div>'
            f'<div style="font-size:46px">{days}</div><div style="font-size:32px;color:#6B5A50;margin-top:6px">{sub}</div></div>')
S[3] = (1, page(FX + f'''
{head("달떡이의 비유", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:84px;line-height:1.15"><span class="p2" style="--d:.1s">작년 10월엔 <span style="color:#7B3FC4">추석 휴무</span></span></div>
  {shop(COL2[0][0], COL2[0][1], "작년 10월 가게", "🏮", "추석 연휴로 쉼", "문 닫은 날이 많았다", "#FFE3E3", .45)}
  {shop(COL2[1][0], COL2[1][1], "올해 10월 가게", "🏪", "일하는 날 ↑", "연휴는 9월로 이동", "#E3F5DF", .8)}
  <div class="abs a-pop" style="left:{P}px;top:720px;--d:1.3s;width:{IW}px;height:170px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;display:flex;align-items:center;justify-content:center;gap:24px">
    <div style="font-size:48px">하루 평균으로 봐도</div><div style="font-size:104px;color:{RED}"><span class="thump" style="--d:1.6s">▲76%</span></div></div>
  {ch(mascot("moon", "happy", "point"), P, 900, 250, 1.7, "a-sl", "squish")}
  {bub("쉬는 날 빼고 따져도<br><b>많이 팔았어요!</b>", 330, 930, 1.9, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 변수: 트럼프 "10분" · 이란 "이틀"
S[4] = (1, page(FX + f'''
{head("근데 변수는?", 4, "#F6EEE4")}
{chat("밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("bamtol", "주말(31일 현지) 중동 소식 두 개!", 110, .1)}
  <div class="abs a-sl" style="left:{P}px;top:260px;--d:.4s;width:{IW}px;height:250px;box-sizing:border-box;background:#FFE3E3;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 30px">
    <div style="font-size:104px">⏱️</div><div><div style="font-size:38px">트럼프 · 남은 표적 한두 곳</div><div style="font-size:100px;line-height:1.05"><span class="thump" style="--d:.8s">"10분이면"</span></div></div></div>
  <div class="abs a-sl" style="left:{P}px;top:550px;--d:1.1s;width:{IW}px;height:250px;box-sizing:border-box;background:#E3EEFF;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 30px">
    <div style="font-size:104px">🚢</div><div><div style="font-size:38px">이란 · 조건 맞으면 호르무즈</div><div style="font-size:100px;line-height:1.05">"이틀 안에"</div></div></div>
  {msg("star", "3일 선거 끝나면…?<br>기름값 또 걱정이네 😰", 860, 1.8, "r", "worried")}
""")}
''', "#4A3E78"))

# 5 ── 공지: 오늘 체크 3
checks = [("반도체 수출이 받쳐 줄까", "실적 기대로 이어지면 반도체 업종에 힘이 될 가능성"),
          ("저PBR 151곳 명단 효과", "주주환원이 나오면 저평가 업종이 주목받을 가능성"),
          ("선거 앞 눈치 보기", "관망하면 지수가 좁게 움직일 가능성")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{300+i*190}px;width:{IW}px;height:166px;box-sizing:border-box;--d:{.5+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:80px;height:80px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:48px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div><div style="font-size:52px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("📌 단톡방 공지", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:0;right:0;top:0;height:90px;background:#FFE36E;border-bottom:4px solid {L};font-size:40px;line-height:90px;padding-left:34px">📌 공지 · 밤톨이</div>
  <div class="abs" style="left:0;right:0;top:140px;text-align:center;font-size:88px"><span class="p2" style="--d:.1s">오늘 장 <span style="color:#E8590C">체크 3</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point"), 680, 805, 220, 2.0, "a-sr", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 서울경제, 한국경제, 연합뉴스, 뉴시스, 뉴스1</div>
''', "#FFE1CC"))

# 6 ── 마무리: 이번 주 일정 + 팔로우
def daycard(day, date, t, col, d, hi=False):
    x, w = col
    bg = "#FFD84D" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:{w}px;height:280px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};'
            f'border-radius:26px;box-shadow:0 6px 0 rgba(0,0,0,.15);text-align:center;padding:14px 8px;color:{L}">'
            f'<div style="font-size:32px;color:#6B5A50">{day}</div><div style="font-size:88px;line-height:1.05">{date}</div>'
            f'<div style="font-size:32px;line-height:1.2;margin-top:6px">{t}</div></div>')
S[6] = (1, page(FX + f'''
{head("이번 주 일정 · 마무리", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:30px;font-size:42px;color:#FFC08A">이번 주, 이 날짜만!</div>
  {daycard("화요일", "3", "미국 중간선거<br>한국 10월 물가", COL3[0], .15, True)}
  {daycard("목요일", "5", "한국 9월<br>국제수지", COL3[1], .3)}
  {daycard("금요일", "6", "미국 10월<br>고용보고서", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("owl", "happy", "wave"), 660, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 톡할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 서울경제, 파이낸셜뉴스, 연합뉴스, 뉴시스, 뉴스1, 한국경제<br>정보 제공용이며 투자 권유가 아닙니다 · 중간선거·고용보고서는 미국 현지 날짜</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.2, 1.5), 3: (4.0, 1.5), 4: (3.9, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "shutter", 1), (1, .0, "msg", .8), (1, .05, "thud", .8), (1, .3, "thud", .9), (1, .45, "msg", .7), (1, .55, "pop", .8), (1, .8, "pop", .8), (1, .9, "question", .6),
 (2, .05, "whoosh", .5), (2, .1, "msg", .7), (2, .35, "pop", .6), (2, .7, "ding", .6), (2, 1.2, "thud", .9), (2, 1.5, "typing", .6), (2, 1.95, "msg", .6),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .45, "pop", .6), (3, .8, "pop", .6), (3, 1.3, "sparkle", .7), (3, 1.7, "boing", .6), (3, 1.9, "ding", .7),
 (4, .05, "whoosh", .5), (4, .1, "msg", .7), (4, .4, "tension", .5), (4, .8, "thud", .7), (4, 1.1, "whoosh", .5), (4, 1.8, "msg", .6), (4, 1.9, "hmm", .5),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "msg", .7), (6, .9, "jingle", .9),
]
