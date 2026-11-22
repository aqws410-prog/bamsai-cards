"""형식: 밤사이 단톡방 v6 (장면 1 '그룹통화 수신 화면 — 울리는 얼굴 타일 3개 + 받기/거절 버튼' 새 구도 · 검수 전 · 2026-11-23 월요일판) — 주말 단톡방 그룹통화로 정부 대책과 시장 반응을 정리.
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(야간선물 ▼6.99% + '정부, 증안펀드 준비 착수')을 0초부터 크게. 시그니처: 단톡방 그룹통화 화면 + 울림 물결 + 띠리링·쾅.
10-19(잠금화면 알림)·10-26(고정 투표판)·11-02(사진 공유)·11-09(채팅 목록)·11-16(위치 공유 지도)와 다르게, 그룹통화 수신 화면 구도로 새로 짰다.
흐름: 1 그룹통화(결론) → 2 금요일 밤 시장 반응(야간선물·MSCI 한국 ETF, 비트코인·걸프) → 3 비유(증안펀드 = 시동 건 소방차) → 4 함께 나온 대책 + 대만 → 5 공지(오늘 시나리오 3) → 6 이번 주 일정·마무리.
숫자는 2026-11-23 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes punch2{0%{transform:scale(1)}12%{transform:scale(1.15)}24%{transform:scale(.96)}34%{transform:scale(1.04)}46%,100%{transform:scale(1)}}
@keyframes jolt2{0%,100%{transform:translateX(0)}20%{transform:translateX(-16px)}40%{transform:translateX(14px)}60%{transform:translateX(-9px)}80%{transform:translateX(5px)}}
@keyframes ring{0%{transform:scale(.6);opacity:.9}100%{transform:scale(1.5);opacity:0}}
@keyframes buzz{0%,100%{transform:rotate(0)}20%{transform:rotate(-9deg)}40%{transform:rotate(8deg)}60%{transform:rotate(-6deg)}80%{transform:rotate(4deg)}}
@keyframes zoom2{0%{transform:scale(1)}30%{transform:scale(1.06)}100%{transform:scale(1)}}
@keyframes siren{0%,100%{opacity:1}50%{opacity:.25}}
.p2{display:inline-block;transform-origin:50% 60%;animation:punch2 1.1s ease-out var(--d,0s) both, jolt2 .45s ease-out calc(var(--d,0s) + .05s) both}
.ring{position:absolute;border-radius:50%;border:6px solid #8FE3A1;animation:ring 1s ease-out var(--d,0s) infinite}
.buzz{animation:buzz .5s ease-in-out var(--d,0s) infinite}
.zoom2{transform-origin:50% 50%;animation:zoom2 .7s ease-out var(--d,0s) both}
.siren{animation:siren .5s ease-in-out infinite}
</style>"""

def tile(kind, mood, col, top, d):
    """그룹통화 얼굴 타일: 둥근 얼굴 + 울림 물결 + 이름."""
    x, w = col
    s = 190
    cx = x + (w - s) // 2
    return (f'<div class="ring" style="left:{cx}px;top:{top}px;width:{s}px;height:{s}px;--d:{d+.15}s"></div>'
            f'<div class="abs" style="left:{cx}px;top:{top}px;width:{s}px;height:{s}px"><div class="buzz" style="--d:{d+.2}s;width:{s}px;height:{s}px;border-radius:50%;background:#fff;border:5px solid {L};overflow:hidden;box-sizing:border-box">{face_svg(kind, mood)}</div></div>'
            f'<div class="abs" style="left:{x}px;top:{top+205}px;width:{w}px;text-align:center;font-size:40px;color:#F6EEE4">{NAMES[kind]}</div>')

def callbtn(x, y, color, icon, d):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:120px;height:120px"><div class="buzz" style="--d:{d+.1}s;width:120px;height:120px;border-radius:50%;background:{color};border:5px solid {L};'
            f'box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:58px">{icon}</div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·그룹통화 화면·놀란 별콩이가 모두 보인다
