"""형식: 밤사이 O/X 퀴즈쇼 — 밤톨이 MC, 별콩이 도전자. 문제 3개로 그날 이야기를 푼다.
예시 내용: 2026-10-15. 새 날짜에는 구조만 참고하고 문제·배치·대사는 그날 이야기에 맞게 새로 짠다.
문제는 '맞히면 오늘 뉴스를 이해하게 되는' 것으로 고르고, 하나쯤은 도전자가 틀리게 해서 재미를 준다.
"""
from lib import *

S = {}
BG = "#3B2E6E"

def stage_lights():
    return "".join(f'<div class="abs" style="left:{x}px;top:0;width:180px;height:1920px;background:linear-gradient(rgba(255,240,180,.18),transparent 70%);transform:skewX({k}deg)"></div>'
                   for x, k in [(80, 12), (450, 0), (820, -12)])

def buzzer(x, y, d):
    return (f'<svg class="abs a-pop" style="left:{x}px;top:{y}px;--d:{d}s" width="150" height="110" viewBox="0 0 150 110">'
            f'<rect x="10" y="60" width="130" height="44" rx="12" fill="#5B5FA8" stroke="{L}" stroke-width="5"/>'
            f'<ellipse cx="75" cy="58" rx="46" ry="26" fill="#E8484A" stroke="{L}" stroke-width="5"/></svg>')

def score(n, x, y, d):
    stars_ = "".join(f'<span style="color:{"#FFD84D" if i < n else "#6B6490"}">★</span>' for i in range(3))
    return f'<div class="abs a-pop" style="left:{x}px;top:{y}px;--d:{d}s;background:{L};color:#FFF6EA;border-radius:18px;padding:6px 20px;font-size:40px">점수 {stars_}</div>'

# 1 ── 오프닝 (훅)
S[1] = (1, page(f'''
{stage_lights()}
{head("밤사이 O/X 퀴즈 · 10.15", 1, "#F6EEE4")}
{big("물가는 겨우 0.1%p 더 올랐는데", 44, 196, 58, 0, "#F6EEE4", "")}
{big("나스닥은 왜 <span style='color:#7DBBFF'>▼1.88%</span>?", 44, 270, 86, 0, "#FFC08A", "")}
<div class="abs a-stamp" style="left:120px;top:430px;--d:.2s;--r:-4deg;width:840px;text-align:center;background:#FFD84D;border:6px solid {L};border-radius:40px;padding:18px 0;font-size:84px;box-shadow:0 10px 0 rgba(0,0,0,.25)">밤사이 O/X 퀴즈!</div>
{ch(mascot("bamtol", "happy", "up"), 90, 720, 330, .7, "a-sl", "hop")}
{ch(mascot("star", "surprised"), 640, 760, 300, 1.0, "a-sr", "squish")}
{buzzer(700, 1100, 1.2)}
{bub("문제 3개만 맞히면<br><b>어젯밤 뉴스</b> 끝!", 60, 1240, 1.4, "t-up", "160px")}
{bub("자신 있어!", 650, 1300, 1.9, "t-up", "120px", "font-size:40px;padding:14px 26px")}
''', BG))

