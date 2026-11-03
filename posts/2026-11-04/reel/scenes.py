"""형식: 밤사이 택배 추적 v2 (검수 전 · 2026-11-04) — 장면 1을 '물류센터 컨베이어 벨트 + 바코드 스캐너' 구도로 새로 짠 버전.
내용: 2026-11-04 (3일 서울 코스피 ▼3.59% 급락 → 그날 밤 미국 반도체 ▲2.63% 반등). 비유: 어제 서울엔 '반도체 걱정' 상자, 오늘 밤 뉴욕에선 '반도체 반등' 상자 출발 / 선거 개표 = 배송길 '공사 중' 안내판(변수).
흐름: 1 결론 먼저(▲2.63% + '미국 반도체, 하루 만에 반등!', 컨베이어) → 2 어제 도착한 상자(코스피 ▼3.59%·삼성·하이닉스) → 3 오늘 밤 발송된 상자(나스닥 ▲0.83%·MS ▲2.74% / 애플 ▼1.90%·다우 ▼0.38%)
     → 4 배송길 변수(선거 개표 오전 8시·상원 오후) → 5 받는 사람 체크 3 → 6 배송 일정·마무리.
숫자는 2026-11-04 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes belt{to{background-position:-120px 0}}
@keyframes slideIn{from{transform:translateX(-520px)}to{transform:translateX(0)}}
@keyframes scanbeam{0%,100%{opacity:.25}50%{opacity:.9}}
@keyframes roll{to{transform:rotate(360deg)}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes cone{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
.belt{background:repeating-linear-gradient(90deg,#5A5F72 0 60px,#4A4F60 60px 120px);animation:belt .35s linear infinite}
.slidein{animation:slideIn .55s cubic-bezier(.2,.9,.3,1.2) both;animation-delay:var(--d,0s)}
.beam{animation:scanbeam .3s ease-in-out infinite}
.roll{animation:roll .6s linear infinite}
.bob{animation:bob .3s ease-in-out infinite}
.cone{transform-origin:50% 100%;animation:cone .5s ease-in-out infinite}
</style>"""

CAP = (f'<path d="M92 118 Q96 70 150 68 Q204 70 208 118 Z" fill="#2F6BD8" stroke="{L}" stroke-width="3.6" stroke-linejoin="round"/>'
       f'<path d="M150 118 Q200 112 236 126 Q212 136 150 128 Z" fill="#2457B8" stroke="{L}" stroke-width="3.6" stroke-linejoin="round"/>'
       f'<rect x="132" y="84" width="36" height="22" rx="6" fill="#FFD84D" stroke="{L}" stroke-width="3"/>')

def box(w=200, label="반도체", tape="#FFF2C4"):
    return (f'<svg viewBox="0 0 200 170" width="{w}" height="{w*0.85:.0f}"><path d="M20 50 L100 20 L180 50 L100 80 Z" fill="#E7B47E" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M20 50 L20 135 L100 162 L100 80 Z" fill="#C98E55" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M180 50 L180 135 L100 162 L100 80 Z" fill="#D9A06A" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M60 35 L140 65" stroke="{tape}" stroke-width="12"/>'
            f'<rect x="112" y="98" width="56" height="34" rx="4" fill="#fff" stroke="{L}" stroke-width="3" transform="skewY(-18)"/>'
            f'<text x="140" y="164" text-anchor="middle" font-size="18" font-family="Jua" fill="{L}" transform="skewY(-18)">{label}</text></svg>')

def label(text, sub, color):
    return (f'<div style="background:#fff;border:5px solid {L};border-radius:16px;padding:10px 20px;text-align:center;box-shadow:0 5px 0 rgba(0,0,0,.18)">'
            f'<div style="font-size:30px;color:#6B5A50">{sub}</div><div style="font-size:46px;color:{color};line-height:1.1">{text}</div></div>')

def appbar(text, right=""):
    return (f'<div class="abs" style="left:0;right:0;top:0;height:88px;background:#FFB27F;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">{text}'
            f'<span style="position:absolute;right:30px;font-size:32px">{right}</span></div>')