S[1] = (1, page(FX + f'''
{stars(14, 123, 0, 180)}
{head("밤사이 단톡방 · 11.23 MON", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:188px;text-align:center;font-size:44px;color:#C9D6FF">코스피200 야간선물 · 20일(금) 밤</div>
<div class="abs" style="left:0;width:1080px;top:246px;text-align:center"><span class="p2" style="--d:0s;font-size:220px;line-height:1;color:#8EC5FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼6.99%</span></div>
<div class="abs" style="left:0;width:1080px;top:490px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">정부, 증안펀드 <span style="color:#FFE36E">준비</span> 착수</div>
<div class="chat zoom2" style="left:44px;top:630px;width:982px;height:560px;background:#2E2A55;--d:.3s">
  <div class="top" style="background:#8FE3A1">📞 밤사이 단톡방 그룹통화 <span style="margin-left:14px;font-size:30px;color:#3B5A44">주말 소식 듣자!</span></div>
  {tile("bamtol", "worried", COL3[0], 130, .25)}
  {tile("owl", "surprised", COL3[1], 130, .4)}
  {tile("moon", "normal", COL3[2], 130, .55)}
</div>
{callbtn(640, 1060, "#FF6B6B", "✕", .5)}
{callbtn(830, 1060, "#5BD17A", "📞", .6)}
<div class="abs" style="left:40px;top:1200px;width:420px"><div class="shiver">{mascot("star", "surprised", "up")}</div></div>
{sfx("띠리링!", 460, 1215, 76, .0, 8, "#8FE3A1")}
{sfx("쾅!", 880, 170, 80, .35, -10, "#FFE36E")}
{sfx("긴급!", 700, 1330, 76, .7, -6, "#FF8A8F")}
''', "#262B55"))

# 2 ── 금요일 밤 시장 반응
S[2] = (1, page(FX + f'''
{head("금요일 밤에 생긴 일", 2, "#F6EEE4")}
{chat("📞 밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("owl", '금요일 밤 미국 반도체지수<br><b>10.73%</b> 급락했어!', 110, .1, mood="surprised")}
  {numbox("코스피200 야간선물", '<span class="thump" style="--d:.8s">▼6.99%</span>', COL2[0], 330, .45, BLUE)}
  {numbox("MSCI 한국 ETF (미국 상장)", '<span class="thump" style="--d:1.0s">▼8.42%</span>', COL2[1], 330, .7, BLUE)}
  {msg("star", "주말엔 좀 나았어? 😥", 560, 1.3, "r", "teary")}
  {msg("bamtol", '비트코인은 <b>6만 달러 아래</b>로,<br>일요일 걸프 증시도 대부분 하락', 730, 1.9, mood="worried")}
  <div class="abs a-fade" style="left:{P}px;top:1000px;width:{IW}px;text-align:center;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#3B4660;--d:2.3s">야간선물이 오늘 지수를 그대로 정하진 않아요</div>
""")}
''', "#2B3060"))

