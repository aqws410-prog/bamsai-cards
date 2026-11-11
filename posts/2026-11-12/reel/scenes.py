"""2026-11-12 릴스 · 탐정 추리(detective) v7 — '결론 먼저' 훅, 장면 1 '감식실 — 대형 돋보기 렌즈 아래 증거 장부 + 지문 가루' 새 구도 (검수 전).
그날 상황: "금리 인상 걱정은 그대로인데 나스닥은 왜 1.60% 올랐을까?" 원인 찾기가 핵심 → 상황표 첫 칸(큰 지표) 해당 없음,
          둘째 칸 1순위 detective(마지막 11-07, 최근 3일 11-09 chat·11-10 news·11-11 talkshow 미사용).
흐름: 1 결론(반도체지수 ▲5.66% 'AI 걱정, 한숨 덜었다!', 감식실 돋보기) → 2 수상한 점(금리 걱정 그대로인데 3대 지수 상승)
      → 3 결정적 단서: 비유 'AI 컴퓨터 PC방(코어위브) — 손님이 예상보다 북적 → 컴퓨터(칩)를 더 사겠지?' + 코어위브 ▲24.71%
      → 4 칩 가게 줄줄이 상승(마이크론·SK하이닉스 ADR·엔비디아) + 서울은 하루 먼저(11일 코스피 ▲2.60%) → 5 수사 노트(체크 3) → 6 다음 사건 예고(어플라이드 머티어리얼즈 실적).
숫자는 posts/2026-11-12 카드·sources.md에 있는 것만 쓴다. '주범'은 출처들이 공통으로 꼽은 이유(코어위브 실적 → AI 투자 걱정 완화)만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes lens{0%{transform:translate(-60px,30px)}100%{transform:translate(0,0)}}
@keyframes dust{0%{opacity:0;transform:scale(.4)}40%{opacity:1}100%{opacity:.85;transform:scale(1)}}
@keyframes glint{0%,100%{opacity:.25}50%{opacity:.9}}
@keyframes blinks{0%,49%{opacity:1}50%,100%{opacity:.35}}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.06)}}
.lens{animation:lens .6s cubic-bezier(.2,.9,.3,1) both}
.dust{animation:dust .5s ease-out both;animation-delay:var(--d,0s)}
.glint{animation:glint 1s ease-in-out infinite}
.blinks{animation:blinks .7s steps(1) infinite}
.pulse{animation:pulse .8s ease-in-out infinite}
</style>"""

def fprint(x, y, s, d, col="#C9B8FF"):
    """지문 자국 (감식 가루)."""
    rings = "".join(f'<ellipse cx="50" cy="56" rx="{8 + i * 7}" ry="{11 + i * 8}" fill="none" stroke="{col}" stroke-width="3.5" stroke-dasharray="{14 + i * 3} 7"/>' for i in range(5))
    return f'<svg class="abs dust" style="left:{x}px;top:{y}px;--d:{d}s" width="{s}" height="{s}" viewBox="0 0 100 110">{rings}</svg>'

def monitor(x, y, w, d, busy=True):
    """PC방 자리 하나 (모니터 + 손님 머리)."""
    h = int(w * .72)
    head = (f'<div class="abs" style="left:{int(w*.22)}px;top:{h + 4}px;width:{int(w*.56)}px;height:{int(w*.5)}px;border-radius:{int(w*.28)}px {int(w*.28)}px 14px 14px;'
            f'background:#5A5196;border:4px solid {L}"></div>') if busy else ""
    return (f'<div class="abs a-pop" style="left:{x}px;top:{y}px;width:{w}px;height:{h + int(w*.5)}px;--d:{d}s">'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;box-sizing:border-box;background:#1D2A4A;border:5px solid {L};border-radius:12px;overflow:hidden">'
            f'<div class="abs glint" style="left:10px;top:10px;right:10px;bottom:10px;background:linear-gradient(135deg,#6FB6FF,#B79CFF)"></div>'
            f'<div class="abs" style="left:0;right:0;top:{int(h*.28)}px;text-align:center;font-size:{int(w*.2)}px;color:#fff">AI</div></div>{head}</div>')

