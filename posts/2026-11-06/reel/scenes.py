"""2026-11-06 릴스 · 토크쇼(talkshow) v2 — '결론 먼저' 훅, 장면 1 '토크쇼 소파 세트 + 대형 LED 화면 롤러코스터' 새 구도 (검수 전).
그날 상황: 선거 랠리 하루 만에 반전 — 나스닥 ▼5.52%(조정 진입), 필라델피아 반도체 ▼12.25% 급변 → 첫 칸(큰 이벤트·급변) 1순위 news는 11-05에 써서(최근 3일) 2순위 talkshow.
흐름: 1 결론(▼12.25% '규제 공포에 반도체 폭락!', 소파 세트 + 롤러코스터 화면) → 2 게스트 토크(달떡이가 '반도체' 역: 데이터센터 규제 걱정 → 칩 주문 걱정)
      → 3 1분 해설(롤러코스터 = 어제 꼭대기·오늘 급강하, 3대 지수, '조정' 뜻) → 4 방청객 질문: 한국은?(5일 코스피 ▼5.28%, 서울은 하루 먼저) → 5 MC 큐카드(오늘 체크 3) → 6 예고(고용보고서, 토요일 아침).
숫자는 posts/2026-11-06 카드·sources.md에 있는 것만 쓴다. 게스트 대사는 기사로 확인된 내용을 쉬운 말로 옮긴 역할극이다(실제 발언 인용 아님).
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes coaster{from{stroke-dashoffset:1500}to{stroke-dashoffset:0}}
.coast{stroke-dasharray:1500;animation:coaster .9s cubic-bezier(.5,0,.6,1) both;animation-delay:var(--d,0s)}
@keyframes cart{0%{offset-distance:0%}100%{offset-distance:100%}}
@keyframes blink2{0%,49%{opacity:1}50%,100%{opacity:.35}}
.blink2{animation:blink2 .5s steps(1) infinite}
@keyframes glowsign{0%,100%{box-shadow:0 0 10px #FFB84D}50%{box-shadow:0 0 26px #FFB84D}}
.glows{animation:glowsign .6s ease-in-out infinite}
@keyframes sink{from{transform:translateY(0)}to{transform:translateY(10px)}}
</style>"""

def p_mic():
    """마이크 (캐릭터 오른손 쪽)."""
    return (f'<path d="M204 222 L188 266" stroke="{L}" stroke-width="13" stroke-linecap="round"/>'
            f'<path d="M204 222 L188 266" stroke="#2F2F3A" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="212" cy="196" r="19" fill="#3A3A48" stroke="{L}" stroke-width="5"/>'
            f'<path d="M200 190 h24 M198 198 h28 M202 206 h20" stroke="#8C92AE" stroke-width="2.5"/>')

def coaster_svg(w, h, d=0):
    """LED 화면 속 롤러코스터: 왼쪽에서 꼭대기(11.4 ▲)까지 올라갔다가 급강하(11.5 ▼)."""
    path = f"M20 {h-60} C {w*.18} {h-70}, {w*.30} 70, {w*.52} 60 C {w*.60} 58, {w*.62} 70, {w*.66} 110 L {w*.80} {h-40} L {w-20} {h-36}"
    sup = "".join(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{h}" stroke="#56607F" stroke-width="5"/>' for x, y in
                  [(w*.22, h-120), (w*.34, 150), (w*.46, 72), (w*.58, 62), (w*.70, 170), (w*.78, h-80)])
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{sup}'
            f'<path d="{path}" fill="none" stroke="#FFD84D" stroke-width="12" stroke-linecap="round" class="coast" style="--d:{d}s"/>'
            f'<text x="{w*.50}" y="40" text-anchor="middle" font-family="Jua" font-size="34" fill="#FF8A8F">11.4 ▲ 선거 랠리</text>'
            f'<text x="{w*.86}" y="{h-70}" text-anchor="middle" font-family="Jua" font-size="34" fill="#8EC5FF">11.5 ▼</text></svg>')