# 3 ── 비유: 증안펀드 = 차고에서 시동 건 소방차
S[3] = (1, page(FX + f'''
{head("달떡이의 비유", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:76px;line-height:1.2"><span class="p2" style="--d:.1s">증안펀드 =<br>시동 건 <span style="color:{RED}">소방차</span></span></div>
  <div class="abs a-pop" style="left:0;right:0;top:240px;--d:.4s;text-align:center;font-size:160px;line-height:1"><span class="siren" style="display:inline-block">🚒</span></div>
  {stamp("출동 대기", 610, 300, .7, 10)}
  {numbox("약정 규모", "10조7,600억원", COL2[0], 450, .9, L)}
  {numbox("마지막 실제 투입", "2008년", COL2[1], 450, 1.15, L)}
  <div class="abs a-fade" style="left:{P}px;top:620px;width:{IW}px;text-align:center;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;--d:1.3s">증안펀드 = 증시가 크게 흔들릴 때 주식을 사 주려고 만든 돈 주머니<br>필요할 때 금융회사들에게서 돈을 걷는 방식</div>
  {ch(mascot("moon", "normal", "point"), P, 860, 250, 1.6, "a-sl", "squish")}
  {bub("시동은 걸었지만<br>아직 <b>출동</b>은 안 했어!<br>언제·얼마나는 미정", 320, 730, 1.8, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 함께 나온 대책 + 대만
S[4] = (1, page(FX + f'''
{head("대책은 또 있어", 4, "#F6EEE4")}
{chat("📞 밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("star", "또 뭐 해 준대?", 110, .1, "r", "normal")}
  <div class="abs a-rise" style="left:{P}px;top:250px;--d:.35s;width:{IW}px;height:230px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;padding:22px 30px">
    <div style="font-size:30px;color:#6B5A50">24일부터 3개월</div><div style="font-size:60px"><span class="thump" style="--d:.7s">자사주 매수 한도 완화</span></div>
    <div style="font-family:Noto Sans CJK KR,sans-serif;font-size:27px;color:#6B5A50">자사주 = 회사가 사들이는 자기 회사 주식</div></div>
  <div class="abs a-rise" style="left:{P}px;top:505px;--d:.8s;width:{IW}px;height:230px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;padding:22px 30px">
    <div style="font-size:30px;color:#6B5A50">3개월 · 금감원·거래소</div><div style="font-size:60px">불법 공매도 특별 감시</div>
    <div style="font-family:Noto Sans CJK KR,sans-serif;font-size:27px;color:#6B5A50">공매도 = 주식을 빌려 먼저 팔고 나중에 사서 갚는 것</div></div>
  {msg("owl", '대만은 <b>오늘부터</b> 공매도를 더 조여!<br>2015년 이후 처음', 790, 1.4, mood="surprised")}
""")}
''', "#4A3E78"))

# 5 ── 공지: 오늘 시나리오 3
checks = [("개장 초 큰 출렁임", "금요일 밤 반도체 급락이 반영되면 변동성이 커질 가능성"),
          ("정부 대책의 힘", "대책이 투자 심리를 받치면 낙폭이 줄어들 가능성"),
          ("외국인 반도체 매도", "지난주 4조 원 넘게 판 매도가 이어지면 부담 가능성")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{300+i*190}px;width:{IW}px;height:166px;box-sizing:border-box;--d:{.5+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:80px;height:80px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:48px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div><div style="font-size:52px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("📌 단톡방 공지", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:0;right:0;top:0;height:90px;background:#FFE36E;border-bottom:4px solid {L};font-size:40px;line-height:90px;padding-left:34px">📌 공지 · 밤톨이 · 오늘 한국장</div>
  <div class="abs" style="left:0;right:0;top:140px;text-align:center;font-size:84px"><span class="p2" style="--d:.1s">충격일까, <span style="color:#E8590C">대책일까?</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point"), 680, 805, 220, 2.0, "a-sr", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 서울경제, OBC, 톱스타뉴스, 이투데이, 더페어</div>
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
  {daycard("수요일 밤", "25", "미국 PCE<br>물가·GDP", COL3[0], .15)}
  {daycard("목요일", "26", "한은<br>금통위", COL3[1], .3, True)}
  {daycard("추수감사절", "26", "미국<br>휴장", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("owl", "happy", "wave"), 660, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 톡할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 아시아경제, 파이낸셜뉴스, 재경일보, 톱스타뉴스, 서울경제, 아이뉴스24, 주간경향, 이투데이, 더페어, 시사저널e, 한겨레, 로이터, 대만 중앙통신<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.4, 1.5), 3: (4.4, 1.5), 4: (4.2, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "msg", .9), (1, .05, "thud", .8), (1, .25, "pop", .5), (1, .3, "whoosh", .5), (1, .35, "thud", .9), (1, .4, "pop", .5), (1, .55, "pop", .5), (1, .7, "tension", .5), (1, .9, "question", .6),
 (2, .05, "whoosh", .5), (2, .1, "msg", .7), (2, .45, "blip_down", .7), (2, .7, "blip_down", .7), (2, 1.3, "msg", .6), (2, 1.4, "sad", .4), (2, 1.9, "msg", .6), (2, 2.3, "tick", .4),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .4, "boing", .6), (3, .7, "thud", .8), (3, .9, "pop", .6), (3, 1.15, "pop", .6), (3, 1.6, "boing", .6), (3, 1.8, "ding", .7),
 (4, .05, "whoosh", .5), (4, .1, "msg", .7), (4, .35, "pop", .6), (4, .7, "ding", .6), (4, .8, "pop", .6), (4, 1.4, "msg", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "msg", .7), (6, .9, "jingle", .9),
]
