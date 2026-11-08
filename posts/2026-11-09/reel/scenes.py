"""형식: 밤사이 단톡방 v4 (장면 1 '채팅 목록 화면 + 안 읽은 배지' 새 구도 · 검수 전 · 2026-11-09 월요일판) — 주말 단톡방에 쌓인 안 읽은 메시지를 열어 보며 정리.
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(지난주 코스피 ▼11.71% + '주말엔 숨통, 단 합의 조건')을 0초부터 크게. 시그니처: 휴대폰 채팅 목록 + 빨간 안 읽은 배지(99+) 펑 + 띵동(msg).
10-19(잠금화면 알림)·10-26(고정 투표판)·11-02(사진 공유+리액션)와 다르게, 채팅방 목록 화면 구도로 새로 짰다.
흐름: 1 채팅 목록(결론) → 2 트럼프 "재공격 매우 낮다"(합의 전제) → 3 비유(앞문은 안 두드리고, 뒷골목까지 막는다) → 4 오늘부터 140%룰 쉰다(떨이 판매 비유) → 5 공지(오늘 시나리오 3) → 6 이번 주 일정·마무리.
숫자는 2026-11-09 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes punch2{0%{transform:scale(1)}12%{transform:scale(1.15)}24%{transform:scale(.96)}34%{transform:scale(1.04)}46%,100%{transform:scale(1)}}
@keyframes jolt2{0%,100%{transform:translateX(0)}20%{transform:translateX(-16px)}40%{transform:translateX(14px)}60%{transform:translateX(-9px)}80%{transform:translateX(5px)}}
@keyframes badge{0%{transform:scale(1)}25%{transform:scale(1.45)}50%{transform:scale(.9)}70%{transform:scale(1.1)}100%{transform:scale(1)}}
@keyframes vib{0%,100%{transform:rotate(0)}20%{transform:rotate(-2deg)}40%{transform:rotate(2deg)}60%{transform:rotate(-1.5deg)}80%{transform:rotate(1deg)}}
@keyframes rowin{from{background:#FFF3B0}to{background:#fff}}
.p2{display:inline-block;transform-origin:50% 60%;animation:punch2 1.1s ease-out var(--d,0s) both, jolt2 .45s ease-out calc(var(--d,0s) + .05s) both}
.badge{display:inline-flex;align-items:center;justify-content:center;min-width:76px;height:64px;padding:0 14px;box-sizing:border-box;border-radius:32px;background:#E8484A;color:#fff;border:4px solid #3A2A22;font-size:36px;animation:badge .6s ease-out var(--d,0s) both}
.vib{transform-origin:50% 50%;animation:vib .5s ease-in-out var(--d,0s) 2 both}
.row{position:absolute;left:0;right:0;height:132px;border-bottom:3px solid #E4DCD2;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box;background:#fff}
.row .ic{flex:none;width:92px;height:92px;border-radius:30px;border:4px solid #3A2A22;overflow:hidden;background:#fff}
.row .t1{font-size:38px}
.row .t2{font-family:'Noto Sans CJK KR',sans-serif;font-size:27px;color:#6B5A50;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:560px}
.rowhot{animation:rowin 1.2s ease-out var(--d,0s) both}
</style>"""

