"""형식: 밤사이 토크쇼 (처음 제작, 검수 전 · 2026-10-31) — 밤톨이 MC, 달떡이 게스트(인텔 역), 솜부엉 패널, 별콩이 방청객.
내용: 2026-10-31 (30일 뉴욕 — 인텔 하루 약 29% 폭락, 1974년 이후 최악 · 나스닥 ▼2.86%). 비유: AI 잔치 계산서(투자비)는 쌓이는데 손님(수익)은 언제 오나.
흐름: 1 결론 먼저(▼약 29% + '1974년 이후 최악', 무대·조명·박수 팻말) → 2 게스트 발언(인텔 역: 4분기 전망 기대 이하, PC 수요 부진) → 3 쉬운 해설(AI 잔치 계산서, 아마존 424억 달러)
     → 4 방청객 질문: 한국은?(30일 코스피·하이닉스·외국인) → 5 MC 큐카드(월요일 체크 3) → 6 다음 회 예고(내일 이번 주 성적표 · 11/3 중간선거).
숫자는 2026-10-31 카드·sources.md에 있는 것만 쓴다. 게스트 대사는 기사로 확인된 사실을 쉬운 말로 옮긴 역할극이다(실제 발언 인용 아님).
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes sweepL{0%{transform:rotate(-28deg)}50%{transform:rotate(-8deg)}100%{transform:rotate(-28deg)}}
@keyframes sweepR{0%{transform:rotate(28deg)}50%{transform:rotate(8deg)}100%{transform:rotate(28deg)}}
@keyframes flash{0%{opacity:0}20%{opacity:.8}100%{opacity:0}}
@keyframes neon{0%,100%{opacity:1}48%{opacity:1}50%{opacity:.35}52%{opacity:1}}
@keyframes billow{0%,100%{transform:scaleX(1)}50%{transform:scaleX(1.03)}}
@keyframes billowR{0%,100%{transform:scaleX(1)}50%{transform:scaleX(1.03)}}
@keyframes paper{0%{transform:translateY(0) rotate(0)}100%{transform:translateY(60px) rotate(25deg);opacity:0}}
.beamL{transform-origin:50% 0;animation:sweepL 1.2s ease-in-out infinite}
.beamR{transform-origin:50% 0;animation:sweepR 1.2s ease-in-out infinite}
.flash{animation:flash .35s ease-out both;animation-delay:var(--d,0s)}
.neon{animation:neon 1.1s steps(1) infinite}
.curL{transform-origin:0 0;animation:billow 2s ease-in-out infinite}
.curR{transform-origin:100% 0;animation:billowR 2s ease-in-out infinite}
</style>"""

def p_mic():
    """마이크 (캐릭터 오른손 쪽) — 검은 그릴 헤드 + 손잡이."""
    return (f'<path d="M204 222 L188 266" stroke="{L}" stroke-width="13" stroke-linecap="round"/>'
            f'<path d="M204 222 L188 266" stroke="#2F2F3A" stroke-width="7" stroke-linecap="round"/>'
            f'<rect x="192" y="212" width="26" height="12" rx="3" fill="#E03131" stroke="{L}" stroke-width="3" transform="rotate(20 205 218)"/>'
            f'<circle cx="212" cy="196" r="19" fill="#3A3A48" stroke="{L}" stroke-width="5"/>'
            f'<path d="M200 190 h24 M198 198 h28 M202 206 h20" stroke="#8C92AE" stroke-width="2.5"/>')

def curtains(h):
    """무대 커튼(좌우) + 위 주름 장식."""
    fold = "".join(f'<div style="position:absolute;left:{i*36}px;top:0;width:18px;height:100%;background:rgba(0,0,0,.14)"></div>' for i in range(4))
    return (f'<div class="abs curL" style="left:0;top:0;width:150px;height:{h}px;background:#B8323F;border-right:5px solid {L}">{fold}</div>'
            f'<div class="abs curR" style="right:0;top:0;width:150px;height:{h}px;background:#B8323F;border-left:5px solid {L}">{fold}</div>'
            f'<div class="abs" style="left:0;right:0;top:0;height:54px;background:repeating-radial-gradient(circle at 50% 0,#D2434F 0 30px,#B8323F 30px 34px);border-bottom:5px solid {L}"></div>')