# 1 ── 결론 먼저 (물류센터): 0초에 숫자·결론·컨베이어·상자·스캐너·밤톨이(클로즈업, 놀람)가 모두 보인다
#      0~1초: 숫자 펀치(0) + 삑 → 상자 미끄러져 들어옴(.0~.55, 처음부터 화면 안) → '분류 완료' 도장(.35) → 밤톨이 떨림 → '서울행' 효과 글자(.7)
S[1] = (1, page(FX + f'''
{stars(14, 41, 0, 180)}
{head("밤사이 택배 · 11.4 WED", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:190px;text-align:center;font-size:44px;color:#C9D6FF">코스피 급락한 그날 밤 · 미국 반도체지수</div>
<div class="abs" style="left:0;width:1080px;top:248px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#FF6B6F;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲2.63%</span></div>
<div class="abs" style="left:0;width:1080px;top:494px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">미국 반도체, <span style="color:#FFE36E">하루 만에 반등!</span></div>
<div class="panel" style="left:44px;top:640px;width:982px;height:760px;background:#3C3550">
  <div class="abs" style="left:0;right:0;top:0;height:300px;background:repeating-linear-gradient(90deg,#463E5E 0 140px,#3C3550 140px 280px)"></div>
  <div class="abs" style="left:{P}px;top:24px;background:#FFD84D;border:4px solid {L};border-radius:12px;padding:2px 22px;font-size:38px">🏭 밤사이 물류센터 · 뉴욕 → 서울</div>
  <div class="abs" style="left:560px;top:110px;width:120px;height:70px;background:#2A2F3E;border:5px solid {L};border-radius:14px"></div>
  <div class="abs beam" style="left:600px;top:178px;width:0;height:0;border-left:90px solid transparent;border-right:90px solid transparent;border-top:200px solid rgba(255,80,80,.45);margin-left:-50px"></div>
  <div class="abs belt" style="left:0;right:0;top:420px;height:46px;border-top:5px solid {L};border-bottom:5px solid {L}"></div>
  <div class="abs" style="left:0;right:0;top:470px;height:30px;display:flex;justify-content:space-around">{"".join(f'<div class="roll" style="width:30px;height:30px;border-radius:50%;background:#C9CDD8;border:4px solid {L};box-sizing:border-box;border-top-color:#888"></div>' for _ in range(9))}</div>
  <div class="abs slidein" style="left:470px;top:180px;--d:0s"><div class="bob">{box(250, "반도체")}</div></div>
  <div class="abs a-pop" style="left:690px;top:230px;--d:.5s;transform:rotate(6deg)">{label("반등", "내용물", RED)}</div>
  <div class="abs" style="left:-30px;top:280px;width:440px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.6s">{mascot("bamtol", "surprised", "up", CAP)}</div></div>
  {sfx("서울행!", 560, 560, 92, .7, -6, "#FFE36E")}
</div>
{sfx("삑!", 800, 600, 92, .0, 10, "#FFE36E")}
<div class="stamp a-stamp" style="left:560px;top:1210px;--d:.35s;--r:-8deg;font-size:62px;white-space:nowrap">분류 완료</div>
''', "#262B55"))

# 2 ── 어제(3일) 서울에 도착한 상자: 반도체 걱정 → 코스피 급락
S[2] = (1, page(FX + f'''
{head("어제 도착한 택배 · 서울", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFFDF6;--d:0s">
  {appbar("📦 3일 배송 완료 · 받은 곳 코스피")}
  <div class="abs a-drop" style="left:{P}px;top:130px;--d:.1s">{box(220, "걱정")}</div>
  <div class="abs a-pop" style="left:290px;top:150px;--d:.25s;font-size:46px;line-height:1.35">어제 서울엔<br><b style="color:{BLUE};font-weight:400">'반도체 걱정'</b> 상자가<br>도착했어요</div>
  <div class="abs" style="left:0;right:0;top:400px;text-align:center"><div style="font-size:42px;color:#6B5A50">코스피 · 3일 종가</div>
    <div style="font-size:170px;line-height:1.05"><span class="thump" style="--d:.6s;color:{BLUE};-webkit-text-stroke:6px {L};paint-order:stroke fill">▼3.59%</span></div></div>
  {numbox("삼성전자", "▼4.15%", COL2[0], 660, 1.0, BLUE)}
  {numbox("SK하이닉스", "▼5.03%", COL2[1], 660, 1.2, BLUE)}
  {ch(mascot("star", "teary", "up"), P, 860, 260, 1.5, "a-sl", "shiver")}
  {bub("외국인·기관이<br><b>함께 팔았대요</b>", 340, 900, 1.7, "t-left", style="font-size:46px")}
</div>
''', "#2B3060"))

