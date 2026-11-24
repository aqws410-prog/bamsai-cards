"""2026-11-25 릴스 · 뉴스 속보(news) v7 — '결론 먼저' 훅, 장면 1 '방송국 분할 화면(스플릿 스크린) — 왼쪽 다우 50,000선 축하 화면 vs 오른쪽 반도체 경보 화면(칩이 굴러떨어짐) + 가운데 앵커 클로즈업' 새 구도 (검수 전).
그날 상황: 필라델피아 반도체지수 ▼7.88%·엔비디아 ▼5.86% 급변 → 상황표 첫 칸(급변) 1순위 news
          (같은 칸 직전 11-24 talkshow(2순위) 다음이라 1순위 차례, 최근 3일 11-22 weather·11-23 chat·11-24 talkshow 미사용, news 마지막 11-21).
흐름: 1 결론(반도체지수 ▼7.88% 'AI 반등, 하루 만에 뚝!', 분할 화면) → 2 현장 연결(3대 지수 엇갈림, 다우 50,000선 위)
      → 3 1분 해설: 비유 '자이로드롭 — 어제 꼭대기까지 올라간(엔비디아 ▲31.48%) 놀이기구가 오늘 뚝(▼5.86%)', 이유 둘(차익실현 · AI 투자 계속될까 걱정) + 앤트로픽 공모가 아래
      → 4 시민 인터뷰: 한국은요?(24일 코스피 ▲6.32% 5,006.03, 삼성전자·SK하이닉스 6%대 ▲, 미국 반도체 급락은 서울 마감 뒤)
      → 5 클로징 체크 3 → 6 예고(오늘 밤 PCE · 26일 금통위·미국 휴장).
숫자·사실은 posts/2026-11-25 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes lamp{0%,49%{background:#FF4B4B;box-shadow:0 0 50px 16px rgba(255,75,75,.7)}50%,100%{background:#7A2A2A;box-shadow:none}}
@keyframes flash{0%{opacity:0}20%{opacity:.75}100%{opacity:0}}
@keyframes tumble{0%{transform:translate(0,0) rotate(0)}100%{transform:translate(var(--tx),var(--ty)) rotate(var(--tr))}}
@keyframes conf{0%{transform:translateY(-60px) rotate(0)}100%{transform:translateY(360px) rotate(540deg)}}
@keyframes ride{0%{transform:translateY(0)}55%{transform:translateY(0)}100%{transform:translateY(var(--dy))}}
@keyframes rise2{0%{transform:translateY(var(--dy))}100%{transform:translateY(0)}}
.lamp{animation:lamp .5s steps(1) infinite}
.flash{animation:flash .35s ease-out both;animation-delay:var(--d,0s)}
.tumble{animation:tumble .7s cubic-bezier(.5,0,.8,.6) both;animation-delay:var(--d,0s)}
.conf{animation:conf 1.5s linear infinite;animation-delay:var(--d,0s)}
.ride{animation:ride 1.3s cubic-bezier(.6,0,.9,.5) both;animation-delay:var(--d,0s)}
.rise2{animation:rise2 .5s cubic-bezier(.2,.9,.3,1) both}
</style>"""

def confetti(n, seed, x0, w, d0=0):
    rnd = random.Random(seed)
    cols = ["#FF6B6B", "#FFD43B", "#69DB7C", "#74C0FC", "#F783AC"]
    return "".join(f'<div class="abs conf" style="left:{x0 + rnd.randint(10, w - 30)}px;top:{rnd.randint(-20, 120)}px;width:14px;height:22px;'
                   f'background:{rnd.choice(cols)};border:3px solid {L};border-radius:3px;--d:{d0 + rnd.random() * 1.2:.2f}s"></div>' for _ in range(n))