def beam(x, cls, d=0):
    return (f'<div class="abs {cls}" style="left:{x}px;top:-10px;width:0;height:0;border-left:90px solid transparent;border-right:90px solid transparent;'
            f'border-top:640px solid rgba(255,236,170,.20);margin-left:-90px;animation-delay:{d}s"></div>')

def sign(text, x, y, d, bg="#E03131", size=46, rot=-6):
    return (f'<div class="abs a-stamp" style="left:{x}px;top:{y}px;--d:{d}s;--r:{rot}deg;background:{bg};color:#fff;border:5px solid {L};'
            f'border-radius:16px;padding:6px 22px;font-size:{size}px;box-shadow:0 6px 0 rgba(0,0,0,.25);white-space:nowrap">{text}</div>')

# 1 ── 결론 먼저 (토크쇼 무대): 0초에 네온 간판·숫자·결론·MC(클로즈업, 놀람)·무대가 모두 보인다
#      0~1초: 숫자 펀치(0) → 조명 플래시(.05) → 'ON AIR' 불빛·스포트라이트 흔들(상시) → '방청객 술렁' 팻말 쾅(.35) → MC 떨림(.5) → '헉!' 효과 글자(.7)
S[1] = (1, page(FX + f'''
{stars(12, 31, 0, 200)}
{head("밤사이 토크쇼 · 10.31 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center"><span class="neon" style="display:inline-block;border:5px solid #FF8FD0;border-radius:20px;padding:2px 30px;font-size:46px;color:#FFD1EE;text-shadow:0 0 14px #FF5CB8;box-shadow:0 0 18px #FF5CB8">★ 오늘의 게스트: 인텔 ★</span></div>
<div class="abs" style="left:0;width:1080px;top:290px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#7DB0FF;-webkit-text-stroke:11px {L};paint-order:stroke fill">▼약 29%</span></div>
<div class="abs" style="left:0;width:1080px;top:540px;text-align:center;font-size:82px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">1974년 이후 <span style="color:#FFE36E">최악의 하루!</span></div>
<div class="panel" style="left:44px;top:690px;width:982px;height:730px;background:#2C2450">
  {beam(290, "beamL")}{beam(690, "beamR", .3)}
  {curtains(730)}
  <div class="abs" style="left:0;right:0;bottom:0;height:150px;background:#7A4E2E;border-top:6px solid {L}"></div>
  <div class="abs" style="left:170px;top:90px;width:470px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "hold", p_mic())}</div></div>
  <div class="abs" style="left:640px;top:110px;width:190px;text-align:center;background:#E03131;color:#fff;border:5px solid {L};border-radius:14px;font-size:40px;padding:4px 0"><span class="neon">● ON AIR</span></div>
  {sfx("헉!", 660, 250, 120, .7, 8, "#FFE36E")}
  <div class="abs flash" style="left:0;right:0;top:0;bottom:0;background:#fff;--d:.05s"></div>
</div>
{sign("방청객 술렁…", 300, 1340, .35, "#3A2A5C", 56, -4)}
''', "#262B55"))