# 2 ── Q1 (도전자 오답)
S[2] = (1, page(f'''
{stage_lights()}
{head("Q1", 2, "#F6EEE4")}
{qcard(1, "어젯밤 미국 물가(CPI)는<br><b style='color:#E8590C;font-weight:400'>예상보다 낮았다?</b>", 60, 200, 900, .05)}
{oxs("X", 290, 560, .5, 2.2)}
<div class="abs a-sl" style="left:60px;top:820px;width:260px;--d:.9s"><div style="animation:fade .15s both reverse;animation-delay:2.2s"><div class="squish">{mascot("star", "happy", "up")}</div></div></div>
{bub("O! 낮았을 거야!", 330, 860, 1.1, "t-left", style="font-size:40px;padding:14px 26px")}
<div class="abs" style="left:60px;top:820px;width:260px"><div style="animation:fade .15s both;animation-delay:2.2s"><div class="shiver">{mascot("star", "teary")}</div></div></div>
{sfx("땡!", 760, 520, 110, 2.2, 10, "#FF8A8A")}
<div class="panel a-pop" style="left:44px;top:1130px;width:982px;height:240px;background:#FFF8E1;--d:2.7s">
  <div class="abs" style="left:36px;top:30px;font-size:40px">정답 <span style="color:#E03131">X</span> — 실제 <b style="color:#E03131;font-weight:400">3.7%</b>, 예상 3.6%보다 높았어요</div>
  <div class="abs" style="left:36px;top:110px;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;line-height:1.5">물가가 오른 속도(1년 전 대비)가 시장 예상보다 빨랐다는 뜻.<br>변동이 큰 품목을 뺀 근원 물가도 2.6%로 예상(2.5%)을 웃돌았어요.</div>
</div>
''', BG))

# 3 ── Q2 (정답)
S[3] = (1, page(f'''
{stage_lights()}
{head("Q2", 3, "#F6EEE4")}
{qcard(2, "물가가 뜨거우면 <b style='color:#E8590C;font-weight:400'>먼 미래 기대주</b><br>(AI·반도체)가 먼저 흔들린다?", 60, 200, 900, .05)}
{oxs("O", 290, 560, .5, 2.0)}
{ch(mascot("star", "worried"), 60, 820, 260, .9, "a-sl", "squish")}
{bub("음… O!", 330, 880, 1.1, "t-left", style="font-size:40px;padding:14px 26px")}
{sfx("딩동댕!", 640, 500, 84, 2.0, -8, "#FFE59A")}
{ch(mascot("bamtol", "normal", "point"), 700, 820, 260, 2.4, "a-sr", "squish2")}
<div class="panel a-pop" style="left:44px;top:1130px;width:982px;height:240px;background:#FFF8E1;--d:2.7s">
  <div class="abs" style="left:36px;top:26px;font-size:38px;line-height:1.35">물가 ↑ → 금리 인상 걱정 ↑ → 나중에 클 회사의<br>'지금 몸값'이 먼저 깎여요</div>
  <div class="abs" style="left:36px;top:150px;font-size:40px">기술주 많은 나스닥 <span style="color:#2F6BD8">▼1.88%</span> · 다우 <span style="color:#2F6BD8">▼0.09%</span></div>
</div>
{score(1, 44, 470, 3.2)}
''', BG))

# 4 ── Q3 (한국)
S[4] = (1, page(f'''
{stage_lights()}
{head("Q3", 4, "#F6EEE4")}
{qcard(3, "어제(14일) 코스피는<br><b style='color:#E8590C;font-weight:400'>오랜만에 올랐다?</b>", 60, 200, 900, .05)}
{oxs("X", 290, 560, .5, 1.9)}
{ch(mascot("star", "happy"), 60, 820, 260, .9, "a-sl", "squish")}
{bub("X! 이건 알아!", 330, 880, 1.1, "t-left", style="font-size:40px;padding:14px 26px")}
{sfx("딩동댕!", 640, 500, 84, 1.9, -8, "#FFE59A")}
<div class="panel a-pop" style="left:44px;top:1130px;width:982px;height:240px;background:#FFF8E1;--d:2.5s">
  <div class="abs" style="left:36px;top:30px;font-size:40px">코스피 <b style="color:#2F6BD8;font-weight:400">6거래일 연속 하락</b> (14일 ▼0.44%)</div>
  <div class="abs" style="left:36px;top:110px;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;line-height:1.5">어젯밤 미국 AI·반도체 약세가 오늘 한국 반도체에도<br>부담이 될 수 있어요.</div>
</div>
{score(2, 44, 470, 2.9)}
''', BG))

