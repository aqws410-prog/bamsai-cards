"""형식: 밤사이 단톡방 v5 (장면 1 '위치 공유 지도 카드 + 핀 꽂힘' 새 구도 · 검수 전 · 2026-11-16 월요일판) — 주말 단톡방에 올라온 '위치 공유'로 중동 소식을 정리.
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(이란 '드론 6대' 주장 + '미군 기지 공격 재개')을 0초부터 크게. 시그니처: 채팅 속 위치 공유 지도 카드 + 바레인에 빨간 핀 콩 + 경보 물결.
10-19(잠금화면 알림)·10-26(고정 투표판)·11-02(사진 공유+리액션)·11-09(채팅 목록+안 읽은 배지)와 다르게, 지도 공유 카드 구도로 새로 짰다.
흐름: 1 지도 공유(결론) → 2 주말 소식(15일 드론 6대 주장·전국 경보·13일 격추) → 3 비유(호르무즈 = 기름이 지나가는 빨대) → 4 이번 주 시험대(지난주 코스피 ▲4.56%, 엔비디아·3자 회담) → 5 공지(오늘 시나리오 3) → 6 이번 주 일정·마무리.
숫자는 2026-11-16 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes punch2{0%{transform:scale(1)}12%{transform:scale(1.15)}24%{transform:scale(.96)}34%{transform:scale(1.04)}46%,100%{transform:scale(1)}}
@keyframes jolt2{0%,100%{transform:translateX(0)}20%{transform:translateX(-16px)}40%{transform:translateX(14px)}60%{transform:translateX(-9px)}80%{transform:translateX(5px)}}
@keyframes pin{0%{transform:translateY(0)}20%{transform:translateY(-70px)}45%{transform:translateY(0) scale(1.15,.85)}60%{transform:translateY(-18px)}80%,100%{transform:translateY(0)}}
@keyframes ring{0%{transform:scale(.3);opacity:.9}100%{transform:scale(2.6);opacity:0}}
@keyframes zoom2{0%{transform:scale(1)}30%{transform:scale(1.06)}100%{transform:scale(1)}}
.p2{display:inline-block;transform-origin:50% 60%;animation:punch2 1.1s ease-out var(--d,0s) both, jolt2 .45s ease-out calc(var(--d,0s) + .05s) both}
.pin{transform-origin:50% 100%;animation:pin .8s ease-out var(--d,0s) both}
.ring{position:absolute;border-radius:50%;border:6px solid #E8484A;animation:ring 1.1s ease-out var(--d,0s) infinite}
.zoom2{transform-origin:50% 50%;animation:zoom2 .7s ease-out var(--d,0s) both}
</style>"""

def gulf_map(w, h, d_pin=.3):
    """위치 공유 지도(간단한 걸프 그림): 위·오른쪽 이란, 왼쪽 아래 아라비아 반도, 왼쪽 가운데 바레인 핀, 오른쪽 좁은 곳 호르무즈."""
    return f'''<svg viewBox="0 0 900 470" width="{w}" height="{h}" style="display:block">
  <rect x="0" y="0" width="900" height="470" fill="#BFE0F5"/>
  <path d="M0 0 H900 V250 C840 230 800 170 730 150 C640 125 560 120 470 95 C370 70 260 60 150 40 C90 30 40 25 0 30 Z" fill="#EADBC2" stroke="{L}" stroke-width="5"/>
  <path d="M0 470 V170 C60 175 120 200 170 240 C210 270 240 300 300 310 C380 325 470 300 560 285 C640 272 700 250 760 300 C790 330 800 380 830 470 Z" fill="#F3E6CF" stroke="{L}" stroke-width="5"/>
  <circle cx="205" cy="232" r="13" fill="#F3E6CF" stroke="{L}" stroke-width="4"/>
  <text x="560" y="70" font-family="Jua" font-size="44" fill="{L}">이란</text>
  <text x="40" y="420" font-family="Jua" font-size="36" fill="#6B5A50">아라비아 반도</text>
  <text x="640" y="225" font-family="Jua" font-size="34" fill="{L}">호르무즈 해협</text>
  <text x="120" y="292" font-family="Jua" font-size="34" fill="{L}">바레인</text>
</svg>
<div class="ring" style="left:{w*205/900-30:.0f}px;top:{h*232/470-30:.0f}px;width:60px;height:60px;--d:{d_pin+.2}s"></div>
<div class="abs pin" style="left:{w*205/900-34:.0f}px;top:{h*232/470-88:.0f}px;--d:{d_pin}s"><svg width="68" height="90" viewBox="0 0 68 90"><path d="M34 88 C34 88 4 52 4 32 A30 30 0 0 1 64 32 C64 52 34 88 34 88Z" fill="#E8484A" stroke="{L}" stroke-width="5"/><circle cx="34" cy="32" r="11" fill="#fff" stroke="{L}" stroke-width="4"/></svg></div>'''