# 3 ── 오늘 밤 뉴욕에서 발송된 상자: 반도체 반등 / 애플은 반품
S[3] = (1, page(FX + f'''
{head("오늘 밤 발송 · 뉴욕", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {appbar("🚚 3일(현지) 발송 · 보낸 곳 월가")}
  {cbub("많이 떨어졌던 AI·반도체주에<br><b>다시 사자</b>가 몰렸어요", 120, .1, "t-down", style="font-size:44px")}
  <div class="abs a-drop" style="left:{P}px;top:330px;--d:.5s">{box(200, "반등")}</div>
  <div class="abs a-pop" style="left:260px;top:330px;--d:.7s;width:680px">
    <div style="font-size:40px">나스닥</div><div style="font-size:120px;line-height:1"><span class="thump" style="--d:.8s;color:{RED};-webkit-text-stroke:5px {L};paint-order:stroke fill">▲0.83%</span></div></div>
  {numbox("마이크로소프트", "▲2.74%", COL2[0], 560, 1.2, RED)}
  {numbox("S&P500 · 나흘 만에", "▲0.36%", COL2[1], 560, 1.4, RED)}
  <div class="abs a-sl" style="left:{P}px;top:750px;--d:1.9s;width:{IW}px;height:190px;box-sizing:border-box;background:#fff;border:5px dashed {L};border-radius:26px;display:flex;align-items:center;gap:24px;padding:0 30px">
    <div style="font-size:84px">↩️</div><div><div style="font-size:42px">반품 상자 · 애플 <span style="color:{BLUE}">▼1.90%</span></div>
    <div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#6B5A50">실적 전망 실망 → 다우는 <span style="color:{BLUE}">▼0.38%</span></div></div></div>
  {ch(mascot("owl", "happy", "point"), 406, 950, 170, 2.3, "a-pop", "squish")}
</div>
''', "#30366E"))

# 4 ── 배송길 변수: 미국 중간선거 개표 = '공사 중' 안내판
CONE = (f'<svg viewBox="0 0 100 120" width="110" height="132"><path d="M40 10 h20 l30 95 h-80 z" fill="#FF8A3D" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
        f'<path d="M33 40 h34 M24 70 h52" stroke="#fff" stroke-width="10"/><rect x="4" y="100" width="92" height="14" rx="5" fill="#FF8A3D" stroke="{L}" stroke-width="5"/></svg>')
S[4] = (1, page(FX + f'''
{head("배송길 변수", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E9F1FF;--d:0s">
  {appbar("⚠ 배송 안내 · 오늘 한국시간")}
  <div class="abs a-drop" style="left:{P}px;top:130px;--d:.1s;width:{IW}px;height:330px;box-sizing:border-box;background:#FFD84D;border:6px solid {L};border-radius:26px;text-align:center;padding-top:22px">
    <div style="font-size:54px">🚧 공사 중 · 미국 중간선거 개표 🚧</div>
    <div style="font-size:120px;line-height:1.1"><span class="thump" style="--d:.5s">오전 8시~</span></div>
    <div style="font-size:40px">첫 윤곽 · 상원 윤곽은 오후</div></div>
  <div class="abs cone" style="left:60px;top:490px">{CONE}</div>
  <div class="abs cone" style="left:810px;top:490px;animation-delay:.2s">{CONE}</div>
  {cbub("결과에 따라 오늘 장이<br><b>출렁일 수 있어요</b>", 510, 1.0, "t-down", style="font-size:46px")}
  {ch(mascot("bamtol", "worried", "point", CAP), P, 760, 290, 1.4, "a-sl", "squish")}
  {bub("택배는 출발했지만<br>길 상황은 <b>지켜봐야!</b>", 360, 800, 1.7, "t-left", style="font-size:44px")}
</div>
''', "#4A3E78"))

