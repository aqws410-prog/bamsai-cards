"""2026-11-07 릴스 · 탐정 추리(detective) v6 — '결론 먼저' 훅, 장면 1 'CCTV 관제실(모니터 벽 + 판독 화면)' 새 구도 (검수 전).
그날 상황: 미국 10월 일자리 +16.5만(예상 크게 웃돎) → "왜 일자리가 좋은데 금리 인상 걱정?" 원인 찾기가 핵심.
  첫 칸(큰 지표) 1순위 news(11-05)·2순위 talkshow(11-06)가 모두 최근 3일 안 → 다음 칸 '원인 찾기' 1순위 detective(마지막 11-03, 최근 3일 밖).
흐름: 1 결론(+16.5만 '좋아도 너무 좋아 금리 걱정!', CCTV 관제실) → 2 증거 셋(일자리·실업률·임금) → 3 추리: 비유 '에어컨'(경제가 뜨거우면 연준이 금리 인상이라는 에어컨을 켤 수도)
      → 4 반전 단서(반도체 ▲4.21% 반등, 나스닥 ▲1.09%, 다우 ▼0.46%) + 서울 현장(6일 코스피 ▼6.02%) → 5 수사 노트(월요일 체크 3) → 6 다음 사건 예고(11/10 CPI, 내일 성적표).
숫자는 posts/2026-11-07 카드·sources.md에 있는 것만 쓴다. '주범'은 출처들이 공통으로 꼽은 이유(강한 고용 → 12월 금리 인상 전망)만, 확률 숫자는 쓰지 않는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes scanl{from{transform:translateY(-20px)}to{transform:translateY(300px)}}
@keyframes flick{0%{opacity:0}30%{opacity:1}45%{opacity:.3}60%,100%{opacity:1}}
@keyframes blinkr{0%,49%{opacity:1}50%,100%{opacity:.2}}
@keyframes fan{0%{opacity:0;transform:translateY(-10px)}30%{opacity:1}100%{opacity:0;transform:translateY(90px)}}
@keyframes shake2{0%,100%{transform:rotate(0)}25%{transform:rotate(-3deg)}75%{transform:rotate(3deg)}}
.scan{animation:scanl 1.2s linear infinite}
.flick{animation:flick .45s steps(4) both;animation-delay:var(--d,0s)}
.rec{animation:blinkr .8s steps(1) infinite}
.wind{animation:fan 1.1s ease-in infinite;animation-delay:var(--d,0s)}
.brr{animation:shake2 .3s ease-in-out infinite}
</style>"""

def mon(inner, x, y, w, h, d, label):
    """관제실 모니터 한 대 (켜질 때 깜빡)."""
    return (f'<div class="abs flick" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;--d:{d}s;box-sizing:border-box;background:#0E2A2A;border:6px solid {L};border-radius:16px;overflow:hidden">'
            f'<div class="abs" style="left:0;right:0;top:0;bottom:0;background:repeating-linear-gradient(0deg,rgba(120,255,200,.06) 0 4px,transparent 4px 8px)"></div>'
            f'<div class="abs" style="left:12px;top:6px;font-size:24px;color:#8FE3C0">{label}</div>'
            f'<div class="abs rec" style="right:12px;top:8px;font-size:22px;color:#FF6B6B">● REC</div>'
            f'<div class="abs" style="left:0;right:0;top:40px;text-align:center">{inner}</div></div>')

def aircon(x, y, w, d=0, on=True):
    """벽걸이 에어컨 + 찬 바람."""
    wind = "".join(f'<div class="abs wind" style="left:{int(w*f)}px;top:{int(w*.30)}px;font-size:44px;color:#BFE6FF;--d:{d + i*.25}s">≋</div>'
                   for i, f in enumerate((.18, .44, .70))) if on else ""
    return (f'<div class="abs a-pop" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s">'
            f'<div style="height:{int(w*.30)}px;background:#F4F7FB;border:5px solid {L};border-radius:22px;position:relative">'
            f'<div class="abs" style="left:24px;right:24px;bottom:16px;height:10px;background:#C9D3E3;border-radius:5px"></div>'
            f'<div class="abs" style="right:20px;top:14px;width:16px;height:16px;border-radius:8px;background:#38D39F"></div></div>{wind}</div>')

