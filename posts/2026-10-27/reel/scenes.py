"""형식: 밤사이 택배 추적 (처음 제작 · 검수 전 · 2026-10-27 화요일판) — 뉴욕에서 보낸 '반도체 호재' 택배가 서울 코스피에 도착할까?
원칙(2026-10-17 훅 규칙): 장면 1 = 결론(미국 반도체지수 ▲2.82%, '반도체 호재, 한국행 출발!')을 0초부터 크게.
시그니처: 배송 조회 앱 화면(운송장 · 뉴욕→서울 점선 경로 · 달리는 트럭) + '발송 완료' 도장 + 바코드 삑(scan)·빵빵(honk).
흐름: 1 배송 조회(결론) → 2 발송지 뉴욕(무엇을 보냈나) → 3 경유지(환율·수급 = 통관) → 4 도착지 코스피 → 5 받는 사람 체크 3 → 6 배송 일정·마무리.
숫자는 2026-10-27 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes truck{from{transform:translateX(0)}to{transform:translateX(var(--dx))}}
@keyframes dash{to{stroke-dashoffset:-40}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:.25}}
@keyframes snow{0%{transform:translateY(-20px);opacity:0}20%{opacity:1}100%{transform:translateY(160px);opacity:0}}
.truck{animation:truck .8s cubic-bezier(.3,.1,.3,1) var(--d,0s) both}
.bob{animation:bob .3s ease-in-out infinite}
.blink{animation:blink .7s steps(1) infinite}
.snow{animation:snow 1.6s linear infinite}
</style>"""

# 택배 기사 모자 (밤톨이 좌표계)
CAP = (f'<path d="M92 118 Q96 70 150 68 Q204 70 208 118 Z" fill="#2F6BD8" stroke="{L}" stroke-width="3.6" stroke-linejoin="round"/>'
       f'<path d="M150 118 Q200 112 236 126 Q212 136 150 128 Z" fill="#2457B8" stroke="{L}" stroke-width="3.6" stroke-linejoin="round"/>'
       f'<rect x="132" y="84" width="36" height="22" rx="6" fill="#FFD84D" stroke="{L}" stroke-width="3"/>')

def box(w=200, label="반도체"):
    return (f'<svg viewBox="0 0 200 170" width="{w}" height="{w*0.85:.0f}"><path d="M20 50 L100 20 L180 50 L100 80 Z" fill="#E7B47E" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M20 50 L20 135 L100 162 L100 80 Z" fill="#C98E55" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M180 50 L180 135 L100 162 L100 80 Z" fill="#D9A06A" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M60 35 L140 65" stroke="#FFF2C4" stroke-width="12"/>'
            f'<rect x="112" y="98" width="56" height="34" rx="4" fill="#fff" stroke="{L}" stroke-width="3" transform="skewY(-18)"/>'
            f'<text x="140" y="164" text-anchor="middle" font-size="18" font-family="Jua" fill="{L}" transform="skewY(-18)">{label}</text></svg>')

TRUCK = (f'<svg viewBox="0 0 160 100" width="150" height="94"><rect x="6" y="18" width="92" height="58" rx="10" fill="#FFB27F" stroke="{L}" stroke-width="5"/>'
         f'<path d="M98 36 h30 l22 22 v18 h-52 z" fill="#FFE59A" stroke="{L}" stroke-width="5" stroke-linejoin="round"/>'
         f'<rect x="108" y="42" width="20" height="14" rx="3" fill="#BFE3FF" stroke="{L}" stroke-width="3"/>'
         f'<text x="52" y="56" text-anchor="middle" font-size="22" font-family="Jua" fill="{L}">밤사이</text>'
         f'<circle cx="34" cy="80" r="13" fill="#fff" stroke="{L}" stroke-width="5"/><circle cx="122" cy="80" r="13" fill="#fff" stroke="{L}" stroke-width="5"/></svg>')

def appbar(text, right=""):
    return (f'<div class="abs" style="left:0;right:0;top:0;height:88px;background:#FFB27F;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">{text}'
            f'<span style="position:absolute;right:30px;font-size:32px">{right}</span></div>')

def step(i, t, sub, on, top, d):
    col = "#FFB27F" if on else "#E6E0F0"
    return (f'<div class="abs a-sl" style="left:{P}px;top:{top}px;--d:{d}s;display:flex;align-items:center;gap:20px">'
            f'<div style="flex:none;width:64px;height:64px;border-radius:50%;background:{col};border:4px solid {L};font-size:36px;display:flex;align-items:center;justify-content:center">{i}</div>'
            f'<div><div style="font-size:40px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:24px;color:#6B5A50">{sub}</div></div></div>')