# 2 ── 게스트 발언 (달떡이가 인텔 역) — 기사로 확인된 사실만 쉬운 말로
S[2] = (1, page(FX + f'''
{head("게스트 토크", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3E3570;--d:0s">
  {curtains(1180)}
  <div class="abs" style="left:170px;top:120px;width:642px;height:150px;background:#FFF8E1;border:5px solid {L};border-radius:22px;text-align:center;box-shadow:0 6px 0 rgba(0,0,0,.2)" >
    <div style="font-size:34px;color:#8A5A3B;margin-top:14px">오늘의 게스트 (역: 달떡이)</div>
    <div style="font-size:64px">반도체 회사 <span style="color:#E8590C">인텔</span></div></div>
  {ch(mascot("moon", "teary", "down"), 170, 560, 300, .2, "a-sl", "squish")}
  <div class="abs" style="left:150px;top:830px;width:360px;height:110px;background:#7E5BB8;border:5px solid {L};border-radius:40px 40px 14px 14px"></div>
  {bub("다음 분기(4분기) 성적 전망이<br><b>기대에 못 미쳤어요…</b>", 300, 320, .4, "t-down", "30%", "font-size:44px")}
  {bub("PC가 덜 팔려서요", 480, 560, 1.2, "t-left", style="font-size:44px")}
  {ch(mascot("bamtol", "surprised", "hold", p_mic()), 600, 700, 230, 1.6, "a-sr", "squish2")}
  {sign("주가 ▼약 29%", 250, 1000, 2.0, "#2F6BD8", 64, -5)}
</div>
''', "#2B3060"))

# 3 ── 쉬운 해설 (비유: AI 잔치 계산서) — 솜부엉 패널
def receipt(y, d, txt):
    return (f'<div class="abs a-drop" style="left:{P + 40}px;top:{y}px;width:330px;--d:{d}s;background:#fff;border:4px solid {L};border-radius:6px;'
            f'padding:6px 14px;font-size:34px;box-shadow:0 4px 0 rgba(0,0,0,.12)">{txt}</div>')
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("AI는 큰 <b>잔치</b>라고 생각해 봐요.<br>빅테크가 잔치 준비에 돈을 쏟는 중!", 30, .1, "t-down", style="font-size:42px")}
  {receipt(250, .4, "🧾 데이터센터")}{receipt(320, .55, "🧾 AI 칩")}{receipt(390, .7, "🧾 전기·서버")}
  <div class="abs a-pop" style="left:{P + 40}px;top:470px;width:330px;--d:.9s;text-align:center;font-size:40px;color:#E8590C">계산서 산더미</div>
  <div class="abs a-pop" style="left:{P + 470}px;top:250px;width:432px;height:260px;box-sizing:border-box;--d:1.1s;background:#FFF8E1;border:4px solid {L};border-radius:24px;text-align:center;padding-top:30px">
    <div style="font-size:70px">🚪❓</div><div style="font-size:40px;line-height:1.3">돈 내는 손님(수익)은<br>언제 오지?</div></div>
  {numbox("아마존 · 1년간 빠져나간 현금", "424억 달러", (P, IW), 560, 1.7, BLUE)}
  {ch(mascot("owl", "worried", "hold", p_tablet()), P, 740, 240, 2.2, "a-sl", "squish")}
  {bub("그래서 잔치에 <b>칩을 납품</b>하던<br>반도체 가게까지 긴장했어요", 320, 780, 2.5, "t-left", style="font-size:40px")}
  {numbox("엔비디아", "▼약 4%", COL2[0], 1020, 3.1, BLUE)}
  {numbox("필라델피아 반도체", "▼ 급락", COL2[1], 1020, 3.3, BLUE)}
