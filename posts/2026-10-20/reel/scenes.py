"""형식: 밤사이 탐정 추리 v2 (검수 전 · 2026-10-20) — 10-17 '결론 먼저' 훅 규칙을 탐정 플롯에 처음 적용한 버전.
내용: 2026-10-20 (19일 뉴욕 — 필라델피아 반도체 ▲1.61%로 8거래일 연속 하락 끝, 나스닥 ▲1.11%). 비유: 8일 내리 값이 내려간 '할인 매대'에 손님이 몰렸다(저가 매수).
흐름: 1 사건 해결 선언(결론: ▲1.61% + '반도체 8일 만에 반등') → 2 용의자 셋 → 3 단서·주범(할인 매대) → 4 한국 현장 조사 → 5 수사 노트(체크 3) → 6 다음 사건 예고.
숫자는 2026-10-20 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes swing{0%{transform:rotate(-4deg)}50%{transform:rotate(-1.5deg)}100%{transform:rotate(-4deg)}}
@keyframes spot{0%{opacity:.0}35%{opacity:1}100%{opacity:1}}
@keyframes sweep{0%{transform:translateX(-260px) rotate(-14deg)}100%{transform:translateX(0) rotate(-14deg)}}
@keyframes linedraw{from{stroke-dashoffset:var(--len)}to{stroke-dashoffset:0}}
@keyframes tapeMove{from{transform:translateX(0)}to{transform:translateX(-520px)}}
.tape-run{animation:tapeMove 3s linear both}
.sweep{animation:sweep .7s cubic-bezier(.2,.9,.3,1) both}
</style>"""

TAPE = "범인 확보 · 밤사이 탐정 · 출입 금지 · " * 5

