"""2026-11-21 릴스 · 뉴스 속보(news) v6 — '결론 먼저' 훅, 장면 1 '지진 관측소 — 지진계 기록지에 요동치는 바늘 선 + 깜박이는 경보등 + 긴급 속보 도장' 새 구도 (검수 전).
그날 상황: 나스닥 ▼5.28%·엔비디아 ▼14.01%·다우·S&P500 조정 진입 급변 → 상황표 첫 칸(급변) 1순위 news
          (같은 칸 직전 11-20 talkshow(2순위) 다음이라 1순위 차례, 최근 3일 11-18 delivery·11-19 detective·11-20 talkshow 미사용, news 마지막 11-17).
흐름: 1 결론(엔비디아 ▼14.01% 'AI 대장주, 하루 만에 와르르!', 지진계) → 2 현장 연결(3대 지수, 다우·S&P500 조정 진입, 나스닥 올해 상승분 반납)
      → 3 1분 해설: 비유 '기대로 높이 쌓은 젠가 탑에서 블록 세 개가 빠졌다'(AI 투자 계속될까? · 앤트로픽 이틀째 ▼8.50% · 로이터 'SEC 회계 조사' 보도)
      → 4 시민 인터뷰: 한국은요?(20일 코스피 ▼5.21%, 4,869.96, 사이드카, 미국 반도체 급락은 서울 마감 뒤) → 5 클로징 체크 3(월요일) → 6 예고(내일 주간 결산·11/26 휴장).
숫자·사실은 posts/2026-11-21 카드·sources.md에 있는 것만 쓴다. 'SEC 조사'는 로이터 보도이며 조사 자체가 위법을 뜻하지 않는다는 점을 함께 적는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes lamp{0%,49%{background:#FF4B4B;box-shadow:0 0 60px 20px rgba(255,75,75,.7)}50%,100%{background:#7A2A2A;box-shadow:none}}
@keyframes paper{from{transform:translateX(0)}to{transform:translateX(-300px)}}
@keyframes flash{0%{opacity:0}20%{opacity:.75}100%{opacity:0}}
@keyframes tumble{0%{transform:translate(0,0) rotate(0)}100%{transform:translate(var(--tx),var(--ty)) rotate(var(--tr))}}
.lamp{animation:lamp .5s steps(1) infinite}
.paper{animation:paper 2.6s linear both}
.flash{animation:flash .35s ease-out both;animation-delay:var(--d,0s)}
.tumble{animation:tumble .6s cubic-bezier(.5,0,.8,.6) both;animation-delay:var(--d,0s)}
</style>"""

def seismo(w, h):
    """지진계 기록지: 잔잔하다가 크게 요동치는 선 (draw 애니메이션 0.1~0.8초)."""
    pts, x = [], 0
    rnd = random.Random(11)
    while x <= w + 300:
        amp = 6 if x < w * .28 else (150 if x < w * .75 else 60)
        pts.append(f"{x},{h // 2 + rnd.randint(-amp, amp)}")
        x += 14
    d = "M" + " L".join(pts)
    ln = 9000
    grid = "".join(f'<path d="M0 {y} H{w + 300}" stroke="#E8DCC4" stroke-width="2"/>' for y in range(20, h, 40))
    return (f'<svg class="abs" style="left:0;top:0" width="{w + 300}" height="{h}">{grid}'
            f'<path d="{d}" fill="none" stroke="#E03131" stroke-width="7" stroke-linejoin="round" '
            f'style="stroke-dasharray:{ln};--len:{ln};stroke-dashoffset:{ln};animation:draw .8s ease-out both;animation-delay:.1s"/></svg>')

# 1 ── 결론 먼저 (지진 관측소): 0초에 숫자·결론·앵커(클로즈업, 놀람)·지진계가 모두 보인다
#      0~1초: 숫자 펀치(0) → 플래시(.05) → 지진계 선 요동(.1~.9) → '긴급 속보' 도장 쾅(.35) → 앵커 떨림(.5) → '와르르!'(.7)
S[1] = (1, page(FX + f'''
{stars(12, 53, 0, 200)}
{head("밤사이 뉴스 · 11.21 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:48px;color:#FFE36E">어젯밤 엔비디아</div>
<div class="abs" style="left:0;width:1080px;top:260px;text-align:center"><span class="punch" style="--d:0s;font-size:230px;line-height:1;color:#7DB0FF;-webkit-text-stroke:11px {L};paint-order:stroke fill">▼14.01%</span></div>
<div class="abs" style="left:0;width:1080px;top:520px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">AI 대장주, <span style="color:#FFE36E">하루 만에 와르르!</span></div>
<div class="panel" style="left:44px;top:680px;width:982px;height:760px;background:#33305E">
  <div class="abs" style="left:{P}px;top:30px;font-size:34px;color:#FFE59A">🌐 밤사이 관측소 · 월가 지진계</div>
  <div class="abs lamp" style="right:{P}px;top:22px;width:56px;height:56px;border-radius:50%;border:5px solid {L}"></div>
  <div class="abs" style="left:{P}px;top:96px;width:{IW}px;height:300px;background:#FFFDF5;border:5px solid {L};border-radius:20px;overflow:hidden">
    <div class="abs paper" style="left:0;top:0">{seismo(IW, 300)}</div>
    <div class="abs" style="left:4px;top:8px;font-size:28px;color:#8A5A3B">잔잔 → 요동</div>
  </div>
  <div class="abs" style="left:0;right:0;bottom:0;height:130px;background:#5B5FA8;border-top:6px solid {L}"></div>
  <div class="abs" style="left:0px;top:300px;width:470px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "point")}</div></div>
  {stamp("긴급 속보", 520, 430, .35, -8)}
  {sfx("와르르!", 470, 540, 96, .7, -6, "#FFE36E")}
  <div class="abs flash" style="left:0;right:0;top:0;bottom:0;background:#fff;--d:.05s"></div>
</div>
''', "#262B55"))

