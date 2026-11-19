"""2026-11-20 릴스 · 토크쇼(talkshow) v4 — '결론 먼저' 훅, 장면 1 '박수 측정기(APPLAUSE METER) 바늘이 HOT→COLD로 곤두박질 + 상장 축하 꽃가루 + 반전 도장' 새 구도 (검수 전).
그날 상황: 3대 지수 모두 2%대 급락(다우 ▼2.19%·S&P ▼2.02%·나스닥 ▼2.25%) → 상황표 첫 칸(급변) 1순위 news는 11-17에 써서(최근 3일 11-17 news·11-18 delivery·11-19 detective)
          2순위 talkshow(마지막 11-11, 최근 3일 밖).
흐름: 1 결론(나스닥 ▼2.25% '상장 잔치에도 증시는 뚝!', 박수 측정기) → 2 게스트 토크(역: 월가 투자자, 앤트로픽 데뷔 무대 성적표 83→111.50→97.17달러)
      → 3 쉬운 해설: 비유 '데뷔 무대는 대박, 그런데 공연장(AI 데이터센터) 지은 돈은 언제 벌지?' = AI 투자 비용·수익성 의문 + 3대 지수 + AMD 공매도 보고서
      → 4 방청객 질문: 한국은?(19일 코스피 ▲1.39%, 장중 4,963.61까지 밀렸다 반등) → 5 MC 큐카드(오늘 체크 3) → 6 다음 회 예고(앤트로픽 둘째 날·11/26 휴장).
숫자·사실은 posts/2026-11-20 카드·sources.md에 있는 것만 쓴다. 게스트 대사는 기사로 확인된 사실을 쉬운 말로 옮긴 역할극이다(실제 발언 인용 아님).
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes needle{0%{transform:rotate(62deg)}18%{transform:rotate(70deg)}55%{transform:rotate(-74deg)}68%{transform:rotate(-62deg)}80%{transform:rotate(-70deg)}100%{transform:rotate(-66deg)}}
@keyframes conf{0%{transform:translateY(-40px) rotate(0)}100%{transform:translateY(560px) rotate(540deg)}}
@keyframes flash{0%{opacity:0}20%{opacity:.75}100%{opacity:0}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.35}}
@keyframes bulbs{0%,100%{background-position:0 0}50%{background-position:30px 0}}
.needle{transform-origin:50% 100%;animation:needle .95s cubic-bezier(.3,.1,.3,1) both}
.conf{animation:conf 1.6s linear infinite}
.flash{animation:flash .35s ease-out both;animation-delay:var(--d,0s)}
.blink{animation:blink .6s steps(1) infinite}
.bulbs{background:repeating-linear-gradient(90deg,#FFE36E 0 14px,transparent 14px 30px);animation:bulbs .5s steps(2) infinite}
</style>"""

def p_mic():
    """마이크 (캐릭터 오른손 쪽)."""
    return (f'<path d="M204 222 L188 266" stroke="{L}" stroke-width="13" stroke-linecap="round"/>'
            f'<path d="M204 222 L188 266" stroke="#2F2F3A" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="212" cy="196" r="19" fill="#3A3A48" stroke="{L}" stroke-width="5"/>'
            f'<path d="M200 190 h24 M198 198 h28 M202 206 h20" stroke="#8C92AE" stroke-width="2.5"/>')

def meter(x, y, w):
    """박수 측정기 — 반원 눈금(COLD 파랑 ~ HOT 빨강) + 바늘."""
    h = w // 2
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h + 60}px">'
            f'<svg viewBox="0 0 400 230" width="{w}" height="{int(w * .575)}">'
            f'<path d="M30 200 A170 170 0 0 1 370 200 Z" fill="#FFFDF5" stroke="{L}" stroke-width="7"/>'
            f'<path d="M58 200 A142 142 0 0 1 130 76" fill="none" stroke="#5AA9FF" stroke-width="30"/>'
            f'<path d="M130 76 A142 142 0 0 1 270 76" fill="none" stroke="#FFE36E" stroke-width="30"/>'
            f'<path d="M270 76 A142 142 0 0 1 342 200" fill="none" stroke="#FF6B6B" stroke-width="30"/>'
            f'<text x="62" y="186" font-family="Jua" font-size="26" fill="{L}">COLD</text>'
            f'<text x="290" y="186" font-family="Jua" font-size="26" fill="{L}">HOT</text></svg>'
            f'<div class="abs needle" style="left:{w // 2 - 7}px;top:{int(w * .09)}px;width:14px;height:{int(w * .41)}px;background:{L};border-radius:7px"></div>'
            f'<div class="abs" style="left:{w // 2 - 22}px;top:{int(w * .475)}px;width:44px;height:44px;border-radius:50%;background:#E03131;border:6px solid {L}"></div>'
            f'<div class="abs" style="left:0;width:{w}px;top:{int(w * .58)}px;text-align:center;font-size:34px;color:#FFE36E">APPLAUSE METER</div></div>')