def remote(x, y, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:{y}px;--d:{d}s;width:90px;height:170px;background:#E8ECF4;border:5px solid {L};border-radius:22px">'
            f'<div class="abs" style="left:24px;top:18px;width:32px;height:32px;border-radius:16px;background:#E03131;border:4px solid {L}"></div>'
            f'<div class="abs" style="left:14px;top:72px;font-size:24px;line-height:1.1;text-align:center;width:52px">금리<br>▲</div></div>')

# 1 ── 결론 먼저 (CCTV 관제실): 0초에 숫자·결론·탐정(클로즈업, 놀람)·모니터 벽이 모두 보인다
#      0~1초: 숫자 펀치(0) → 모니터 깜빡 켜짐(.1/.25/.4) → '단서 포착!' 도장 쾅(.35) → 판독 화면 스캔선(상시) → 탐정 떨림(.5~) → '삐빅!' 효과 글자(.7)
S[1] = (1, page(FX + f'''
{stars(12, 77, 0, 180)}
{head("밤사이 탐정 · 11.7 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">미국 10월 일자리 · 예상 크게 웃돌아</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#FF6B6B;-webkit-text-stroke:10px {L};paint-order:stroke fill">+16.5만</span></div>
<div class="abs" style="left:0;width:1080px;top:504px;text-align:center;font-size:86px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">좋아도 너무 좋아 <span style="color:#FFE36E">금리 걱정!</span></div>
<div class="panel" style="left:44px;top:660px;width:982px;height:760px;background:#1B2233">
  {mon('<div style="font-size:30px;color:#CFEFE2">실업률</div><div style="font-size:64px;color:#fff">4.1%</div>', COL3[0][0], 26, COL3[0][1], 170, .1, "CAM 1")}
  {mon('<div style="font-size:30px;color:#CFEFE2">시간당 임금</div><div style="font-size:64px;color:#FF8A8F">▲0.4%</div>', COL3[1][0], 26, COL3[1][1], 170, .25, "CAM 2")}
  {mon('<div style="font-size:30px;color:#CFEFE2">미국 반도체</div><div style="font-size:64px;color:#FF8A8F">▲4.21%</div>', COL3[2][0], 26, COL3[2][1], 170, .4, "CAM 3")}
  <div class="abs" style="left:470px;top:220px;width:472px;height:270px;box-sizing:border-box;background:#0B1A2E;border:6px solid {L};border-radius:20px;overflow:hidden">
    <div class="abs" style="left:16px;top:10px;font-size:26px;color:#9FC3FF">🔍 판독 중</div>
    <div class="abs" style="left:0;right:0;top:70px;text-align:center;font-size:40px;color:#C9D6FF">수상한 그림자</div>
    <div class="abs" style="left:0;right:0;top:112px;text-align:center;font-size:66px;color:#FFE36E;line-height:1.15">12월<br>금리 인상?</div>
    <div class="abs scan" style="left:0;right:0;top:0;height:8px;background:rgba(140,255,200,.55)"></div></div>
  <div class="abs" style="left:-10px;top:230px;width:470px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
  {sfx("삐빅!", 250, 196, 84, .7, 8, "#8FE3C0")}
  <div class="abs" style="left:500px;top:590px"><div class="stamp a-stamp" style="position:relative;--d:.35s;--r:-7deg;font-size:64px;white-space:nowrap">단서 포착!</div></div>
</div>
''', "#262B55"))