# 1 ── 결론 먼저: 0초에 숫자·결론·지도 카드·놀란 별콩이가 모두 보인다
S[1] = (1, page(FX + f'''
{stars(14, 71, 0, 180)}
{head("밤사이 단톡방 · 11.16 MON", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:188px;text-align:center;font-size:44px;color:#C9D6FF">이란 혁명수비대 주장 · 15일(현지)</div>
<div class="abs" style="left:0;width:1080px;top:246px;text-align:center"><span class="p2" style="--d:0s;font-size:220px;line-height:1;color:#FFE36E;-webkit-text-stroke:10px {L};paint-order:stroke fill">드론 6대</span></div>
<div class="abs" style="left:0;width:1080px;top:490px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">미군 기지 공격 <span style="color:#FF8A8F">재개</span></div>
<div class="chat zoom2" style="left:44px;top:630px;width:982px;height:620px;background:#F7F1E8;--d:.3s">
  <div class="top" style="background:#FFE36E">📍 밤사이 단톡방 <span style="margin-left:14px;font-size:30px;color:#6B5A50">솜부엉님이 위치를 공유했어요</span></div>
  <div class="abs" style="left:{P}px;top:105px;width:{IW}px;height:430px;border:5px solid {L};border-radius:26px;overflow:hidden;box-sizing:border-box">{gulf_map(IW-10, 420)}</div>
  <div class="abs" style="left:{P}px;top:548px;width:{IW}px;font-size:40px;text-align:center;color:#6B5A50">바레인 미군 기지 · <span style="color:{RED}">피해는 아직 미확인</span></div>
</div>
<div class="abs" style="left:40px;top:1210px;width:420px"><div class="shiver">{mascot("star", "surprised", "up")}</div></div>
{sfx("띵동!", 720, 612, 80, .0, 10, "#FFE36E")}
{sfx("콕!", 210, 700, 64, .35, -8, "#fff")}
{sfx("삐용삐용!", 480, 1300, 72, .7, 6, "#FF8A8F")}
''', "#262B55"))

# 2 ── 주말 소식 정리
S[2] = (1, page(FX + f'''
{head("주말 단톡방 열어 보기", 2, "#F6EEE4")}
{chat("📍 밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("owl", "15일(현지) 이란 혁명수비대 발표!", 110, .1, mood="surprised")}
  <div class="abs a-rise" style="left:{P}px;top:260px;--d:.35s;width:{IW}px;height:330px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;text-align:center;padding-top:30px">
    <div style="font-size:46px">바레인 미군 레이더에</div>
    <div style="font-size:150px;line-height:1.2"><span class="thump" style="--d:.7s">드론 6대</span></div></div>
  {stamp("공격 주장", 600, 520, 1.0, -8)}
  {msg("star", "진짜 맞은 거야?! 😱", 650, 1.4, "r", "surprised")}
  {msg("bamtol", '바레인은 <b>여러 발 요격</b>했대.<br>9월 이후 첫 <b>전국 경보</b>, 피해는 미확인', 820, 2.0, mood="worried")}
""")}
''', "#2B3060"))

