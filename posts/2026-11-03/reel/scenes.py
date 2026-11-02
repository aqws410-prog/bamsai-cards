"""형식: 밤사이 탐정 추리 v5 (검수 전 · 2026-11-03) — 장면 1을 '취조실(흔들리는 전등 + 책상 건너 용의자 칩)' 구도로 새로 짠 버전.
내용: 2026-11-03 (2일 뉴욕 — 유가 7%대 급락에도 나스닥 ▼1.07%, 필라델피아 반도체 ▼3.37%). 비유: 시소(유가 하락으로 한쪽은 가벼워졌지만 반도체 걱정 돌이 더 무거웠다).
흐름: 1 결론 먼저(나스닥 ▼1.07% + '범인은 반도체 걱정', 취조실) → 2 수상한 점(유가 ▼7.63%·다우 ▲0.41%인데 나스닥은 ▼) → 3 단서·주범(시소 비유, 반도체 ▼3.37%·인텔 ▼8.80%)
     → 4 한국 현장 조사(2일 코스피 ▲2.24%·하이닉스·삼성) → 5 수사 메모판(오늘 체크 3) → 6 다음 사건 예고(선거 첫 소식).
숫자는 2026-11-03 카드·sources.md에 있는 것만 쓴다. 주범은 출처들이 공통으로 꼽은 원인(AI 투자 부담에 따른 반도체·기술주 약세)만, 다른 요인을 '무죄'로 단정하지 않는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes swing{0%,100%{transform:rotate(-7deg)}50%{transform:rotate(7deg)}}
@keyframes flash{0%{opacity:0}20%{opacity:.85}100%{opacity:0}}
@keyframes tiltR{from{transform:rotate(0)}to{transform:rotate(10deg)}}
@keyframes sweat{0%{opacity:0;transform:translateY(0)}30%{opacity:1}100%{opacity:0;transform:translateY(40px)}}
.lamp{transform-origin:50% 0;animation:swing 1.3s ease-in-out infinite}
.flash{animation:flash .35s ease-out both;animation-delay:var(--d,0s)}
.tilt{transform-origin:50% 50%;animation:tiltR .7s cubic-bezier(.3,1.4,.5,1) both;animation-delay:var(--d,0s)}
.sweat{animation:sweat .9s ease-in infinite;animation-delay:var(--d,0s)}
</style>"""

def lamp(x, h):
    """천장에서 흔들리는 취조실 전등 + 빛 원뿔."""
    return (f'<div class="abs lamp" style="left:{x - 240}px;top:0;width:480px;height:{h}px">'
            f'<div class="abs" style="left:237px;top:0;width:6px;height:120px;background:{L}"></div>'
            f'<div class="abs" style="left:170px;top:116px;width:140px;height:64px;background:#4A4F5E;border:5px solid {L};border-radius:70px 70px 8px 8px"></div>'
            f'<div class="abs" style="left:0;top:180px;width:0;height:0;border-left:240px solid transparent;border-right:240px solid transparent;border-bottom:{h - 180}px solid rgba(255,236,170,.22)"></div></div>')

# 1 ── 결론 먼저 (취조실): 0초에 숫자·결론·탐정(클로즈업, 놀람)·용의자·전등이 모두 보인다
#      0~1초: 숫자 펀치(0) → 카메라 플래시(.05) → 전등 흔들(상시) → '주범 지목!' 도장 쾅(.35) → 용의자 칩 땀(.5~) → 탐정 떨림(.6) → '딱 걸렸어!' 효과 글자(.75)
S[1] = (1, page(FX + f'''
{stars(14, 33, 0, 240)}
{head("밤사이 탐정 · 11.3 TUE", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:200px;text-align:center;font-size:46px;color:#C9D6FF">기름값 7% 급락했는데 · 나스닥</div>
<div class="abs" style="left:0;width:1080px;top:258px;text-align:center"><span class="punch" style="--d:0s;font-size:244px;line-height:1;color:#7DB0FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼1.07%</span></div>
<div class="abs" style="left:0;width:1080px;top:510px;text-align:center;font-size:88px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">범인은 <span style="color:#FFE36E">반도체 걱정!</span></div>
<div class="panel" style="left:44px;top:670px;width:982px;height:750px;background:#2B2F3E">
  <div class="abs" style="left:0;right:0;top:0;bottom:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.035) 0 60px,transparent 60px 120px)"></div>
  {lamp(640, 560)}
  <div class="abs" style="left:560px;top:250px;width:250px"><div class="shiver" style="animation-delay:.5s">{chip("#9AA7C7")}</div></div>
  <div class="abs" style="left:582px;top:228px;background:#fff;border:4px solid {L};border-radius:10px;font-size:32px;padding:0 14px">용의자: 반도체</div>
  <div class="abs sweat" style="left:800px;top:300px;font-size:46px;--d:.5s">💧</div>
  <div class="abs" style="left:300px;top:540px;width:640px;height:40px;background:#8A5A3B;border:5px solid {L};border-radius:10px"></div>
  <div class="abs" style="left:20px;top:170px;width:450px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.6s">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
  {sfx("딱 걸렸어!", 470, 70, 84, .75, -6, "#FFE36E")}
  <div class="abs flash" style="left:0;right:0;top:0;bottom:0;background:#fff;--d:.05s"></div>
</div>
<div class="stamp a-stamp" style="left:330px;top:1330px;--d:.35s;--r:-7deg;font-size:62px;white-space:nowrap">주범 지목!</div>
''', "#262B55"))