def row(top, icon, t1, t2, badge, d, hot=False):
    return (f'<div class="row {"rowhot" if hot else ""}" style="top:{top}px;--d:{d}s"><div class="ic">{icon}</div>'
            f'<div style="flex:1;min-width:0"><div class="t1">{t1}</div><div class="t2">{t2}</div></div>'
            f'<span class="badge" style="--d:{d}s">{badge}</span></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·채팅 목록·놀란 별콩이가 모두 보인다
S[1] = (1, page(FX + f'''
{stars(14, 59, 0, 180)}
{head("밤사이 단톡방 · 11.09 MON", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:188px;text-align:center;font-size:44px;color:#C9D6FF">지난주 코스피 (11/2~6)</div>
<div class="abs" style="left:0;width:1080px;top:246px;text-align:center"><span class="p2" style="--d:0s;font-size:230px;line-height:1;color:#5AA9FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼11.71%</span></div>
<div class="abs" style="left:0;width:1080px;top:490px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">주말엔 숨통, <span style="color:#FFE36E">단 '합의' 조건</span></div>
<div class="abs vib" style="left:44px;top:630px;width:982px;height:760px;--d:.3s">
 <div class="chat" style="left:0;top:0;width:982px;height:760px;background:#F7F1E8">
  <div class="top" style="background:#FFE36E">💬 채팅 <span style="margin-left:14px;font-size:30px;color:#6B5A50">주말 사이 안 읽은 메시지</span></div>
  {row(84, face_svg("owl", "surprised"), "📌 밤사이 단톡방", '솜부엉: 트럼프 "재공격 가능성 매우 낮다"', "99+", .3, True)}
  {row(216, face_svg("moon", "normal"), "달떡이", "오늘부터 '140%룰' 3개월 쉰대!", "3", .55)}
  {row(348, face_svg("bamtol", "worried"), "밤톨이", "근데 조건이 붙었어…", "1", .8)}
 </div>
 {stamp("합의 조건", 470, 560, .45, -10)}
 <div class="abs" style="left:30px;top:470px;width:340px"><div class="shiver">{mascot("star", "surprised", "up")}</div></div>
</div>
{sfx("띵동!", 720, 612, 80, .0, 10, "#FFE36E")}
{sfx("펑!", 640, 700, 64, .3, -8, "#fff")}
''', "#262B55"))

# 2 ── 트럼프 "재공격 매우 낮다" — 단, 합의 전제
S[2] = (1, page(FX + f'''
{head("주말 단톡방 열어 보기", 2, "#F6EEE4")}
{chat("📌 밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("owl", "8일(현지) 트럼프 CNN 인터뷰!", 110, .1, mood="surprised")}
  <div class="abs a-rise" style="left:{P}px;top:260px;--d:.35s;width:{IW}px;height:380px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;text-align:center;padding-top:34px">
    <div style="font-size:46px">🇺🇸 이란 재공격 가능성?</div>
    <div style="font-size:150px;line-height:1.2"><span class="thump" style="--d:.7s">"매우 낮다"</span></div></div>
  {stamp("합의 전제", 560, 560, 1.0, -8)}
  {msg("star", "그럼 이제 끝난 거야?! 🙌", 700, 1.4, "r", "happy")}
  {msg("bamtol", '이란이 <b>강력한 합의</b>에 서명해야 해.<br>"교량 38개, 1시간이면" 경고도 했고', 880, 2.0, mood="worried")}
""")}
''', "#2B3060"))

# 3 ── 비유: 앞문은 안 두드리는데, 뒷골목까지 막는다
def door(col, icon, title, big_, sub, bg, d):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:250px;width:{w}px;height:430px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:28px;text-align:center;padding-top:22px">'
            f'<div style="font-size:42px">{title}</div><div style="font-size:120px;line-height:1.2">{icon}</div>'
            f'<div style="font-size:60px">{big_}</div><div style="font-size:32px;color:#6B5A50;margin-top:6px">{sub}</div></div>')