# 5 ── 받는 사람 체크 3
checks = [("반도체, 어제 낙폭 되찾을까", "미국 반등이 이어지면 반도체 업종 반등 시도 가능성"),
          ("선거 개표, 장중 출렁임", "윤곽에 따라 지수가 흔들릴 가능성"),
          ("AMD 실적, 시장 반응은", "반응에 따라 반도체 분위기가 달라질 가능성")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{290+i*190}px;width:{IW}px;height:166px;box-sizing:border-box;--d:{.5+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:14px;background:#FFF6EA;border:4px solid {L};font-size:54px;line-height:70px;text-align:center;color:{RED}">✔</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("받는 사람 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  {appbar("📋 수령 체크리스트 · 오늘 한국장")}
  <div class="abs" style="left:0;right:0;top:130px;text-align:center;font-size:88px"><span class="punch" style="--d:.1s">오늘 장 <span style="color:#E8590C">체크 3</span></span></div>
  {rows}
  {ch(mascot("star", "happy", "point"), P, 850, 180, 2.0, "a-sl", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 서울신문, 국민일보, 서울경제, 뉴스1, 블록미디어(CNBC 인용)</div>
''', "#FFE1CC"))

# 6 ── 배송 일정 · 마무리
def daycard(day, date, t, col, d, hi=False):
    x, w = col
    bg = "#FFD84D" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:{w}px;height:280px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};'
            f'border-radius:26px;box-shadow:0 6px 0 rgba(0,0,0,.15);text-align:center;padding:14px 8px;color:{L}">'
            f'<div style="font-size:32px;color:#6B5A50">{day}</div><div style="font-size:88px;line-height:1.05">{date}</div>'
            f'<div style="font-size:32px;line-height:1.2;margin-top:6px">{t}</div></div>')
S[6] = (1, page(FX + f'''
{head("배송 일정 · 마무리", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:30px;font-size:42px;color:#FFC08A">다음 택배 도착 예정일</div>
  {daycard("오늘 · 개표", "4", "미국<br>중간선거 결과", COL3[0], .15, True)}
  {daycard("어젯밤 · 미국", "3", "AMD 실적<br>(장 마감 뒤)", COL3[1], .3)}
  {daycard("금 · 미국", "6", "10월<br>고용보고서", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("bamtol", "happy", "wave", CAP), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("moon", "happy", "wave"), 680, 230, 260, .4, "a-sr", "squish")}
  {bub("선거 결과, 내일 아침<br><b>8시에 배달할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 이투데이, 파이낸셜뉴스, 서울신문, 국민일보, 뉴스핌, 서울경제, 뉴스1<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (4.4, 1.5), 4: (3.6, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "scan", 1), (1, .05, "whoosh", .6), (1, .35, "thud", 1), (1, .5, "pop", .7), (1, .6, "boing", .5), (1, .7, "honk", .8),
 (2, .05, "whoosh", .5), (2, .1, "thud", .7), (2, .25, "pop", .7), (2, .6, "blip_down", .8), (2, 1.0, "blip_down", .6), (2, 1.2, "blip_down", .6), (2, 1.5, "sad", .5), (2, 1.7, "pop", .7),
 (3, .05, "whoosh", .5), (3, .1, "pop", .8), (3, .5, "thud", .7), (3, .8, "sparkle", .7), (3, 1.2, "pop", .6), (3, 1.4, "pop", .6), (3, 1.9, "whoosh", .5), (3, 2.0, "blip_down", .5), (3, 2.3, "boing", .5),
 (4, .05, "whoosh", .5), (4, .1, "thud", .8), (4, .5, "dundun", .6), (4, 1.0, "pop", .7), (4, 1.4, "boing", .5), (4, 1.7, "hmm", .5),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "honk", .5), (6, .9, "jingle", .9),
]