# 2 ── 수상한 점: 호재(유가 급락·다우 상승)가 있었는데 나스닥은 내렸다
S[2] = (1, page(FX + f'''
{head("수상한 점", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cbub("미·이란 <b>협상 기대</b>에<br>기름값이 확 내렸어요", 40, .1, "t-down", style="font-size:46px")}
  {numbox("브렌트유", "▼7.63%", COL2[0], 270, .4, BLUE)}
  {numbox("다우", "▲0.41%", COL2[1], 270, .6, RED)}
  <div class="abs a-pop" style="left:{P}px;top:470px;width:{IW}px;--d:1.0s;text-align:center;font-size:52px;color:#FFF6EA">그런데…</div>
  <div class="abs a-pop" style="left:{P}px;top:540px;width:{IW}px;--d:1.2s;text-align:center">
    <div style="font-size:42px;color:#DDE3FF">나스닥</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:1.3s;color:#7DB0FF;-webkit-text-stroke:6px {L};paint-order:stroke fill">▼1.07%</span></div></div>
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 860, 260, 1.7, "a-sl", "squish")}
  {bub("호재가 있었는데<br><b>왜 내렸지?</b>", 340, 930, 1.9, "t-left", style="font-size:46px")}
</div>
''', "#2B3060"))

# 3 ── 단서·주범 (비유: 시소) — 유가 하락으로 가벼워진 쪽 vs 반도체 걱정 돌
SEESAW = (f'<div class="abs" style="left:{P}px;top:300px;width:{IW}px;height:330px">'
          f'<div class="abs" style="left:401px;top:200px;width:0;height:0;border-left:50px solid transparent;border-right:50px solid transparent;border-bottom:110px solid #8A5A3B"></div>'
          f'<div class="abs tilt" style="left:30px;top:180px;width:842px;--d:.9s">'
          f'<div style="height:24px;background:#C98B4A;border:5px solid {L};border-radius:12px"></div>'
          f'<div class="abs" style="left:10px;top:-120px;width:230px;height:110px;box-sizing:border-box;background:#E6F6FF;border:5px solid {L};border-radius:20px;text-align:center;font-size:34px;line-height:1.2;padding-top:12px">유가 하락<br><span style="font-size:28px">짐이 가벼워짐</span></div>'
          f'<div class="abs" style="right:10px;top:-150px;width:260px;height:140px;box-sizing:border-box;background:#7A7F8F;color:#fff;border:5px solid {L};border-radius:50px 60px 30px 40px;text-align:center;font-size:36px;line-height:1.2;padding-top:22px">반도체<br>걱정</div>'
          f'</div></div>')
S[3] = (1, page(FX + f'''
{head("단서 분석", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("시장을 <b>시소</b>라고 생각해 봐요.<br>어느 쪽이 더 무거웠을까?", 26, .1, "t-down", style="font-size:44px")}
  {SEESAW}
  <div class="abs a-pop" style="left:{P}px;top:640px;width:{IW}px;--d:1.4s;text-align:center;font-size:42px">반도체 쪽이 <b style="color:#E8590C;font-weight:400">쿵</b> 내려앉았어요</div>
  {nar("AI 투자 부담 걱정이 이어지며<br>반도체주가 <b>또 밀렸어요</b>", P, 720, 1.9, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {stamp("주범: 반도체 걱정", 230, 870, 2.4, -6)}
  {numbox("필라델피아 반도체", "▼3.37%", COL2[0], 980, 2.8, BLUE)}
  {numbox("인텔", "▼8.80%", COL2[1], 980, 3.0, BLUE)}
</div>
''', "#30366E"))

