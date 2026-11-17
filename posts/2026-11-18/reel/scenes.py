"""2026-11-18 릴스 · 택배 추적(delivery) v3 — 장면 1 '공항 화물 터미널 출발 전광판(플립 보드) + 이륙하는 화물기' 새 구도 (검수 전).
그날 상황: 엔비디아(젠슨 황 사임 후 첫 실적) 매출·전망 모두 예상 상회 → 하루 먼저 서울은 코스피 ▼2.59%(5,000선 아래).
          미국발 호재가 오늘 한국장으로 번질지가 핵심 → '해외 소식이 한국으로 번지는 날' 1순위 delivery
          (앞 칸: 큰 지표·급변 아님(3대 지수 ▼0.7~1.6%), 원인 찾기·원인 여럿·이슈 나란히·개념·발언 칸도 아님. 최근 3일 11-15 weather·11-16 chat·11-17 news 미사용, delivery 마지막 11-04).
흐름: 1 결론(1,158억$ '엔비디아 실적, 예상 넘었다', 출발 전광판) → 2 발송지 뉴욕(상자 속 내용물: 매출·데이터센터)
      → 3 다음 분기 예약 물량(1,300억$, 중국행 상자는 빼고도 예상 위) → 4 서울 도착 전 상황(어제 코스피 ▼2.59%, 시간외 2%대 ▲)
      → 5 받는 사람 체크 3 → 6 배송 일정(FOMC 의사록·앤트로픽 상장·미중러 회담).
숫자·사실은 posts/2026-11-18 카드·sources.md에 있는 것만 쓴다. 황 사임 배경은 쓰지 않는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes flip{0%{transform:rotateX(55deg)}60%{transform:rotateX(-12deg)}100%{transform:rotateX(0)}}
@keyframes takeoff{0%{transform:translate(0,0) rotate(-4deg)}100%{transform:translate(260px,-120px) rotate(-14deg)}}
@keyframes blinkr{0%,49%{opacity:1}50%,100%{opacity:.25}}
@keyframes runway{to{background-position:-160px 0}}
@keyframes cross{from{width:0}to{width:100%}}
.flip{display:inline-block;transform-origin:50% 50%;animation:flip .32s ease-out both;animation-delay:var(--d,0s)}
.takeoff{animation:takeoff 1.4s cubic-bezier(.4,0,.6,1) both;animation-delay:var(--d,0s)}
.blinkr{animation:blinkr .6s steps(1) infinite}
.runway{background:repeating-linear-gradient(90deg,#F6EEE4 0 70px,transparent 70px 160px);animation:runway .3s linear infinite}
.xline{position:absolute;left:0;top:50%;height:10px;background:#E03131;border-radius:5px;animation:cross .4s ease-out both;animation-delay:var(--d,0s)}
</style>"""

CAP = (f'<path d="M92 118 Q96 70 150 68 Q204 70 208 118 Z" fill="#2F6BD8" stroke="{L}" stroke-width="3.6" stroke-linejoin="round"/>'
       f'<path d="M150 118 Q200 112 236 126 Q212 136 150 128 Z" fill="#2457B8" stroke="{L}" stroke-width="3.6" stroke-linejoin="round"/>'
       f'<rect x="132" y="84" width="36" height="22" rx="6" fill="#FFD84D" stroke="{L}" stroke-width="3"/>')

def box(w=200, label="AI 칩", tape="#FFF2C4"):
    return (f'<svg viewBox="0 0 200 170" width="{w}" height="{w*0.85:.0f}"><path d="M20 50 L100 20 L180 50 L100 80 Z" fill="#E7B47E" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M20 50 L20 135 L100 162 L100 80 Z" fill="#C98E55" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M180 50 L180 135 L100 162 L100 80 Z" fill="#D9A06A" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M60 35 L140 65" stroke="{tape}" stroke-width="12"/>'
            f'<rect x="112" y="98" width="56" height="34" rx="4" fill="#fff" stroke="{L}" stroke-width="3" transform="skewY(-18)"/>'
            f'<text x="140" y="164" text-anchor="middle" font-size="18" font-family="Jua" fill="{L}" transform="skewY(-18)">{label}</text></svg>')

