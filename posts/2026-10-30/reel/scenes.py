"""형식: 밤사이 탐정 추리 v4 (검수 전 · 2026-10-30) — 장면 1을 '사건 현장 분필 윤곽선(절벽처럼 꺾인 주가 선) + 증거 번호표' 구도로 새로 짠 버전.
내용: 2026-10-30 (29일 뉴욕 — 알파벳 ▼12.6%, 2004년 상장 이후 최대 낙폭 · 나스닥 ▼1.38%). 비유: AI 투자 = 씨앗값, 매출 = 수확.
흐름: 1 사건 결론(▼12.6% + '상장 이후 최악의 날') → 2 증거 봉투 셋(매출·AI 투자비·물가) → 3 단서·주범(씨앗값 산더미, 수확은 기대 이하) → 4 한국 현장 조사(29일 코스피·삼성·하이닉스) → 5 수사 메모판(오늘 체크 3) → 6 다음 사건 예고.
숫자는 2026-10-30 카드·sources.md에 있는 것만 쓴다. 다른 용의자를 '무죄'로 단정하지 않는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes linedraw{from{stroke-dashoffset:var(--len)}to{stroke-dashoffset:0}}
@keyframes swing{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes flash{0%{opacity:0}20%{opacity:.85}100%{opacity:0}}
.swing{transform-origin:50% 0;animation:swing 1.6s ease-in-out infinite}
.grow{transform-origin:50% 100%;animation:grow .5s cubic-bezier(.2,.9,.3,1) both;animation-delay:var(--d,0s)}
.flash{animation:flash .35s ease-out both;animation-delay:var(--d,0s)}
</style>"""

def tent(n, x, y, d):
    """노란 증거 번호표(삼각 텐트)."""
    return (f'<div class="abs a-drop" style="left:{x}px;top:{y}px;--d:{d}s">'
            f'<svg width="96" height="86" viewBox="0 0 96 86"><path d="M10 80 L48 8 L86 80 Z" fill="#FFD84D" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<text x="48" y="70" text-anchor="middle" font-size="40" font-family="Jua" fill="{L}">{n}</text></svg></div>')

# 1 ── 결론 먼저 (분필 윤곽선 사건 현장): 0초에 숫자·결론·탐정(클로즈업)·현장이 모두 보인다
#      0~1초: 숫자 펀치(0) → 카메라 플래시(.05) → 분필 선이 절벽처럼 꺾임(.1~.7) → 번호표 1·2 툭(.35/.5) → '사건 번호 1029' 도장(.55) → 탐정 흔들림
CHALK = (f'<svg width="560" height="430" viewBox="0 0 560 430" style="overflow:visible">'
         f'<path d="M20 120 L120 100 L210 112 L300 80 L340 92 L380 360 L540 380" fill="none" stroke="#F4F1E8" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 0" '
         f'style="stroke-dasharray:1000;--len:1000;stroke-dashoffset:1000;animation:linedraw .6s ease-in .1s both"/>'
         f'<path d="M338 70 l20 0" stroke="#F4F1E8" stroke-width="6" stroke-linecap="round" opacity=".6"/>'
         f'<text x="390" y="330" font-size="44" font-family="Jua" fill="#9EC2FF" class="a-pop" style="--d:.6s">뚝!</text></svg>')
S[1] = (1, page(FX + f'''
{stars(14, 30, 0, 260)}
{head("밤사이 탐정 · 10.30 FRI", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:205px;text-align:center;font-size:46px;color:#C9D6FF">알파벳(구글) · 29일 뉴욕 하루</div>
<div class="abs" style="left:0;width:1080px;top:262px;text-align:center"><span class="punch" style="--d:0s;font-size:250px;line-height:1;color:#7DB0FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼12.6%</span></div>
<div class="abs" style="left:0;width:1080px;top:512px;text-align:center;font-size:92px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">상장 이후 <span style="color:#FFE36E">최악의 날!</span></div>
<div class="panel" style="left:44px;top:680px;width:982px;height:740px;background:#2A2E3A">
  <div class="abs" style="left:0;right:0;top:0;bottom:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.04) 0 120px,transparent 120px 240px)"></div>
  <div class="abs" style="left:{P}px;top:36px;font-size:40px;color:#FFD84D">사건 현장 · 주가 선</div>
  <div class="abs" style="left:{P}px;top:120px">{CHALK}</div>
  {tent(1, 300, 160, .35)}
  {tent(2, 430, 470, .5)}
  <div class="abs" style="left:520px;top:170px;width:380px"><div class="shiver" style="animation-delay:.65s">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
  <div class="abs flash" style="left:0;right:0;top:0;bottom:0;background:#fff;--d:.05s"></div>
</div>
<div class="stamp a-stamp" style="left:120px;top:1330px;--d:.55s;--r:-7deg;font-size:58px;white-space:nowrap">사건 번호 1029</div>
''', "#262B55"))

