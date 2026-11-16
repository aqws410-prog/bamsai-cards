"""2026-11-17 릴스 · 뉴스 속보(news) v5 — '결론 먼저' 훅, 장면 1 '헬기 중계 카메라 뷰파인더(REC·모서리 표시) 속 무너지는 칩 빌딩 + 하락 화살표 + 투매 도장' 새 구도 (검수 전).
그날 상황: 미국 반도체지수 ▼5.28%·나스닥 ▼2.49% 급변 → 첫 칸(급변) 1순위 news (같은 칸 직전 11-11 talkshow(2순위) 다음이라 1순위 차례,
          최근 3일 11-14 clinic·11-15 weather·11-16 chat 미사용, news 마지막 11-10).
흐름: 1 결론(▼5.28% '실적 하루 앞, AI 칩 투매', 헬기 중계 뷰파인더) → 2 현장 연결(CNBC '이사회, 황 복귀 검토 안 해', 엔비디아 ▼4.12%, 3대 지수)
      → 3 1분 해설: 비유 '차(칩) 사 가는 길에 이어 렌터카(원격 접속)까지 허가제' → 4 한국은요?(16일 코스피 ▼3.59%, 삼성전자·SK하이닉스, ADR 7%대, 유가 ▼3.21%)
      → 5 클로징 체크 3 → 6 예고(엔비디아 실적, 내일 아침 8시).
숫자·사실은 posts/2026-11-17 카드·sources.md에 있는 것만 쓴다. 황 사임 배경(사생활 등)은 쓰지 않고 '경영 불확실성'까지만.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes rec{0%,49%{opacity:1}50%,100%{opacity:.2}}
@keyframes bracket{0%{transform:scale(1.18);opacity:0}100%{transform:scale(1);opacity:1}}
@keyframes sink{0%{transform:translateY(0) rotate(0)}100%{transform:translateY(46px) rotate(var(--rt,4deg))}}
@keyframes rotor{from{transform:scaleX(1)}50%{transform:scaleX(.15)}to{transform:scaleX(1)}}
.rec{animation:rec .8s steps(1) infinite}
.brk{animation:bracket .35s ease-out both;animation-delay:var(--d,0s)}
.sink{animation:sink 1.2s cubic-bezier(.5,0,.6,1) both;animation-delay:var(--d,0s)}
.rotor{transform-origin:50% 50%;animation:rotor .18s linear infinite}
.dline path{animation:draw .7s ease-out both;animation-delay:var(--d,0s)}
</style>"""

def brackets(w, h, inset=22, arm=70, col="#FFE36E", d=0):
    """카메라 뷰파인더 모서리 표시."""
    b = f"position:absolute;width:{arm}px;height:{arm}px;border-color:{col};border-style:solid;border-width:0"
    return (f'<div class="abs brk" style="left:0;top:0;width:{w}px;height:{h}px;--d:{d}s">'
            f'<div style="{b};left:{inset}px;top:{inset}px;border-left-width:8px;border-top-width:8px"></div>'
            f'<div style="{b};right:{inset}px;top:{inset}px;border-right-width:8px;border-top-width:8px"></div>'
            f'<div style="{b};left:{inset}px;bottom:{inset}px;border-left-width:8px;border-bottom-width:8px"></div>'
            f'<div style="{b};right:{inset}px;bottom:{inset}px;border-right-width:8px;border-bottom-width:8px"></div></div>')

def chipb(x, y, w, d, rt, label):
    """가라앉는 칩 빌딩(칩 캐릭터 + 이름표)."""
    return (f'<div class="abs sink" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s;--rt:{rt}deg">{chip("#BFD3FF", "tired")}'
            f'<div style="text-align:center;font-size:32px;color:#fff;margin-top:-8px">{label}</div></div>')