def sofa(x, y, w):
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:150px">'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:110px;background:#C0504D;border:5px solid {L};border-radius:40px 40px 10px 10px"></div>'
            f'<div class="abs" style="left:-14px;top:50px;width:{w+28}px;height:90px;background:#A63E3C;border:5px solid {L};border-radius:24px"></div></div>')

def sign(text, x, y, d, bg="#E03131", size=46, rot=-6):
    return (f'<div class="abs a-stamp" style="left:{x}px;top:{y}px;--d:{d}s;--r:{rot}deg;background:{bg};color:#fff;border:5px solid {L};'
            f'border-radius:16px;padding:6px 22px;font-size:{size}px;box-shadow:0 6px 0 rgba(0,0,0,.25);white-space:nowrap">{text}</div>')

# 1 ── 결론 먼저 (토크쇼 소파 세트): 0초에 숫자·결론·LED 화면·MC(클로즈업, 놀람)·게스트 소파가 모두 보인다
#      0~1초: 숫자 펀치(0) → 롤러코스터 선 그리기(0~.9) → '웅성웅성' 팻말 쾅(.35) → MC 떨림(.5~) → '털썩!' 효과 글자(.7)
S[1] = (1, page(FX + f'''
{stars(12, 61, 0, 180)}
{head("밤사이 토크쇼 · 11.6 FRI", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:190px;text-align:center;font-size:44px;color:#C9D6FF">선거 랠리, 하루 만에 반전 · 미국 반도체지수</div>
<div class="abs" style="left:0;width:1080px;top:248px;text-align:center"><span class="punch" style="--d:0s;font-size:228px;line-height:1;color:#5AA9FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼12.25%</span></div>
<div class="abs" style="left:0;width:1080px;top:494px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">규제 공포에 <span style="color:#FFE36E">반도체 폭락!</span></div>
<div class="panel" style="left:44px;top:640px;width:982px;height:760px;background:#2C2450">
  <div class="abs" style="left:{P}px;top:30px;width:{IW}px;height:330px;box-sizing:border-box;background:#0B1220;border:6px solid {L};border-radius:22px;overflow:hidden">
    <div class="abs" style="left:24px;top:16px;font-size:30px;color:#9FB7E0">📺 오늘의 화면</div>
    <div class="abs" style="left:10px;top:20px">{coaster_svg(IW-32, 300, 0)}</div></div>
  {sign("웅성웅성…", 650, 6, .35, "#3A2A5C", 46, 5)}
  {sofa(480, 570, 380)}
  <div class="abs" style="left:545px;top:410px;width:250px"><div class="squish">{mascot("moon", "teary", "down")}</div></div>
  <div class="abs" style="left:-20px;top:350px;width:450px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "hold", p_mic())}</div></div>
  {sfx("털썩!", 400, 380, 96, .7, 10, "#5AA9FF")}
</div>
''', "#262B55"))

# 2 ── 게스트 토크 (달떡이가 '반도체' 역) — 기사로 확인된 내용만 쉬운 말로
S[2] = (1, page(FX + f'''
{head("게스트 토크", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3E3570;--d:0s">
  <div class="abs glows" style="left:{P}px;top:36px;width:{IW}px;box-sizing:border-box;background:#FFF8E1;border:5px solid {L};border-radius:22px;text-align:center;padding:10px 0">
    <div style="font-size:32px;color:#8A5A3B">오늘의 게스트 (역: 달떡이)</div>
    <div style="font-size:60px"><span style="color:#E8590C">미국 반도체</span>주 대표</div></div>
  {bub("민주당이 의회를 잡자<br><b>데이터센터 규제</b> 걱정이…", P, 250, .3, "t-down", "70%", "font-size:44px")}
  {sofa(80, 620, 360)}
  {ch(mascot("moon", "teary", "down"), 130, 400, 270, .15, "a-sl", "squish")}
  {bub("AI 공장을 덜 지으면<br><b>칩 주문</b>도 줄까 봐요", 430, 420, 1.0, "t-left", style="font-size:42px")}
  {ch(mascot("bamtol", "surprised", "hold", p_mic()), 700, 560, 170, 1.4, "a-sr", "squish2")}
  <div class="abs" style="left:0;right:0;top:770px;text-align:center;line-height:1"><span class="thump" style="--d:1.6s;font-size:120px;color:#8EC5FF;-webkit-text-stroke:6px {L};paint-order:stroke fill">▼12.25%</span></div>
  {numbox("엔비디아", "▼9%대", (P + 10, 380), 910, 2.0, BLUE)}
  {numbox("브로드컴", "▼10%대", (P + 430, 380), 910, 2.2, BLUE)}
</div>
''', "#2B3060"))