def confetti(n, seed, w, h):
    rnd = random.Random(seed)
    cols = ["#FF6B6B", "#FFE36E", "#9AD3FF", "#C9B8FF", "#8CE0A8"]
    return "".join(f'<div class="abs conf" style="left:{rnd.randint(20, w - 40)}px;top:{rnd.randint(-80, h // 3)}px;width:{rnd.randint(14, 22)}px;height:{rnd.randint(8, 14)}px;'
                   f'background:{rnd.choice(cols)};border:2px solid {L};animation-delay:-{rnd.random() * 1.6:.2f}s"></div>' for _ in range(n))

def sign(text, x, y, d, bg="#E03131", size=46, rot=-6):
    return (f'<div class="abs a-stamp" style="left:{x}px;top:{y}px;--d:{d}s;--r:{rot}deg;background:{bg};color:#fff;border:5px solid {L};'
            f'border-radius:16px;padding:6px 22px;font-size:{size}px;box-shadow:0 6px 0 rgba(0,0,0,.25);white-space:nowrap">{text}</div>')

# 1 ── 결론 먼저 (박수 측정기): 0초에 숫자·결론·MC(클로즈업, 놀람)·측정기가 모두 보인다
#      0~1초: 숫자 펀치(0) → 플래시(.05) → 바늘 HOT→COLD 곤두박질(.1~.6) → '반전!' 도장 쾅(.4) → MC 떨림(.5) → '어라?!'(.7)
S[1] = (1, page(FX + f'''
{stars(12, 47, 0, 200)}
{head("밤사이 토크쇼 · 11.20 FRI", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:48px;color:#FFE36E">어젯밤 나스닥</div>
<div class="abs" style="left:0;width:1080px;top:260px;text-align:center"><span class="punch" style="--d:0s;font-size:240px;line-height:1;color:#7DB0FF;-webkit-text-stroke:11px {L};paint-order:stroke fill">▼2.25%</span></div>
<div class="abs" style="left:0;width:1080px;top:520px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">상장 잔치에도 <span style="color:#FFE36E">증시는 뚝!</span></div>
<div class="panel" style="left:44px;top:680px;width:982px;height:760px;background:#2C2450">
  <div class="abs bulbs" style="left:0;right:0;top:0;height:16px"></div>
  {confetti(26, 7, 982, 760)}
  {meter(470, 60, 470)}
  <div class="abs" style="left:0;right:0;bottom:0;height:150px;background:#5B3E8A;border-top:6px solid {L}"></div>
  <div class="abs" style="left:10px;top:150px;width:470px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "hold", p_mic())}</div></div>
  {sign("반전!", 640, 380, .4, "#2F6BD8", 72, 8)}
  {sfx("어라?!", 560, 560, 96, .7, -6, "#FFE36E")}
  <div class="abs flash" style="left:0;right:0;top:0;bottom:0;background:#fff;--d:.05s"></div>
</div>
''', "#262B55"))

# 2 ── 게스트 토크 (달떡이가 '월가 투자자' 역) — 앤트로픽 데뷔 성적표
def step(k, v, sub, col, top, d, color):
    x, w = col
    return (f'<div class="num a-pop" style="left:{x}px;top:{top}px;width:{w}px;box-sizing:border-box;text-align:center;--d:{d}s">'
            f'<div class="k">{k}</div><div class="v" style="color:{color};font-size:50px">{v}</div><div style="font-size:28px">{sub}</div></div>')
