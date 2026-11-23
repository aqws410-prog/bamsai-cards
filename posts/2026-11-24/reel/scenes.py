"""2026-11-24 릴스 · 토크쇼(talkshow) v5 — '결론 먼저' 훅, 장면 1 '스포트라이트 아래 다시 채워진 CEO 의자(빈 의자 → 착석 표시) + 이름표 + 복귀 도장 + 꽃가루' 새 구도 (검수 전).
그날 상황: 나스닥 ▲6.51%·S&P500 ▲4.73%(2025년 4월 이후 최대), 엔비디아 ▲31.48% 급변 → 상황표 첫 칸(급변) 1순위 news는 11-21에 써서(최근 3일 11-21 news·11-22 weather·11-23 chat)
          2순위 talkshow(마지막 11-20, 최근 3일 밖). 이사회 결정·한 인물(CEO) 복귀가 핵심이라 '한 인물' 칸과도 맞음.
흐름: 1 결론(엔비디아 ▲31.48% 'CEO 돌아오자 하루 만에 쑥!', CEO 의자) → 2 게스트 토크(역: 엔비디아 이사회, 만장일치·사임 11일 만·정부 의견·국가안보 위험 없음)
      → 3 쉬운 해설: 비유 '꺼졌던 등대에 불이 다시 켜지자 배들이 항구로' = 엔비디아 반등에 AI·반도체주 동반 반등 + 3대 지수
      → 4 방청객 질문: 한국은?(23일 코스피 ▼3.31% 4,708.54, 복귀 소식은 서울 마감 뒤) → 5 MC 큐카드(오늘 체크 3) → 6 다음 회 예고(델 실적·PCE·금통위).
숫자는 posts/2026-11-24 카드·sources.md에 있는 것만 쓴다. 실존 인물은 그리지 않고(빈 의자·이름표로만), 게스트 대사는 기사로 확인된 사실을 쉬운 말로 옮긴 역할극이다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes sweepL{0%{transform:rotate(-26deg)}50%{transform:rotate(-6deg)}100%{transform:rotate(-26deg)}}
@keyframes sweepR{0%{transform:rotate(26deg)}50%{transform:rotate(6deg)}100%{transform:rotate(26deg)}}
@keyframes flash{0%{opacity:0}20%{opacity:.8}100%{opacity:0}}
@keyframes conf{0%{transform:translateY(-80px) rotate(0)}100%{transform:translateY(760px) rotate(540deg)}}
@keyframes glow{0%,100%{box-shadow:0 0 0 0 rgba(255,226,120,.0)}50%{box-shadow:0 0 70px 24px rgba(255,226,120,.75)}}
@keyframes lbeam{0%{transform:rotate(-38deg)}50%{transform:rotate(38deg)}100%{transform:rotate(-38deg)}}
@keyframes sail{from{transform:translateX(var(--dx))}to{transform:translateX(0)}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.beamL{transform-origin:50% 0;animation:sweepL 1.3s ease-in-out infinite}
.beamR{transform-origin:50% 0;animation:sweepR 1.3s ease-in-out infinite}
.flash{animation:flash .35s ease-out both;animation-delay:var(--d,0s)}
.conf{animation:conf 1.6s linear infinite;animation-delay:var(--d,0s)}
.glow{animation:glow 1s ease-in-out infinite}
.lbeam{transform-origin:0 50%;animation:lbeam 2.4s ease-in-out infinite}
.sail{animation:sail .9s cubic-bezier(.2,.9,.3,1) both;animation-delay:var(--d,0s)}
.bob{animation:bob 1.2s ease-in-out infinite}
</style>"""

def p_mic():
    return (f'<path d="M204 222 L188 266" stroke="{L}" stroke-width="13" stroke-linecap="round"/>'
            f'<path d="M204 222 L188 266" stroke="#2F2F3A" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="212" cy="196" r="19" fill="#3A3A48" stroke="{L}" stroke-width="5"/>'
            f'<path d="M200 190 h24 M198 198 h28 M202 206 h20" stroke="#8C92AE" stroke-width="2.5"/>')

def beam(x, cls, d=0, h=640):
    return (f'<div class="abs {cls}" style="left:{x}px;top:-10px;width:0;height:0;border-left:110px solid transparent;border-right:110px solid transparent;'
            f'border-top:{h}px solid rgba(255,236,170,.22);margin-left:-110px;animation-delay:{d}s"></div>')

