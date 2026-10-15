"""형식: 밤사이 뉴스 속보 — 밤톨이 앵커, 솜부엉 현장 기자, 달떡이 전문가, 별콩이 시민 인터뷰.
예시 내용: 2026-10-15 (미국 9월 CPI, 나스닥 ▼1.88%). 새 날짜에는 구조만 참고하고 장면·배치·대사는 그날 이야기에 맞게 새로 짠다.
"""
from lib import *

S = {}
NAVY = "#2B2F63"

# 1 ── 속보 오프닝 (훅)
S[1] = (1, page(f'''
{stars(18, 21, 0, 500)}
{head("밤사이 뉴스 · 10.15 THU", 1, "#F6EEE4")}
{live(44, 186, "LIVE · 속보")}
{big("물가 0.1%p 차이에", 44, 262, 66, 0, "#F6EEE4", "")}
{big("나스닥 <span style='color:#7DBBFF'>▼1.88%</span>?!", 44, 344, 92, 0, "#FFC08A", "")}
<div class="panel a-pop" style="left:44px;top:520px;width:982px;height:820px;background:#3C4485;--d:.15s">
  <div class="abs" style="left:0;right:0;top:0;height:520px;background:linear-gradient(#4B529A,#3C4485)"></div>
  <div class="abs" style="left:620px;top:60px;width:300px;height:200px;background:#1F2347;border:5px solid {L};border-radius:18px;overflow:hidden">
     <svg viewBox="0 0 300 200" width="290" height="190"><path d="M20 50 L90 60 L140 90 L190 130 L240 150 L280 175" fill="none" stroke="#7DBBFF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" style="stroke-dasharray:360;--len:360;animation:draw 1s ease-in both;animation-delay:.5s"/></svg>
     <div class="abs" style="left:14px;top:8px;font-size:26px;color:#FFE59A">나스닥</div>
  </div>
  {ch(mascot("bamtol", "normal", "point"), 300, 240, 320, .3, "a-pop", "squish")}
  {desk(150, 600, 680)}
  {bub("밤사이 뉴스입니다!<br>어젯밤 월가에 <b>찬바람</b>이 불었어요", 40, 60, .9, "t-down", "380px", "font-size:38px")}
</div>
{ticker("미국 9월 소비자물가 3.7% · 예상 3.6% 웃돌아 · 나스닥 ▼1.88% · S&P500 ▼1.11% · 다우 ▼0.09%", 1380)}
''', "#262B55"))

# 2 ── 현장 연결 (솜부엉 기자)
S[2] = (1, page(f'''
{head("현장 연결 · 뉴욕", 2, "#F6EEE4")}
{screen(f"""
  <div class="abs" style="left:0;right:0;bottom:0;height:260px;background:#2A2F5E"></div>
  {''.join(f'<div class="abs" style="left:{x}px;bottom:200px;width:{w}px;height:{h}px;background:#3A4080;border:4px solid {L};border-radius:6px 6px 0 0"></div>' for x,w,h in [(30,110,300),(160,90,380),(270,130,250),(620,120,340),(760,100,420),(880,80,260)])}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), 330, 300, 330, .5, "a-pop", "squish")}
""", 44, 200, 982, 760, .1, "● 월가 현장")}
{lower_third("솜부엉 기자", "뉴욕 월가", 80, 860, .7)}
{bub("미국 물가 성적표(CPI)가<br><b>3.7%</b>! 예상 3.6%보다 뜨거워요", 300, 250, 1.1, "t-down", "200px", "font-size:38px")}
<div class="panel a-pop" style="left:44px;top:1000px;width:982px;height:330px;background:#FFF8E1;--d:1.9s">
  <div class="abs" style="left:40px;top:34px;font-size:36px">미국 9월 소비자물가 (1년 전보다)</div>
  <div class="abs a-pop" style="left:40px;top:110px;--d:2.3s;width:400px;height:170px;background:#fff;border:4px solid {L};border-radius:24px;text-align:center">
     <div style="font-size:32px;margin-top:16px">시장 예상</div><div style="font-size:84px">3.6%</div></div>
  <div class="abs a-fade" style="left:470px;top:160px;font-size:70px;--d:2.6s">→</div>
  <div class="abs a-stamp" style="left:560px;top:110px;--d:2.8s;--r:0deg;width:380px;height:170px;background:#FFE3E3;border:4px solid {L};border-radius:24px;text-align:center">
     <div style="font-size:32px;margin-top:16px">실제 발표</div><div style="font-size:84px;color:#E03131">3.7%</div></div>
</div>
{ticker("근원 소비자물가도 2.6%로 예상(2.5%) 웃돌아 · 미 국채 금리 상승", 1380, "현장")}
''', "#262B55"))