# 3 ── 비유: 호르무즈 해협 = 기름이 지나가는 빨대
S[3] = (1, page(FX + f'''
{head("달떡이의 비유", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:76px;line-height:1.2"><span class="p2" style="--d:.1s">호르무즈 해협 =<br>기름이 지나가는 <span style="color:{RED}">빨대</span></span></div>
  <div class="abs a-pop" style="left:0;right:0;top:250px;--d:.5s;text-align:center;font-size:150px;line-height:1">🥤</div>
  {numbox("유조선 기뢰·화재 (이란 주장)", "3척", COL2[0], 440, .8, RED)}
  {numbox("지난달 선박 공격 (전쟁 뒤 최다)", "37건", COL2[1], 440, 1.1, RED)}
  <div class="abs a-fade" style="left:{P}px;top:610px;width:{IW}px;text-align:center;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;--d:1.2s">3척: 14일(현지) 이란 주장, 로이터 확인 못 함<br>37건: 로이즈 리스트 집계</div>
  {ch(mascot("moon", "worried", "point"), P, 860, 250, 1.6, "a-sl", "squish")}
  {bub("빨대 근처가 시끄러우면<br>원유를 사 오는 한국엔<br><b>기름값·환율</b> 걱정!", 320, 720, 1.8, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 이번 주 시험대
S[4] = (1, page(FX + f'''
{head("이번 주 시험대", 4, "#F6EEE4")}
{chat("📍 밤사이 단톡방 (4)", 44, 200, 982, 1180, 0, f"""
  {msg("star", "근데 지난주 코스피는 어땠어?", 110, .1, "r", "normal")}
  <div class="abs a-rise" style="left:{P}px;top:250px;--d:.35s;width:{IW}px;height:280px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;text-align:center;padding-top:24px">
    <div style="font-size:44px">지난주 코스피 (11/9~13)</div>
    <div style="font-size:150px;line-height:1.1;color:{RED}"><span class="thump" style="--d:.7s">▲4.56%</span></div></div>
  {msg("owl", "이번 주엔 큰 시험이 두 개!", 570, 1.1, mood="happy")}
  <div class="abs a-pop" style="left:{COL2[0][0]}px;top:720px;width:{COL2[0][1]}px;height:230px;box-sizing:border-box;--d:1.4s;background:#E3EEFF;border:5px solid {L};border-radius:26px;text-align:center;padding-top:18px">
    <div style="font-size:36px;color:#6B5A50">18일(수) 아침</div><div style="font-size:64px">엔비디아</div><div style="font-size:32px">젠슨 황 없는 첫 실적</div></div>
  <div class="abs a-pop" style="left:{COL2[1][0]}px;top:720px;width:{COL2[1][1]}px;height:230px;box-sizing:border-box;--d:1.7s;background:#FFE3E3;border:5px solid {L};border-radius:26px;text-align:center;padding-top:18px">
    <div style="font-size:36px;color:#6B5A50">19일 · 중국 선전</div><div style="font-size:64px">미·중·러</div><div style="font-size:32px">핵 감축·이란 논의 예정</div></div>
""")}
''', "#4A3E78"))

# 5 ── 공지: 오늘 시나리오 3
checks = [("유가 다시 오를까", "오르면 지난주 반등을 도운 유가 하락 효과가 약해질 가능성"),
          ("엔비디아 앞 눈치 보기", "18일 실적 전까지 반도체가 방향을 못 잡을 가능성"),
          ("앤트로픽 공모 수급", "공모 자금 마련에 주식을 팔면 수급 부담 가능성")]
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
  <div class="abs" style="left:0;right:0;top:140px;text-align:center;font-size:84px"><span class="p2" style="--d:.1s">중동 긴장 속, <span style="color:#E8590C">반등?</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point"), 680, 805, 220, 2.0, "a-sr", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 파이낸셜뉴스, 아시아경제, 머니투데이</div>
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
  {daycard("수요일 아침", "18", "엔비디아<br>실적", COL3[0], .15, True)}
  {daycard("목요일 새벽", "19", "FOMC<br>의사록", COL3[1], .3)}
  {daycard("19일(현지)", "19", "앤트로픽<br>상장", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("owl", "happy", "wave"), 660, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 톡할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 이투데이, 파이낸셜뉴스, 서울경제, 아주경제, 뉴스1, 로이터, 머니투데이, 아시아경제, 한국경제, SBS, 연합뉴스, 엔비디아 공시<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.4, 1.5), 3: (4.4, 1.5), 4: (4.2, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "msg", .9), (1, .05, "thud", .8), (1, .3, "whoosh", .5), (1, .35, "thud", .9), (1, .5, "pop", .7), (1, .7, "tension", .5), (1, .9, "question", .6),
 (2, .05, "whoosh", .5), (2, .1, "msg", .7), (2, .35, "pop", .6), (2, .7, "ding", .6), (2, 1.0, "thud", .9), (2, 1.4, "msg", .6), (2, 2.0, "msg", .6), (2, 2.1, "hmm", .4),
 (3, .05, "whoosh", .5), (3, .1, "thud", .7), (3, .5, "boing", .6), (3, .8, "pop", .6), (3, 1.1, "pop", .6), (3, 1.6, "boing", .6), (3, 1.8, "ding", .7),
 (4, .05, "whoosh", .5), (4, .1, "msg", .7), (4, .35, "pop", .6), (4, .7, "ding", .6), (4, 1.1, "msg", .6), (4, 1.4, "pop", .6), (4, 1.7, "pop", .6),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "msg", .7), (6, .9, "jingle", .9),
]