def sign(text, x, y, d, bg="#E03131", size=46, rot=-6):
    return (f'<div class="abs a-stamp" style="left:{x}px;top:{y}px;--d:{d}s;--r:{rot}deg;background:{bg};color:#fff;border:5px solid {L};'
            f'border-radius:16px;padding:6px 22px;font-size:{size}px;box-shadow:0 6px 0 rgba(0,0,0,.25);white-space:nowrap">{text}</div>')

def chair(x, y, w=300):
    """사장님 의자(CEO 의자) — 높은 등받이 가죽 의자."""
    return (f'<svg class="abs" style="left:{x}px;top:{y}px" width="{w}" height="{int(w*1.3)}" viewBox="0 0 200 260">'
            f'<rect x="38" y="8" width="124" height="138" rx="34" fill="#7A3E2B" stroke="{L}" stroke-width="7"/>'
            f'<path d="M62 30 v96 M100 26 v104 M138 30 v96" stroke="#5E2E20" stroke-width="5" stroke-linecap="round"/>'
            f'<rect x="22" y="132" width="156" height="42" rx="18" fill="#8C4A33" stroke="{L}" stroke-width="7"/>'
            f'<rect x="10" y="104" width="28" height="56" rx="12" fill="#5E2E20" stroke="{L}" stroke-width="6"/>'
            f'<rect x="162" y="104" width="28" height="56" rx="12" fill="#5E2E20" stroke="{L}" stroke-width="6"/>'
            f'<rect x="92" y="174" width="16" height="46" fill="#3A3A48" stroke="{L}" stroke-width="5"/>'
            f'<path d="M40 238 L100 216 L160 238" fill="none" stroke="{L}" stroke-width="9" stroke-linecap="round"/>'
            f'<circle cx="40" cy="244" r="10" fill="#3A3A48" stroke="{L}" stroke-width="4"/><circle cx="160" cy="244" r="10" fill="#3A3A48" stroke="{L}" stroke-width="4"/>'
            f'</svg>')

def confetti(n, seed, w, d0=0):
    rnd = random.Random(seed)
    cols = ["#FF6B6B", "#FFD43B", "#69DB7C", "#74C0FC", "#F783AC"]
    return "".join(f'<div class="abs conf" style="left:{rnd.randint(10, w - 20)}px;top:{rnd.randint(-40, 200)}px;width:18px;height:28px;'
                   f'background:{rnd.choice(cols)};border:3px solid {L};border-radius:4px;--d:{d0 + rnd.random() * 1.4:.2f}s"></div>' for _ in range(n))

# 1 ── 결론 먼저 (토크쇼 무대 · CEO 의자): 0초에 숫자·결론·MC(클로즈업, 놀람)·스포트라이트 속 의자가 모두 보인다
#      0~1초: 숫자 펀치(0) → 플래시(.05) → 의자 빛남(상시)·꽃가루(0~) → '복귀' 도장 쾅(.35) → MC 떨림(.5) → '쑥!' 효과 글자(.7)
S[1] = (1, page(FX + f'''
{stars(12, 24, 0, 200)}
{head("밤사이 토크쇼 · 11.24 TUE", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:48px;color:#FFE36E">어젯밤 엔비디아</div>
<div class="abs" style="left:0;width:1080px;top:258px;text-align:center"><span class="punch" style="--d:0s;font-size:226px;line-height:1;color:#FF6B6B;-webkit-text-stroke:11px {L};paint-order:stroke fill">▲31.48%</span></div>
<div class="abs" style="left:0;width:1080px;top:520px;text-align:center;font-size:78px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">CEO 돌아오자 <span style="color:#FFE36E">하루 만에 쑥!</span></div>
<div class="panel" style="left:44px;top:680px;width:982px;height:760px;background:#2C2450">
  {beam(700, "beamR", 0, 700)}{beam(300, "beamL", .3, 700)}
  <div class="abs" style="left:0;right:0;bottom:0;height:150px;background:#7A4E2E;border-top:6px solid {L}"></div>
  <div class="abs glow" style="left:560px;top:250px;width:320px;height:320px;border-radius:50%"></div>
  {chair(570, 170, 300)}
  <div class="abs" style="left:590px;top:96px;width:260px;text-align:center;background:#FFF8E1;border:5px solid {L};border-radius:14px;font-size:40px;padding:4px 0">CEO 자리</div>
  {stamp("복귀!", 650, 300, .35, -10)}
  <div class="abs" style="left:-10px;top:120px;width:520px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "hold", p_mic())}</div></div>
  {sfx("쑥!", 430, 70, 120, .7, 8, "#FF8A8F")}
  {confetti(10, 7, 982)}
  <div class="abs flash" style="left:0;right:0;top:0;bottom:0;background:#fff;--d:.05s"></div>
</div>
''', "#262B55"))