# 1 ── 결론 먼저 (감식실): 0초에 숫자·결론·탐정(클로즈업, 놀람)·돋보기 렌즈 속 증거가 모두 보인다
#      0~1초: 숫자 펀치(0) → 렌즈가 장부 위로 미끄러짐(0~.6) → 지문 가루(.15/.3/.45) → '단서 발견!' 도장 쾅(.4) → 탐정 떨림 + '번쩍!'(.7)
S[1] = (1, page(FX + f'''
{stars(12, 41, 0, 180)}
{head("밤사이 탐정 · 11.12 THU", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">미국 반도체지수 · 11일 뉴욕</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#FF6B6B;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲5.66%</span></div>
<div class="abs" style="left:0;width:1080px;top:504px;text-align:center;font-size:86px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">AI 걱정, <span style="color:#FFE36E">한숨 덜었다!</span></div>
<div class="panel" style="left:44px;top:660px;width:982px;height:760px;background:#22213F">
  <div class="abs" style="left:{P}px;top:30px;background:#FFD84D;border:5px solid {L};border-radius:12px;padding:2px 18px;font-size:36px">🔬 감식실</div>
  <div class="abs" style="left:{P}px;top:110px;width:520px;height:420px;box-sizing:border-box;background:#FFFDF5;border:6px solid {L};border-radius:16px;transform:rotate(-3deg);
       background-image:repeating-linear-gradient(0deg,transparent 0 60px,#ECE6F5 60px 63px)">
    <div class="abs" style="left:26px;top:16px;font-size:40px">📒 코어위브 3분기 장부</div>
    <div class="abs" style="left:26px;top:96px;font-size:38px;color:#6B5A50">매출 · <span style="color:{RED}">예상 웃돎 ✔</span></div>
    <div class="abs" style="left:26px;top:160px;font-size:38px;color:#6B5A50">연간 전망 · <span style="color:{RED}">올림 ✔</span></div>
  </div>
  <div class="abs lens" style="left:90px;top:335px;width:300px;height:300px">
    <div class="abs" style="left:0;top:0;width:240px;height:240px;border-radius:50%;border:14px solid #3A3A48;background:rgba(220,240,255,.35);box-shadow:inset 0 0 0 5px {L}, 0 0 0 5px {L};overflow:hidden">
      <div class="abs" style="left:0;right:0;top:56px;text-align:center;font-size:62px;line-height:1.05;color:{RED};-webkit-text-stroke:3px {L};paint-order:stroke fill">예상<br>웃돎!</div></div>
    <div class="abs" style="left:215px;top:215px;width:36px;height:120px;background:#3A3A48;border:5px solid {L};border-radius:18px;transform:rotate(-45deg);transform-origin:20px 0"></div>
  </div>
  {fprint(560, 90, 110, .15)}{fprint(330, 14, 80, .3)}{fprint(360, 640, 90, .45)}
  <div class="abs" style="left:440px;top:210px;width:470px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
  <div class="abs" style="left:30px;top:610px"><div class="stamp a-stamp" style="position:relative;--d:.4s;--r:-8deg;font-size:64px;white-space:nowrap">단서 발견!</div></div>
  {sfx("번쩍!", 690, 120, 86, .7, 8, "#FFE36E")}
</div>
''', "#262B55"))