PLANE = (f'<svg viewBox="0 0 300 140" width="300" height="140">'
         f'<path d="M20 78 Q30 58 70 58 L230 58 Q282 60 290 78 Q282 96 230 98 L70 98 Q30 98 20 78 Z" fill="#F6EEE4" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
         f'<path d="M120 62 L170 8 L196 8 L176 62 Z" fill="#FFB27F" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
         f'<path d="M130 94 L176 134 L200 134 L182 94 Z" fill="#FFB27F" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
         f'<path d="M30 62 L14 24 L40 24 L62 60 Z" fill="#5AA9FF" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
         + "".join(f'<circle cx="{x}" cy="76" r="7" fill="#5AA9FF" stroke="{L}" stroke-width="3"/>' for x in (200, 222, 244))
         + '</svg>')

def frow(cells, top, d, hi=False):
    """출발 전광판 한 줄 — 칸마다 플립 글자."""
    bg = "#2A2F3E" if not hi else "#3A3220"
    out = f'<div class="abs" style="left:{P}px;top:{top}px;width:{IW}px;height:84px;background:{bg};border:4px solid {L};border-radius:12px;display:flex;align-items:center;gap:14px;padding:0 18px;box-sizing:border-box">'
    for i, (txt, w, col) in enumerate(cells):
        out += f'<div style="width:{w}px;font-size:40px;color:{col};white-space:nowrap;overflow:hidden"><span class="flip" style="--d:{d + i*.06:.2f}s">{txt}</span></div>'
    return out + '</div>'

# 1 ── 결론 먼저 (공항 화물 터미널): 0초에 숫자·결론·전광판·화물기·밤톨이(클로즈업, 놀람)가 모두 보인다
#      0~1초: 숫자 펀치(0) + 삑 → 전광판 글자 플립(0~.4) → '출발' 도장 쾅(.35) → 화물기 이륙(.2~1.6) → '슝~!'(.7) → 밤톨이 떨림
S[1] = (1, page(FX + f'''
{stars(14, 53, 0, 180)}
{head("밤사이 택배 · 11.18 WED", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:190px;text-align:center;font-size:44px;color:#C9D6FF">황 없는 첫 실적 · 엔비디아 3분기 매출</div>
<div class="abs" style="left:0;width:1080px;top:248px;text-align:center"><span class="punch" style="--d:0s;font-size:214px;line-height:1;color:#FFE36E;-webkit-text-stroke:10px {L};paint-order:stroke fill">1,158억$</span></div>
<div class="abs" style="left:0;width:1080px;top:494px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">엔비디아 실적, <span style="color:#FF8A8F">예상 넘었다</span></div>
<div class="panel" style="left:44px;top:640px;width:982px;height:760px;background:#1E2238">
  <div class="abs" style="left:{P}px;top:24px;font-size:38px;color:#FFE36E">✈ DEPARTURES · 화물 출발 <span class="blinkr" style="color:#FF8A8F">●</span></div>
  {frow([("뉴욕", 120, "#fff"), ("→ 서울", 170, "#fff"), ("엔비디아 실적", 330, "#FFE36E"), ("출발", 120, "#7CE38B")], 90, 0, True)}
  {frow([("시간외", 150, "#C9D6FF"), ("엔비디아 주가", 330, "#C9D6FF"), ("2%대 ▲", 220, "#FF8A8F")], 186, .15)}
  <div class="abs" style="left:0;right:0;bottom:0;height:210px;background:#2A2F4A;border-top:5px solid {L}"></div>
  <div class="abs runway" style="left:0;right:0;bottom:96px;height:16px"></div>
  <div class="abs takeoff" style="left:430px;top:390px;--d:.2s"><div style="position:relative">{PLANE}<div class="abs" style="left:58px;top:-34px">{box(110, "실적")}</div></div></div>
  <div class="abs" style="left:-40px;top:290px;width:440px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.6s">{mascot("bamtol", "surprised", "up", CAP)}</div></div>
  {sfx("슝~!", 700, 300, 92, .7, -8, "#FFE36E")}
</div>
{sfx("삑!", 820, 600, 88, .0, 10, "#FFE36E")}
<div class="stamp a-stamp" style="left:500px;top:1190px;--d:.35s;--r:-8deg;font-size:66px;white-space:nowrap">서울행 출발</div>
''', "#262B55"))