S[3] = (1, page(FX + f'''
{head("달떡이의 비유", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:84px;line-height:1.15"><span class="p2" style="--d:.1s">공격은 <span style="color:{BLUE}">멈칫</span>, 봉쇄는 <span style="color:{RED}">꽉</span></span></div>
  {door(COL2[0], "🚪", "앞문 (공격)", "안 두드림", '"재공격 매우 낮다"', "#E3EEFF", .45)}
  {door(COL2[1], "🚧", "뒷골목 (봉쇄)", "더 막음", "바다 → 육로·카스피해", "#FFE3E3", .8)}
  <div class="abs a-pop" style="left:{P}px;top:720px;--d:1.3s;width:{IW}px;height:170px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;display:flex;align-items:center;justify-content:center;gap:20px">
    <div style="font-size:46px">미군 새 전담팀</div><div style="font-size:84px;color:{RED}"><span class="thump" style="--d:1.6s">'아이언 게이트'</span></div></div>
  {ch(mascot("moon", "normal", "point"), P, 900, 250, 1.7, "a-sl", "squish")}
  {bub("원유를 사 오는 한국엔<br><b>기름값·환율</b>이 걸린 일!", 330, 930, 1.9, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 오늘부터 140%룰 쉰다 (떨이 판매 비유)
S[4] = (1, page(FX + f'''
{head("오늘 한국장 소식", 4, "#F6EEE4")}
{chat("📌 밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("moon", "오늘(9일)부터 3개월간 쉬는 규칙!", 110, .1, mood="happy")}
  <div class="abs a-rise" style="left:{P}px;top:260px;--d:.35s;width:{IW}px;height:300px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;text-align:center;padding-top:26px">
    <div style="font-size:44px">빚투 담보비율 유지의무</div>
    <div style="font-size:150px;line-height:1.1"><span class="thump" style="--d:.7s">140%룰</span> <span style="font-size:70px;color:#6B5A50">면제</span></div></div>
  <div class="abs a-sl" style="left:{P}px;top:600px;--d:1.1s;width:{IW}px;height:200px;box-sizing:border-box;background:#FFE3E3;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:24px;padding:0 30px">
    <div style="font-size:100px">🏷️</div><div><div style="font-size:52px">주가가 빠지면 빚 낸 주식을</div><div style="font-size:52px">강제로 <span style="color:{RED}">'떨이'</span> 판매 (반대매매)</div></div></div>
  {msg("star", "떨이가 몰리면 값이 더 빠지니까<br>잠깐 쉬게 한 거구나! 💡", 830, 1.9, "r", "surprised")}
""")}
''', "#4A3E78"))

# 5 ── 공지: 오늘 시나리오 3
checks = [("반대매매 진정", "강제 매도가 줄면 급락세가 누그러질 가능성"),
          ("이란 협상 기대", "합의 기대 ↑면 기름값 부담 ↓, 멈추면 유가 출렁 가능성"),
          ("물가 앞 눈치 보기", "내일 밤 미국 CPI 앞두고 급등락 되풀이 가능성")]
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
  <div class="abs" style="left:0;right:0;top:140px;text-align:center;font-size:88px"><span class="p2" style="--d:.1s">5,000선, <span style="color:#E8590C">오늘은?</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point"), 680, 805, 220, 2.0, "a-sr", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 정책브리핑, SBS Biz, 파이낸셜뉴스, 아시아경제, 연합인포맥스</div>
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
  <div class="abs" style="left:{P}px;top:30px;font-size:42px;color:#FFC08A">이번 주, 이 날짜만! (한국시간)</div>
  {daycard("화요일 밤", "10", "미국<br>10월 CPI", COL3[0], .15, True)}
  {daycard("수요일 아침", "11", "코어위브<br>실적", COL3[1], .3)}
  {daycard("목요일", "12", "옵션<br>만기일", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("owl", "happy", "wave"), 660, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 톡할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 뉴스1, SBS Biz, 파이낸셜뉴스, 아시아경제, 한국경제, 정책브리핑, 코어위브 공시<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.4, 1.5), 3: (4.0, 1.5), 4: (4.2, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "msg", .9), (1, .05, "thud", .8), (1, .3, "pop", .9), (1, .3, "msg", .6), (1, .45, "thud", .9), (1, .55, "pop", .7), (1, .8, "pop", .7), (1, .9, "question", .6),
 (2, .05, "whoosh", .5), (2, .1, "msg", .7), (2, .35, "pop", .6), (2, .7, "ding", .6), (2, 1.0, "thud", .9), (2, 1.4, "msg", .6), (2, 2.0, "msg", .6), (2, 2.1, "hmm", .4),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .45, "pop", .6), (3, .8, "pop", .6), (3, 1.3, "thud", .7), (3, 1.7, "boing", .6), (3, 1.9, "ding", .7),
 (4, .05, "whoosh", .5), (4, .1, "msg", .7), (4, .35, "pop", .6), (4, .7, "ding", .6), (4, 1.1, "slidedown", .5), (4, 1.9, "msg", .6), (4, 2.0, "ding", .6),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "msg", .7), (6, .9, "jingle", .9),
]