# 1 ── 결론 먼저 (헬기 중계 뷰파인더): 0초에 숫자·결론·앵커(클로즈업, 놀람)·중계 화면이 모두 보인다
#      0~1초: 숫자 펀치(0) → 뷰파인더 모서리 쾅(.05) + 칩 빌딩 가라앉기(0~1.2) → 말풍선(.2) → 하락 화살표 긋기(.25~.95) → '투매' 도장(.45) → '와르르!'(.7) → 앵커 떨림(상시)
PW, PH = 982, 780
S[1] = (1, page(FX + f'''
{stars(12, 17, 0, 180)}
{head("밤사이 뉴스 · 11.17 TUE", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">어젯밤 뉴욕 · 미국 반도체지수</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#5AA9FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼5.28%</span></div>
<div class="abs" style="left:0;width:1080px;top:504px;text-align:center;font-size:78px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">실적 하루 앞, <span style="color:#FFE36E">AI 칩 투매</span></div>
<div class="panel" style="left:44px;top:640px;width:{PW}px;height:{PH}px;background:#151A35">
  <div class="abs" style="left:0;right:0;bottom:0;height:260px;background:#1F2550"></div>
  {chipb(P + 40, 120, 210, 0, -5, "AMD")}
  {chipb(P + 330, 70, 250, .1, 3, "엔비디아")}
  {chipb(P + 660, 130, 200, .2, 6, "마이크론")}
  <svg class="abs dline" style="left:0;top:0;overflow:visible" width="{PW}" height="{PH}">
    <path d="M60 96 L300 150 L420 118 L640 236 L880 300 M836 262 L882 302 L826 322" fill="none" stroke="#5AA9FF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"
      style="stroke-dasharray:1200;--len:1200;stroke-dashoffset:1200;--d:.25s;filter:drop-shadow(0 0 8px #5AA9FF)"/>
  </svg>
  {brackets(PW, PH, d=.05)}
  <div class="abs" style="left:{P + 20}px;top:36px;font-size:34px;color:#fff"><span class="rec" style="color:#FF5A5F">●</span> REC · 헬기 중계 · 월가 상공</div>
  <svg class="abs" style="right:{P + 20}px;top:30px" width="120" height="60" viewBox="0 0 120 60"><rect class="rotor" x="6" y="6" width="108" height="8" rx="4" fill="#C9D6FF"/><rect x="56" y="12" width="8" height="12" fill="#C9D6FF"/><rect x="34" y="22" width="56" height="30" rx="15" fill="#C9D6FF" stroke="{L}" stroke-width="4"/></svg>
  <div class="stamp a-stamp" style="left:400px;top:430px;--d:.45s;--r:-8deg;font-size:70px;padding:2px 24px">투매</div>
  {ch(mascot("bamtol", "surprised", "point"), P - 10, 420, 330, 0, "", "shiver")}
  {bub("실적 하루 전인데<br><b>반도체가 와르르!</b>", 370, 560, .2, "t-left", style="font-size:42px;padding:16px 26px")}
  {sfx("와르르!", 690, 560, 76, .7, 8, "#7DBBFF")}
</div>
{ticker("나스닥 ▼2.49% · S&P500 ▼1.92% · 다우 ▼1.41% · 엔비디아 ▼4.12% · 마이크론 ▼7.62%", 1440)}
''', "#262B55"))

# 2 ── 현장 연결 (솜부엉 기자, 뉴욕): CNBC 보도 + 엔비디아·3대 지수
bld = ''.join(f'<div class="abs" style="left:{x}px;bottom:150px;width:{w}px;height:{h}px;background:#3A4080;border:4px solid {L};border-radius:6px 6px 0 0"></div>'
              for x, w, h in [(20, 120, 260), (150, 90, 340), (700, 110, 300), (830, 120, 230)])
S[2] = (1, page(FX + f'''
{head("현장 연결 · 뉴욕", 2, "#F6EEE4")}
{screen(f"""
  <div class="abs" style="left:0;right:0;bottom:0;height:150px;background:#2A2F5E"></div>
  {bld}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), 330, 250, 320, .3, "a-pop", "squish")}
  {cbub("CNBC 보도: 엔비디아 이사회<br>젠슨 황 복귀 <b>검토 안 해</b>", 60, .5, style="font-size:42px", width=968)}
""", 44, 200, 982, 660, .05, "● 월가 현장")}
{lower_third("솜부엉 기자", "뉴욕 월가", 44 + P, 800, .4)}
<div class="panel a-pop" style="left:44px;top:930px;width:982px;height:420px;background:#FFF8E1;--d:1.1s">
  <div class="abs" style="left:0;width:982px;top:20px;text-align:center;font-size:46px">엔비디아 <span class="thump" style="--d:1.4s;color:{BLUE};font-size:72px">▼4.12%</span></div>
  {numbox("다우", "▼1.41%", COL3[0], 150, 1.6)}
  {numbox("S&amp;P500", "▼1.92%", COL3[1], 150, 1.75)}
  {numbox("나스닥", "▼2.49%", COL3[2], 150, 1.9)}
  <div class="abs a-fade" style="left:0;width:982px;top:330px;text-align:center;font-size:36px;color:#6B5A50;--d:2.2s">경영 불확실성이 길어진다는 걱정</div>
</div>
{ticker("엔비디아 3분기 실적, 17일(현지) 장 마감 후 발표", 1380, "현장")}
''', "#2B3060"))