# 2 ── 수상한 점: 금리 걱정은 그대로인데 지수는 올랐다
S[2] = (1, page(FX + f'''
{head("사건 개요 · 수상한 점", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cbub("12월 금리 인상 걱정은<br><b>그대로</b>인데…", 36, .1, "t-down", style="font-size:48px")}
  <div class="abs a-pop" style="left:{P}px;top:260px;width:{IW}px;--d:.4s;text-align:center">
    <div style="font-size:40px;color:#E6E9FF">나스닥 (11일 뉴욕)</div>
    <div style="font-size:170px;line-height:1.05"><span class="thump" style="--d:.6s;color:#FF8A8F;-webkit-text-stroke:7px {L};paint-order:stroke fill">▲1.60%</span></div></div>
  {numbox("다우", "▲0.49%", COL2[0], 540, 1.0, RED)}
  {numbox("S&amp;P500", "▲1.31%", COL2[1], 540, 1.15, RED)}
  {ch(mascot("star", "surprised", "up"), P, 760, 270, 1.5, "a-sl", "hop")}
  {bub("걱정은 그대로인데<br><b>왜 올랐지?</b>", 340, 820, 1.7, "t-left", style="font-size:48px")}
</div>
''', "#2B3060"))

# 3 ── 결정적 단서: 'AI 컴퓨터 PC방' 코어위브
S[3] = (1, page(FX + f'''
{head("결정적 단서", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#EEF0FF;--d:0s">
  {cbub("코어위브 = AI 컴퓨터를<br>빌려주는 <b>PC방</b>이에요", 30, .1, "t-down", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:250px;width:{IW}px;height:330px;box-sizing:border-box;--d:.3s;background:#2B2950;border:5px solid {L};border-radius:24px"></div>
  <div class="abs blinks" style="left:{P + 24}px;top:270px;background:#FF6B6B;color:#fff;border:4px solid {L};border-radius:12px;padding:0 16px;font-size:36px">손님 북적!</div>
  {monitor(P + 30, 340, 150, .45)}{monitor(P + 200, 340, 150, .55)}{monitor(P + 370, 340, 150, .65)}
  {ch(mascot("moon", "happy", "point"), 600, 250, 280, .8, "a-sr", "squish")}
  <div class="abs a-fade" style="left:{P}px;top:600px;--d:.9s;font-size:30px;color:#6B5A50">역: 달떡이 = 코어위브 사장님</div>
  <div class="abs a-pop" style="left:{P}px;top:650px;width:{IW}px;--d:1.2s;text-align:center">
    <div style="font-size:40px">손님이 예상보다 많아 <b style="font-weight:400;color:#E8590C">올해 전망도 올림</b></div>
    <div style="font-size:130px;line-height:1.1"><span style="font-size:64px">코어위브 </span><span class="thump" style="--d:1.4s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲24.71%</span></div></div>
  {nar("자리가 북적이면 → 컴퓨터(칩)를 <b>더 사겠지?</b>", P, 900, 2.0, f"font-size:42px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(chip("#9AD3FF", "normal"), 120, 990, 150, 2.4, "a-pop", "hop")}
  {ch(chip("#FFC46B", "normal"), 416, 990, 150, 2.5, "a-pop", "hop")}
  {ch(chip("#C9B8FF", "normal"), 712, 990, 150, 2.6, "a-pop", "hop")}
</div>
''', "#30366E"))

# 4 ── 칩 가게 줄줄이 + 서울은 하루 먼저
S[4] = (1, page(FX + f'''
{head("공범 수사 · 서울 현장", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {cbub("AI 걱정이 덜하자<br><b>칩 가게</b>들이 줄줄이 올랐다!", 30, .1, "t-down", style="font-size:44px")}
  {numbox("마이크론", "▲11.89%", COL3[0], 250, .4, RED)}
  {numbox("SK하이닉스 ADR", "▲9%대", COL3[1], 250, .55, RED)}
  {numbox("엔비디아", "▲2.87%", COL3[2], 250, .7, RED)}
  <div class="abs a-fade" style="left:{P}px;top:458px;width:{IW}px;--d:.9s;text-align:center;font-size:30px;color:#5B5070">ADR = 미국에 상장된 예탁증서 · 엔비디아는 이틀 급락 뒤 반등</div>
  <div class="abs a-pop" style="left:{P}px;top:530px;width:{IW}px;height:600px;box-sizing:border-box;--d:1.3s;background:#fff;border:5px solid {L};border-radius:26px">
    <div class="abs" style="left:0;right:0;top:24px;text-align:center;font-size:40px">🇰🇷 서울은 하루 먼저 (11일 코스피)</div>
    <div class="abs" style="left:0;right:0;top:80px;text-align:center;font-size:150px;line-height:1"><span class="thump" style="--d:1.6s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲2.60%</span></div>
    <div class="abs" style="left:0;right:0;top:250px;text-align:center;font-size:38px;color:#5B5070">5,375.36 · 외국인 6,587억원 순매수</div>
    {ch(mascot("bamtol", "happy", "hold", p_mag()), 30, 330, 230, 1.9, "a-sl", "squish2")}
    {bub("코어위브 소식이<br>서울에 <b>먼저 반영</b>됐어요", 290, 380, 2.1, "t-left", style="font-size:42px")}
  </div>
</div>
''', "#4A3E78"))