# 2 ── 현장 연결 (솜부엉 기자) — 3대 지수
S[2] = (1, page(FX + f'''
{head("현장 연결 · 뉴욕", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3C4485;--d:0s">
  <div class="live" style="right:{P}px;top:30px"><i></i>LIVE</div>
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 40, 300, .1, "a-sl", "squish")}
  {bub("3대 지수<br><b>모두 급락!</b>", 380, 90, .3, "t-left", style="font-size:50px")}
  {numbox("다우", "▼1.93%", COL3[0], 400, .6, BLUE)}
  {numbox("S&amp;P500", "▼3.70%", COL3[1], 400, .75, BLUE)}
  {numbox("나스닥", "<span class='thump' style='--d:1.1s'>▼5.28%</span>", COL3[2], 400, .9, BLUE)}
  <div class="abs a-pop" style="left:{P}px;top:600px;width:{IW}px;box-sizing:border-box;--d:1.4s;background:#FFF8E1;border:5px solid {L};border-radius:24px;text-align:center;padding:22px 10px">
    <div style="font-size:52px">다우·S&amp;P500 <span style="color:#E8590C">조정 국면</span> 진입</div>
    <div style="font-size:34px;margin-top:6px">조정 = 기록 고점보다 10% 넘게 하락</div></div>
  {stamp("나스닥 올해 상승분 반납", 150, 860, 2.0, -5)}
</div>
{lower_third("솜부엉 기자", "뉴욕 월가", 44 + P, 1300, .5)}
''', "#2B3060"))

# 3 ── 1분 해설 — 젠가 탑에서 블록 세 개가 빠졌다
def block(text, y, d, tx, ty, tr, col="#FFD9A8"):
    return (f'<div class="abs" style="left:{P + 60}px;top:{y}px;width:340px;height:96px"><div class="tumble" style="--d:{d}s;--tx:{tx}px;--ty:{ty}px;--tr:{tr}deg;'
            f'width:340px;height:96px;box-sizing:border-box;background:{col};border:5px solid {L};border-radius:12px;font-size:29px;line-height:86px;white-space:nowrap;text-align:center">{text}</div></div>')
plain = "".join(f'<div class="abs" style="left:{P + 60}px;top:{y}px;width:340px;height:96px;box-sizing:border-box;background:#F2C98E;border:5px solid {L};border-radius:12px"></div>'
                for y in (840, 744, 552))
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("AI 기대로 높이 쌓은 <b>젠가 탑</b>,<br>블록 세 개가 빠지자 흔들!", 30, .1, "t-down", style="font-size:44px")}
  <div class="abs" style="left:{P + 40}px;top:936px;width:380px;height:30px;background:#8A5A3B;border:5px solid {L};border-radius:8px"></div>
  {plain}
  <div class="abs" style="left:{P + 60}px;top:270px;width:340px;height:80px;font-size:40px;text-align:center;line-height:80px">🏗 AI 기대</div>
  {block("① AI 투자 계속될까?", 648, .7, 130, 0, 4, "#FFB3B3")}
  {block("② 앤트로픽 ▼8.50%", 456, 1.3, 130, 0, -4, "#FFB3B3")}
  {block("③ 회계 조사 보도", 360, 1.9, 130, 0, 5, "#FFB3B3")}
  <div class="abs a-rise" style="left:600px;top:380px;width:342px;box-sizing:border-box;--d:2.3s;font-size:32px;line-height:1.35;background:#fff;border:4px solid {L};border-radius:20px;padding:14px 18px">③ 로이터: "SEC가<br>엔비디아 회계 조사"<br><span style="font-size:26px;color:#6B5A50">조사 자체가 위법을<br>뜻하진 않아요</span></div>
  {ch(mascot("moon", "worried", "point"), 640, 700, 250, 2.6, "a-sr", "squish")}
  {lower_third("달떡이 박사", "AI 산업 전문가", P, 1040, 2.8)}