# 1 ── 결론 먼저: 0초에 숫자·결론·배송 조회 화면·놀란 밤톨이(클로즈업)가 모두 보인다
S[1] = (1, page(FX + f'''
{stars(14, 27, 0, 180)}
{head("밤사이 택배 · 10.27 TUE", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:188px;text-align:center;font-size:44px;color:#C9D6FF">📦 미국 반도체지수 · 26일 마감</div>
<div class="abs" style="left:0;width:1080px;top:246px;text-align:center"><span class="punch" style="--d:0s;font-size:220px;line-height:1;color:{RED};-webkit-text-stroke:10px {L};paint-order:stroke fill">▲2.82%</span></div>
<div class="abs" style="left:0;width:1080px;top:486px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">반도체 호재, <span style="color:#FFE36E">한국행 출발!</span></div>
<div class="panel" style="left:44px;top:630px;width:982px;height:760px;background:#FFFDF6">
  {appbar("🚚 배송 조회 · 운송장 1027", '<span class="blink" style="color:#E8484A">● 배송 중</span>')}
  <div class="abs" style="left:{P}px;top:120px;width:{IW}px;height:210px;box-sizing:border-box;background:#F1EEFF;border:4px solid {L};border-radius:26px">
    <div class="abs" style="left:24px;top:22px;text-align:center;width:150px"><div style="font-size:64px;line-height:1">🗽</div><div style="font-size:36px">뉴욕</div></div>
    <div class="abs" style="right:24px;top:22px;text-align:center;width:150px"><div style="font-size:64px;line-height:1">🏠</div><div style="font-size:36px">서울</div></div>
    <svg class="abs" style="left:170px;top:70px" width="562" height="20"><path d="M0 10 H562" stroke="{L}" stroke-width="6" stroke-dasharray="18 22" style="animation:dash .5s linear infinite"/></svg>
    <div class="abs truck" style="left:170px;top:30px;--dx:250px;--d:.45s"><div class="bob">{TRUCK}</div></div>
  </div>
  {stamp("발송 완료", 520, 360, .3, -10)}
  <div class="abs" style="left:-20px;top:330px;width:420px"><div class="shiver">{mascot("bamtol", "surprised", "up", CAP)}</div></div>
  <div class="abs a-pop" style="left:400px;top:500px;--d:.65s;width:540px;box-sizing:border-box;background:#FFE36E;border:4px solid {L};border-radius:26px;padding:16px 22px;font-size:48px;line-height:1.3;text-align:center">받는 곳은 <span style="color:{BLUE}">코스피</span>!<br>무사히 도착할까?</div>
</div>
{sfx("삑!", 830, 590, 92, .0, 10, "#FFE36E")}
''', "#262B55"))

# 2 ── 발송지 뉴욕: 무엇을 보냈나
S[2] = (1, page(FX + f'''
{head("발송지 · 뉴욕", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFFDF6;--d:0s">
  {appbar("📦 보낸 물건 확인")}
  <div class="abs" style="left:0;right:0;top:120px;text-align:center;font-size:76px;line-height:1.15"><span class="punch" style="--d:.1s">AI 회사 <span style="color:#7B3FC4">상장 신청서</span></span></div>
  <div class="abs a-drop" style="left:{P}px;top:240px;--d:.4s;width:{IW}px;height:250px;box-sizing:border-box;background:#FFF2DC;border:4px solid {L};border-radius:24px">
    <div class="abs" style="left:24px;top:22px">{box(200, "AI")}</div>
    <div class="abs" style="left:260px;top:34px;font-size:40px;line-height:1.5">보낸 곳: <span style="color:#7B3FC4">앤트로픽</span> (AI 회사)<br>내용물: 나스닥 상장 서류<br><span style="font-family:Noto Sans CJK KR,sans-serif;font-size:26px;color:#6B5A50">매출이 빠르게 늘어난 게 확인됐다</span></div>
  </div>
  {numbox("미국 반도체지수", "▲2.82%", COL2[0], 530, 1.0, RED)}
  {numbox("SK하이닉스 ADR", "▲4.09%", COL2[1], 530, 1.3, RED)}
  {ch(mascot("owl", "happy", "point"), P, 760, 300, 1.6, "a-sl", "squish")}
  {bub("AI에 쓰는 돈, 돌아올까<br>하던 걱정이 <b>누그러졌어요</b>", 360, 790, 1.8, "t-left", style="font-size:42px")}
</div>
''', "#2B3060"))

# 3 ── 경유지: 환율·수급 = 통관
S[3] = (1, page(FX + f'''
{head("경유지 · 환율·수급", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {appbar("🛃 통관 중 · 26일 서울")}
  <div class="abs a-sl" style="left:{P}px;top:130px;--d:.3s;width:{IW}px;height:230px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px">
    <div style="font-size:100px">💱</div><div><div style="font-size:38px">원/달러 · 장중 올해 최저 경신</div><div style="font-size:96px;line-height:1"><span class="thump" style="--d:.6s">1,323.1원 <span style="color:{BLUE};font-size:64px">▼1.5원</span></span></div></div></div>
  <div class="abs a-sl" style="left:{P}px;top:400px;--d:.9s;width:{IW}px;height:230px;box-sizing:border-box;background:#2A2F5E;color:#fff;border:5px solid {L};border-radius:28px;display:flex;align-items:center;gap:26px;padding:0 34px">
    <div style="font-size:100px">🙅</div><div><div style="font-size:38px">외국인 · 코스피</div><div style="font-size:92px;line-height:1;color:#7DBBFF">계속 팔았다</div></div></div>
  {stamp("통관 대기", 560, 580, 1.3, -8)}
  {ch(mascot("moon", "worried", "point"), P, 760, 300, 1.6, "a-sl", "squish")}
  {bub("외국인이 다시 사야<br><b>통관이 빨라져요</b>", 380, 800, 1.9, "t-left", style="font-size:46px")}
</div>
''', "#30366E"))

