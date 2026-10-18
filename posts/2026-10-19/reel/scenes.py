"""형식: 밤사이 단톡방 (처음 제작 · 검수 전 · 2026-10-19 월요일판) — 솜부엉이 속보를 올리고, 별콩이가 묻고, 달떡이가 비유로 풀고, 밤톨이가 정리.
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(야간선물 ▼3.50% + '금요일 밤 야간선물 급락')을 0초부터 크게. 시그니처: 휴대폰 잠금화면 알림 + 단톡방 화면 + 띵동(msg)·타닥(typing).
흐름: 1 속보 알림(결론) → 2 차트 사진 공유·질문 → 3 비유(단골손님 지갑 걱정) → 4 한국 이야기(낮엔 반등, 밤엔 급락) → 5 공지(오늘 체크 3) → 6 마무리.
숫자는 2026-10-19 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes punch{0%{transform:scale(1)}12%{transform:scale(1.15)}24%{transform:scale(.96)}34%{transform:scale(1.04)}46%,100%{transform:scale(1)}}
@keyframes jolt{0%,100%{transform:translateX(0)}20%{transform:translateX(-16px)}40%{transform:translateX(14px)}60%{transform:translateX(-9px)}80%{transform:translateX(5px)}}
@keyframes buzz{0%,100%{transform:rotate(0)}10%{transform:rotate(-2.2deg)}20%{transform:rotate(2.2deg)}30%{transform:rotate(-1.6deg)}40%{transform:rotate(1.6deg)}50%{transform:rotate(-.8deg)}60%,99%{transform:rotate(0)}}
@keyframes bardrop{from{transform:scaleY(1)}to{transform:scaleY(var(--s))}}
@keyframes badge{0%,100%{transform:scale(1)}50%{transform:scale(1.2)}}
.punch2{display:inline-block;transform-origin:50% 60%;animation:punch 1.1s ease-out var(--d,0s) both, jolt .45s ease-out calc(var(--d,0s) + .05s) both}
.buzz{transform-origin:50% 50%;animation:buzz .6s ease-out var(--d,0s) both}
.badge{display:inline-block;animation:badge .5s ease-in-out infinite}
</style>"""

APP = (f'<div style="flex:none;width:92px;height:92px;border-radius:26px;background:#2A2F5E;border:4px solid {L};overflow:hidden">'
       f'{face_svg("owl", "surprised")}</div>')

def notif(title, body, top, d=0, anim=""):
    """잠금화면 알림 카드 (단톡방 시그니처)."""
    return (f'<div class="abs {anim}" style="left:44px;top:{top}px;width:982px;--d:{d}s"><div class="buzz" style="--d:{d}s;box-sizing:border-box;background:rgba(255,255,255,.96);'
            f'border:6px solid {L};border-radius:30px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;gap:22px;align-items:center;padding:16px 24px">{APP}'
            f'<div style="flex:1"><div style="font-size:34px;color:#6B5A50">{title}</div><div style="font-size:46px;line-height:1.25">{body}</div></div></div></div>')

# 1 ── 결론 먼저: 0초에 알림·숫자·결론·놀란 별콩이 모두 보인다
S[1] = (1, page(FX + f'''
{stars(14, 61, 0, 180)}
{head("밤사이 단톡방 · 10.19 MON", 1, "#F6EEE4")}
{notif("💬 밤사이 단톡방 · 지금", "솜부엉: 속보!! 야간선물 봤어?", 186)}
<div class="abs" style="left:0;width:1080px;top:360px;text-align:center;font-size:48px;color:#C9D6FF">코스피200 야간선물 · 16일 밤</div>
<div class="abs" style="left:0;width:1080px;top:420px;text-align:center"><span class="punch2" style="--d:0s;font-size:230px;line-height:1;color:#7DBBFF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼3.50%</span></div>
<div class="abs" style="left:0;width:1080px;top:668px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">금요일 밤, <span style="color:#FFE36E">야간선물 급락</span></div>
<div class="panel" style="left:44px;top:810px;width:982px;height:580px;background:#BFD0E6">
  <div class="abs" style="left:0;right:0;top:0;height:84px;background:#AFC2DC;border-bottom:4px solid {L};font-size:36px;line-height:84px;padding-left:30px">밤사이 단톡방 (4) <span class="badge" style="margin-left:10px;background:#E8484A;color:#fff;border-radius:999px;padding:0 14px;font-size:30px">+99</span></div>
  <div class="abs" style="left:-10px;top:120px;width:500px"><div class="shiver">{mascot("star", "surprised", "up")}</div></div>
  <div class="abs a-pop" style="left:470px;top:150px;--d:.6s;width:470px;box-sizing:border-box;background:#FFE36E;border:4px solid {L};border-radius:26px;padding:16px 22px;font-size:48px;line-height:1.3;text-align:center">헉, 금요일엔<br><span style="color:{RED}">반등</span>했잖아?!</div>
  <div class="abs a-pop" style="left:520px;top:390px;--d:.85s;font-size:40px;background:#fff;border:4px solid {L};border-radius:999px;padding:6px 22px">무슨 일이야 😱</div>
</div>
{sfx("띵동!", 770, 830, 92, .3, 10, "#FFE36E")}
''', "#262B55"))

