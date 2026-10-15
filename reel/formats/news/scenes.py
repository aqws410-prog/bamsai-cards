"""형식: 밤사이 뉴스 속보 (2026-10-15 사용자 검수 완료 — 훅·정렬·템포의 기준) — 밤톨이 앵커, 솜부엉 현장 기자, 달떡이 전문가, 별콩이 시민 인터뷰.
예시 내용: 2026-10-15 (미국 9월 CPI, 나스닥 ▼1.88%). 새 날짜에는 구조만 참고하고 장면·배치·대사는 그날 이야기에 맞게 새로 짠다.
"""
from lib import *

S = {}

# 1 ── 긴급 속보 (훅) — 첫 프레임부터 배너·질문·앵커가 모두 보인다
S[1] = (1, page(f'''
{stars(22, 21, 0, 600)}
{head("밤사이 뉴스 · 10.15 THU", 1, "#F6EEE4")}
{alert_banner("긴급 속보")}
<div class="abs hook" style="left:44px;top:330px;font-size:80px;color:#F6EEE4">겨우 0.1%p 때문에</div>
<div class="abs hook" style="left:44px;top:430px;font-size:118px;color:#FFC08A">나스닥 <span style="color:#7DBBFF">▼1.88%</span>?!</div>
<div class="panel" style="left:44px;top:640px;width:982px;height:700px;background:#3C4485;overflow:hidden">
  <div class="abs" style="left:{P}px;top:60px;width:540px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="squish">{mascot("bamtol", "surprised", "point")}</div></div>
  <div class="abs" style="left:0;right:0;top:560px;height:140px;background:#5B5FA8;border-top:6px solid {L};text-align:center;color:#FFE59A;font-size:50px;line-height:130px">🌙 밤사이 뉴스</div>
  <div class="live" style="right:{P}px;top:26px"><i></i>LIVE</div>
  {bub("<span style='font-size:52px'>긴급 속보입니다!</span><br>어젯밤 <b>나스닥이 1.88%</b><br>떨어졌습니다", 560, 110, .2, "t-left", style="font-size:40px;padding:22px 30px")}
</div>
{ticker("미국 9월 소비자물가 3.7% · 예상 3.6% 웃돌아 · 나스닥 ▼1.88% · S&P500 ▼1.11% · 다우 ▼0.09%", 1380)}
''', "#262B55"))

# 2 ── 현장 연결 (솜부엉 기자)
bld = ''.join(f'<div class="abs" style="left:{x}px;bottom:200px;width:{w}px;height:{h}px;background:#3A4080;border:4px solid {L};border-radius:6px 6px 0 0"></div>'
              for x, w, h in [(30, 110, 300), (160, 90, 380), (270, 130, 250), (612, 130, 250), (762, 90, 380), (872, 110, 300)])
S[2] = (1, page(f'''
{head("현장 연결 · 뉴욕", 2, "#F6EEE4")}
{screen(f"""
  <div class="abs" style="left:0;right:0;bottom:0;height:260px;background:#2A2F5E"></div>
  {bld}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), 326, 300, 330, .5, "a-pop", "squish")}
  {cbub("미국 물가 성적표(CPI)가<br><b>3.7%</b>! 예상 3.6%보다 뜨거워요", 70, 1.1, style="font-size:38px", width=968)}
""", 44, 200, 982, 760, .1, "● 월가 현장")}
{lower_third("솜부엉 기자", "뉴욕 월가", 44 + P, 860, .7)}
<div class="panel a-pop" style="left:44px;top:1000px;width:982px;height:330px;background:#FFF8E1;--d:1.9s">
  <div class="abs" style="left:{P}px;top:30px;font-size:36px">미국 9월 소비자물가 (1년 전보다)</div>
  <div class="abs a-pop" style="left:{P}px;top:100px;--d:2.3s;width:380px;height:180px;box-sizing:border-box;background:#fff;border:4px solid {L};border-radius:24px;text-align:center">
     <div style="font-size:32px;margin-top:16px">시장 예상</div><div style="font-size:84px">3.6%</div></div>
  <div class="abs a-fade" style="left:{P + 380}px;top:150px;width:142px;text-align:center;font-size:70px;--d:2.6s">→</div>
  <div class="abs a-stamp" style="left:{P + 380 + 142}px;top:100px;--d:2.8s;--r:0deg;width:380px;height:180px;box-sizing:border-box;background:#FFE3E3;border:4px solid {L};border-radius:24px;text-align:center">
     <div style="font-size:32px;margin-top:16px">실제 발표</div><div style="font-size:84px;color:#E03131">3.7%</div></div>
</div>
{ticker("근원 소비자물가도 2.6%로 예상(2.5%) 웃돌아 · 미 국채 금리 상승", 1380, "현장")}
''', "#2B3060"))