# 4 ── 도착지: 코스피 (아직 꽁꽁)
flakes = "".join(f'<div class="abs snow" style="left:{x}px;top:{y}px;font-size:46px;animation-delay:{dl}s">❄</div>'
                 for x, y, dl in ((40, 150, 0), (120, 380, .5), (860, 140, .9), (900, 400, .3), (60, 560, 1.2), (880, 600, .7)))
S[4] = (1, page(FX + f'''
{head("도착지 · 코스피", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E9F1FF;--d:0s">
  {appbar("🏠 받는 곳 상태 · 26일 종가")}
  {flakes}
  <div class="abs" style="left:0;right:0;top:150px;text-align:center;font-size:150px;line-height:1"><span class="punch" style="--d:.15s">5,469.47</span></div>
  <div class="abs" style="left:0;right:0;top:320px;text-align:center;font-size:96px;color:{BLUE}"><span class="thump" style="--d:.5s">▼1.46%</span></div>
  <div class="abs a-pop" style="left:0;right:0;top:470px;--d:.8s;text-align:center"><span style="display:inline-block;background:#fff;border:4px solid {L};border-radius:999px;padding:10px 36px;font-size:50px">❄ 7개월 만의 최저 ❄</span></div>
  {ch(mascot("star", "teary", "up"), 640, 660, 300, 1.1, "a-sr", "shiver")}
  <div class="abs a-drop" style="left:520px;top:870px;--d:1.0s">{box(180, "반도체")}</div>
  {bub("받는 집이 꽁꽁…<br>택배가 <b>녹여 줄까?</b>", P, 720, 1.4, "t-right", style="font-size:46px")}
</div>
''', "#4A3E78"))

# 5 ── 받는 사람 체크 3
checks = [("반도체, 미국 따라 오를까", "온기가 번지면 반도체 업종 반등 시도 가능성"),
          ("외국인 매도, 멈출까", "돌아오면 낙폭 회복 시도 가능성"),
          ("오늘 3분기 성장률(GDP)", "한국은행 발표 · 경기 흐름 확인")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{290+i*190}px;width:{IW}px;height:166px;box-sizing:border-box;--d:{.5+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:14px;background:#FFF6EA;border:4px solid {L};font-size:54px;line-height:70px;text-align:center;color:{RED}">✔</div>'
    f'<div><div style="font-size:50px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("받는 사람 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  {appbar("📋 수령 체크리스트 · 오늘 한국장")}
  <div class="abs" style="left:0;right:0;top:130px;text-align:center;font-size:88px"><span class="punch" style="--d:.1s">오늘 장 <span style="color:#E8590C">체크 3</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point", CAP), 690, 820, 210, 2.0, "a-sr", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 뉴스1, AP, SBS, 서울경제</div>
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
  {daycard("오늘 밤", "27", "FOMC<br>회의 시작", COL3[0], .15)}
  {daycard("수요일", "28", "SK하이닉스<br>실적", COL3[1], .3, True)}
  {daycard("목요일 새벽", "29", "FOMC 결과<br>삼성전자 실적", COL3[2], .45, True)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("bamtol", "happy", "wave", CAP), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("star", "happy", "wave"), 680, 230, 260, .4, "a-sr", "squish")}
  {bub("내일 아침 8시에<br><b>또 배달할게요!</b>", 330, 40, .65, "t-down", "50%", "font-size:44px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: AP, 뉴스핌, 뉴스1, 로이터, SBS, 서울경제, 비즈니스워치<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.2, 1.5), 3: (4.0, 1.5), 4: (3.6, 1.5), 5: (4.2, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "scan", 1), (1, .05, "thud", .8), (1, .3, "thud", .9), (1, .45, "honk", .7), (1, .65, "pop", .8), (1, .9, "question", .5),
 (2, .05, "whoosh", .5), (2, .1, "scan", .7), (2, .4, "boing", .6), (2, 1.0, "pop", .7), (2, 1.3, "pop", .7), (2, 1.6, "boing", .5), (2, 1.8, "ding", .7),
 (3, .05, "whoosh", .5), (3, .3, "tick", .6), (3, .6, "blip_down", .7), (3, .9, "tick", .6), (3, 1.3, "thud", .9), (3, 1.6, "boing", .5), (3, 1.9, "pop", .7),
 (4, .05, "whoosh", .5), (4, .15, "thud", .8), (4, .5, "blip_down", .8), (4, .8, "pop", .6), (4, 1.1, "boing", .5), (4, 1.4, "sad", .5),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "honk", .5), (6, .9, "jingle", .9),
]