# 3 ── 1분 해설 (비유: 롤러코스터) + '조정' 뜻
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("증시가 <b>롤러코스터</b>를 탄 셈!<br>어제 꼭대기 → 오늘 급강하", 30, .1, "t-down", style="font-size:46px")}
  {numbox("다우", "▼3.44%", COL3[0], 250, .6, BLUE)}
  {numbox("S&P500", "▼4.36%", COL3[1], 250, .8, BLUE)}
  {numbox("나스닥", "▼5.52%", COL3[2], 250, 1.0, BLUE)}
  <div class="abs a-pop" style="left:{P}px;top:470px;width:{IW}px;height:330px;box-sizing:border-box;--d:1.4s;background:#fff;border:5px solid {L};border-radius:26px">
    <div class="abs" style="left:30px;top:30px;width:240px;height:16px;background:#FF8A8F;border:4px solid {L};border-radius:8px"></div>
    <div class="abs" style="left:30px;top:56px;font-size:30px;color:#6B5A50">10월 6일 최고치</div>
    <div class="abs" style="left:130px;top:100px;font-size:110px;line-height:1;color:{BLUE}">↓</div>
    <div class="abs" style="left:30px;top:230px;width:240px;height:16px;background:#8EC5FF;border:4px solid {L};border-radius:8px"></div>
    <div class="abs" style="left:30px;top:256px;font-size:30px;color:#6B5A50">나스닥 지금</div>
    <div class="abs" style="left:310px;top:60px;width:580px;font-size:46px;line-height:1.35">최고치보다 <span class="thump" style="--d:1.8s;color:{BLUE}">10% 넘게</span><br>내려오면 <b style="color:#6A4FD8">'조정'</b>이라 불러요</div>
    <div class="abs" style="left:310px;top:220px;width:580px;font-size:34px;color:#6B5A50">나스닥, 어젯밤 조정 진입</div></div>
  {ch(mascot("owl", "worried", "hold", p_tablet()), P, 840, 250, 2.2, "a-sl", "squish")}
  {bub("작년 4월 관세 충격 이후<br><b>가장 큰 하루 낙폭</b>이래요", 330, 900, 2.4, "t-left", style="font-size:42px")}