# 3 ── 1분 해설: 차(칩)를 사 가는 길에 이어 렌터카(원격 접속)까지 허가제
CAR = f'<svg viewBox="0 0 120 70" width="150"><path d="M14 44 l10 -22 h58 l18 22 z" fill="#FFB27F" stroke="{L}" stroke-width="5" stroke-linejoin="round"/><rect x="6" y="40" width="108" height="18" rx="9" fill="#FFB27F" stroke="{L}" stroke-width="5"/><circle cx="32" cy="60" r="9" fill="{L}"/><circle cx="90" cy="60" r="9" fill="{L}"/></svg>'
KEY = f'<svg viewBox="0 0 120 70" width="150"><circle cx="34" cy="35" r="20" fill="#FFE59A" stroke="{L}" stroke-width="5"/><circle cx="34" cy="35" r="7" fill="#fff" stroke="{L}" stroke-width="4"/><path d="M54 35 h54 M92 35 v14 M104 35 v10" stroke="{L}" stroke-width="7" stroke-linecap="round"/></svg>'
def road(icon, t1, t2, col, d, lock_d, lock):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:470px;width:{w}px;height:270px;box-sizing:border-box;--d:{d}s;background:#fff;border:4px solid {L};border-radius:26px;text-align:center;padding-top:16px">'
            f'{icon}<div style="font-size:40px;line-height:1.25;margin-top:4px">{t1}</div><div style="font-size:30px;color:#6B5A50">{t2}</div>'
            f'<div class="stamp a-stamp" style="left:{w-170}px;top:-30px;--d:{lock_d}s;--r:12deg;font-size:40px;padding:0 14px">{lock}</div></div>')
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#F3EEFF;--d:.05s">
  {ch(mascot("moon", "normal", "point"), P, 40, 280, .2, "a-sl", "squish")}
  {lower_third("달떡이 박사", "반도체 규제 해설", 350, 50, .3)}
  {bub("칩을 사 가는 길에 이어<br><b>빌려 쓰는 길</b>까지 막았어요", 350, 150, .5, "t-left", style="font-size:40px")}
  <div class="abs a-fade" style="left:{P}px;top:380px;width:{IW}px;text-align:center;font-size:44px;--d:1.0s">미국산 AI칩 → 중국 기업</div>
  {road(CAR, "차(칩) 사 가기", "직접 수출", COL2[0], 1.2, 1.5, "규제")}
  {road(KEY, "렌터카로 빌려 타기", "원격 접속", COL2[1], 1.8, 2.2, "허가제")}
  {nar("싱가포르 등 동남아 4개국·브라질로 보낼 때도 <b>사전 허가</b>", P, 790, 2.7, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("마이크론", "▼7.62%", COL2[0], 900, 3.2)}
  {numbox("AMD", "▼5.58%", COL2[1], 900, 3.35)}
</div>
''', "#30366E"))

# 4 ── 시민 인터뷰 (한국)
mic = f'<svg viewBox="0 0 80 160" width="60"><rect x="22" y="4" width="36" height="56" rx="18" fill="#9AA3B8" stroke="{L}" stroke-width="5"/><rect x="34" y="60" width="12" height="90" rx="6" fill="#4A3838"/></svg>'
S[4] = (1, page(FX + f'''
{head("한국은요?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#E2F6EA;--d:.05s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:46px">어제(16일) 서울 코스피</div>
  <div class="abs" style="left:0;right:0;top:100px;text-align:center;font-size:190px;line-height:1"><span class="punch" style="--d:.15s;color:{BLUE};-webkit-text-stroke:8px {L};paint-order:stroke fill">▼3.59%</span></div>
  <div class="abs a-fade" style="left:0;right:0;top:300px;text-align:center;font-size:40px;color:#3B4A40;--d:.4s">5,100.50 · 5,100선 턱걸이</div>
  {numbox("삼성전자", "▼4.47%", COL2[0], 380, .7)}
  {numbox("SK하이닉스", "▼7.89%", COL2[1], 380, .85)}
  {nar("외국인 1조3천억원대 순매도 · <b>‘D램 담합’ 소송</b> 부담도", P, 560, 1.2, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("star", "worried", "up"), P, 690, 260, 1.6, "a-sl", "shiver")}
  <div class="abs a-pop" style="left:{P + 250}px;top:820px;--d:1.7s">{mic}</div>
  {bub("밤사이 미국 상장<br>SK하이닉스도 <b>7%대</b> 뚝!", 340, 680, 1.9, "t-left", style="font-size:40px")}
  <div class="abs a-pop" style="left:340px;top:900px;width:{982 - 340 - P}px;height:150px;box-sizing:border-box;--d:2.5s;background:#fff;border:4px solid {L};border-radius:24px;text-align:center">
    <div style="font-size:34px;margin-top:14px">그래도 반가운 소식 ⛽</div>
    <div style="font-size:48px">WTI 유가 <span style="color:{BLUE}">▼3.21%</span></div></div>
</div>
''', "#4A3E78"))

# 5 ── 클로징 체크 (복숭아빛)
items = [("chip", "반도체, 또 흔들릴까", "미국 반도체 <span style='color:#1D4ED8'>▼5.28%</span> 반영될지"),
         ("won", "엔비디아 실적 앞 눈치", "실적 확인 전까지 외국인 관망"),
         ("oil", "유가 하락은 숨통", "WTI <span style='color:#1D4ED8'>▼3.21%</span> · 물가·환율 부담")]
cards = "".join(
    f'<div class="panel a-sr" style="left:44px;top:{690+i*190}px;width:982px;height:164px;background:#fff;--d:{1.0+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ICONS[k]}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (k, t, d) in enumerate(items))
S[5] = (1, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("클로징 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:450px;background:#FFF8E1;--d:.05s">
  {live(40, 34, "밤사이 뉴스", .1)}
  {ch(mascot("bamtol", "normal", "point"), 40, 110, 280, .2, "a-sl", "squish")}
  {bub("오늘 한국장은<br>딱 <b>세 가지</b>만 보세요!", 380, 150, .45, "t-left", style="font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1270px;color:#6B5A50;--d:2.2s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스1, 뉴스핌, 서울경제, 이투데이, 연합뉴스</div>
{ticker("오늘 밤 엔비디아 3분기 실적 · 콘퍼런스콜은 내일(수) 아침 7시", 1380, "예고")}
''', "#FFE1CC"))

# 6 ── 예고·사인오프 (아침)
S[6] = (1, page(f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">오늘 밤 (미국 장 마감 후)</div>
  <div class="abs" style="left:44px;top:100px;font-size:66px;line-height:1.2">엔비디아<br>3분기 실적 발표</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.35s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.2s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .35, "a-sl", "hop")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 210, 290, .45, "a-sr", "squish")}
  {bub("이상, <b>밤사이 뉴스</b>였습니다!", 330, 40, .75, "t-down", "60%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.1s">출처: 이투데이, 파이낸셜뉴스, 뉴스핌, 뉴스1, MTN, SBS, 서울경제, 연합뉴스 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (5.0, 1.5), 4: (4.4, 1.6), 5: (3.8, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .8), (1, .05, "shutter", .6), (1, .2, "pop", .9), (1, .25, "slidedown", .7), (1, .45, "thud", 1), (1, .7, "blip_down", .9), (1, 1.2, "tension", .4),
 (2, .05, "whoosh", .6), (2, .3, "pop", .6), (2, .4, "tick", .8), (2, .5, "pop", .8), (2, 1.1, "whoosh", .5), (2, 1.4, "blip_down", .8), (2, 1.6, "pop", .6), (2, 1.75, "pop", .6), (2, 1.9, "pop", .6), (2, 2.2, "hmm", .5),
 (3, .2, "whoosh", .6), (3, .3, "tick", .8), (3, .5, "pop", .8), (3, 1.0, "tick", .7), (3, 1.2, "pop", .7), (3, 1.5, "thud", .8), (3, 1.8, "pop", .7), (3, 2.2, "thud", .9), (3, 2.7, "tick", .8), (3, 3.2, "blip_down", .7), (3, 3.35, "blip_down", .7),
 (4, .05, "whoosh", .5), (4, .15, "blip_down", 1), (4, .2, "thud", .8), (4, .4, "tick", .6), (4, .7, "pop", .6), (4, .85, "pop", .6), (4, 1.2, "tick", .8), (4, 1.6, "whoosh", .5), (4, 1.9, "pop", .8), (4, 2.5, "ding", .8),
 (5, .05, "news", .5), (5, .2, "whoosh", .5), (5, .45, "pop", .8), (5, 1.0, "CHECK1", 1), (5, 1.45, "CHECK2", 1), (5, 1.9, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .35, "whoosh", .5), (6, .45, "boing", .7), (6, .75, "pop", .8), (6, .9, "news", .6), (6, 1.0, "jingle", .9),
]