# 4 ── 한국 현장 조사 (2일 서울: 인텔 쇼크 딛고 반등)
def bar(label, val, h, col, d, color):
    x, w = col
    return (f'<div class="abs" style="left:{x}px;top:310px;width:{w}px;height:300px">'
            f'<div class="abs a-rise" style="left:{w//2 - 55}px;bottom:0;width:110px;height:{h}px;background:{color};border:5px solid {L};border-radius:14px 14px 0 0;--d:{d}s"></div></div>'
            f'<div class="abs a-pop" style="left:{x}px;top:630px;width:{w}px;text-align:center;--d:{d + .2:.1f}s"><div style="font-size:36px">{label}</div><div style="font-size:56px;color:{color}">{val}</div></div>')
S[4] = (1, page(FX + f'''
{head("한국 현장 조사", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {cbub("어제(2일) 서울은 인텔 쇼크 딛고<br><b>3거래일 만에 반등</b>했어요", 34, .15, "t-down", style="font-size:42px")}
  <div class="abs" style="left:{P}px;top:610px;width:{IW}px;height:5px;background:{L}"></div>
  {bar("코스피", "▲2.24%", 170, COL3[0], .5, RED)}
  {bar("삼성전자", "▲1.78%", 130, COL3[1], .7, RED)}
  {bar("SK하이닉스", "▲3.81%", 250, COL3[2], .9, RED)}
  {ch(mascot("star", "worried", "up"), P, 830, 240, 1.5, "a-sl", "squish")}
  {bub("그런데 밤사이 미국<br>반도체가 또 밀렸잖아요?", 300, 850, 1.7, "t-left", style="font-size:40px")}
  {nar("오늘은 반등을 <b>이어갈 수 있을지</b>가 관건", P, 1080, 2.4, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
''', "#4A3E78"))

# 5 ── 수사 메모판 (오늘 체크 3)
def memo(n, title, sub, x, y, d, rot):
    return (f'<div class="abs a-drop" style="left:{x}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="transform:rotate({rot}deg);background:#FFF7C9;border:5px solid {L};border-radius:14px;padding:20px 28px 20px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:{RED};border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:48px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 메모판 · 오늘 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#C99A64;--d:0s">
  <div class="abs" style="left:{P}px;top:36px;font-size:58px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill">오늘 한국장, 볼 것은 셋</div>
  {memo(1, "반도체, 반등 이어갈까", "미국 반도체 약세가 이어지면 부담 가능성", P, 150, .5, -1.5)}
  {memo(2, "유가 급락, 누가 웃을까", "더 내리면 항공·화학 업종에 숨통 가능성", P, 360, .95, 1.2)}
  {memo(3, "물가 발표·선거 눈치", "관망하면 지수가 좁게 움직일 가능성", P, 570, 1.4, -1)}
  {ch(mascot("bamtol", "normal", "point"), 640, 790, 240, 2.0, "a-sr", "squish")}
  {bub("메모 셋,<br><b>꼭 챙겨요!</b>", 300, 830, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: AP, 뉴스핌, 이투데이, 서울신문, 뉴스1</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 사건 파일</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">오늘 밤 미국 중간선거<br>· AMD 실적</div>
  <div class="abs a-rise" style="left:44px;top:320px;--d:.3s;font-size:44px">선거 첫 소식, 내일 아침 <span style="color:#FFC08A">8시</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("사건 종결!<br><b>밤사이 탐정</b>이었습니다", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, AP, 이투데이, 서울신문, 파이낸셜뉴스, 한국일보, 뉴스1 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.6, 1.5), 3: (4.4, 1.5), 4: (3.8, 1.5), 5: (3.6, 1.5), 6: (3.4, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .6), (1, .05, "shutter", .9), (1, .1, "blip_down", .6), (1, .35, "thud", 1), (1, .5, "pant", .4), (1, .6, "hmm", .5), (1, .75, "reveal", .7),
 (2, .05, "whoosh", .5), (2, .1, "pop", .8), (2, .4, "blip_down", .6), (2, .6, "sparkle", .5), (2, 1.0, "tick", .7), (2, 1.2, "dundun", .6), (2, 1.3, "blip_down", .7), (2, 1.7, "whoosh", .5), (2, 1.9, "question", .7),
 (3, .1, "pop", .8), (3, .9, "thud", .9), (3, 1.0, "boing", .5), (3, 1.4, "tick", .6), (3, 1.9, "hmm", .6), (3, 2.4, "thud", 1), (3, 2.4, "reveal", .8), (3, 2.8, "blip_down", .7), (3, 3.0, "blip_down", .6),
 (4, .05, "whoosh", .5), (4, .15, "pop", .8), (4, .5, "sparkle", .5), (4, .7, "sparkle", .5), (4, .9, "yay", .5), (4, 1.5, "whoosh", .5), (4, 1.7, "question", .7), (4, 2.4, "tick", .8),
 (5, .05, "whoosh", .5), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
