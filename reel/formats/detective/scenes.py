"""형식: 밤사이 탐정 — "범인을 찾아라!" 하락(또는 상승)의 원인을 용의자로 세우고 단서로 범인을 밝힌다.
예시 내용: 2026-10-15. 새 날짜에는 구조만 참고하고 사건·용의자·단서는 그날 이야기에 맞게 새로 짠다.
주의: '범인'은 출처 기사들이 공통으로 꼽은 원인만 지목한다. 다른 용의자를 '무죄'라고 단정하지 말고 '이번 사건의 주범은 아님' 정도로 쓴다.
"""
from lib import *

S = {}
BG = "#2A2238"

hat = f'<path d="M78 128 Q150 60 222 128 Z" fill="#8A6A4A" stroke="{L}" stroke-width="4"/><ellipse cx="150" cy="128" rx="96" ry="14" fill="#6E5238" stroke="{L}" stroke-width="4"/>'
def detective(mood="normal", pose="hold"):
    return mascot("bamtol", mood, pose, p_mag()).replace('<g filter="url(#w)">', '<g filter="url(#w)">', 1).replace('</g></svg>', hat + '</g></svg>')

def tape(y, rot):
    return (f'<div class="abs" style="left:-40px;top:{y}px;width:1160px;height:66px;background:#FFD84D;border:4px solid {L};transform:rotate({rot}deg);'
            f'font-size:34px;line-height:58px;white-space:nowrap;overflow:hidden">' + "출입금지 · 사건 현장 · " * 8 + '</div>')

def suspect(inner, name, sub, x, y, d, rot):
    return pola(f'<div style="width:240px;height:200px;background:#EDE7F6;display:flex;align-items:center;justify-content:center;overflow:hidden">{inner}</div>',
                f'{name}<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:22px;color:#6B5A50">{sub}</div>', x, y, 266, d, rot)

chart_down = f'<svg viewBox="0 0 200 150" width="190"><path d="M15 30 L70 40 L110 75 L150 95 L185 130" fill="none" stroke="#2F6BD8" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M168 128 L188 132 L182 112" fill="none" stroke="#2F6BD8" stroke-width="10" stroke-linecap="round"/></svg>'
thermo = f'<svg viewBox="0 0 100 180" width="90"><rect x="38" y="10" width="24" height="120" rx="12" fill="#fff" stroke="{L}" stroke-width="5"/><rect x="44" y="40" width="12" height="96" fill="#E8484A"/><circle cx="50" cy="146" r="26" fill="#E8484A" stroke="{L}" stroke-width="5"/></svg>'

# 1 ── 사건 발생 (훅)
S[1] = (1, page(f'''
{head("밤사이 탐정 · 10.15", 1, "#F6EEE4")}
{big("나스닥 <span style='color:#7DBBFF'>▼1.88%</span> 사건!", 44, 190, 84, 0, "#FFC08A", "")}
{big("범인은 누구?", 44, 296, 76, 0, "#F6EEE4", "")}
<div class="panel a-pop" style="left:44px;top:440px;width:982px;height:900px;background:#3A3150;--d:.1s">
  {tape(80, -6)}
  <div class="abs a-pop" style="left:560px;top:250px;--d:.4s;width:360px;height:260px;background:#fff;border:5px solid {L};border-radius:20px;display:flex;align-items:center;justify-content:center">{chart_down}</div>
  <div class="abs a-fade" style="left:600px;top:520px;--d:.6s;font-size:36px;color:#F6EEE4">피해자: 나스닥</div>
  {ch(detective("worried"), 60, 300, 380, .7, "a-sl", "squish")}
  {bub("물가는 겨우 0.1%p 더 올랐는데<br>왜 이렇게 크게 빠졌지…?", 60, 720, 1.3, "t-up", "200px", "font-size:38px")}
</div>
''', BG))

# 2 ── 용의자 3명
S[2] = (1, page(f'''
{head("용의자 조사", 2, "#F6EEE4")}
{cork(44, 200, 982, 1130, .05)}
{big("용의자는 셋!", 90, 240, 64, .2, L)}
{suspect(mascot("moon", "worried", "hold", p_card("은행", "BofA")), "① 은행 실적", "BofA 매출 기대 못 미침", 80, 380, .5, -4)}
{suspect(thermo, "② 물가 성적표", "CPI 3.7% (예상 3.6%)", 400, 400, 1.0, 3)}
{suspect(f'<div style="font-size:120px">🛢️</div>', "③ 기름값", "WTI 95.09달러 ▲1.01%", 720, 380, 1.5, -2)}
{ch(detective("normal", "point"), 380, 900, 300, 2.1, "a-rise", "squish")}
{bub("셋 중 진짜 범인은?", 600, 1000, 2.5, "t-left", style="font-size:40px")}
''', BG))

# 3 ── 단서 → 범인 지목 (1분 공부)
S[3] = (1, page(f'''
{head("결정적 단서", 3, "#F6EEE4")}
{cork(44, 200, 982, 1130, .05)}
{pola('<div style="font-size:34px;padding:12px 6px;line-height:1.35">기술주 많은 나스닥<br><b style="color:#2F6BD8;font-weight:400">▼1.88%</b></div>', "단서 1", 90, 250, 330, .2, -3)}
{pola('<div style="font-size:34px;padding:12px 6px;line-height:1.35">AI·반도체주<br><b style="color:#2F6BD8;font-weight:400">동반 약세</b></div>', "단서 2", 640, 250, 330, .6, 3)}
{pola(f'<div style="width:280px;height:200px;display:flex;align-items:center;justify-content:center">{thermo}</div>', "물가 3.7%", 360, 640, 320, 1.0, -1)}
{string(255, 470, 520, 660, 1.3)}{string(805, 470, 540, 660, 1.5)}
{stamp("주범!", 560, 650, 1.9, -12)}
{nar("물가 ↑ → <b>금리 인상 걱정</b> → '나중에 클 회사'인<br>AI·반도체주의 지금 몸값이 먼저 깎였어요", 80, 1060, 2.5, "font-size:36px")}
{ch(detective("happy", "point"), 790, 790, 220, 2.2, "a-sr", "squish")}
''', BG))