# 5 ── 수사 노트 (오늘 한국장 체크 3)
def note(n, title, sub, y, d):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="background:#FFFDF2;border:5px solid {L};border-radius:14px;padding:16px 28px 16px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#F1E6C8 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#E8590C;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:46px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 노트 · 오늘 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#5E6BB8;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:62px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill"><span class="punch" style="--d:.1s">오늘 한국장, 볼 것은 셋</span></div>
  {note(1, "반도체, 미국 급등 이어받을까", "미국 반도체 급등이 국내 반도체 업종엔 우호적일 가능성", 160, .5)}
  {note(2, "외국인, 매수 이어갈까", "12월 미국 금리 인상 전망은 그대로 · 매수 지속엔 변수", 370, .95)}
  {note(3, "환율, 1,330원대 지킬까", "외국인 매수·수출 달러 매도 이어지면 하락 압력 가능성", 580, 1.4)}
  {ch(mascot("bamtol", "normal", "point"), 630, 800, 220, 2.0, "a-sr", "squish")}
  {bub("수사 노트 셋,<br><b>꼭 챙겨요!</b>", 320, 840, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 서울신문, 뉴스1, 뉴스핌, 한국경제, 핀포인트뉴스</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 다음 사건", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 사건 파일 · 오늘 밤 장 마감 후</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:72px;line-height:1.2">반도체 장비 성적표<br>어플라이드 머티어리얼즈</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>에</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 590, 220, 270, .4, "a-sr", "hop")}
  {bub("오늘 수사는 여기까지!<br><b>사건 해결~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 한국경제TV, 서울신문, 뉴스1, 한국경제, 굿모닝경제<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.4, 1.5), 3: (4.8, 1.5), 4: (4.4, 1.5), 5: (4.0, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .5), (1, .05, "whoosh", .6), (1, .15, "sparkle", .5), (1, .4, "thud", 1), (1, .5, "shutter", .6), (1, .7, "ding", .8),
 (2, .1, "pop", .8), (2, .4, "whoosh", .5), (2, .6, "dundun", .5), (2, 1.0, "pop", .7), (2, 1.15, "pop", .7), (2, 1.5, "boing", .5), (2, 1.7, "question", .8),
 (3, .1, "pop", .7), (3, .3, "whoosh", .5), (3, .45, "pop", .5), (3, .55, "pop", .5), (3, .65, "pop", .5), (3, .8, "boing", .5), (3, 1.2, "whoosh", .5), (3, 1.4, "dundun", .6), (3, 2.0, "tick", .8), (3, 2.4, "boing", .5), (3, 2.5, "boing", .5), (3, 2.6, "yay", .6),
 (4, .1, "pop", .8), (4, .4, "pop", .6), (4, .55, "pop", .6), (4, .7, "pop", .6), (4, 1.3, "whoosh", .5), (4, 1.6, "sparkle", .8), (4, 1.9, "boing", .5), (4, 2.1, "pop", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .6), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .6), (6, .9, "jingle", .9),
]