# 2 ── 발송지 뉴욕: 상자 속 내용물
S[2] = (1, page(FX + f'''
{head("발송지 · 뉴욕", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:0;right:0;top:0;height:88px;background:#FFB27F;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">📦 송장 · 보낸 곳 엔비디아</div>
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 120, 250, .1, "a-pop", "squish")}
  {bub("황 없이 처음 보낸 상자,<br>열어 보니 <b>꽉 찼어요!</b>", 320, 150, .25, "t-left", style="font-size:44px")}
  <div class="abs a-pop" style="left:{P}px;top:440px;width:{IW}px;--d:.6s;text-align:center">
    <div style="font-size:42px;color:#6B5A50">3분기 매출 · 시장 예상 약 1,091억$</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.8s;color:{L}">1,158억$</span></div></div>
  {numbox("데이터센터 매출", "1,076억$", COL2[0], 700, 1.2, L)}
  {numbox("1년 전보다", "▲110%", COL2[1], 700, 1.4, RED)}
  {cbub("AI 데이터센터용 칩이<br><b>1년 새 두 배 넘게</b> 팔렸어요", 920, 1.8, "t-up", style="font-size:42px")}
</div>
''', "#2B3060"))

# 3 ── 다음 분기 예약 물량: 중국행 상자는 빼고도 예상 위
S[3] = (1, page(FX + f'''
{head("다음 분기 예약 물량", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {ch(mascot("moon", "happy", "point"), P, 40, 250, .1, "a-sl", "squish")}
  {lower_third("달떡이 센터장", "엔비디아 역할", 320, 50, .2)}
  {bub("다음 분기 <b>예약 물량</b>도<br>예상보다 많아요", 320, 150, .4, "t-left", style="font-size:44px")}
  <div class="abs a-pop" style="left:{P}px;top:400px;width:{IW}px;--d:.8s;text-align:center">
    <div style="font-size:42px;color:#6B5A50">4분기 매출 전망 · 시장 예상 약 1,253억$</div>
    <div style="font-size:150px;line-height:1.05"><span class="punch" style="--d:1.0s;color:{RED};-webkit-text-stroke:5px {L};paint-order:stroke fill">1,300억$</span></div></div>
  <div class="abs a-pop" style="left:{COL2[0][0]}px;top:700px;width:{COL2[0][1]}px;height:260px;box-sizing:border-box;--d:1.5s;background:#fff;border:4px solid {L};border-radius:26px;text-align:center;padding-top:10px">
    {box(150, "예약")}<div style="font-size:40px">예약 확정 상자</div></div>
  <div class="abs a-pop" style="left:{COL2[1][0]}px;top:700px;width:{COL2[1][1]}px;height:260px;box-sizing:border-box;--d:1.8s;background:#EEE;border:4px dashed {L};border-radius:26px;text-align:center;padding-top:10px">
    <div style="position:relative;display:inline-block"><div style="opacity:.55">{box(150, "중국행")}</div><div class="xline" style="--d:2.1s;top:45%;transform:rotate(-20deg)"></div></div><div style="font-size:40px">아예 뺐어요</div></div>
  {nar("중국 데이터센터 매출을 <b>빼고도</b> 예상보다 높게 잡았다", P, 1010, 2.5, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
''', "#30366E"))

# 4 ── 서울 도착 전 상황: 어제 코스피, 시간외 반응
S[4] = (1, page(FX + f'''
{head("도착지 · 서울", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:0;height:88px;background:#7CE38B;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">📍 받는 곳 코스피 · 어제(17일) 상황</div>
  <div class="abs" style="left:0;right:0;top:120px;text-align:center"><div style="font-size:42px;color:#3B4A40">코스피 4,968.48</div>
    <div style="font-size:170px;line-height:1.05"><span class="punch" style="--d:.15s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼2.59%</span></div></div>
  <div class="stamp a-stamp" style="left:250px;top:385px;--d:.5s;--r:6deg;font-size:48px;padding:0 18px;white-space:nowrap">9개월 만에 5,000 아래</div>
  {nar("외국인 1조4천억원 넘게 순매도 · 4거래일 연속 하락", P, 500, .9, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("star", "worried", "up"), P, 640, 250, 1.2, "a-sl", "shiver")}
  {bub("힘든 하루였는데<br><b>좋은 택배</b> 오는 중?", 320, 660, 1.4, "t-left", style="font-size:44px")}
  <div class="abs a-pop" style="left:{P}px;top:900px;width:{IW}px;height:200px;box-sizing:border-box;--d:1.9s;background:#fff;border:5px solid {L};border-radius:26px;text-align:center;padding-top:20px">
    <div style="font-size:38px;color:#6B5A50">배송 조회 · 엔비디아 주가</div>
    <div style="font-size:60px">정규장 <span style="color:{BLUE}">▼0.44%</span> → 시간외 <span class="thump" style="--d:2.3s;color:{RED}">2%대 ▲</span></div></div>
</div>
''', "#4A3E78"))

