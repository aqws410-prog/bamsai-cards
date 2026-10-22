"""2026-10-23 릴스 · 뉴스 속보(news) — '결론 먼저' 훅. 메타 현금흐름 적자 전환에 'AI 돈줄 걱정'이 번져 나스닥·반도체가 급락한 날.
장면 1: 노란 속보 배너 + 초대형 하락 숫자 + 결론 한 줄 + 앵커 밤톨이 클로즈업(뉴스 데스크) + 'AI 돈줄 걱정' 도장 + 내려가는 차트 선.
숫자·사실은 posts/2026-10-23 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes linedraw{from{stroke-dashoffset:1400}to{stroke-dashoffset:0}}
@keyframes barup{from{transform:scaleY(.05)}to{transform:scaleY(1)}}
.dline{stroke-dasharray:1400;animation:linedraw .7s ease-out both}
.bar{transform-origin:50% 100%;animation:barup .6s cubic-bezier(.2,.9,.3,1) both}
</style>"""

def down_line(w, h, d):
    pts = (f"M0 {h*.18} L{w*.12} {h*.26} L{w*.22} {h*.16} L{w*.34} {h*.30} L{w*.44} {h*.26} L{w*.56} {h*.50} "
           f"L{w*.66} {h*.44} L{w*.78} {h*.70} L{w*.88} {h*.64} L{w} {h*.92}")
    return (f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<path class="dline" style="animation-delay:{d}s" d="{pts}" fill="none" stroke="#5AA9FF" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/></svg>')

# 1 ── 결론 먼저: 0초에 배너·숫자·결론·앵커가 모두 보임. 0~1초에 펀치·도장·차트 선·효과 글자
S[1] = (1, page(FX + f'''
{stars(14, 23, 0, 300)}
{head("밤사이 뉴스 · 10.23 FRI", 1, "#F6EEE4")}
{alert_banner("긴급 속보")}
<div class="abs" style="left:44px;top:304px;width:982px;text-align:center;font-size:50px;color:#FFD84D">22일 뉴욕 · 나스닥</div>
<div class="abs" style="left:0;width:1080px;top:368px;text-align:center"><span class="punch" style="font-size:222px;line-height:1;color:#5AA9FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼2.60%</span></div>
<div class="abs" style="left:44px;top:610px;width:982px;box-sizing:border-box;background:#FFFDF6;border:6px solid {L};border-radius:26px;box-shadow:0 8px 0 rgba(0,0,0,.25);text-align:center;padding:10px 10px 14px">
  <div style="font-size:84px;line-height:1.15"><span style="color:#C2410C">메타 현금 적자</span>에 AI주 급락</div>
</div>
<div class="panel" style="left:44px;top:790px;width:982px;height:560px;background:#3C4485;overflow:hidden">
  <div class="abs" style="left:470px;top:70px;width:470px;height:260px;background:#14202A;border:5px solid {L};border-radius:18px;overflow:hidden">
    <div class="abs" style="left:16px;top:10px;font-size:30px;color:#9FB7E0">AI·반도체주</div>
    <div class="abs" style="left:26px;top:56px;width:418px;height:180px">{down_line(418, 180, .6)}</div>
  </div>
  <div class="abs" style="left:{P}px;top:40px;width:400px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="squish">{mascot("bamtol", "surprised", "point")}</div></div>
  <div class="abs" style="left:0;right:0;top:440px;height:120px;background:#5B5FA8;border-top:6px solid {L};text-align:center;color:#FFE59A;font-size:46px;line-height:110px">🌙 밤사이 뉴스</div>
  <div class="live" style="right:{P}px;top:14px"><i></i>LIVE</div>
  {stamp("AI 돈줄 걱정", 500, 336, .35, -8)}
  {sfx("와르르", 560, 200, 80, .8, -8, "#FFD84D")}
</div>
{ticker("나스닥 ▼2.60% · S&P500 ▼1.21% · 필라델피아 반도체 ▼6.7% · 메타 3분기 현금흐름 마이너스 전환", 1380)}
''', "#262B55"))

# 2 ── 현장 연결 (솜부엉 기자): 매출은 늘었는데 현금흐름은 마이너스
bld = ''.join(f'<div class="abs" style="left:{x}px;bottom:150px;width:{w}px;height:{h}px;background:#3A4080;border:4px solid {L};border-radius:6px 6px 0 0"></div>'
              for x, w, h in [(30, 110, 260), (160, 90, 330), (270, 120, 220), (622, 120, 220), (772, 90, 330), (882, 70, 260)])
S[2] = (1, page(f'''
{head("현장 연결 · 실리콘밸리", 2, "#F6EEE4")}
{screen(f"""
  <div class="abs" style="left:0;right:0;bottom:0;height:200px;background:#2A2F5E"></div>
  {bld}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), 336, 250, 310, .3, "a-pop", "squish")}
  {cbub("메타 매출은 늘었는데<br><b>현금흐름은 마이너스</b>예요!", 40, .6, style="font-size:42px", width=982)}
  {stamp("적자 전환", 660, 400, 2.6, 8)}
""", 44, 200, 982, 660, .05, "● 메타 실적 현장")}
{lower_third("솜부엉 기자", "빅테크 실적 담당", 44 + P, 760, .5)}
<div class="panel a-pop" style="left:44px;top:900px;width:982px;height:430px;background:#FFF8E1;--d:1.4s">
  <div class="abs" style="left:{P}px;top:24px;font-size:36px">메타 3분기 성적표</div>
  {numbox("매출 (1년 전보다)", "▲26%", COL2[0], 90, 1.8, RED)}
  {numbox("잉여현금흐름", "마이너스", COL2[1], 90, 2.3, BLUE)}
  {nar("AI 투자 돈을 위해 <b>의결권 없는 주식</b>도 새로 낸대요", P, 300, 2.9, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
{ticker("메타 3분기 매출 1년 전보다 26% 증가 · 잉여현금흐름은 적자 전환", 1380, "현장")}
''', "#2B3060"))

# 3 ── 전문가 해설: 가계부로 보면 (들어온 돈 < 나간 돈)
def bar(label, sub, col, h, color, d):
    x, w = col
    return (f'<div class="abs" style="left:{x}px;top:{760 - h}px;width:{w}px;height:{h}px">'
            f'<div class="bar" style="width:100%;height:100%;box-sizing:border-box;background:{color};border:5px solid {L};border-radius:20px 20px 0 0;animation-delay:{d}s"></div></div>'
            f'<div class="abs a-fade" style="left:{x}px;top:776px;width:{w}px;text-align:center;font-size:40px;--d:{d}s">{label}</div>'
            f'<div class="abs a-fade" style="left:{x}px;top:828px;width:{w}px;text-align:center;font-size:30px;color:#6B5A50;--d:{d}s">{sub}</div>')
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#F3EEFF;--d:.05s">
  {ch(mascot("moon", "normal", "point"), P, 40, 260, .15, "a-sl", "squish")}
  {lower_third("달떡이 박사", "가계부 전문가", 330, 50, .3)}
  {bub("메타 가계부를<br>펼쳐 볼까요?", 330, 150, .4, "t-left", style="font-size:42px")}
  <div class="abs" style="left:{P}px;top:400px;width:{IW}px;height:360px;border-bottom:6px solid {L}"></div>
  {bar("들어온 돈", "광고로 번 돈", COL2[0], 250, "#8FD3A8", .9)}
  {bar("나간 돈", "AI 데이터센터 투자", COL2[1], 330, "#FF9A9A", 1.3)}
  {stamp("통장 마이너스!", 300, 470, 1.9, -6)}
  {nar("쓴 돈이 더 많으니 <b>“AI에 쓸 돈, 어디서 구하지?”</b>", P, 900, 2.4, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("필라델피아 반도체", "▼6.7%", COL2[0], 990, 3.0)}
  {numbox("나스닥", "▼2.60%", COL2[1], 990, 3.3)}
</div>
''', "#30366E"))

# 4 ── 시민 인터뷰 (한국)
mic = f'<svg viewBox="0 0 80 160" width="70"><rect x="22" y="4" width="36" height="56" rx="18" fill="#9AA3B8" stroke="{L}" stroke-width="5"/><rect x="34" y="60" width="12" height="90" rx="6" fill="#4A3838"/></svg>'
c0 = COL2[0][0] + COL2[0][1] // 2; c1 = COL2[1][0] + COL2[1][1] // 2
S[4] = (1, page(f'''
{head("한국은요?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#E2F6EA;--d:.05s">
  <div class="abs" style="left:0;right:0;top:700px;height:430px;background:#CBE9D6;border-top:5px solid {L}"></div>
  {bub("한국 주식은<br>괜찮을까요?", P, 50, .5, "t-down", f"{c0 - P - 15}px")}
  {bub("코스피는 22일에<br>이미 <span style='color:#2F6BD8'>▼3.52%</span> 빠졌어요", 0, 210, 1.2, "t-down", "60%", f"font-size:38px;left:auto;right:{P}px")}
  {ch(mascot("star", "worried"), c0 - 150, 400, 300, .2, "a-sl", "squish")}
  <div class="abs a-sr" style="left:{491 - 35}px;top:480px;--d:.4s;transform:rotate(-20deg)">{mic}</div>
  {ch(mascot("bamtol", "normal", "hold"), c1 - 150, 400, 300, .3, "a-sr", "squish2")}
  {lower_third("별콩이 씨", "초보 투자자", P, 730, .6)}
  {numbox("코스피 (22일)", "▼3.52%", COL2[0], 860, 1.8)}
  {numbox("한은 기준금리", "3.00% 동결", COL2[1], 860, 2.2, "#4A3838")}
  {nar("원/달러는 1,324.2원, 5거래일째 올해 최저", P, 1030, 2.7, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
{ticker("미국 반도체 급락 → 반도체 비중 큰 한국 증시에 부담 가능성", 1380, "한국")}
''', "#4A3E78"))

# 5 ── 클로징 체크 (복숭아빛)
items = [("chip", "반도체 충격, 이어질까?", "미국 반도체지수 ▼6.7%"),
         ("oil", "기름값 다시 들썩", "브렌트유 5개월 만에 최고"),
         ("won", "한은 동결, 그다음은?", "연 3.00% 동결 · 추가 인상 여지")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{1.0+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ICONS[k]}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (k, t, d) in enumerate(items))
S[5] = (1, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("클로징 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFF8E1;--d:.05s">
  {live(P, 34, "밤사이 뉴스", .1)}
  {ch(mascot("bamtol", "normal", "point"), 600, 120, 290, .15, "a-sr", "squish")}
  {desk(520, 360, 422)}
  {bub("오늘 한국장은<br>딱 <b>세 가지</b>만 보세요!", P, 150, .35, "t-right", style="font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.2s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 서울경제, 한국경제, 뉴스1, SBS Biz</div>
{ticker("다음 주 27~28일 미국 연준 FOMC · 오늘 밤 미국장 한 주 마감", 1380, "예고")}
''', "#FFE1CC"))

# 6 ── 예고·사인오프 (아침)
S[6] = (1, page(f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 주 (미국 시간 10/27~28)</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:66px;line-height:1.2">미국 연준 FOMC<br>금리 결정</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">이번 주 마감은 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), P, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 210, 290, .4, "a-sr", "hop")}
  {bub("이상, <b>밤사이 뉴스</b>였습니다!", 380, 40, .65, "t-down", "380px", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 서울경제, 한국경제, 뉴스1, SBS Biz · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.4, 1.2), 2: (4.4, 1.6), 3: (4.6, 1.6), 4: (3.9, 1.6), 5: (3.6, 1.6), 6: (2.8, 1.2)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .9), (1, .05, "thud", .8), (1, .35, "thud", 1), (1, .6, "slidedown", .7), (1, .8, "boing", .6),
 (2, .05, "whoosh", .6), (2, .3, "pop", .6), (2, .5, "tick", .9), (2, .6, "pop", .9), (2, 1.4, "whoosh", .5), (2, 1.8, "ding", .7), (2, 2.3, "blip_down", 1), (2, 2.6, "thud", .9), (2, 2.9, "tick", .8),
 (3, .15, "whoosh", .6), (3, .3, "tick", .9), (3, .4, "pop", .8), (3, .9, "boing", .6), (3, 1.3, "boing", .7), (3, 1.9, "thud", 1), (3, 2.4, "hmm", .8), (3, 3.0, "blip_down", 1), (3, 3.3, "blip_down", .8),
 (4, .2, "whoosh", .6), (4, .5, "question", .9), (4, .6, "tick", .8), (4, 1.2, "pop", .8), (4, 1.8, "blip_down", 1), (4, 2.2, "pop", .7), (4, 2.7, "tick", .8),
 (5, .05, "news", .5), (5, .15, "whoosh", .5), (5, .35, "pop", .8), (5, 1.0, "CHECK1", 1), (5, 1.45, "CHECK2", 1), (5, 1.9, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