</div>
''', "#30366E"))

# 4 ── 시민 인터뷰: 한국은요? (20일 서울)
S[4] = (1, page(FX + f'''
{head("시민 인터뷰 · 서울", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {ch(mascot("star", "teary", "up"), P, 40, 240, .1, "a-sl", "squish")}
  {bub("한국은<br><b>괜찮았어요?</b>", 300, 70, .3, "t-left", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:330px;width:{IW}px;--d:.7s;text-align:center">
    <div style="font-size:40px">코스피 (20일 종가 4,869.96)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.9s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼5.21%</span></div></div>
  {nar("코스피·코스닥 <b>매도 사이드카</b> 발동<br>(프로그램 매도 5분 멈춤)", P, 580, 1.3, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("삼성전자", "▼7.01%", COL2[0], 740, 1.7, BLUE)}
  {numbox("SK하이닉스", "▼5.92%", COL2[1], 740, 1.85, BLUE)}
  {ch(mascot("bamtol", "worried", "point"), 652, 920, 230, 2.3, "a-sr", "squish2")}
  {bub("미국 반도체 급락은<br><b>서울 장 끝난 뒤</b>예요", 190, 960, 2.5, "t-right", style="font-size:40px")}
</div>
''', "#4A3E78"))

# 5 ── 클로징 체크 (월요일 한국장)
def chk(n, title, sub, y, d):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="background:#FFFFFF;border:5px solid {L};border-radius:20px;padding:18px 28px 18px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#E8590C;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:48px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("클로징 · 월요일 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#6F8FD8;--d:0s">
  <div class="abs" style="left:{P}px;top:36px;font-size:58px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill">월요일 한국장, 볼 것은 셋</div>
  {chk(1, "반도체, 2차 충격 올까", "서울 마감 뒤 미국 반도체주가 더 크게 빠져 부담 가능성", 150, .4)}
  {chk(2, "외국인 매도 이어질까", "20일 1조원 넘게 판 외국인, 더 팔면 하락 압력", 360, .8)}
  {chk(3, "금리·환율 부담", "12월 금리 인상 거의 확실히 반영, 원/달러 주목", 570, 1.2)}
  {ch(mascot("bamtol", "normal", "point"), 640, 790, 240, 1.7, "a-sr", "squish")}
  {bub("체크 셋,<br><b>꼭 챙겨요!</b>", 330, 830, 1.9, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.1s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 파이낸셜뉴스, 폴리뉴스, M이코노미뉴스, 로이터</div>
''', "#FFE1CC"))

# 6 ── 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 뉴스 예고</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">내일은 이번 주 성적표<br>11/26 미국장 휴장</div>
  <div class="abs a-rise" style="left:44px;top:320px;--d:.3s;font-size:44px">내일 아침 <span style="color:#FFC08A">8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 210, 290, .4, "a-sr", "hop")}
  {bub("지금까지 밤사이 뉴스!<br><b>주말 잘 보내세요</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 파이낸셜뉴스, MTN, 디지털타임스, 이투데이, 로이터, CBS, 아시아경제, 폴리뉴스 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.2, 1.5), 3: (5.0, 1.6), 4: (4.6, 1.5), 5: (3.6, 1.45), 6: (3.0, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .6), (1, .05, "shutter", .8), (1, .1, "tension", .6), (1, .35, "thud", .9), (1, .5, "slidedown", .6), (1, .7, "boing", .6),
 (2, .0, "whoosh", .5), (2, .1, "pop", .6), (2, .3, "pop", .8), (2, .6, "blip_down", .7), (2, .75, "blip_down", .6), (2, .9, "blip_down", .6), (2, 1.4, "dundun", .6), (2, 2.0, "thud", .8),
 (3, .1, "pop", .8), (3, .7, "slidedown", .6), (3, 1.3, "slidedown", .6), (3, 1.9, "thud", .8), (3, 2.3, "tick", .7), (3, 2.6, "hmm", .6), (3, 2.8, "whoosh", .5),
 (4, .1, "whoosh", .5), (4, .3, "question", .7), (4, .7, "dundun", .6), (4, .9, "sad", .5), (4, 1.3, "tick", .8), (4, 1.7, "blip_down", .6), (4, 1.85, "blip_down", .5), (4, 2.3, "boing", .5), (4, 2.5, "pop", .8),
 (5, .05, "whoosh", .5), (5, .4, "CHECK1", 1), (5, .8, "CHECK2", 1), (5, 1.2, "CHECK3", 1), (5, 1.9, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .6), (6, .9, "jingle", .9),
]
