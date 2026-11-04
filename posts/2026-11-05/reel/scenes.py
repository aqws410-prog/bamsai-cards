"""2026-11-05 릴스 · 뉴스 속보(news) v3 — '결론 먼저' 훅, 장면 1 '선거 개표 상황판(의석 막대 + 당선 확정 도장)' 새 구도 (검수 전).
그날 상황: 미국 중간선거 민주당 상·하원 장악 → 다우 ▲3.03%·유가 ▼8%대 급변, 반도체만 ▼3.13% → 첫 칸(큰 이벤트·급변) 1순위 news
          (같은 칸 직전 10-31이 2순위 talkshow라 1순위 차례, 최근 3일 chat·detective·delivery 미사용).
흐름: 1 결론(▼3.13% '다우는 뛰고, 반도체는 뚝!', 개표 상황판) → 2 개표 결과 속보(민주당 상·하원 + 3대 지수) → 3 1분 해설(줄다리기 = 교착 · 유가 ▼8.7%)
      → 4 반도체는 왜?(데이터센터 공사장 '허가 먼저' 표지판 → 한국 반도체 부담, 코스피 4일) → 5 오늘 체크 3 → 6 예고(고용보고서, 토요일 아침).
숫자·사실은 posts/2026-11-05 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes fillbar{from{width:0}to{width:var(--w)}}
.fill{animation:fillbar .5s cubic-bezier(.2,.9,.3,1) both;animation-delay:var(--d,0s)}
@keyframes tug{0%,100%{transform:translateX(-10px)}50%{transform:translateX(10px)}}
.tug{animation:tug .5s ease-in-out infinite}
@keyframes sway{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
.sway{transform-origin:50% 100%;animation:sway .6s ease-in-out infinite}
@keyframes blink2{0%,49%{opacity:1}50%,100%{opacity:.35}}
.blink2{animation:blink2 .5s steps(1) infinite}
</style>"""