# 2 ── 증거 봉투 셋 (빨랫줄에 매단 봉투, COL3) — 다른 용의자를 '무죄'로 단정하지 않는다
def bag(no, icon, title, note, col, d, ncol):
    x, w = col
    return (f'<div class="abs a-drop" style="left:{x}px;top:250px;width:{w}px;--d:{d}s"><div class="swing">'
            f'<div style="margin:0 auto;width:26px;height:40px;background:#C98B4A;border:4px solid {L};border-radius:6px"></div>'
            f'<div style="margin-top:-8px;height:400px;box-sizing:border-box;background:#E9DDBF;border:5px solid {L};border-radius:18px;padding:18px 14px;text-align:center;box-shadow:0 6px 0 rgba(0,0,0,.2)">'
            f'<div style="font-size:30px;color:#8A5A3B">증거 {no}</div>'
            f'<div style="font-size:92px;line-height:1.2">{icon}</div>'
            f'<div style="font-size:46px;line-height:1.15">{title}</div>'
            f'<div style="margin-top:14px;display:inline-block;background:{ncol};color:#fff;border:4px solid {L};border-radius:999px;padding:6px 16px;font-size:32px">{note}</div>'
            f'</div></div></div>')
S[2] = (1, page(FX + f'''
{head("증거 봉투 셋", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cbub("나스닥을 <b>끌어내린 범인</b>,<br>증거부터 볼까요?", 40, .1, "t-down", style="font-size:44px")}
  <div class="abs" style="left:0;right:0;top:262px;height:6px;background:#C9B48A"></div>
  {bag(1, "📉", "매출", "기대 이하", COL3[0], .4, BLUE)}
  {bag(2, "💸", "AI 투자비", "현금 −91억$", COL3[1], .65, BLUE)}
  {bag(3, "🌡️", "물가", "PCE 3.6%", COL3[2], .9, "#8A6A3A")}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 860, 270, 1.4, "a-sl", "squish")}
  {bub("물가도 높았는데<br><b>공범</b>일까요?", 340, 930, 1.7, "t-left", style="font-size:46px")}
</div>
''', "#2B3060"))

# 3 ── 단서·주범 (비유: AI 투자 = 씨앗값, 매출 = 수확)
def seedbag(x, y, d):
    return (f'<div class="abs a-drop" style="left:{x}px;top:{y}px;--d:{d}s;width:120px;height:130px;background:#D9A877;border:5px solid {L};border-radius:26px 26px 18px 18px;'
            f'text-align:center;font-size:30px;line-height:130px">씨앗</div>')