</div>
''', "#30366E"))

# 4 ── 방청객 질문: 한국은? (30일 서울)
S[4] = (1, page(FX + f'''
{head("방청객 질문", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {ch(mascot("star", "worried", "up"), P, 40, 240, .1, "a-sl", "squish")}
  {bub("한국 증시는<br><b>괜찮았어요?</b>", 300, 70, .3, "t-left", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:330px;width:{IW}px;--d:.7s;text-align:center">
    <div style="font-size:40px">코스피 (30일 종가)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.9s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼3.48%</span></div></div>
  {numbox("SK하이닉스", "▼7.08%", COL2[0], 580, 1.3, BLUE)}
  {numbox("삼성전자", "▼3.02%", COL2[1], 580, 1.45, BLUE)}
  {nar("외국인이 <b>1조6천억 원대</b>를 팔았고<br>장중엔 매도 <b>사이드카</b>(프로그램 매도 5분 정지)까지", P, 790, 2.0, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("bamtol", "worried", "hold", p_mic()), 620, 940, 230, 2.5, "a-sr", "squish2")}
  {bub("금요일 밤 미국 급락,<br><b>월요일</b> 반응을 봐요", 160, 980, 2.7, "t-right", style="font-size:40px")}
</div>
''', "#4A3E78"))

# 5 ── MC 큐카드 (월요일 한국장 체크 3)
def cue(n, title, sub, y, d, rot):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="transform:rotate({rot}deg);background:#FFFFFF;border:5px solid {L};border-radius:14px;padding:18px 28px 18px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#E7ECF7 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#7E5BB8;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:48px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("MC 큐카드 · 월요일 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#8E6CC8;--d:0s">
  <div class="abs" style="left:{P}px;top:36px;font-size:58px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill">월요일 한국장, 볼 것은 셋</div>
  {cue(1, "반도체, 충격 견딜까", "미국 반도체주 급락이 이어지면 부담 가능성", 150, .5, -1.2)}
  {cue(2, "외국인이 돌아올까", "30일 1조6천억 원대 순매도, 멈추는지 확인", 360, .95, 1)}
  {cue(3, "기름값·중동 긴장", "유가 더 오르면 물가·금리 걱정 커질 가능성", 570, 1.4, -1)}
  {ch(mascot("bamtol", "normal", "point"), 640, 790, 240, 2.0, "a-sr", "squish")}
  {bub("큐카드 셋,<br><b>꼭 챙겨요!</b>", 300, 830, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: AP, 로이터, 뉴스핌, MTN, 비즈니스코리아</div>
''', "#FFE1CC"))

# 6 ── 다음 회 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 토크쇼 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 회 예고</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">내일은 이번 주 성적표<br>11/3 미국 중간선거</div>
  <div class="abs a-rise" style="left:44px;top:320px;--d:.3s;font-size:44px">내일 아침 <span style="color:#FFC08A">8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("moon", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 210, 290, .4, "a-sr", "hop")}
  {bub("오늘 토크쇼는 여기까지!<br><b>박수~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, MTN, AP, 로이터, 더스트리트, 비즈니스코리아 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (5.0, 1.6), 4: (4.4, 1.5), 5: (3.6, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "applause", .7), (1, .05, "shutter", .8), (1, .1, "blip_down", .6), (1, .35, "thud", .9), (1, .4, "hmm", .6), (1, .5, "tension", .5), (1, .7, "sparkle", .5),
 (2, .0, "mic", .7), (2, .2, "whoosh", .5), (2, .4, "pop", .8), (2, 1.2, "pop", .7), (2, 1.6, "boing", .6), (2, 2.0, "thud", .9), (2, 2.0, "blip_down", .6),
 (3, .1, "pop", .8), (3, .4, "tick", .6), (3, .55, "tick", .6), (3, .7, "tick", .6), (3, .9, "boing", .5), (3, 1.1, "question", .6), (3, 1.7, "blip_down", .7), (3, 2.2, "whoosh", .5), (3, 2.5, "pop", .8), (3, 3.1, "blip_down", .6), (3, 3.3, "slidedown", .5),
 (4, .1, "whoosh", .5), (4, .3, "question", .7), (4, .7, "dundun", .6), (4, .9, "blip_down", .7), (4, 1.3, "blip_down", .6), (4, 1.45, "blip_down", .5), (4, 2.0, "tick", .8), (4, 2.5, "boing", .5), (4, 2.7, "pop", .8),
 (5, .05, "whoosh", .5), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "applause", .6), (6, .9, "jingle", .9),
]