# 3 ── 전문가 해설 (1분 공부)
def stepbox(icon, t, x, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:640px;width:270px;--d:{d}s;background:#fff;border:4px solid {L};border-radius:26px;text-align:center;padding:16px 8px">'
            f'<div style="font-size:70px;line-height:1.1">{icon}</div><div style="font-size:34px;line-height:1.3">{t}</div></div>')
S[3] = (1, page(f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#F3EEFF;--d:.05s">
  {ch(mascot("moon", "normal", "point"), 40, 60, 300, .25, "a-sl", "squish")}
  {lower_third("달떡이 박사", "금리 전문가", 350, 80, .4)}
  {bub("물가가 뜨거우면<br>미국 중앙은행이 <b>금리</b>를<br>올릴 수도 있어요", 350, 170, .7, "t-left", style="font-size:40px")}
  {stepbox("🌡️", "물가<br>예상보다 ↑", 30, 1.4)}
  <div class="abs a-fade" style="left:310px;top:700px;font-size:64px;--d:1.7s">→</div>
  {stepbox("🏦", "금리 인상<br>걱정 ↑", 356, 1.8)}
  <div class="abs a-fade" style="left:636px;top:700px;font-size:64px;--d:2.1s">→</div>
  {stepbox("🚀", "먼 미래 기대주<br>(AI·반도체) ↓", 680, 2.2)}
  {nar("금리가 오르면 '나중에 클 회사'의<br>지금 몸값이 <b>먼저 깎여요</b>", 30, 900, 2.9, "font-size:40px")}
  <div class="num a-pop" style="left:560px;top:1050px;--d:3.4s"><div class="k">나스닥 (기술주 많음)</div><div class="v">▼1.88%</div></div>
  <div class="num a-pop" style="left:200px;top:1050px;--d:3.7s"><div class="k">다우</div><div class="v">▼0.09%</div></div>
</div>
''', "#30366E"))

# 4 ── 시민 인터뷰 (한국)
mic = f'<svg viewBox="0 0 80 160" width="70"><rect x="22" y="4" width="36" height="56" rx="18" fill="#9AA3B8" stroke="{L}" stroke-width="5"/><rect x="34" y="60" width="12" height="90" rx="6" fill="#4A3838"/></svg>'
S[4] = (1, page(f'''
{head("한국은요?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#E2F6EA;--d:.05s">
  <div class="abs" style="left:0;right:0;top:760px;height:370px;background:#CBE9D6;border-top:5px solid {L}"></div>
  {ch(mascot("star", "worried"), 70, 420, 320, .3, "a-sl", "squish")}
  <div class="abs a-sr" style="left:420px;top:520px;--d:.5s;transform:rotate(-20deg)">{mic}</div>
  {ch(mascot("bamtol", "normal", "hold"), 560, 420, 320, .4, "a-sr", "squish2")}
  {lower_third("별콩이 씨", "초보 투자자", 60, 860, .7)}
  {bub("그럼 한국 주식은요?<br>어제도 빠졌던데…", 40, 60, .9, "t-down", "200px")}
  {bub("코스피는 <b>6거래일 연속</b><br>내렸어요", 520, 210, 1.7, "t-down", "200px", "font-size:38px")}
  <div class="num a-pop" style="left:520px;top:960px;--d:2.4s"><div class="k">코스피 (14일)</div><div class="v">▼0.44%</div></div>
  <div class="num a-pop" style="left:120px;top:960px;--d:2.7s"><div class="k">원/달러 (14일)</div><div class="v">1,338.3원</div></div>
</div>
{ticker("미국 AI·반도체주 약세 → 한국 반도체에도 부담 가능성", 1380, "한국")}
''', "#4A3E78"))

# 5 ── 클로징
items = [("chip", "반도체", "미국 AI·반도체 약세가 이어지는지"), ("won", "환율", "원/달러 1,338원대, 외국인 수급"), ("oil", "기름값", "WTI 95.09달러 ▲1.01%")]
rows = "".join(
    f'<div class="abs a-sl" style="left:30px;top:{150+i*150}px;width:922px;--d:{.8+i*.4:.1f}s;display:flex;align-items:center;gap:20px">'
    f'<div style="flex:none">{ICONS[k]}</div><div style="font-size:46px;flex:none;width:170px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50">{s}</div></div>'
    for i, (k, t, s) in enumerate(items))
S[5] = (1, page(f'''
{head("클로징", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:640px;background:#fff;--d:.05s">
  {nar("오늘 한국장, 이 세 가지만 체크!", 30, 30, .3, "font-size:42px")}
  {rows}
  <div class="abs a-fade" style="left:30px;top:590px;--d:2.2s;font-family:Noto Sans CJK KR,sans-serif;font-size:23px;color:#6B5A50">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게</div>
</div>
<div class="panel a-pop" style="left:44px;top:880px;width:982px;height:450px;background:#3A3460;--d:2.4s;color:#FFF6EA">
  {ch(mascot("bamtol", "happy", "wave"), 660, 140, 280, 2.8, "a-sr", "hop")}
  <div class="abs a-rise" style="left:40px;top:40px;--d:2.7s;font-size:36px;color:#FFC08A">오늘 밤 (미국 시간 10/15)</div>
  <div class="abs a-rise" style="left:40px;top:100px;--d:2.9s;font-size:56px;line-height:1.25">생산자물가(PPI)·소매판매<br>TSMC 실적</div>
  <div class="abs a-rise" style="left:40px;top:300px;--d:3.3s;font-size:42px">이상, <span style="color:#FFC08A">밤사이 뉴스</span>였습니다!</div>
</div>
<div class="abs a-pop" style="left:0;right:0;top:1380px;--d:3.6s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};border-radius:999px;padding:12px 44px;font-size:46px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1480px;color:#6B5A50;--d:3.7s">출처: AP, 연합뉴스, 뉴스핌, 서울경제, 아시아경제, 파이낸셜뉴스 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (5.0, 1.2), 2: (5.6, 1.3), 3: (6.0, 1.3), 4: (5.0, 1.4), 5: (5.4, 1.4)}
CUES = [
 (1, .0, "news", 1), (1, .0, "dundun", .6), (1, .15, "whoosh", .5), (1, .3, "boing", .6), (1, .5, "slidedown", .6), (1, .9, "pop", .8),
 (2, .1, "whoosh", .6), (2, .5, "pop", .6), (2, .7, "tick", 1), (2, 1.1, "pop", .8), (2, 1.9, "whoosh", .5), (2, 2.3, "pop", .6), (2, 2.8, "thud", .8),
 (3, .25, "whoosh", .6), (3, .4, "tick", 1), (3, .7, "pop", .8), (3, 1.4, "pop", .6), (3, 1.8, "pop", .6), (3, 2.2, "pop", .6), (3, 2.9, "ding", .9), (3, 3.4, "blip_down", 1), (3, 3.7, "blip_down", .7),
 (4, .3, "whoosh", .6), (4, .7, "tick", 1), (4, .9, "question", .9), (4, 1.7, "pop", .8), (4, 2.4, "blip_down", 1), (4, 2.7, "pop", .6),
 (5, .3, "tick", 1), (5, .8, "CHECK1", 1), (5, 1.2, "CHECK2", 1), (5, 1.6, "CHECK3", 1), (5, 2.4, "whoosh", .5), (5, 2.8, "boing", .7), (5, 3.3, "news", .6), (5, 3.6, "jingle", .8),
]