# 5 ── 결과 + 오늘 체크
S[5] = (1, page(f'''
{stage_lights()}
{head("결과 발표", 5, "#F6EEE4")}
<div class="abs a-stamp" style="left:140px;top:200px;--d:.1s;--r:3deg;width:800px;text-align:center;background:#FFD84D;border:6px solid {L};border-radius:36px;padding:14px 0;font-size:72px">3문제 중 2개 정답!</div>
{ch(mascot("star", "happy", "up"), 110, 400, 270, .5, "a-pop", "hop")}
{ch(mascot("bamtol", "happy", "wave"), 680, 400, 270, .6, "a-pop", "hop")}
<div class="panel a-pop" style="left:44px;top:730px;width:982px;height:420px;background:#fff;--d:1.0s">
  {nar("보너스! 오늘 한국장 체크 3", 30, 26, 1.2, "font-size:40px")}
  <div class="abs a-sl" style="left:40px;top:130px;--d:1.5s;font-size:42px">① 반도체 — 미국 약세가 이어지는지</div>
  <div class="abs a-sl" style="left:40px;top:205px;--d:1.8s;font-size:42px">② 환율 — 원/달러 1,338원대, 외국인 수급</div>
  <div class="abs a-sl" style="left:40px;top:280px;--d:2.1s;font-size:42px">③ 기름값 — WTI 95.09달러 <span style="color:#E03131">▲1.01%</span></div>
  <div class="abs a-fade" style="left:40px;top:360px;--d:2.3s;font-family:Noto Sans CJK KR,sans-serif;font-size:23px;color:#6B5A50">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게</div>
</div>
<div class="abs a-rise" style="left:44px;top:1190px;width:982px;--d:2.6s;text-align:center;font-size:44px;color:#F6EEE4">다음 문제는 <span style="color:#FFC08A">PPI·소매판매·TSMC 실적</span>!<br>내일 아침 8시에 만나요</div>
<div class="abs a-pop" style="left:0;right:0;top:1360px;--d:3.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};border-radius:999px;padding:12px 44px;font-size:46px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1470px;color:#CFC4E8;--d:3.1s">출처: AP, 연합뉴스, 뉴스핌, 서울경제, 파이낸셜뉴스 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', BG))

PLAN = {1: (5.0, 1.3), 2: (5.6, 1.3), 3: (5.6, 1.3), 4: (5.2, 1.3), 5: (4.8, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .2, "reveal", .8), (1, .7, "whoosh", .5), (1, .7, "boing", .7), (1, 1.0, "boing", .5), (1, 1.4, "pop", .8), (1, 1.9, "pop", .7),
 (2, .05, "whoosh", .6), (2, .5, "pop", .6), (2, .6, "pop", .6), (2, 1.1, "pop", .8), (2, 1.3, "drumroll", .8), (2, 2.2, "wrong", 1), (2, 2.4, "sad", .7), (2, 2.7, "tick", 1),
 (3, .05, "whoosh", .6), (3, .5, "pop", .6), (3, .6, "pop", .6), (3, 1.1, "pop", .8), (3, 1.1, "drumroll", .7), (3, 2.0, "correct", 1), (3, 2.4, "boing", .6), (3, 2.7, "tick", 1), (3, 3.2, "sparkle", .6),
 (4, .05, "whoosh", .6), (4, .5, "pop", .6), (4, .6, "pop", .6), (4, 1.1, "pop", .8), (4, 1.1, "drumroll", .7), (4, 1.9, "correct", 1), (4, 2.5, "tick", 1), (4, 2.9, "sparkle", .6),
 (5, .1, "reveal", .9), (5, .5, "yay", .8), (5, 1.2, "tick", 1), (5, 1.5, "CHECK1", 1), (5, 1.8, "CHECK2", 1), (5, 2.1, "CHECK3", 1), (5, 3.0, "jingle", .9),
]