# 2 ── 사진(차트) 공유 + 질문
bars = [(1, .92), (2, .86), (3, .80), (4, .72), (5, .66), (6, .58), (7, .5), (8, .38)]
barhtml = "".join(
    f'<div class="abs" style="left:{30 + (i-1)*62}px;bottom:50px;width:44px;height:240px;transform-origin:50% 100%;--s:{s};'
    f'animation:bardrop .35s ease-out {0.55 + i*0.09:.2f}s both;background:#7DBBFF;border:4px solid {L};border-radius:8px 8px 0 0"></div>'
    f'<div class="abs" style="left:{30 + (i-1)*62}px;bottom:8px;width:44px;text-align:center;font-size:26px;color:#C9D6FF">{i}</div>'
    for i, s in bars)
chart = (f'<div style="position:relative;width:560px;height:340px;background:#1F2347;border-radius:16px;overflow:hidden">'
         f'<div class="abs" style="left:20px;top:14px;font-size:30px;color:#FFE59A">미국 반도체 · 하락 일수</div>{barhtml}</div>')
S[2] = (1, page(FX + f'''
{head("사진 1장이 올라왔어요", 2, "#F6EEE4")}
{chat("밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("owl", "📷 금요일 밤 미국 반도체", 110, .1)}
  <div class="abs a-rise" style="left:124px;top:250px;--d:.3s;background:#fff;border:4px solid {L};border-radius:24px;padding:14px">{chart}</div>
  <div class="abs a-stamp" style="left:560px;top:270px;--d:1.4s;--r:-8deg;background:#fff;border:6px solid {L};border-radius:22px;padding:4px 20px;font-size:64px;color:{BLUE}">▼3.83%</div>
  <div class="abs a-pop" style="left:124px;top:660px;--d:1.7s;font-size:58px;background:#FFF0B3;border:4px solid {L};border-radius:20px;padding:8px 24px"><span class="thump" style="--d:1.9s">8일 연속</span> 하락 · 2008년 이후 최장</div>
  {msg("star", "근데 미국 반도체가<br>왜 우리 선물까지?", 860, 2.3, "r", "worried")}
""")}
''', "#2B3060"))

# 3 ── 비유: 단골손님이 지갑 걱정을 하면 가게도 긴장
def shopbox(icon, t, col, d, bg="#fff"):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:470px;width:{w}px;height:250px;box-sizing:border-box;--d:{d}s;background:{bg};border:4px solid {L};border-radius:26px;text-align:center;padding:14px 8px">'
            f'<div style="font-size:84px;line-height:1.15">{icon}</div><div style="font-size:36px;line-height:1.25">{t}</div></div>')
def arrow(after, d):
    x0 = after[0] + after[1]
    return f'<div class="abs a-fade" style="left:{x0}px;top:550px;width:76px;text-align:center;font-size:64px;--d:{d}s">→</div>'
S[3] = (1, page(FX + f'''
{head("달떡이의 비유", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:96px;line-height:1.1"><span class="punch2" style="--d:.1s">단골손님이<br><span style="color:#7B3FC4">지갑 걱정</span>을 하면?</span></div>
  {shopbox("🏢", "단골손님<br>AI 빅테크", COL3[0], .5)}
  {arrow(COL3[0], .8)}
  {shopbox("💸❓", "'AI 투자,<br>돈 될까?'", COL3[1], .9, "#FFF0B3")}
  {arrow(COL3[1], 1.2)}
  {shopbox("🏪", "반도체 가게<br>긴장", COL3[2], 1.3, "#E3EDFF")}
  {ch(mascot("moon", "normal", "point"), P, 790, 290, 1.8, "a-sl", "squish")}
  {bub("반도체를 많이 사 주던<br>손님이 망설이면<br><b>파는 쪽 주가</b>도 흔들려요", 350, 800, 2.1, "t-left", style="font-size:42px")}
</div>
''', "#30366E"))