# 4 ── 한국 피해 조사
S[4] = (1, page(f'''
{head("한국 피해 조사", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#EDE7F6;--d:.05s">
  {ch(mascot("star", "teary"), 60, 120, 300, .3, "a-sl", "shiver")}
  {lower_third("조수 별콩이", "현장 보고", 380, 140, .5)}
  {bub("코스피도 <b>6거래일 연속</b><br>내렸대요…", 380, 240, .8, "t-left", style="font-size:42px")}
  <div class="num a-pop" style="left:120px;top:520px;--d:1.4s"><div class="k">코스피 (14일)</div><div class="v">▼0.44%</div></div>
  <div class="num a-pop" style="left:520px;top:520px;--d:1.7s"><div class="k">원/달러 (14일)</div><div class="v">1,338.3원</div></div>
  {ch(detective("normal", "point"), 60, 760, 280, 2.1, "a-sl", "squish2")}
  {bub("미국 반도체가 흔들려서<br>오늘 <b>한국 반도체</b>도 조심!", 360, 820, 2.5, "t-left", style="font-size:40px")}
</div>
''', BG))

# 5 ── 남은 수사 (체크) + 예고
S[5] = (1, page(f'''
{head("수사 노트", 5, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:700px;background:#FFFDF4;--d:.05s;background-image:repeating-linear-gradient(transparent 0 68px,#E4DCCB 68px 71px)">
  {nar("오늘 한국장 수사 노트 🔍", 30, 26, .3, "font-size:42px")}
  <div class="abs a-sl" style="left:50px;top:170px;--d:.7s;font-size:44px">☐ 반도체 — 미국 약세가 이어지나</div>
  <div class="abs a-sl" style="left:50px;top:310px;--d:1.1s;font-size:44px">☐ 환율 — 원/달러 1,338원대</div>
  <div class="abs a-sl" style="left:50px;top:450px;--d:1.5s;font-size:44px">☐ 기름값 — WTI <span style="color:#E03131">▲1.01%</span></div>
  <div class="abs a-fade" style="left:50px;top:620px;--d:1.9s;font-family:Noto Sans CJK KR,sans-serif;font-size:23px;color:#6B5A50">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게</div>
</div>
<div class="panel a-pop" style="left:44px;top:940px;width:982px;height:390px;background:#3A3150;--d:2.1s;color:#FFF6EA">
  {ch(detective("happy", "wave"), 690, 90, 250, 2.5, "a-sr", "hop")}
  <div class="abs a-rise" style="left:40px;top:44px;--d:2.4s;font-size:36px;color:#FFC08A">다음 사건 예고 (미국 시간 10/15)</div>
  <div class="abs a-rise" style="left:40px;top:110px;--d:2.6s;font-size:54px;line-height:1.25">PPI·소매판매<br>TSMC 실적</div>
  <div class="abs a-rise" style="left:40px;top:290px;--d:3.0s;font-size:40px">내일 아침 8시, <span style="color:#FFC08A">수사 계속!</span></div>
</div>
<div class="abs a-pop" style="left:0;right:0;top:1380px;--d:3.3s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};border-radius:999px;padding:12px 44px;font-size:46px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1480px;color:#CFC4E8;--d:3.4s">출처: AP, 연합뉴스, 뉴스핌, 서울경제, 미디어펜, CNBC · 정보 제공용이며 투자 권유가 아닙니다</div>
''', BG))

PLAN = {1: (5.0, 1.3), 2: (5.4, 1.4), 3: (6.2, 1.3), 4: (5.0, 1.4), 5: (4.8, 1.4)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .6), (1, .1, "whoosh", .5), (1, .4, "slidedown", .7), (1, .7, "whoosh", .6), (1, 1.3, "pop", .8),
 (2, .05, "whoosh", .5), (2, .2, "tick", 1), (2, .5, "shutter", 1), (2, 1.0, "shutter", 1), (2, 1.5, "shutter", 1), (2, 2.1, "boing", .6), (2, 2.5, "pop", .8),
 (3, .2, "pop", .7), (3, .6, "pop", .7), (3, 1.0, "tension", .7), (3, 1.3, "whoosh", .4), (3, 1.5, "whoosh", .4), (3, 1.9, "thud", 1), (3, 1.95, "reveal", .8), (3, 2.5, "ding", .9),
 (4, .3, "sad", .6), (4, .5, "tick", 1), (4, .8, "pop", .8), (4, 1.4, "blip_down", 1), (4, 1.7, "pop", .6), (4, 2.1, "whoosh", .5), (4, 2.5, "pop", .8),
 (5, .3, "tick", 1), (5, .7, "CHECK1", 1), (5, 1.1, "CHECK2", 1), (5, 1.5, "CHECK3", 1), (5, 2.5, "boing", .6), (5, 3.3, "jingle", .9),
]