# 1 ── 결론 먼저 (방송국 분할 화면): 0초에 숫자·결론·앵커(클로즈업, 놀람)·두 화면이 모두 보인다
#      0~1초: 숫자 펀치(0) → 플래시(.05) → 칩 굴러떨어짐(.1~.8)·경보등(상시)·꽃가루(상시) → '긴급 속보' 도장(.35) → 앵커 떨림(.5) → '뚝!'(.7)
L_SCR, R_SCR = COL2[0], COL2[1]
S[1] = (1, page(FX + f'''
{stars(12, 61, 0, 200)}
{head("밤사이 뉴스 · 11.25 WED", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:48px;color:#FFE36E">어젯밤 미국 반도체지수</div>
<div class="abs" style="left:0;width:1080px;top:258px;text-align:center"><span class="punch" style="--d:0s;font-size:226px;line-height:1;color:#7DB0FF;-webkit-text-stroke:11px {L};paint-order:stroke fill">▼7.88%</span></div>
<div class="abs" style="left:0;width:1080px;top:520px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">AI 반등, <span style="color:#FFE36E">하루 만에 뚝!</span></div>
<div class="panel" style="left:44px;top:680px;width:982px;height:760px;background:#2E2A58">
  <div class="abs" style="left:{L_SCR[0]}px;top:34px;width:{L_SCR[1]}px;height:300px;box-sizing:border-box;background:#E7F7EC;border:5px solid {L};border-radius:20px;overflow:hidden;text-align:center">
    <div style="font-size:34px;margin-top:22px">화면 1 · 다우</div>
    <div style="font-size:84px;color:{RED};line-height:1.1">▲0.85%</div>
    <div style="font-size:38px;margin-top:8px">50,000선 위 마감</div>
    {confetti(8, 3, 0, L_SCR[1])}
  </div>
  <div class="abs" style="left:{R_SCR[0]}px;top:34px;width:{R_SCR[1]}px;height:300px;box-sizing:border-box;background:#FFE3E3;border:5px solid {L};border-radius:20px;overflow:hidden;text-align:center">
    <div style="font-size:34px;margin-top:22px">화면 2 · 반도체</div>
    <div class="abs lamp" style="right:20px;top:18px;width:40px;height:40px;border-radius:50%;border:4px solid {L}"></div>
    <div class="abs tumble" style="left:160px;top:70px;--d:.1s;--tx:40px;--ty:50px;--tr:200deg"><div style="width:100px">{chip("#9AD3FF", "tired")}</div></div>
    <div class="abs" style="left:0;right:0;bottom:16px;font-size:38px">엔비디아 <span style="color:{BLUE}">▼5.86%</span></div>
  </div>
  <div class="abs" style="left:0;right:0;bottom:0;height:120px;background:#5B5FA8;border-top:6px solid {L};text-align:center;color:#FFE59A;font-size:44px;line-height:112px">🌙 밤사이 뉴스</div>
  <div class="abs" style="left:250px;top:300px;width:480px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "point")}</div></div>
  {stamp("긴급 속보", 620, 370, .35, -8)}
  {sfx("뚝!", 90, 420, 130, .7, -10, "#7DB0FF")}
  <div class="abs flash" style="left:0;right:0;top:0;bottom:0;background:#fff;--d:.05s"></div>
</div>
''', "#262B55"))