# 2 ── 게스트 토크 (달떡이가 '엔비디아 이사회' 역) — 기사로 확인된 사실만
S[2] = (1, page(FX + f'''
{head("게스트 토크", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3E3570;--d:0s">
  <div class="abs" style="left:{P}px;top:40px;width:{IW}px;box-sizing:border-box;background:#FFF8E1;border:5px solid {L};border-radius:22px;text-align:center;padding:10px 0">
    <div style="font-size:34px;color:#8A5A3B">오늘의 게스트 (역: 달떡이)</div>
    <div style="font-size:62px">엔비디아 <span style="color:#E8590C">이사회</span></div></div>
  {ch(mascot("moon", "happy", "point"), P, 560, 300, .2, "a-sl", "squish")}
  {bub("사임 <b>11일 만에</b><br>CEO로 다시 모셨어요", 300, 250, .4, "t-down", "25%", "font-size:46px")}
  {bub("미국 정부 의견도 듣고<br><b>국가안보 위험 없다</b>고 봤죠", 360, 560, 1.2, "t-left", style="font-size:42px")}
  {sign("만장일치", 380, 790, 1.8, "#7E5BB8", 54, -4)}
  {ch(mascot("bamtol", "surprised", "hold", p_mic()), 680, 840, 220, 2.0, "a-sr", "squish2")}
  {sign("엔비디아 ▲31.48%", 70, 990, 2.3, RED, 62, -3)}
</div>
''', "#2B3060"))

# 3 ── 1분 해설 — 꺼졌던 등대에 불이 다시 켜지자 배들이 항구로
def boat(label, y, d, dx, col="#FFD9A8"):
    return (f'<div class="abs sail" style="left:470px;top:{y}px;--d:{d}s;--dx:{dx}px"><div class="bob">'
            f'<svg width="420" height="120" viewBox="0 0 420 120"><path d="M10 50 H410 L370 112 H50 Z" fill="{col}" stroke="{L}" stroke-width="6" stroke-linejoin="round"/></svg>'
            f'<div class="abs" style="left:0;top:52px;width:420px;text-align:center;font-size:40px">{label}</div></div></div>')
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#22305E;--d:0s">
  {stars(10, 5, 160, 420, 0, 960)}
  <div class="abs" style="left:0;right:0;top:620px;height:560px;background:#2F5D9E;border-top:6px solid {L}"></div>
  <div class="abs" style="left:190px;top:290px;width:0;height:0"><div class="lbeam a-fade" style="--d:.5s;width:620px;height:0;border-top:70px solid transparent;border-bottom:70px solid transparent;border-left:620px solid rgba(255,230,120,.45);margin-top:-70px"></div></div>
  <svg class="abs" style="left:{P + 60}px;top:200px" width="180" height="440" viewBox="0 0 180 440">
    <path d="M50 120 L130 120 L150 440 L30 440 Z" fill="#FFF6EA" stroke="{L}" stroke-width="7"/>
    <path d="M42 230 H138 M36 330 H144" stroke="#E03131" stroke-width="26"/>
    <rect x="40" y="56" width="100" height="68" rx="10" fill="#FFE36E" stroke="{L}" stroke-width="7"/>
    <path d="M30 60 L90 10 L150 60 Z" fill="#E03131" stroke="{L}" stroke-width="7" stroke-linejoin="round"/></svg>
  <div class="abs a-pop" style="left:{P + 20}px;top:640px;--d:.4s;background:#FFF8E1;border:4px solid {L};border-radius:16px;padding:4px 18px;font-size:36px">등대 = 엔비디아</div>
  {boat("AI주", 500, .9, 520)}
  {boat("반도체주", 630, 1.3, 520, "#C7E2FF")}
  {numbox("다우", "▲3.01%", COL3[0], 800, 1.9, RED)}
  {numbox("S&amp;P500", "▲4.73%", COL3[1], 800, 2.05, RED)}
  {numbox("나스닥", "<span class='thump' style='--d:2.4s'>▲6.51%</span>", COL3[2], 800, 2.2, RED)}
  {stamp("2025년 4월 이후 최대", 170, 1010, 2.7, -4)}
  {cbub("꺼졌던 <b>등대</b>에 불이 다시 켜지자<br>배들이 줄줄이 돌아왔어요", 30, .1, "t-down", style="font-size:44px")}