def seatbar(name, y, d, w=560):
    # 개표 상황판 한 줄: 의회 이름 + 채워지는 막대 + '민주 승' 도장 (막대 색은 정당 표시용 보라 — 등락 색과 겹치지 않게)
    return (f'<div class="abs" style="left:{P}px;top:{y}px;width:{IW}px;height:110px">'
            f'<div class="abs" style="left:0;top:20px;font-size:52px;color:#FFF6EA">{name}</div>'
            f'<div class="abs" style="left:150px;top:22px;width:{w}px;height:66px;background:#1B2040;border:5px solid {L};border-radius:16px;overflow:hidden">'
            f'<div class="fill" style="--w:{int(w*.62)}px;--d:{d}s;height:100%;background:#8C7CF0"></div>'
            f'<div class="abs" style="left:{int(w*.5)}px;top:0;bottom:0;border-left:5px dashed #FFE36E"></div></div>'
            f'<div class="stamp a-stamp" style="left:730px;top:12px;--d:{d+.25:.2f}s;--r:-10deg;font-size:44px;white-space:nowrap">민주 승</div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·상황판·밤톨이(클로즈업, 놀람)가 모두 보인다
#      0~1초: 숫자 펀치(0) → 막대 채워짐(0~.7) → '민주 승' 도장 쾅(.25/.45) → '뚝!' 효과 글자(.7) → 밤톨이 떨림(.6~)
S[1] = (1, page(FX + f'''
{stars(14, 51, 0, 180)}
{head("밤사이 뉴스 · 11.5 THU", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:190px;text-align:center;font-size:44px;color:#C9D6FF">민주당 압승의 밤 · 미국 반도체지수</div>
<div class="abs" style="left:0;width:1080px;top:248px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#5AA9FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼3.13%</span></div>
<div class="abs" style="left:0;width:1080px;top:494px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">다우는 뛰고, <span style="color:#FFE36E">반도체는 뚝!</span></div>
<div class="panel" style="left:44px;top:640px;width:982px;height:760px;background:#2E3466">
  <div class="abs" style="left:{P}px;top:24px;background:#FFD84D;border:4px solid {L};border-radius:12px;padding:2px 22px;font-size:38px">🗳 개표 상황판 · 미국 중간선거</div>
  <div class="live" style="right:{P}px;top:28px"><i></i>LIVE</div>
  {seatbar("상원", 110, .0)}
  {seatbar("하원", 230, .2)}
  <div class="abs" style="left:-20px;top:330px;width:460px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.6s">{mascot("bamtol", "surprised", "point")}</div></div>
  <div class="abs" style="left:470px;top:400px;width:472px;height:250px;box-sizing:border-box;background:#0B1220;border:5px solid {L};border-radius:22px;padding:18px 26px;font-size:46px;line-height:1.5;color:#F6EEE4">
    <div>다우 <span style="color:#FF6B6F">▲3.03%</span></div><div>반도체 <span class="blink2" style="color:#5AA9FF">▼3.13%</span></div><div style="font-size:34px;color:#9FB7E0">11.4 현지 마감</div></div>
  {sfx("뚝!", 330, 560, 110, .7, 10, "#5AA9FF")}
</div>
''', "#262B55"))

# 2 ── 개표 결과 속보: 민주당 상·하원 모두 장악 → 3대 지수 동반 상승
S[2] = (1, page(FX + f'''
{head("개표 결과 속보", 2, "#F6EEE4")}
{alert_banner("개표 결과", 196)}
<div class="panel a-pop" style="left:44px;top:330px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:76px;line-height:1.2"><span class="punch" style="--d:.15s">민주당, <span style="color:#6A4FD8">상·하원</span> 모두 장악</span></div>
  {cbub("의회는 민주당, 백악관은 공화당<br><b>'분점정부'</b>가 돼요", 170, .5, "t-down", style="font-size:44px")}
  {numbox("다우", "▲3.03%", COL3[0], 400, 1.0, RED)}
  {numbox("S&P500", "▲1.58%", COL3[1], 400, 1.2, RED)}
  {numbox("나스닥", "▲1.44%", COL3[2], 400, 1.4, RED)}
  {ch(mascot("owl", "happy", "hold", p_tablet()), P, 600, 300, 1.7, "a-sl", "squish")}
  {bub("선거 불확실성이<br><b>걷혔대요!</b>", 380, 680, 1.9, "t-left", style="font-size:46px")}
  {lower_third("솜부엉 기자", "뉴욕 월가", 400, 900, 2.0)}
</div>
''', "#2B3060"))

# 3 ── 1분 해설: 줄다리기(교착) + 유가 급락
rope = f'<div class="abs tug" style="left:180px;top:420px;width:622px;height:16px;background:#B57D55;border:4px solid {L};border-radius:8px"><div class="abs" style="left:290px;top:-30px;width:20px;height:70px;background:#E8590C;border:3px solid {L};border-radius:6px"></div></div>'
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  <div class="abs" style="left:{P}px;top:30px;font-size:44px">🎙 달떡이 박사의 1분 해설</div>
  {cbub("양쪽이 팽팽한 <b>줄다리기</b>!<br>줄이 크게 안 움직여요", 110, .2, "t-down", style="font-size:46px")}
  <div class="abs a-fade" style="left:{P}px;top:340px;--d:.5s;font-size:40px;color:#6A4FD8">의회(민주)</div>
  <div class="abs a-fade" style="right:{P}px;top:340px;--d:.5s;font-size:40px;color:#C2410C">백악관(공화)</div>
  {rope}
  {ch(mascot("star", "happy", "up"), P, 400, 170, .6, "a-sl", "squish")}
  {ch(mascot("moon", "normal", "up"), 772, 400, 170, .7, "a-sr", "squish2")}
  {nar("큰 정책 변화가 어려워 → 시장은 <b>'교착'을 호재로</b>", P, 640, 1.2, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  <div class="abs a-pop" style="left:{P}px;top:780px;--d:1.8s;width:{IW}px;height:330px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:26px;text-align:center;padding-top:20px">
    <div style="font-size:42px">🛢 이란 전쟁 끝날 거란 기대에 · 브렌트유</div>
    <div style="font-size:150px;line-height:1.1"><span class="thump" style="--d:2.0s;color:{BLUE};-webkit-text-stroke:5px {L};paint-order:stroke fill">▼8.7%</span></div>
    <div style="font-size:40px;color:#6B5A50">94.62달러로 마감</div></div>
</div>
''', "#30366E"))

# 4 ── 반도체는 왜? 데이터센터 공사장 '허가 먼저' 표지판 → 한국 반도체 부담
SIGN = (f'<svg viewBox="0 0 300 260" width="300" height="260"><rect x="140" y="120" width="20" height="135" fill="#8A6A4A" stroke="{L}" stroke-width="5"/>'
        f'<rect x="10" y="10" width="280" height="130" rx="14" fill="#FFD84D" stroke="{L}" stroke-width="6"/>'
        f'<text x="150" y="65" text-anchor="middle" font-size="40" font-family="Jua" fill="{L}">🚧 공사 규제</text>'
        f'<text x="150" y="115" text-anchor="middle" font-size="36" font-family="Jua" fill="{L}">강해질까?</text></svg>')
S[4] = (1, page(FX + f'''
{head("반도체는 왜?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E9F1FF;--d:0s">
  <div class="abs" style="left:{P}px;top:30px;font-size:44px">🏗 AI 공장(데이터센터) 공사장</div>
  <div class="abs a-drop sway" style="left:{P}px;top:100px;--d:.1s">{SIGN}</div>
  {bub("공장을 덜 지으면<br><b>칩 주문</b>도 줄까 걱정!", 380, 130, .5, "t-left", style="font-size:44px")}
  <div class="abs" style="left:0;right:0;top:400px;text-align:center"><div style="font-size:42px;color:#6B5A50">미국 필라델피아 반도체지수</div>
    <div style="font-size:170px;line-height:1.05"><span class="thump" style="--d:.9s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼3.13%</span></div></div>
  {cbub("반도체 비중이 큰 <b>한국 증시엔 부담</b>", 660, 1.3, "t-down", style="font-size:44px")}
  {numbox("코스피 (4일)", "▲0.62%", COL2[0], 820, 1.7, RED)}
  {numbox("삼성전자 (4일)", "▼0.68%", COL2[1], 820, 1.9, BLUE)}
  {nar("4일 코스피는 장중 약 4% 밀렸다가 반등", P, 1020, 2.2, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
''', "#4A3E78"))

# 5 ── 오늘 체크 3
checks = [("반도체, 규제 걱정 이어질까", "미국 반도체 약세가 이어지면 국내 반도체도 부담 가능성"),
          ("유가 급락, 원가 부담 덜까", "100달러 아래에 머물면 기름값 부담 큰 업종엔 숨통 가능성"),
          ("외국인, 매도 멈출까", "어제 2조5071억원 순매도 · 수급에 따라 방향 달라질 가능성")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{290+i*190}px;width:{IW}px;height:166px;box-sizing:border-box;--d:{.5+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:48px;line-height:70px;text-align:center">{i+1}</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:27px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("클로징 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  {live(P, 34, "밤사이 뉴스", .05)}
  <div class="abs" style="left:0;right:0;top:130px;text-align:center;font-size:88px"><span class="punch" style="--d:.1s">오늘 장 <span style="color:#E8590C">체크 3</span></span></div>
  {rows}
  {ch(mascot("bamtol", "happy", "point"), P, 850, 180, 2.0, "a-sl", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 서울신문, 파이낸셜뉴스, 뉴스1, 뉴스웨이</div>
''', "#FFE1CC"))

# 6 ── 예고·사인오프
S[6] = (1, page(FX + f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 일정 (미국 시간 11/6 금)</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:72px;line-height:1.2">미국 10월<br>고용보고서</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.35s;font-size:44px">결과는 <span style="color:#FFC08A">토요일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 660, 210, 280, .4, "a-sr", "hop")}
  {bub("이상, <b>밤사이 뉴스</b>였습니다!", 330, 40, .65, "t-down", "50%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 서울신문, 이투데이, 파이낸셜뉴스, 한국경제, 뉴스1, AP<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (4.4, 1.5), 4: (4.2, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .8), (1, .05, "whoosh", .5), (1, .25, "thud", 1), (1, .45, "thud", .8), (1, .6, "boing", .5), (1, .7, "slidedown", .8),
 (2, .0, "news", .6), (2, .15, "dundun", .7), (2, .5, "pop", .8), (2, 1.0, "pop", .6), (2, 1.2, "pop", .6), (2, 1.4, "pop", .6), (2, 1.7, "whoosh", .5), (2, 1.9, "yay", .6), (2, 2.0, "tick", .7),
 (3, .05, "whoosh", .5), (3, .2, "pop", .8), (3, .6, "boing", .5), (3, .7, "boing", .5), (3, 1.2, "tick", .9), (3, 1.8, "pop", .7), (3, 2.0, "slidedown", .8),
 (4, .05, "whoosh", .5), (4, .1, "thud", .8), (4, .5, "pop", .8), (4, .9, "blip_down", 1), (4, 1.3, "hmm", .5), (4, 1.7, "pop", .6), (4, 1.9, "blip_down", .6), (4, 2.2, "tick", .8),
 (5, .05, "news", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .6), (6, .65, "pop", .7), (6, .9, "jingle", .9),
]