# 2 ── 현장 연결 (솜부엉 기자) — 3대 지수 엇갈림
S[2] = (1, page(FX + f'''
{head("현장 연결 · 뉴욕", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3C4485;--d:0s">
  <div class="live" style="right:{P}px;top:30px"><i></i>LIVE</div>
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 40, 300, .1, "a-sl", "squish")}
  {bub("지수가<br><b>엇갈렸어요!</b>", 380, 90, .3, "t-left", style="font-size:50px")}
  {numbox("다우", "▲0.85%", COL3[0], 400, .6, RED)}
  {numbox("S&amp;P500", "▼0.50%", COL3[1], 400, .75, BLUE)}
  {numbox("나스닥", "<span class='thump' style='--d:1.1s'>▼1.48%</span>", COL3[2], 400, .9, BLUE)}
  {lower_third("솜부엉 기자", "뉴욕 월가", P, 600, 1.2)}
  <div class="abs a-pop" style="left:{P}px;top:740px;width:{IW}px;--d:1.5s;box-sizing:border-box;background:#FFF8E1;border:5px solid {L};border-radius:26px;text-align:center;padding:18px 0">
    <div style="font-size:40px">다우 종가</div>
    <div style="font-size:110px;line-height:1.1"><span class="thump" style="--d:1.8s;color:{RED}">50,018.70</span></div>
    <div style="font-size:42px">50,000선 위에서 마감</div></div>
  {cbub("그런데 <b>반도체</b>는 크게 밀렸어요", 1040, 2.2, "t-up", style="font-size:44px")}
</div>
''', "#2B3060"))

# 3 ── 1분 해설 — 자이로드롭: 어제 꼭대기, 오늘 뚝
def tower():
    return (f'<svg class="abs" style="left:{P + 40}px;top:120px" width="160" height="900" viewBox="0 0 160 900">'
            f'<rect x="60" y="0" width="40" height="900" fill="#C9D2F0" stroke="{L}" stroke-width="6"/>'
            + "".join(f'<path d="M60 {y} L100 {y + 60} M100 {y} L60 {y + 60}" stroke="#8C96C8" stroke-width="4"/>' for y in range(20, 880, 80))
            + f'<path d="M30 10 L80 -30 L130 10 Z" fill="#E03131" stroke="{L}" stroke-width="6" stroke-linejoin="round"/></svg>')
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#22305E;--d:0s">
  {stars(10, 9, 0, 400, 0, 960)}
  <div class="abs" style="left:0;right:0;top:1030px;height:150px;background:#3E6B4E;border-top:6px solid {L}"></div>
  {tower()}
  <div class="abs ride" style="left:{P}px;top:150px;--d:.3s;--dy:760px">
    <div style="width:240px;height:110px;background:#FFD84D;border:6px solid {L};border-radius:22px;text-align:center;font-size:40px;line-height:98px">엔비디아</div></div>
  <div class="abs a-pop" style="left:320px;top:150px;--d:.2s;background:#FFE3E3;border:4px solid {L};border-radius:18px;padding:6px 20px;font-size:40px">어제 꼭대기 <span style="color:{RED}">▲31.48%</span></div>
  <div class="abs a-stamp" style="left:320px;top:880px;--d:1.5s;--r:-4deg;background:#DFEBFF;border:5px solid {L};border-radius:18px;padding:6px 22px;font-size:56px">오늘 뚝 <span style="color:{BLUE}">▼5.86%</span></div>
  {cbub("어제 꼭대기까지 오른 <b>자이로드롭</b>,<br>오늘은 아래로 뚝!", 270, .1, "t-down", style="font-size:42px", left=260, width=722)}
  <div class="abs a-sr" style="left:320px;top:500px;width:620px;--d:1.9s;background:#FFF8E1;border:4px solid {L};border-radius:18px;padding:10px 20px;font-size:38px">① 많이 올랐으니 이익 챙기기<br><span style="font-size:30px">(차익실현)</span></div>
  <div class="abs a-sr" style="left:320px;top:680px;width:620px;--d:2.4s;background:#FFF8E1;border:4px solid {L};border-radius:18px;padding:10px 20px;font-size:38px">② "AI 투자, 계속될까?" 걱정</div>
  {stamp("앤트로픽 공모가 아래", 120, 1050, 3.0, -3)}