# 2 ── 증거 셋: 어젯밤 발표된 일자리 성적표
S[2] = (1, page(FX + f'''
{head("증거 수집", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cbub("어젯밤 발표된<br><b>미국 일자리 성적표</b>", 36, .1, "t-down", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:250px;width:{IW}px;--d:.4s;text-align:center">
    <div style="font-size:38px;color:#E6E9FF">증거 1 · 10월 일자리</div>
    <div style="font-size:170px;line-height:1.05"><span class="thump" style="--d:.6s;color:#FF8A8F;-webkit-text-stroke:7px {L};paint-order:stroke fill">+16.5만</span></div></div>
  {numbox("증거 2 · 실업률", "4.2% → 4.1%", COL2[0], 530, 1.0, L)}
  {numbox("증거 3 · 시간당 임금", "▲0.4%", COL2[1], 530, 1.2, RED)}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 760, 270, 1.6, "a-sl", "squish")}
  {bub("셋 다 <b>예상보다 강해요!</b><br>경제가 뜨겁다는 신호", 330, 820, 1.8, "t-left", style="font-size:44px")}
</div>
''', "#2B3060"))

# 3 ── 추리: 비유 '에어컨' — 경제가 너무 뜨거우면 연준이 금리 인상(에어컨)을 켤 수도
S[3] = (1, page(FX + f'''
{head("탐정의 추리", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFF1E6;--d:0s">
  <div class="abs" style="left:{P}px;top:30px;width:{IW}px;height:300px;box-sizing:border-box;background:#FFD8B8;border:5px solid {L};border-radius:26px"></div>
  <div class="abs a-pop" style="left:{P + 30}px;top:60px;--d:.1s;font-size:120px;line-height:1">🔥</div>
  <div class="abs a-rise" style="left:{P + 180}px;top:70px;--d:.2s;font-size:56px;line-height:1.25">경제 방이<br><span style="color:#E8590C">너무 후끈!</span></div>
  {aircon(560, 70, 360, .6)}
  {remote(860, 210, .9)}
  {ch(mascot("moon", "worried", "point"), P, 360, 260, 1.0, "a-sl", "squish")}
  {bub("12월에 <b>금리 인상</b>이라는<br>에어컨을 켤까?", 320, 400, 1.2, "t-left", style="font-size:44px")}
  <div class="abs a-fade" style="left:330px;top:560px;--d:1.4s;font-size:30px;color:#6B5A50">역: 달떡이 = 연준(미국 중앙은행)</div>
  {nar("금리를 올리면 돈 빌리기가 비싸져<br>뜨거운 경기를 <b>식히는</b> 효과", P, 660, 2.0, "font-size:40px;width:902px;box-sizing:border-box;text-align:center")}
  {ch(mascot("star", "worried", "down"), P, 820, 230, 2.6, "a-sl", "brr")}
  {bub("주식 시장은<br><b>추워질까</b> 걱정", 300, 860, 2.8, "t-left", style="font-size:42px")}
</div>
''', "#30366E"))

# 4 ── 반전 단서: 반도체는 반등 + 서울 현장
S[4] = (1, page(FX + f'''
{head("반전 단서 · 서울 현장", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {cbub("그런데 이틀 폭락한 <b>반도체</b>는<br>싸게 사자는 손님에 반등!", 30, .1, "t-down", style="font-size:44px")}
  <div class="abs" style="left:{P}px;top:250px;width:{IW}px;text-align:center">
    <div class="a-fade" style="--d:.4s;font-size:38px">미국 반도체 (전날 <span style="color:{BLUE}">▼12.25%</span>)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.5s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲4.21%</span></div></div>
  {numbox("나스닥", "▲1.09%", COL2[0], 480, 1.0, RED)}
  {numbox("다우", "▼0.46%", COL2[1], 480, 1.15, BLUE)}
  <div class="abs a-pop" style="left:{P}px;top:690px;width:{IW}px;height:440px;box-sizing:border-box;--d:1.7s;background:#fff;border:5px solid {L};border-radius:26px">
    <div class="abs" style="left:0;right:0;top:20px;text-align:center;font-size:36px">🇰🇷 서울은 금요일에 (6일 코스피)</div>
    <div class="abs" style="left:0;right:0;top:70px;text-align:center;font-size:120px;line-height:1"><span class="thump" style="--d:2.0s;color:{BLUE};-webkit-text-stroke:5px {L};paint-order:stroke fill">▼6.02%</span></div>
    <div class="abs" style="left:0;right:0;top:206px;text-align:center;font-size:36px;color:#5B5070">서킷브레이커(매매 20분 정지)까지</div>
    {ch(mascot("bamtol", "worried", "hold", p_mag()), 30, 250, 170, 2.3, "a-sl", "squish2")}
    {bub("미국 반등, 월요일에<br><b>반영될지</b> 지켜봐요", 230, 280, 2.5, "t-left", style="font-size:38px")}
  </div>
</div>
''', "#4A3E78"))