</div>
''', "#30366E"))

# 4 ── 방청객 질문: 한국은? (23일 서울)
S[4] = (1, page(FX + f'''
{head("방청객 질문", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {ch(mascot("star", "worried", "up"), P, 40, 240, .1, "a-sl", "squish")}
  {bub("한국 증시는<br><b>어땠어요?</b>", 300, 70, .3, "t-left", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:330px;width:{IW}px;--d:.7s;text-align:center">
    <div style="font-size:40px">코스피 (23일 종가 4,708.54)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.9s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼3.31%</span></div></div>
  {numbox("삼성전자", "▼3.06%", COL2[0], 580, 1.3, BLUE)}
  {numbox("SK하이닉스", "▼2.52%", COL2[1], 580, 1.45, BLUE)}
  {nar("매도 <b>사이드카</b> 이틀 연속<br>(프로그램 매도 5분 멈춤)", P, 790, 1.9, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("bamtol", "normal", "hold", p_mic()), 652, 940, 230, 2.4, "a-sr", "squish2")}
  {bub("복귀 소식은<br><b>서울 장 끝난 뒤</b>예요", 190, 980, 2.6, "t-right", style="font-size:42px")}
</div>
''', "#4A3E78"))

# 5 ── MC 큐카드 (오늘 한국장 체크 3)
def cue(n, title, sub, y, d, rot):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="transform:rotate({rot}deg);background:#FFFFFF;border:5px solid {L};border-radius:14px;padding:18px 28px 18px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#E7ECF7 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#7E5BB8;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:48px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("MC 큐카드 · 오늘 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#8E6CC8;--d:0s">
  <div class="abs" style="left:{P}px;top:36px;font-size:58px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill">오늘 한국장, 볼 것은 셋</div>
  {cue(1, "반도체, 따라 오를까", "복귀 소식 반영되면 반도체 업종 반등 가능성", 150, .4, -1.2)}
  {cue(2, "외국인, 돌아올까", "7거래일 연속 순매도, 멈추면 부담 줄 가능성", 360, .8, 1)}
  {cue(3, "환율 1,350원 고비", "더 오르면 외국인 수급에 부담 가능성", 570, 1.2, -1)}
  {ch(mascot("bamtol", "happy", "point"), 640, 790, 240, 1.7, "a-sr", "squish")}
  {bub("큐카드 셋,<br><b>꼭 챙겨요!</b>", 300, 830, 1.9, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.1s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 서울경제, 헤럴드경제, 산경투데이, 아시아경제, 재경일보</div>
''', "#FFE1CC"))

# 6 ── 다음 회 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 토크쇼 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 회 예고</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">오늘 밤 델 실적<br>25일 PCE · 26일 금통위</div>
  <div class="abs a-rise" style="left:44px;top:320px;--d:.3s;font-size:44px">내일 아침 <span style="color:#FFC08A">8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("moon", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 210, 290, .4, "a-sr", "hop")}
  {bub("오늘 토크쇼는 여기까지!<br><b>박수~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 헤럴드경제, 이투데이, 파이낸셜뉴스, 뉴스1, 로이터, 야후파이낸스, 서울경제 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.0, 1.5), 3: (4.6, 1.6), 4: (4.2, 1.5), 5: (3.4, 1.45), 6: (3.0, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "applause", .7), (1, .05, "shutter", .8), (1, .1, "sparkle", .6), (1, .35, "thud", .9), (1, .5, "tension", .4), (1, .7, "yay", .6),
 (2, .0, "mic", .7), (2, .2, "whoosh", .5), (2, .4, "pop", .8), (2, 1.2, "pop", .7), (2, 1.8, "thud", .8), (2, 2.0, "boing", .6), (2, 2.3, "sparkle", .7),
 (3, .1, "pop", .8), (3, .5, "ding", .7), (3, .9, "whoosh", .5), (3, 1.3, "whoosh", .5), (3, 1.9, "sunrise", .5), (3, 2.05, "pop", .5), (3, 2.2, "pop", .6), (3, 2.7, "thud", .8),
 (4, .1, "whoosh", .5), (4, .3, "question", .7), (4, .7, "dundun", .6), (4, .9, "blip_down", .7), (4, 1.3, "blip_down", .6), (4, 1.45, "blip_down", .5), (4, 1.9, "tick", .8), (4, 2.4, "boing", .5), (4, 2.6, "pop", .8),
 (5, .05, "whoosh", .5), (5, .4, "CHECK1", 1), (5, .8, "CHECK2", 1), (5, 1.2, "CHECK3", 1), (5, 1.9, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "applause", .6), (6, .9, "jingle", .9),
]