</div>
''', "#30366E"))

# 4 ── 시민 인터뷰 (한국) — 24일 서울은 반도체 급락 전에 끝났다
S[4] = (1, page(FX + f'''
{head("한국은요?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {ch(mascot("star", "surprised", "up"), P, 40, 240, .1, "a-sl", "squish")}
  {bub("어제 한국은<br><b>엄청 올랐던데요?</b>", 300, 70, .3, "t-left", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:330px;width:{IW}px;--d:.7s;text-align:center">
    <div style="font-size:40px">코스피 (24일 종가 5,006.03)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.9s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲6.32%</span></div></div>
  {numbox("삼성전자", "▲6.70%", COL2[0], 580, 1.3, RED)}
  {numbox("SK하이닉스", "▲6.73%", COL2[1], 580, 1.45, RED)}
  {nar("젠슨 황 복귀 소식에 <b>5,000선 회복</b>", P, 790, 1.9, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("bamtol", "worried", "point"), 652, 900, 230, 2.3, "a-sr", "squish2")}
  {bub("미국 반도체 급락은<br><b>서울 장 끝난 뒤</b>예요", 150, 960, 2.5, "t-right", style="font-size:42px")}
</div>
''', "#4A3E78"))

# 5 ── 클로징 체크 3 (복숭아빛)
items = [("chip", "반도체, 오른 만큼 지킬까?", "미국 반도체지수 <span style='color:#2F6BD8'>▼7.88%</span> 부담 가능성"),
         ("chip", "델이 보여 준 AI 서버 수요", "매출 1년 새 두 배 <span style='color:#C92A2A'>▲103%</span>"),
         ("won", "금통위 하루 전", "내일(26일) 한은 금리 결정")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{1.0+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ICONS[k]}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (k, t, d) in enumerate(items))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("클로징 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFF8E1;--d:0s">
  {live(40, 34, "밤사이 뉴스", .1)}
  {ch(mascot("bamtol", "normal", "point"), 600, 120, 290, .15, "a-sr", "squish")}
  {desk(520, 360, 440)}
  {bub("오늘 한국장은<br>딱 <b>세 가지</b>만 보세요!", 40, 150, .4, "t-right", style="font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.2s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 서울신문, 이투데이, 시대, 팁랭크스, 퀀티스나우</div>
''', "#FFE1CC"))

# 6 ── 예고·사인오프 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">오늘 밤 10시 30분</div>
  <div class="abs" style="left:44px;top:100px;font-size:66px;line-height:1.2">미국 10월 PCE 물가<br>26일 금통위 · 미국 휴장</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.3s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("이상, <b>밤사이 뉴스</b>였습니다!", 380, 40, .65, "t-down", "380px", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 서울신문, 이투데이, 시대, 이코노미블록, 노컷뉴스, 폴리뉴스, 신아일보 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (4.8, 1.6), 4: (4.3, 1.5), 5: (3.2, 1.45), 6: (3.0, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .9), (1, .05, "shutter", .7), (1, .1, "slidedown", .7), (1, .35, "thud", .9), (1, .5, "tension", .4), (1, .7, "blip_down", .8),
 (2, .1, "whoosh", .6), (2, .3, "pop", .8), (2, .6, "ding", .5), (2, .75, "blip_down", .6), (2, .9, "blip_down", .7), (2, 1.2, "whoosh", .5), (2, 1.5, "sparkle", .7), (2, 2.2, "pop", .8),
 (3, .1, "pop", .8), (3, .2, "ding", .5), (3, .9, "tension", .5), (3, 1.0, "slidedown", .8), (3, 1.5, "thud", .9), (3, 1.9, "whoosh", .5), (3, 2.4, "whoosh", .5), (3, 3.0, "thud", .7),
 (4, .1, "whoosh", .5), (4, .3, "question", .7), (4, .7, "sparkle", .7), (4, 1.3, "pop", .6), (4, 1.45, "pop", .5), (4, 1.9, "tick", .8), (4, 2.3, "boing", .5), (4, 2.5, "pop", .8),
 (5, .05, "news", .5), (5, .15, "whoosh", .5), (5, .4, "pop", .8), (5, 1.0, "CHECK1", 1), (5, 1.45, "CHECK2", 1), (5, 1.9, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "news", .6), (6, 1.0, "jingle", .9),
]