# 3 ── 전문가 해설 (1분 공부)
def stepbox(icon, t, col, d):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:480px;width:{w}px;height:200px;box-sizing:border-box;--d:{d}s;background:#fff;border:4px solid {L};border-radius:26px;text-align:center;padding:16px 8px">'
            f'<div style="font-size:70px;line-height:1.1">{icon}</div><div style="font-size:34px;line-height:1.3">{t}</div></div>')
def arrow(after, d):
    x0 = after[0] + after[1]
    return f'<div class="abs a-fade" style="left:{x0}px;top:540px;width:76px;text-align:center;font-size:60px;--d:{d}s">→</div>'
S[3] = (1, page(f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#F3EEFF;--d:.05s">
  {ch(mascot("moon", "normal", "point"), P, 60, 300, .25, "a-sl", "squish")}
  {lower_third("달떡이 박사", "금리 전문가", 380, 70, .4)}
  {bub("물가가 뜨거우면<br>미국 중앙은행이 <b>금리</b>를<br>올릴 수도 있어요", 380, 170, .7, "t-left", style="font-size:40px")}
  {stepbox("🌡️", "물가<br>예상보다 ↑", COL3[0], 1.4)}
  {arrow(COL3[0], 1.7)}
  {stepbox("🏦", "금리 인상<br>걱정 ↑", COL3[1], 1.8)}
  {arrow(COL3[1], 2.1)}
  {stepbox("🚀", "먼 미래 기대주<br>(AI·반도체) ↓", COL3[2], 2.2)}
  {nar("금리가 오르면 '나중에 클 회사'의 지금 몸값이 <b>먼저 깎여요</b>", P, 730, 2.9, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("다우", "▼0.09%", COL2[0], 880, 3.4)}
  {numbox("나스닥 (기술주 많음)", "▼1.88%", COL2[1], 880, 3.7)}
</div>
''', "#30366E"))

# 4 ── 시민 인터뷰 (한국)
mic = f'<svg viewBox="0 0 80 160" width="70"><rect x="22" y="4" width="36" height="56" rx="18" fill="#9AA3B8" stroke="{L}" stroke-width="5"/><rect x="34" y="60" width="12" height="90" rx="6" fill="#4A3838"/></svg>'
c0 = COL2[0][0] + COL2[0][1] // 2; c1 = COL2[1][0] + COL2[1][1] // 2   # 두 칸의 가운데
S[4] = (1, page(f'''
{head("한국은요?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#E2F6EA;--d:.05s">
  <div class="abs" style="left:0;right:0;top:760px;height:370px;background:#CBE9D6;border-top:5px solid {L}"></div>
  {bub("그럼 한국 주식은요?<br>어제도 빠졌던데…", P, 60, .9, "t-down", f"{c0 - P - 15}px")}
  {bub("코스피는 <b>6거래일 연속</b><br>내렸어요", 0, 220, 1.7, "t-down", "60%", f"font-size:38px;left:auto;right:{P}px")}
  {ch(mascot("star", "worried"), c0 - 150, 430, 300, .3, "a-sl", "squish")}
  <div class="abs a-sr" style="left:{491 - 35}px;top:520px;--d:.5s;transform:rotate(-20deg)">{mic}</div>
  {ch(mascot("bamtol", "normal", "hold"), c1 - 150, 430, 300, .4, "a-sr", "squish2")}
  {lower_third("별콩이 씨", "초보 투자자", P, 790, .7)}
  {numbox("원/달러 (14일)", "1,338.3원", COL2[0], 900, 2.7)}
  {numbox("코스피 (14일)", "▼0.44%", COL2[1], 900, 2.4)}
</div>
{ticker("미국 AI·반도체주 약세 → 한국 반도체에도 부담 가능성", 1380, "한국")}
''', "#4A3E78"))

# 5 ── 오늘 체크 (복숭아빛)
items = [("chip", "반도체가 다시 힘낼까?", "미국 AI·반도체 약세가 이어지는지"),
         ("won", "외국인이 돌아올까?", "원/달러 1,338원대 · 외국인 수급"),
         ("oil", "기름값은?", "WTI 95.09달러 <span style='color:#C92A2A'>▲1.01%</span>")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{1.3+i*.5:.1f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ICONS[k]}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (k, t, d) in enumerate(items))
S[5] = (1, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("클로징 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFF8E1;--d:.05s">
  {live(40, 34, "밤사이 뉴스", .1)}
  {ch(mascot("bamtol", "normal", "point"), 600, 120, 290, .2, "a-sr", "squish")}
  {desk(520, 360, 440)}
  {bub("오늘 한국장은<br>딱 <b>세 가지</b>만 보세요!", 40, 150, .5, "t-right", style="font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 파이낸셜뉴스, 이투데이, 서울경제</div>
{ticker("오늘 밤(미국 시간) 생산자물가(PPI)·소매판매·TSMC 실적 발표", 1380, "예고")}
''', "#FFE1CC"))

# 6 ── 예고·사인오프 (아침)
S[6] = (1, page(f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">오늘 밤 (미국 시간 10/15)</div>
  <div class="abs" style="left:44px;top:100px;font-size:66px;line-height:1.2">생산자물가(PPI)<br>소매판매 · TSMC 실적</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.35s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.2s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .35, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .45, "a-sr", "hop")}
  {bub("이상, <b>밤사이 뉴스</b>였습니다!", 380, 40, .75, "t-down", "380px", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.1s">출처: AP, 연합뉴스, 뉴스핌, 서울경제, 아시아경제 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.8, 1.3), 2: (4.0, 1.6), 3: (4.6, 1.6), 4: (3.9, 1.7), 5: (4.2, 1.7), 6: (3.2, 1.2)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .9), (1, .02, "whoosh", .4), (1, .2, "pop", .9), (1, .25, "tick", .8), (1, .7, "slidedown", .5),
 (2, .1, "whoosh", .6), (2, .5, "pop", .6), (2, .7, "tick", 1), (2, 1.1, "pop", .8), (2, 1.9, "whoosh", .5), (2, 2.3, "pop", .6), (2, 2.8, "thud", .8),
 (3, .25, "whoosh", .6), (3, .4, "tick", 1), (3, .7, "pop", .8), (3, 1.4, "pop", .6), (3, 1.8, "pop", .6), (3, 2.2, "pop", .6), (3, 2.9, "ding", .9), (3, 3.4, "blip_down", 1), (3, 3.7, "blip_down", .7),
 (4, .3, "whoosh", .6), (4, .7, "tick", 1), (4, .9, "question", .9), (4, 1.7, "pop", .8), (4, 2.4, "blip_down", 1), (4, 2.7, "pop", .6),
 (5, .05, "news", .5), (5, .2, "whoosh", .5), (5, .5, "pop", .8), (5, 1.3, "CHECK1", 1), (5, 1.8, "CHECK2", 1), (5, 2.3, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .35, "whoosh", .5), (6, .45, "boing", .7), (6, .75, "pop", .8), (6, .9, "news", .6), (6, 1.0, "jingle", .9),
]