# 4 ── 한국 이야기: 낮엔 반등, 밤엔 급락
S[4] = (1, page(FX + f'''
{head("우리 코스피는?", 4, "#F6EEE4")}
{chat("밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("bamtol", "금요일(16일) 정리해 줄게!", 110, .1)}
  <div class="abs a-sl" style="left:{P}px;top:270px;--d:.4s;width:{IW}px;height:250px;box-sizing:border-box;background:#FFF6EA;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px">
    <div style="font-size:110px">☀️</div><div><div style="font-size:40px">낮 · 코스피</div><div style="font-size:110px;line-height:1;color:{RED}">▲2.05%</div></div></div>
  <div class="abs a-sl" style="left:{P}px;top:560px;--d:1.0s;width:{IW}px;height:250px;box-sizing:border-box;background:#2A2F5E;color:#fff;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px">
    <div style="font-size:110px">🌙</div><div><div style="font-size:40px">밤 · 야간선물</div><div style="font-size:110px;line-height:1;color:#7DBBFF"><span class="thump" style="--d:1.3s">▼3.50%</span></div></div></div>
  {msg("star", "낮엔 웃고<br>밤엔 울었네…", 860, 1.7, "r", "teary")}
  {msg("owl", "외국인도 그날은 <b style='color:#E03131;font-weight:400'>샀어</b>!", 1010, 2.2, mood="happy")}
""")}
''', "#4A3E78"))

# 5 ── 공지: 오늘 체크 3
checks = [("반도체가 출발선", f"야간선물 <span style='color:#1D4ED8'>▼3.50%</span> 반영되면 약한 출발 가능성"),
          ("외국인이 또 살까", "이어지면 낙폭을 줄일 가능성"),
          ("중국 GDP와 기름값", "오늘 중국 3분기 성적 발표")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{300+i*190}px;width:{IW}px;height:166px;box-sizing:border-box;--d:{.6+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:80px;height:80px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:48px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div><div style="font-size:52px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("📌 단톡방 공지", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:0;right:0;top:0;height:90px;background:#FFE36E;border-bottom:4px solid {L};font-size:40px;line-height:90px;padding-left:34px">📌 공지 · 밤톨이</div>
  <div class="abs" style="left:0;right:0;top:140px;text-align:center;font-size:88px"><span class="punch2" style="--d:.1s">오늘 장 <span style="color:#E8590C">체크 3</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point"), 680, 805, 220, 2.1, "a-sr", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 연합뉴스, 서울경제, 뉴스핌, 뉴스1, 한국경제</div>
''', "#FFE1CC"))

# 6 ── 마무리: 이번 주 일정 + 팔로우
def daycard(day, date, t, col, d, hi=False):
    x, w = col
    bg = "#FFD84D" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:{w}px;height:280px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};'
            f'border-radius:26px;box-shadow:0 6px 0 rgba(0,0,0,.15);text-align:center;padding:14px 8px;color:{L}">'
            f'<div style="font-size:32px;color:#6B5A50">{day}</div><div style="font-size:88px;line-height:1.05">{date}</div>'
            f'<div style="font-size:34px;line-height:1.2;margin-top:6px">{t}</div></div>')
S[6] = (1, page(FX + f'''
{head("이번 주 일정 · 마무리", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:30px;font-size:42px;color:#FFC08A">이번 주, 이 날짜만!</div>
  {daycard("오늘(월)", "19", "중국 GDP", COL3[0], .15)}
  {daycard("수요일", "21", "메타 실적<br>(현지)", COL3[1], .3)}
  {daycard("목요일", "22", "한은 금리", COL3[2], .45, True)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("owl", "happy", "wave"), 660, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 톡할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 연합뉴스, 로이터, 뉴스핌, 뉴스1, 서울경제, 한국경제, SBS Biz<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.9, 1.5), 3: (4.0, 1.5), 4: (3.9, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "msg", 1), (1, .05, "thud", .8), (1, .3, "msg", .8), (1, .35, "thud", .7), (1, .6, "pop", .8), (1, .85, "question", .6),
 (2, .05, "whoosh", .5), (2, .1, "msg", .7), (2, .3, "shutter", .8), (2, .6, "slidedown", .6), (2, 1.4, "thud", .9), (2, 1.7, "pop", .7), (2, 2.3, "typing", .6), (2, 2.4, "msg", .6),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .5, "pop", .6), (3, .9, "hmm", .5), (3, 1.3, "pop", .6), (3, 1.8, "boing", .6), (3, 2.1, "ding", .7),
 (4, .05, "whoosh", .5), (4, .1, "msg", .7), (4, .4, "sparkle", .6), (4, 1.0, "blip_down", .8), (4, 1.3, "thud", .7), (4, 1.7, "sad", .5), (4, 2.2, "msg", .6),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .6, "CHECK1", 1), (5, 1.05, "CHECK2", 1), (5, 1.5, "CHECK3", 1), (5, 2.1, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "msg", .7), (6, .9, "jingle", .9),
]