</div>
''', "#30366E"))

# 4 ── 방청객 질문: 한국은? (5일 서울 — 하루 먼저 맞았다)
S[4] = (1, page(FX + f'''
{head("방청객 질문", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {ch(mascot("star", "worried", "up"), P, 40, 230, .1, "a-sl", "squish")}
  {bub("한국 증시는<br><b>괜찮았어요?</b>", 300, 70, .3, "t-left", style="font-size:46px")}
  {cbub("서울은 <b>하루 먼저</b> 같은 걱정에 맞았어요", 330, .8, "t-down", style="font-size:42px")}
  <div class="abs" style="left:{P}px;top:470px;width:{IW}px;text-align:center">
    <div class="a-fade" style="--d:1.0s;font-size:40px">코스피 (5일 종가)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:1.1s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼5.28%</span></div></div>
  {numbox("삼성전자", "▼7.57%", COL2[0], 680, 1.5, BLUE)}
  {numbox("SK하이닉스", "▼9.46%", COL2[1], 680, 1.65, BLUE)}
  {nar("외국인 <b>약 3.4조원</b> 순매도<br>매도 <b>사이드카</b>(프로그램 매도 5분 정지)까지", P, 870, 2.1, f"font-size:38px;width:800px;box-sizing:border-box;text-align:center")}
  {ch(mascot("bamtol", "worried", "hold", p_mic()), P, 1010, 170, 2.5, "a-sl", "squish2")}
  {bub("오늘 한국장에<br><b>얼마나 반영될지</b> 봐요", 240, 1030, 2.7, "t-left", style="font-size:38px")}
</div>
''', "#4A3E78"))

# 5 ── MC 큐카드 (오늘 한국장 체크 3) — 큐카드를 손에 든 MC, 카드는 부채꼴로
def cue(n, title, sub, y, d, rot):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="transform:rotate({rot}deg);background:#FFFFFF;border:5px solid {L};border-radius:14px;padding:16px 28px 16px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#E7ECF7 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#7E5BB8;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:46px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("MC 큐카드 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#8E6CC8;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:62px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill"><span class="punch" style="--d:.1s">오늘 한국장, 볼 것은 셋</span></div>
  {cue(1, "반도체, 충격 이틀째?", "미국 반도체 폭락이 반영되면 추가 부담 가능성", 160, .5, -1.2)}
  {cue(2, "외국인, 매도 멈출까", "어제 약 3.4조원 순매도 · 더 팔면 하락 압력 가능성", 370, .95, 1)}
  {cue(3, "유가, 반등 이어질까", "더 오르면 기름값 부담 큰 업종엔 부담 가능성", 580, 1.4, -1)}
  {ch(mascot("bamtol", "normal", "point"), 630, 800, 220, 2.0, "a-sr", "squish")}
  {bub("큐카드 셋,<br><b>꼭 챙겨요!</b>", 320, 840, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 서울신문, 국민일보, 재경일보, AP</div>
''', "#FFE1CC"))

# 6 ── 다음 회 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 토크쇼 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 회 예고 (미국 시간 11/6 금)</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:72px;line-height:1.2">미국 10월<br>고용보고서</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">결과는 <span style="color:#FFC08A">토요일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("moon", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 590, 220, 270, .4, "a-sr", "hop")}
  {bub("오늘 토크쇼는 여기까지!<br><b>박수~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 서울신문, 국민일보, MTN, 로이터, AP<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (4.6, 1.5), 4: (4.2, 1.5), 5: (4.0, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "applause", .5), (1, .05, "whoosh", .6), (1, .1, "slidedown", .8), (1, .35, "thud", 1), (1, .4, "hmm", .6), (1, .5, "tension", .5), (1, .7, "thud", .8),
 (2, .0, "mic", .7), (2, .15, "whoosh", .5), (2, .3, "pop", .8), (2, 1.0, "pop", .7), (2, 1.4, "boing", .6), (2, 1.6, "blip_down", .9), (2, 2.0, "pop", .6), (2, 2.2, "pop", .6),
 (3, .1, "pop", .8), (3, .6, "blip_down", .6), (3, .8, "blip_down", .6), (3, 1.0, "blip_down", .7), (3, 1.4, "whoosh", .5), (3, 1.8, "ding", .7), (3, 2.2, "boing", .5), (3, 2.4, "pop", .8),
 (4, .1, "whoosh", .5), (4, .3, "question", .7), (4, .8, "pop", .7), (4, 1.1, "dundun", .6), (4, 1.1, "blip_down", .7), (4, 1.5, "blip_down", .6), (4, 1.65, "blip_down", .5), (4, 2.1, "tick", .8), (4, 2.5, "boing", .5), (4, 2.7, "pop", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .6), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "applause", .6), (6, .9, "jingle", .9),
]