def tape(top, rot, d=0):
    return (f'<div class="abs" style="left:-80px;top:{top}px;width:1240px;height:80px;background:#FFD84D;border-top:6px solid {L};border-bottom:6px solid {L};'
            f'transform:rotate({rot}deg);overflow:hidden;box-shadow:0 8px 0 rgba(0,0,0,.25)">'
            f'<div class="tape-run" style="position:absolute;left:0;top:8px;white-space:nowrap;font-size:44px;line-height:56px;padding-left:20px;--d:{d}s">{TAPE}</div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·탐정(클로즈업)·폴리스 라인이 모두 보인다
#      0~1초: 숫자 펀치(0) → 상승 그래프 선 그리기(0~.7) → '범인 확보' 도장(.45) → 탐정 돋보기 쓸기(.6)
CHART = (f'<svg width="430" height="250" viewBox="0 0 430 250" style="overflow:visible">'
         f'<path d="M10 40 L60 70 L110 95 L160 120 L210 150 L260 170 L310 195 L350 215" fill="none" stroke="#7DBBFF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
         f'<path d="M350 215 L410 120" fill="none" stroke="{RED}" stroke-width="14" stroke-linecap="round" style="stroke-dasharray:130;--len:130;stroke-dashoffset:130;animation:linedraw .5s ease-out .2s both"/>'
         f'<circle cx="410" cy="120" r="14" fill="{RED}" stroke="{L}" stroke-width="4"/>'
         f'<text x="20" y="30" font-size="30" fill="#C9D6FF" font-family="Jua">8일 연속 ↓</text><text x="300" y="100" font-size="30" fill="#FF9DA0" font-family="Jua">19일 ↑</text></svg>')
S[1] = (1, page(FX + f'''
{stars(14, 20, 0, 260)}
<div class="abs" style="left:300px;top:720px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(255,236,170,.30) 0,rgba(255,236,170,.10) 45%,transparent 70%)"></div>
{head("밤사이 탐정 · 10.20 TUE", 1, "#F6EEE4")}
{tape(222, -3)}
<div class="abs" style="left:0;width:1080px;top:330px;text-align:center;font-size:46px;color:#C9D6FF">필라델피아 반도체지수 · 19일 뉴욕</div>
<div class="abs" style="left:0;width:1080px;top:385px;text-align:center"><span class="punch" style="--d:0s;font-size:252px;line-height:1;color:#FF7A7F;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲1.61%</span></div>
<div class="abs" style="left:0;width:1080px;top:632px;text-align:center;font-size:88px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">반도체, <span style="color:#FFE36E">8일 만에 반등!</span></div>
<div class="abs" style="left:44px;top:776px;width:360px;height:66px;background:#D9B06A;border:5px solid {L};border-bottom:none;border-radius:20px 20px 0 0;font-size:34px;line-height:62px;text-align:center">사건 파일 No.1020</div>
<div class="abs" style="left:44px;top:836px;width:982px;height:590px;box-sizing:border-box;background:#E9C98A;border:5px solid {L};border-radius:0 26px 26px 26px;box-shadow:0 8px 0 rgba(0,0,0,.22);overflow:hidden">
  <div class="abs" style="right:{P}px;top:26px;width:440px;height:280px;box-sizing:border-box;background:#14202A;border:5px solid {L};border-radius:20px;padding:14px 0 0 0">{CHART}</div>
  <div class="abs" style="right:{P}px;top:322px;width:440px;font-size:40px;line-height:1.3;color:#5A3A1A;text-align:center">2008년 이후 가장 길었던<br>연속 하락이 멈췄다</div>
</div>
<div class="abs" style="left:-10px;top:900px;width:540px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="squish">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
<div class="stamp a-stamp" style="left:560px;top:1322px;--d:.45s;--r:-8deg;font-size:70px;white-space:nowrap">범인 확보!</div>
''', "#262B55"))

# 2 ── 용의자 셋 (코르크 보드) — 다른 용의자를 '무죄'로 단정하지 않는다
def suspect(icon, name, note, col, d, rot, ncol):
    x, w = col
    return (pola(f'<div style="height:170px;font-size:110px;line-height:170px;background:#EEF1FA;text-align:center">{icon}</div>', name, x, 300, w, d, rot)
            + f'<div class="abs a-pop" style="left:{x}px;top:600px;width:{w}px;text-align:center;--d:{d + .3:.1f}s"><span class="tag" style="position:relative;background:{ncol}">{note}</span></div>')
S[2] = (1, page(FX + f'''
{head("용의자 셋", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cork(P, 240, IW, 470, .05)}
  {cbub("반도체를 <b>끌어올린 범인</b>은<br>이 셋 중 누구일까요?", 40, .1, "t-down", style="font-size:44px")}
  {suspect("🏷️", "저가 매수", "8일 내리 하락 뒤", COL3[0], .5, -4, RED)}
  {suspect("📄", "인텔 의견 상향", "JP모건", COL3[1], .8, 3, "#7B6FD6")}
  {suspect("🛢️", "기름값", "오히려 ▲2.22%", COL3[2], 1.1, -3, "#8A6A3A")}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 760, 320, 1.6, "a-sl", "squish")}
  {bub("기름값은 오히려<br><b>올랐는데</b>요?", 400, 820, 1.9, "t-left", style="font-size:46px")}
</div>
''', "#2B3060"))

# 3 ── 단서·주범 지목 (비유: 8일 내리 값이 내린 '할인 매대'에 손님이 몰렸다)
S[3] = (1, page(FX + f'''
{head("단서 분석", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("단서를 보면 주범은…<br><b>'싸다' 손님</b>이에요!", 30, .1, "t-down", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:240px;width:{IW}px;height:330px;box-sizing:border-box;background:#FFF6D6;border:5px solid {L};border-radius:26px;--d:.4s">
    <div class="abs" style="left:30px;top:20px;font-size:40px">반도체 할인 매대</div>
    <div class="abs" style="left:30px;top:80px;display:flex;gap:10px;align-items:flex-end">
      {"".join(f'<div style="width:46px;height:{200 - i*20}px;background:#9DB8EE;border:4px solid {L};border-radius:8px"></div>' for i in range(8))}
      <div class="a-pop" style="--d:1.0s;width:46px;height:110px;background:{RED};border:4px solid {L};border-radius:8px"></div></div>
    <div class="abs" style="left:640px;top:60px;font-size:120px;transform:rotate(-8deg)"><span class="thump" style="--d:.8s">🏷️</span></div>
    <div class="abs" style="left:600px;top:230px;font-size:40px;color:#C2410C">8일 내리 값↓</div>
  </div>
  {stamp("주범: 저가 매수", 200, 600, 1.3, -6)}
  {nar("값이 많이 내리자 <b>'이 정도면 싸다'</b>며<br>사려는 손님이 몰렸어요", P, 730, 1.8, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {nar("공범: JP모건의 <b>인텔 투자의견 상향</b>", P, 870, 2.3, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center;background:#E8E2FF")}
  {numbox("필라델피아 반도체", "▲1.61%", COL2[0], 980, 2.7, RED)}
  {numbox("나스닥", "▲1.11%", COL2[1], 980, 2.9, RED)}
</div>
''', "#30366E"))

# 4 ── 한국 현장 조사
S[4] = (1, page(FX + f'''
{head("한국 현장 조사", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:780px;height:400px;background:#CBE9D6;border-top:5px solid {L}"></div>
  {cbub("그보다 앞서 서울에선?<br>19일 코스피는 <b>장 초반 급락</b> 뒤<br><b>상승으로</b> 마쳤어요", 40, .2, "t-down", style="font-size:42px")}
  {ch(mascot("star", "happy", "up"), COL2[0][0] + 50, 380, 330, .5, "a-sl", "hop")}
  {ch(mascot("bamtol", "normal", "hold", p_mag()), COL2[1][0] + 50, 380, 330, .6, "a-sr", "squish2")}
  {numbox("코스피 (19일)", "▲1.76%", COL2[0], 830, 1.2, RED)}
  {numbox("원/달러 (19일)", "1,330.3원", COL2[1], 830, 1.5, L)}
  <div class="abs a-pop" style="left:{COL2[1][0]}px;top:1010px;width:{COL2[1][1]}px;text-align:center;font-size:36px;--d:1.8s">2년여 만에 최저 종가</div>
  <div class="abs a-pop" style="left:{COL2[0][0]}px;top:1010px;width:{COL2[0][1]}px;text-align:center;font-size:36px;--d:1.6s">5,768.01 마감</div>
</div>
''', "#4A3E78"))

# 5 ── 수사 노트 (오늘의 체크)
items = [(ICONS["chip"], "반도체, 바통 이어받을까", f"미국 반도체지수 <span style='color:#C92A2A'>▲1.61%</span>"),
         ("🛢️", "기름값 부담 여전", f"WTI 103.66달러 <span style='color:#C92A2A'>▲2.22%</span>"),
         (ICONS["won"], "외국인·환율은?", "원/달러 1,330.3원, 2년여 만에 최저")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{.7+i*.4:.1f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none;font-size:60px;width:70px;text-align:center">{ic}</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 노트 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFF8E1;--d:0s">
  {ch(mascot("bamtol", "normal", "point"), 600, 120, 290, .1, "a-sr", "squish")}
  {bub("반등이 하루로<br>끝나지 않으려면<br>이 <b>세 가지</b>!", P, 80, .25, "t-right", style="font-size:44px")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:1.8s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 서울경제, SBS Biz, 뉴스1, 한국경제, 로이터</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 사건 · 오늘 밤 (미국 현지 20일)</div>
  <div class="abs" style="left:44px;top:100px;font-size:66px;line-height:1.2">스페이스X<br>실적 발표</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.3s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("사건 종결!<br><b>밤사이 탐정</b>이었습니다", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, SBS Biz, 뉴스1, 한국경제, 서울경제, 로이터, 이데일리 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.8, 1.3), 2: (3.9, 1.5), 3: (4.6, 1.5), 4: (3.7, 1.5), 5: (4.0, 1.5), 6: (3.4, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .6), (1, .05, "thud", .8), (1, .2, "whoosh", .5), (1, .45, "thud", .9), (1, .5, "reveal", .6), (1, .6, "ding", .6),
 (2, .05, "whoosh", .5), (2, .1, "pop", .8), (2, .5, "shutter", .7), (2, .8, "shutter", .7), (2, 1.1, "shutter", .7), (2, 1.6, "whoosh", .5), (2, 1.9, "question", .6),
 (3, .1, "pop", .8), (3, .4, "pop", .6), (3, .8, "boing", .5), (3, 1.0, "pop", .6), (3, 1.3, "thud", 1), (3, 1.3, "reveal", .8), (3, 1.8, "tick", 1), (3, 2.3, "tick", .8), (3, 2.7, "ding", .8), (3, 2.9, "ding", .6),
 (4, .05, "whoosh", .5), (4, .2, "pop", .8), (4, .5, "boing", .6), (4, .6, "whoosh", .4), (4, 1.2, "sparkle", .7), (4, 1.5, "pop", .6),
 (5, .05, "whoosh", .5), (5, .25, "pop", .8), (5, .7, "CHECK1", 1), (5, 1.1, "CHECK2", 1), (5, 1.5, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
