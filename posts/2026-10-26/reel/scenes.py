"""형식: 밤사이 단톡방 v2 (장면 1 '고정 투표판' 새 구도 · 검수 전 · 2026-10-26 월요일판) — 솜부엉이 주말 뉴스를 올리고, 별콩이가 묻고, 달떡이가 비유로 풀고, 밤톨이가 공지로 정리.
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(트럼프 결정 '보류' + 핵심 숫자)을 0초부터 크게. 시그니처: 단톡방 상단 고정 투표판(합의 vs 공격) + '보류' 도장 + 띵동(msg)·타닥(typing).
10-19 chat의 잠금화면 알림 구도와 다르게, 투표판 + 단톡방 대화 구도로 새로 짰다.
흐름: 1 투표판(결론) → 2 주말 뉴스 3줄 공유·질문 → 3 비유(공중에 뜬 동전) → 4 한국 이야기(기름값·외국인) → 5 공지(오늘 체크 3) → 6 이번 주 일정·마무리.
숫자는 2026-10-26 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

# 훅 숫자 (카드 1장 하단과 같은 숫자)
HOOK_K = "브렌트유 · 23일 마감 · 4월 이후 최고 수준"
HOOK_V = "116.72달러"
HOOK_C = RED

FX = """<style>
@keyframes punch2{0%{transform:scale(1)}12%{transform:scale(1.15)}24%{transform:scale(.96)}34%{transform:scale(1.04)}46%,100%{transform:scale(1)}}
@keyframes jolt2{0%,100%{transform:translateX(0)}20%{transform:translateX(-16px)}40%{transform:translateX(14px)}60%{transform:translateX(-9px)}80%{transform:translateX(5px)}}
@keyframes barL{from{width:0}to{width:var(--w)}}
@keyframes flip{0%{transform:translateY(0) rotateY(0)}50%{transform:translateY(-120px) rotateY(900deg)}100%{transform:translateY(0) rotateY(1800deg)}}
@keyframes hover{0%,100%{transform:translateY(0) rotate(-10deg)}50%{transform:translateY(-30px) rotate(10deg)}}
@keyframes wob{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:.25}}
.p2{display:inline-block;transform-origin:50% 60%;animation:punch2 1.1s ease-out var(--d,0s) both, jolt2 .45s ease-out calc(var(--d,0s) + .05s) both}
.coin{animation:hover 1.2s ease-in-out infinite}
.wob{animation:wob .8s ease-in-out infinite}
.blink{animation:blink .7s steps(1) infinite}
</style>"""

def pollbar(icon, t, w, top, d, col):
    return (f'<div class="abs" style="left:{P}px;top:{top}px;width:{IW}px;height:92px;box-sizing:border-box;background:#fff;border:4px solid {L};border-radius:22px;overflow:hidden">'
            f'<div class="abs" style="left:0;top:0;height:100%;--w:{w}%;width:{w}%;background:{col};animation:barL .5s ease-out {d}s both"></div>'
            f'<div class="abs" style="left:24px;top:0;line-height:84px;font-size:50px">{icon} {t}</div>'
            f'<div class="abs" style="right:24px;top:0;line-height:84px;font-size:44px">?</div></div>')

# 1 ── 결론 먼저: 0초에 투표판·숫자·결론·놀란 별콩이가 모두 보인다
S[1] = (1, page(FX + f'''
{stars(14, 26, 0, 180)}
{head("밤사이 단톡방 · 10.26 MON", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:188px;text-align:center;font-size:44px;color:#C9D6FF">{HOOK_K}</div>
<div class="abs" style="left:0;width:1080px;top:246px;text-align:center"><span class="p2" style="--d:0s;font-size:210px;line-height:1;color:{HOOK_C};-webkit-text-stroke:10px {L};paint-order:stroke fill">{HOOK_V}</span></div>
<div class="abs" style="left:0;width:1080px;top:478px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">트럼프 결정, <span style="color:#FFE36E">일단 보류</span></div>
<div class="chat" style="left:44px;top:620px;width:982px;height:770px">
  <div class="top">밤사이 단톡방 (4) <span class="blink" style="margin-left:10px;color:#E8484A">● 투표 중</span></div>
  <div class="abs" style="left:0;right:0;top:84px;height:330px;background:#FFFDF6;border-bottom:4px solid {L}">
    <div class="abs" style="left:{P}px;top:22px;font-size:44px">📊 트럼프의 선택은?</div>
    {pollbar("🤝", "합의", 50, 96, .05, "#CDE8C8")}
    {pollbar("💥", "공격", 50, 206, .15, "#FFC9C9")}
  </div>
  {stamp("보류", 640, 120, .35, -12)}
  <div class="abs" style="left:-10px;top:400px;width:420px"><div class="shiver">{mascot("star", "surprised", "up")}</div></div>
  <div class="abs a-pop" style="left:420px;top:460px;--d:.6s;width:520px;box-sizing:border-box;background:#FFE36E;border:4px solid {L};border-radius:26px;padding:16px 22px;font-size:48px;line-height:1.3;text-align:center">"오늘은 공격 없다"<br>근데 <span style="color:{RED}">결정은 임박</span>?!</div>
</div>
{sfx("띵동!", 800, 600, 88, .3, 10, "#FFE36E")}
''', "#262B55"))

# 2 ── 주말 뉴스 3줄 공유 + 질문
news3 = [("📺", "폭스 인터뷰", "\"합의냐, 끝내느냐\""), ("🎤", "기자 문답", "\"오늘은 공격 없다\""), ("🚀", "사우디 리야드", "후티, 재개장 공항 공격")]
newsrows = "".join(
    f'<div class="abs a-sl" style="left:20px;top:{80 + i*118}px;--d:{.5 + i*.4:.2f}s;width:600px;height:100px;box-sizing:border-box;background:#F4F7FF;border:3px solid {L};border-radius:18px;display:flex;align-items:center;gap:16px;padding:0 16px">'
    f'<div style="font-size:52px">{ic}</div><div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:22px;color:#6B5A50">{k}</div><div style="font-size:40px;line-height:1.1">{t}</div></div></div>'
    for i, (ic, k, t) in enumerate(news3))
S[2] = (1, page(FX + f'''
{head("주말 뉴스 3줄", 2, "#F6EEE4")}
{chat("밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("owl", "📌 주말(25일 현지) 3줄 요약!", 110, .1)}
  <div class="abs a-rise" style="left:124px;top:250px;--d:.3s;width:640px;height:450px;background:#fff;border:4px solid {L};border-radius:24px">
    <div class="abs" style="left:20px;top:18px;font-size:36px;color:#7B3FC4">트럼프 · 이란 · 후티</div>{newsrows}</div>
  <div class="abs a-stamp" style="left:600px;top:640px;--d:1.8s;--r:-8deg;background:#FFE36E;border:6px solid {L};border-radius:22px;padding:4px 22px;font-size:60px"><span class="thump" style="--d:2.0s">결정 임박</span></div>
  {msg("star", "그래서 한다는 거야,<br>안 한다는 거야? 🤔", 840, 2.3, "r", "worried")}
""")}
''', "#2B3060"))

# 3 ── 비유: 공중에 뜬 동전
coin = (f'<svg viewBox="0 0 200 200" width="260" height="260"><circle cx="100" cy="100" r="92" fill="#FFD84D" stroke="{L}" stroke-width="8"/>'
        f'<circle cx="100" cy="100" r="70" fill="none" stroke="#E0A800" stroke-width="6"/><text x="100" y="128" text-anchor="middle" font-size="84" font-family="Jua">?</text></svg>')
S[3] = (1, page(FX + f'''
{head("달떡이의 비유", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:92px;line-height:1.1"><span class="p2" style="--d:.1s">아직 <span style="color:#7B3FC4">공중에 뜬 동전</span></span></div>
  <div class="abs" style="left:361px;top:200px;width:260px"><div class="coin">{coin}</div></div>
  <div class="abs a-pop" style="left:{COL2[0][0]}px;top:520px;--d:.6s;width:{COL2[0][1]}px;height:210px;box-sizing:border-box;background:#E3F5DF;border:4px solid {L};border-radius:26px;text-align:center;padding-top:16px"><div style="font-size:80px;line-height:1.1">🤝</div><div style="font-size:46px">앞면 = 합의</div></div>
  <div class="abs a-pop" style="left:{COL2[1][0]}px;top:520px;--d:.9s;width:{COL2[1][1]}px;height:210px;box-sizing:border-box;background:#FFE3E3;border:4px solid {L};border-radius:26px;text-align:center;padding-top:16px"><div style="font-size:80px;line-height:1.1">💥</div><div style="font-size:46px">뒷면 = 공격</div></div>
  {ch(mascot("moon", "normal", "point"), P, 790, 290, 1.3, "a-sl", "squish")}
  {bub("동전이 떨어질 때까지<br><b>기름값</b>도 마음을<br>못 놓아요", 350, 800, 1.6, "t-left", style="font-size:44px")}
</div>
''', "#30366E"))

# 4 ── 한국 이야기: 기름값 · 외국인
S[4] = (1, page(FX + f'''
{head("우리 코스피는?", 4, "#F6EEE4")}
{chat("밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("bamtol", "한국에 중요한 건 이 두 개!", 110, .1)}
  <div class="abs a-sl" style="left:{P}px;top:270px;--d:.4s;width:{IW}px;height:250px;box-sizing:border-box;background:#FFF6EA;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px">
    <div style="font-size:110px">🛢️</div><div><div style="font-size:40px">기름값 · 브렌트유 (23일)</div><div style="font-size:104px;line-height:1;color:{RED}">▲3.1%</div></div></div>
  <div class="abs a-sl" style="left:{P}px;top:560px;--d:1.0s;width:{IW}px;height:250px;box-sizing:border-box;background:#2A2F5E;color:#fff;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px">
    <div style="font-size:110px">💸</div><div><div style="font-size:40px">외국인 · 23일 하루</div><div style="font-size:92px;line-height:1;color:#7DBBFF"><span class="thump" style="--d:1.3s">1조938억 팔았다</span></div></div></div>
  {msg("star", "원유를 사 오는 우리한텐<br>기름값이 부담이구나…", 860, 1.7, "r", "teary")}
""")}
''', "#4A3E78"))

# 5 ── 공지: 오늘 체크 3
checks = [("기름값이 출발선", "중동 긴장이 유가를 밀어 올리면 원가 부담 업종에 부담"),
          ("반도체는 실적 눈치", "28일 SK하이닉스 · 29일 삼성전자 실적 대기"),
          ("외국인 돌아올까", "매도가 멈추면 지수 안정에 힘이 될 가능성")]
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
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 한국경제, 서울경제, 뉴스핌, 뉴스1, AP</div>
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
  {daycard("화요일", "27", "이스라엘 총선<br>FOMC 시작", COL3[0], .15)}
  {daycard("수요일", "28", "SK하이닉스<br>실적", COL3[1], .3, True)}
  {daycard("목요일", "29", "삼성전자 실적<br>FOMC 결과", COL3[2], .45, True)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("owl", "happy", "wave"), 660, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 톡할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: AP, 뉴스핌, 뉴스1, 한국경제, 서울경제, SBS Biz, 이투데이, 아시아경제<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.3, 1.5), 3: (3.9, 1.5), 4: (3.9, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "msg", 1), (1, .05, "thud", .8), (1, .1, "drumroll", .4), (1, .3, "msg", .8), (1, .35, "thud", .9), (1, .6, "pop", .8), (1, .85, "question", .6),
 (2, .05, "whoosh", .5), (2, .1, "msg", .7), (2, .3, "pop", .6), (2, .5, "tick", .6), (2, .9, "tick", .6), (2, 1.3, "tick", .6), (2, 1.8, "thud", .9), (2, 2.2, "typing", .6), (2, 2.3, "msg", .6),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .2, "boing", .5), (3, .6, "pop", .6), (3, .9, "pop", .6), (3, 1.3, "boing", .6), (3, 1.6, "ding", .7),
 (4, .05, "whoosh", .5), (4, .1, "msg", .7), (4, .4, "pop", .6), (4, 1.0, "blip_down", .8), (4, 1.3, "thud", .7), (4, 1.7, "sad", .5),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "msg", .7), (6, .9, "jingle", .9),
]