SEEDS = "".join(seedbag(P + 20 + (i % 3) * 110, 410 - (i // 3) * 112, .35 + i * .08) for i in range(6))
S[3] = (1, page(FX + f'''
{head("단서 분석", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("AI 투자는 <b>씨앗값</b>,<br>매출은 <b>수확</b>이라고 생각해 봐요", 26, .1, "t-down", style="font-size:44px")}
  <div class="abs" style="left:{P}px;top:575px;width:{IW}px;height:8px;background:#8A6A3A;border-radius:4px"></div>
  {SEEDS}
  <div class="abs" style="left:{P + 20}px;top:595px;width:340px;text-align:center;font-size:40px">씨앗값은 산더미</div>
  <div class="abs a-pop" style="left:{P + 560}px;top:420px;width:300px;--d:1.1s;text-align:center">
    <div style="margin:0 auto;width:220px;height:130px;background:#E8C27A;border:5px solid {L};border-radius:0 0 90px 90px;position:relative">
      <div style="position:absolute;left:84px;top:-34px;width:52px;height:52px;border-radius:50%;background:#FF8A3D;border:4px solid {L}"></div></div>
  </div>
  <div class="abs" style="left:{P + 540}px;top:595px;width:340px;text-align:center;font-size:40px">수확은 기대 이하</div>
  {nar("투자자들: '이 농사, <b>남는 게 있나?</b>'<br>→ 알파벳 주가 급락 → 기술주로 번짐", P, 690, 1.8, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {stamp("주범: AI 투자 의심", 190, 850, 2.4, -6)}
  {numbox("알파벳 (29일)", "▼12.6%", COL2[0], 970, 2.9, BLUE)}
  {numbox("나스닥 (29일)", "▼1.38%", COL2[1], 970, 3.1, BLUE)}
</div>
''', "#30366E"))

# 4 ── 한국 현장 조사 (29일 서울: 코스피 하락, 삼성·하이닉스 엇갈림)
def bar(label, val, h, col, d, color):
    x, w = col
    return (f'<div class="abs" style="left:{x}px;top:310px;width:{w}px;height:300px">'
            f'<div class="abs grow" style="left:{w//2 - 55}px;bottom:0;width:110px;height:{h}px;background:{color};border:5px solid {L};border-radius:14px 14px 0 0;--d:{d}s"></div></div>'
            f'<div class="abs a-pop" style="left:{x}px;top:630px;width:{w}px;text-align:center;--d:{d + .2:.1f}s"><div style="font-size:36px">{label}</div><div style="font-size:56px;color:{color}">{val}</div></div>')
S[4] = (1, page(FX + f'''
{head("한국 현장 조사", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {cbub("29일 서울에선 <b>하루 만에</b><br>코스피 6,000선을 내줬어요", 34, .15, "t-down", style="font-size:42px")}
  <div class="abs" style="left:{P}px;top:610px;width:{IW}px;height:5px;background:{L}"></div>
  {bar("코스피", "▼1.24%", 120, COL3[0], .5, BLUE)}
  {bar("삼성전자", "▼4.13%", 260, COL3[1], .8, BLUE)}
  {bar("SK하이닉스", "▲2.62%", 160, COL3[2], 1.1, RED)}
  {nar("삼성전자는 <b>사상 최대 실적</b>에도<br>주주환원 계획에 실망 매물", P, 800, 1.8, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("star", "worried", "down"), 120, 940, 240, 2.2, "a-sl", "squish")}
  {ch(mascot("bamtol", "normal", "hold", p_mag()), 620, 940, 240, 2.3, "a-sr", "squish2")}
</div>
''', "#4A3E78"))

# 5 ── 수사 메모판 (코르크판 + 메모 3장, 오늘 체크)
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
  {memo(1, "반도체, AI 의심 견딜까", "미국 반도체주 약세가 이어지면 부담 가능성", P, 150, .5, -1.5)}
  {memo(2, "삼성전자 실망 매물", "29일 ▼4.13% · 세부 환원안은 내년 1월 말", P, 360, .95, 1.2)}
  {memo(3, "미국 물가 3.6%", "금리 인상 걱정 커지면 외국인 수급 부담", P, 570, 1.4, -1)}
  {ch(mascot("bamtol", "normal", "point"), 640, 790, 240, 2.0, "a-sr", "squish")}
  {bub("메모 셋,<br><b>꼭 챙겨요!</b>", 300, 830, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 로이터, 야후파이낸스, 아시아경제, 한국경제, 한국일보, 전자신문</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 사건 파일</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">오늘 밤 이번 주<br>마지막 미국장</div>
  <div class="abs a-rise" style="left:44px;top:320px;--d:.3s;font-size:44px">내일 아침 <span style="color:#FFC08A">8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("사건 종결!<br><b>밤사이 탐정</b>이었습니다", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 로이터, AP, 야후파이낸스, 인베스팅닷컴, 아시아경제, 뉴스1, 한국경제, 한국일보 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.6, 1.5), 3: (4.4, 1.5), 4: (3.8, 1.5), 5: (3.6, 1.5), 6: (3.4, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .6), (1, .05, "shutter", .9), (1, .1, "slidedown", .7), (1, .35, "thud", .8), (1, .5, "thud", .8), (1, .55, "reveal", .6), (1, .6, "blip_down", .6), (1, .8, "hmm", .5),
 (2, .05, "whoosh", .5), (2, .1, "pop", .8), (2, .4, "boing", .6), (2, .65, "boing", .6), (2, .9, "boing", .6), (2, 1.4, "whoosh", .5), (2, 1.7, "question", .6),
 (3, .1, "pop", .8), (3, .35, "tick", .6), (3, .6, "tick", .6), (3, .8, "tick", .6), (3, 1.1, "boing", .6), (3, 1.8, "hmm", .7), (3, 2.4, "thud", 1), (3, 2.4, "reveal", .8), (3, 2.9, "blip_down", .7), (3, 3.1, "blip_down", .6),
 (4, .05, "whoosh", .5), (4, .15, "pop", .8), (4, .5, "blip_down", .5), (4, .8, "slidedown", .5), (4, 1.1, "sparkle", .6), (4, 1.8, "tick", .9), (4, 2.2, "sad", .5), (4, 2.3, "boing", .5),
 (5, .05, "whoosh", .5), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