S[2] = (1, page(FX + f'''
{head("게스트 토크", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3E3570;--d:0s">
  <div class="abs bulbs" style="left:0;right:0;top:0;height:16px"></div>
  <div class="abs" style="left:{P}px;top:50px;width:{IW}px;height:150px;box-sizing:border-box;background:#FFF8E1;border:5px solid {L};border-radius:22px;text-align:center;box-shadow:0 6px 0 rgba(0,0,0,.2)">
    <div style="font-size:34px;color:#8A5A3B;margin-top:14px">오늘의 화제 · 역대 최대 상장</div>
    <div style="font-size:64px">앤트로픽 <span style="color:#E8590C">데뷔 무대</span></div></div>
  {step("공모가", "83달러", "출발선", COL3[0], 250, .3, L)}
  {step("첫 거래", "111.50달러", "34% 높게", COL3[1], 250, .6, RED)}
  {step("첫날 종가", "▲17.07%", "97.17달러", COL3[2], 250, .9, RED)}
  {ch(mascot("moon", "happy", "point"), P, 600, 300, 1.2, "a-sl", "squish")}
  <div class="abs a-pop" style="left:{P}px;top:930px;width:330px;--d:1.3s;text-align:center;background:#7E5BB8;color:#fff;border:5px solid {L};border-radius:16px;font-size:28px;padding:6px 0;white-space:nowrap">게스트 · 역: 월가 투자자</div>
  {bub("데뷔는 <b>대박</b>,<br>함성은 조금 식었죠", 380, 620, 1.5, "t-left", style="font-size:46px")}
  {ch(mascot("bamtol", "surprised", "hold", p_mic()), 652, 860, 230, 2.1, "a-sr", "squish2")}
  {bub("그런데 증시는<br>왜 빠졌죠?", 330, 900, 2.3, "t-right", style="font-size:42px")}
</div>
''', "#2B3060"))

# 3 ── 쉬운 해설 (비유: 데뷔 무대 vs 공연장 지은 돈)
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("무대가 대박이어도 관객은 걱정해요.<br><b>공연장(AI 데이터센터)</b> 지은 돈, 언제 벌지?", 30, .1, "t-down", style="font-size:40px")}
  <div class="abs a-pop" style="left:{P}px;top:250px;width:431px;height:250px;box-sizing:border-box;--d:.5s;background:#FFF8E1;border:4px solid {L};border-radius:24px;text-align:center;padding-top:24px">
    <div style="font-size:44px">🏟 공연장 공사비</div><div style="font-size:38px;line-height:1.35;margin-top:10px">= AI 투자 비용<br>계속 불어나는 중</div></div>
  <div class="abs a-pop" style="left:{P + 471}px;top:250px;width:431px;height:250px;box-sizing:border-box;--d:.8s;background:#FFF8E1;border:4px solid {L};border-radius:24px;text-align:center;padding-top:24px">
    <div style="font-size:44px">🎟 티켓 수입 ❓</div><div style="font-size:38px;line-height:1.35;margin-top:10px">= 수익성<br>아직 물음표</div></div>
  {numbox("다우", "▼2.19%", COL3[0], 550, 1.3, BLUE)}
  {numbox("S&amp;P500", "▼2.02%", COL3[1], 550, 1.45, BLUE)}
  {numbox("나스닥", "▼2.25%", COL3[2], 550, 1.6, BLUE)}
  {ch(mascot("owl", "worried", "hold", p_tablet()), P, 790, 240, 2.0, "a-sl", "squish")}
  {bub("AMD는 <b>공매도 보고서</b><br>(주가 하락에 거는 쪽)에 급락", 320, 820, 2.3, "t-left", style="font-size:40px")}