# 5 ── 받는 사람 체크 3
checks = [("반도체, 숨 돌릴까", "시간외 상승이 이어지면 반도체 심리 개선 가능성"),
          ("외국인 매도 멈출까", "매도가 줄면 5,000선 회복 시도 가능성"),
          ("금리 인상 경계", "의사록 인상 신호 강하면 성장주·환율 부담")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{290+i*190}px;width:{IW}px;height:166px;box-sizing:border-box;--d:{.5+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:14px;background:#FFF6EA;border:4px solid {L};font-size:54px;line-height:70px;text-align:center;color:{RED}">✔</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("받는 사람 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:0;right:0;top:0;height:88px;background:#FFB27F;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">📋 수령 체크리스트 · 오늘 한국장</div>
  <div class="abs" style="left:0;right:0;top:130px;text-align:center;font-size:88px"><span class="punch" style="--d:.1s">오늘 장 <span style="color:#E8590C">체크 3</span></span></div>
  {rows}
  {ch(mascot("bamtol", "happy", "point", CAP), P, 850, 180, 2.0, "a-sl", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 엔비디아 실적 발표, 뉴스핌, 파이낸셜뉴스, 로이터, 비즈니스코리아</div>
''', "#FFE1CC"))

# 6 ── 배송 일정 · 마무리
def daycard(day, date, t, col, d, hi=False):
    x, w = col
    bg = "#FFD84D" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:{w}px;height:280px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};'
            f'border-radius:26px;box-shadow:0 6px 0 rgba(0,0,0,.15);text-align:center;padding:14px 8px;color:{L}">'
            f'<div style="font-size:32px;color:#6B5A50">{day}</div><div style="font-size:88px;line-height:1.05">{date}</div>'
            f'<div style="font-size:32px;line-height:1.2;margin-top:6px">{t}</div></div>')
S[6] = (1, page(FX + f'''
{head("배송 일정 · 마무리", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:30px;font-size:42px;color:#FFC08A">다음 택배 도착 예정 · 19일</div>
  {daycard("목 새벽 4시", "19", "FOMC<br>의사록", COL3[0], .15, True)}
  {daycard("미국 현지", "19", "앤트로픽<br>나스닥 상장", COL3[1], .3)}
  {daycard("중국 선전", "19", "미·중·러<br>정상회담", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("bamtol", "happy", "wave", CAP), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("star", "happy", "wave"), 680, 230, 260, .4, "a-sr", "squish")}
  {bub("의사록 결과, 내일 아침<br><b>8시에 배달할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 엔비디아 실적 발표, 뉴스핌, 이투데이, 파이낸셜뉴스, 야후파이낸스, 로이터, AP, 비즈니스코리아<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (4.2, 1.5), 4: (3.8, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "scan", 1), (1, .05, "tick", .6), (1, .2, "whoosh", .8), (1, .35, "thud", 1), (1, .6, "boing", .5), (1, .7, "whoosh", .7),
 (2, .05, "whoosh", .5), (2, .1, "pop", .6), (2, .25, "pop", .8), (2, .6, "reveal", .8), (2, .8, "sparkle", .6), (2, 1.2, "pop", .6), (2, 1.4, "pop", .6), (2, 1.8, "ding", .7),
 (3, .05, "whoosh", .5), (3, .2, "tick", .6), (3, .4, "pop", .8), (3, 1.0, "dundun", .7), (3, 1.5, "pop", .6), (3, 1.8, "pop", .6), (3, 2.1, "wrong", .5), (3, 2.5, "tick", .8),
 (4, .05, "whoosh", .5), (4, .15, "blip_down", 1), (4, .5, "thud", .8), (4, .9, "tick", .7), (4, 1.2, "whoosh", .4), (4, 1.4, "pop", .8), (4, 1.9, "scan", .8), (4, 2.3, "sparkle", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "honk", .5), (6, .9, "jingle", .9),
]