# 5 ── 수사 노트 (월요일 한국장 체크 3)
def note(n, title, sub, y, d):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="background:#FFFDF2;border:5px solid {L};border-radius:14px;padding:16px 28px 16px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#F1E6C8 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#E8590C;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:46px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 노트 · 월요일 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#5E6BB8;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:62px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill"><span class="punch" style="--d:.1s">월요일 한국장, 볼 것은 셋</span></div>
  {note(1, "반도체, 반등 이어받을까", "미국 반도체 ▲4.21%가 반영되면 부담이 줄 가능성", 160, .5)}
  {note(2, "외국인, 매도 멈출까", "이틀 연속 대규모 순매도 · 더 팔면 하락 압력 가능성", 370, .95)}
  {note(3, "금리 인상 걱정", "12월 인상 전망이 더 커지면 기술주엔 부담 가능성", 580, 1.4)}
  {ch(mascot("bamtol", "normal", "point"), 630, 800, 220, 2.0, "a-sr", "squish")}
  {bub("수사 노트 셋,<br><b>꼭 챙겨요!</b>", 320, 840, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 미 노동통계국, 뉴스핌, 뉴스1, 이투데이, 아시아경제</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 다음 사건", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 사건 파일 (미국 시간 11/10 화)</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:72px;line-height:1.2">미국 10월<br>소비자물가(CPI)</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">이번 주 성적표는 <span style="color:#FFC08A">내일 아침 8시</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave", "", False), 590, 220, 270, .4, "a-sr", "hop")}
  {bub("오늘 수사는 여기까지!<br><b>주말 잘 보내요~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: 미 노동통계국, 뉴스핌, 뉴스1, 이투데이, 아시아경제, AP<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.6, 1.5), 3: (4.6, 1.5), 4: (4.4, 1.5), 5: (4.0, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "beep", .6), (1, .05, "whoosh", .6), (1, .1, "scan", .6), (1, .35, "thud", 1), (1, .4, "tension", .5), (1, .7, "beep", .8),
 (2, .1, "pop", .8), (2, .4, "shutter", .7), (2, .6, "dundun", .5), (2, 1.0, "pop", .7), (2, 1.2, "pop", .7), (2, 1.6, "whoosh", .5), (2, 1.8, "ding", .7),
 (3, .1, "pop", .7), (3, .2, "tick", .6), (3, .6, "whoosh", .6), (3, .9, "boing", .5), (3, 1.0, "whoosh", .4), (3, 1.2, "pop", .8), (3, 2.0, "tick", .8), (3, 2.6, "boing", .5), (3, 2.8, "pop", .7),
 (4, .1, "pop", .8), (4, .5, "sparkle", .8), (4, 1.0, "pop", .6), (4, 1.15, "blip_down", .6), (4, 1.7, "whoosh", .5), (4, 2.0, "blip_down", .7), (4, 2.3, "boing", .5), (4, 2.5, "pop", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .6), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .6), (6, .9, "jingle", .9),
]