</div>
''', "#30366E"))

# 4 ── 방청객 질문: 한국은? (19일 서울)
S[4] = (1, page(FX + f'''
{head("방청객 질문", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {ch(mascot("star", "surprised", "up"), P, 40, 240, .1, "a-sl", "squish")}
  {bub("한국은<br><b>어땠어요?</b>", 300, 70, .3, "t-left", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:330px;width:{IW}px;--d:.7s;text-align:center">
    <div style="font-size:40px">코스피 (19일 종가)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.9s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲1.39%</span></div></div>
  {nar("장중 <b>4,963.61</b>까지 밀렸다가<br>5,137.89로 반등 마감", P, 580, 1.3, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("SK하이닉스", "▲3.41%", COL2[0], 740, 1.7, RED)}
  {numbox("삼성전자", "▲1.13%", COL2[1], 740, 1.85, RED)}
  {ch(mascot("bamtol", "worried", "hold", p_mic()), 652, 920, 230, 2.3, "a-sr", "squish2")}
  {bub("그런데 밤새 미국<br><b>반도체주가 꺾였어요</b>", 200, 960, 2.5, "t-right", style="font-size:40px")}
</div>
''', "#4A3E78"))

# 5 ── MC 큐카드 (오늘 한국장 체크 3)
def cue(n, title, sub, y, d, rot):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="transform:rotate({rot}deg);background:#FFFFFF;border:5px solid {L};border-radius:14px;padding:18px 28px 18px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#E7ECF7 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#E8590C;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:48px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("MC 큐카드 · 오늘 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#6F8FD8;--d:0s">
  <div class="abs" style="left:{P}px;top:36px;font-size:58px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill">오늘 한국장, 볼 것은 셋</div>
  {cue(1, "반도체 반등 이어갈까", "미국 AI·반도체주 약세가 이어지면 부담 가능성", 150, .4, -1.2)}
  {cue(2, "한한령 완화 기대", "한중 합의가 실제로 이행되는지 확인 단계", 360, .8, 1)}
  {cue(3, "12월 금리 인상 경계", "성장주·환율에 부담이 이어질 가능성", 570, 1.2, -1)}
  {ch(mascot("bamtol", "normal", "point"), 640, 790, 240, 1.7, "a-sr", "squish")}
  {bub("큐카드 셋,<br><b>꼭 챙겨요!</b>", 300, 830, 1.9, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.1s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 로이터, 블록미디어, 한국경제, 서울파이낸스</div>
''', "#FFE1CC"))

# 6 ── 다음 회 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 토크쇼 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 회 예고</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">오늘 밤 앤트로픽 둘째 날<br>11/26 미국장 휴장</div>
  <div class="abs a-rise" style="left:44px;top:320px;--d:.3s;font-size:44px">내일 아침 <span style="color:#FFC08A">8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 210, 290, .4, "a-sr", "hop")}
  {bub("오늘 토크쇼는 여기까지!<br><b>박수~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 헤럴드경제, SBS Biz, 이투데이, 파이낸셜뉴스, 로이터, 블록미디어, 한국경제, 미디어펜 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.4, 1.5), 3: (4.6, 1.55), 4: (4.6, 1.5), 5: (3.6, 1.45), 6: (3.0, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "applause", .6), (1, .05, "shutter", .8), (1, .1, "slidedown", .7), (1, .4, "thud", .9), (1, .5, "tension", .5), (1, .7, "question", .6),
 (2, .0, "mic", .7), (2, .3, "pop", .7), (2, .6, "ding", .6), (2, .9, "sparkle", .6), (2, 1.2, "whoosh", .5), (2, 1.5, "pop", .8), (2, 2.1, "boing", .6), (2, 2.3, "question", .7),
 (3, .1, "pop", .8), (3, .5, "tick", .6), (3, .8, "question", .6), (3, 1.3, "blip_down", .7), (3, 1.45, "blip_down", .6), (3, 1.6, "blip_down", .6), (3, 2.0, "whoosh", .5), (3, 2.3, "pop", .8),
 (4, .1, "whoosh", .5), (4, .3, "question", .7), (4, .7, "dundun", .6), (4, .9, "yay", .5), (4, 1.3, "tick", .8), (4, 1.7, "ding", .6), (4, 1.85, "ding", .5), (4, 2.3, "boing", .5), (4, 2.5, "pop", .8),
 (5, .05, "whoosh", .5), (5, .4, "CHECK1", 1), (5, .8, "CHECK2", 1), (5, 1.2, "CHECK3", 1), (5, 1.9, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "applause", .6), (6, .9, "jingle", .9),
]
