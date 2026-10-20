"""형식: 밤사이 스포츠 중계 (처음 제작 · 검수 전 · 2026-10-21) — '결론 먼저' 훅 + 전광판·잔디 구장 시그니처.
내용: 2026-10-21 (20일 뉴욕 — 다우 ▲1.02% vs 나스닥 ▼0.02%, 돈이 AI 기술주에서 헬스케어로). 비유: 돈(선수)이 'AI 기술주 FC'에서 '헬스케어 FC'로 이적.
흐름: 1 전광판 결론(▲1.02% + '돈이 헬스케어로 이적!') → 2 하이라이트(지수 경주) → 3 해설(이적 시장) → 4 한국 팀 상황 → 5 작전판(체크 3) → 6 다음 경기 일정.
숫자는 2026-10-21 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

# 중계 헤드셋 (캐릭터 좌표계: 귀 높이 ~190, 입 ~240)
HEADSET = (f'<path d="M66 186 Q66 96 150 92 Q234 96 234 186" fill="none" stroke="#2B2B3A" stroke-width="10" stroke-linecap="round"/>'
           f'<rect x="50" y="168" width="30" height="50" rx="12" fill="#E8484A" stroke="{L}" stroke-width="4"/>'
           f'<rect x="220" y="168" width="30" height="50" rx="12" fill="#E8484A" stroke="{L}" stroke-width="4"/>'
           f'<path d="M66 214 Q80 252 124 250" fill="none" stroke="#2B2B3A" stroke-width="6" stroke-linecap="round"/>'
           f'<circle cx="128" cy="250" r="10" fill="#2B2B3A"/>')

FX = """<style>
@keyframes arrowdraw{from{stroke-dashoffset:var(--len)}to{stroke-dashoffset:0}}
@keyframes flash{0%,100%{opacity:1}50%{opacity:.55}}
@keyframes transfer{0%{transform:translateX(0)}100%{transform:translateX(var(--dx))}}
.bulb{animation:flash .5s steps(1) infinite}
.go{animation:transfer .9s cubic-bezier(.3,.9,.3,1) var(--d,0s) both}
</style>"""

def field(x, y, w, h, extra=""):
    stripes = "".join(f'<div class="abs" style="left:{i*w//8}px;top:0;width:{w//16}px;height:{h}px;background:rgba(255,255,255,.07)"></div>' for i in range(8))
    return (f'<div class="panel" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#3E9C5A">{stripes}'
            f'<div class="abs" style="left:{w//2 - 3}px;top:0;width:6px;height:{h}px;background:rgba(255,255,255,.55)"></div>'
            f'<div class="abs" style="left:{w//2 - 110}px;top:{h//2 - 110}px;width:220px;height:220px;border:6px solid rgba(255,255,255,.55);border-radius:50%"></div>{extra}</div>')

def crest(label, icon, bg, x, y, w, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s;text-align:center">'
            f'<div style="margin:0 auto;width:190px;height:220px;background:{bg};border:6px solid {L};border-radius:24px 24px 95px 95px;'
            f'display:flex;align-items:center;justify-content:center;font-size:110px;box-shadow:0 8px 0 rgba(0,0,0,.18)">{icon}</div>'
            f'<div style="font-size:44px;margin-top:12px">{label}</div></div>')

# 1 ── 결론 먼저: 0초에 전광판 숫자·결론·중계 캐스터(클로즈업)가 모두 보인다
#      0~1초: 숫자 펀치(0) → '삐익!' 효과 글자(.2) → '다우 승!' 도장(.45) → 이적 화살표 그리기(.6~1.0)
ARROW = (f'<svg width="420" height="120" viewBox="0 0 420 120" style="overflow:visible">'
         f'<path d="M20 70 Q210 -10 380 60" fill="none" stroke="#FFE36E" stroke-width="12" stroke-linecap="round" style="stroke-dasharray:420;--len:420;stroke-dashoffset:420;animation:arrowdraw .45s ease-out .6s both"/>'
         f'<path d="M352 30 L392 64 L346 86" fill="none" stroke="#FFE36E" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" class="a-fade" style="--d:1.0s"/></svg>')
S[1] = (1, page(FX + f'''
{stars(12, 33, 0, 170)}
{head("밤사이 스포츠 · 10.21 WED", 1, "#F6EEE4")}
<div class="abs" style="left:44px;top:186px;width:982px;height:470px;box-sizing:border-box;background:#14181F;border:6px solid {L};border-radius:26px;box-shadow:0 8px 0 rgba(0,0,0,.3);overflow:hidden">
  {"".join(f'<div class="abs bulb" style="left:{30 + i*104}px;top:16px;width:20px;height:20px;border-radius:50%;background:#FFE36E;animation-delay:{(i%2)*.25}s"></div>' for i in range(9))}
  <div class="abs" style="left:0;right:0;top:46px;text-align:center;font-size:50px;color:#FFE36E">20일 뉴욕 · 다우</div>
  <div class="abs" style="left:0;right:0;top:104px;text-align:center"><span class="punch" style="font-size:230px;line-height:1;color:#FF7A7F;-webkit-text-stroke:10px #000;paint-order:stroke fill">▲1.02%</span></div>
  <div class="abs" style="left:0;right:0;top:362px;text-align:center;font-size:56px;color:#7DBBFF">나스닥 ▼0.02% · 제자리</div>
</div>
<div class="abs" style="left:0;width:1080px;top:684px;text-align:center;font-size:86px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">돈이 <span style="color:#FFE36E">헬스케어로 이적!</span></div>
{field(44, 820, 982, 600)}
<div class="abs" style="left:540px;top:860px;width:460px;height:300px;box-sizing:border-box;background:rgba(20,24,31,.85);border:5px solid {L};border-radius:24px">
  <div class="abs" style="left:20px;top:22px;font-size:40px;color:#9FC2FF">AI 기술주</div>
  <div class="abs" style="right:20px;top:22px;font-size:40px;color:#FFB27F">헬스케어</div>
  <div class="abs" style="left:20px;top:110px">{ARROW}</div>
  <div class="abs" style="left:0;right:0;top:220px;text-align:center;font-size:34px;color:#fff">💰 → 🏥</div>
</div>
<div class="abs" style="left:-10px;top:880px;width:560px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="squish">{mascot("bamtol", "surprised", "point", HEADSET)}</div></div>
{sfx("삐익!", 90, 850, 100, .2, -10, "#FFE36E")}
<div class="stamp a-stamp" style="left:560px;top:1196px;--d:.45s;--r:-8deg;font-size:74px;white-space:nowrap;background:rgba(255,255,255,.9)">다우 승!</div>
''', "#262B55"))

# 2 ── 하이라이트: 지수 경주
def lane(i, name, dx, color, d, stuck=False):
    y = 330 + i * 150
    runner = (f'<div class="abs {"shiver" if stuck else "go"}" style="left:{P + 150}px;top:{y + 10}px;--dx:{dx}px;--d:{d}s">'
              f'<div style="width:110px;height:110px;border-radius:50%;background:{color};border:5px solid {L};display:flex;align-items:center;justify-content:center;font-size:30px;color:#fff">{name}</div></div>')
    return (f'<div class="abs" style="left:{P}px;top:{y}px;width:{IW}px;height:130px;background:#C8553D;border:5px solid {L};border-radius:18px"></div>'
            f'<div class="abs" style="left:{P + 20}px;top:{y + 40}px;font-size:40px;color:#fff">{i + 1}번</div>{runner}')
S[2] = (1, page(FX + f'''
{head("오늘의 하이라이트", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E6F0FA;--d:0s">
  {cbub("다우 선수, <b>500포인트 넘게</b> 질주!", 40, .1, "t-down", style="font-size:48px")}
  <div class="abs" style="left:{P + IW - 26}px;top:320px;width:16px;height:470px;background:repeating-linear-gradient(#fff 0 22px,{L} 22px 44px);border:3px solid {L}"></div>
  {lane(0, "다우", 600, RED, .3)}
  {lane(1, "S&P", 260, "#E8743B", .45)}
  {lane(2, "나스닥", 0, BLUE, .6, True)}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P + 20, 795, 200, 1.1, "a-sl", "squish")}
  {bub("나스닥은<br><b>제자리걸음</b>!", 290, 820, 1.3, "t-left", style="font-size:44px")}
  {numbox("다우", "▲1.02%", COL3[0], 1010, 1.7, RED)}
  {numbox("S&P500", "▲0.28%", COL3[1], 1010, 1.9, RED)}
  {numbox("나스닥", "▼0.02%", COL3[2], 1010, 2.1, BLUE)}
</div>
''', "#2B3060"))

# 3 ── 해설: 이적 시장 (돈이 AI 기술주 FC → 헬스케어 FC)
S[3] = (1, page(FX + f'''
{head("1분 해설 · 이적 시장", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("왜 갈렸을까? <b>돈(선수)이 이적</b>했어요!", 36, .1, "t-down", style="font-size:46px")}
  {crest("AI 기술주 FC", "🤖", "#BFD3FF", COL2[0][0], 220, COL2[0][1], .3)}
  {crest("헬스케어 FC", "🏥", "#FFD3C2", COL2[1][0], 220, COL2[1][1], .45)}
  <div class="abs go" style="left:{COL2[0][0] + 150}px;top:520px;--dx:470px;--d:.8s;font-size:120px">💰</div>
  {nar("이유: AI에 쏟는 돈, <b>제값 할까?</b> 의구심", P, 690, 1.3, f"font-size:42px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {stamp("헬스케어 사상 최고!", 170, 810, 1.8, -5)}
  {nar("도움: <b>유가 하락</b> + 3M 등 <b>호실적</b>", P, 960, 2.3, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center;background:#E8E2FF")}
  {ch(mascot("star", "surprised", "up"), 400, 250, 180, .6, "a-pop", "shiver")}
</div>
''', "#30366E"))

# 4 ── 한국 팀 상황 (전날 20일 서울)
S[4] = (1, page(FX + f'''
{head("한국 팀 상황", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:52px">그 전날(20일) 코스피</div>
  <div class="abs" style="left:0;right:0;top:110px;text-align:center;font-size:210px;line-height:1"><span class="punch" style="--d:.1s;color:{BLUE};-webkit-text-stroke:8px {L};paint-order:stroke fill">▼3.73%</span></div>
  {cbub("외국인·기관이<br><b>함께 팔았어요</b>", 360, .5, "t-down", style="font-size:46px")}
  {ch(mascot("star", "teary", "down"), COL2[0][0] + 60, 540, 300, .8, "a-sl", "shiver")}
  {ch(mascot("bamtol", "worried", "hold", HEADSET), COL2[1][0] + 60, 540, 300, 1.0, "a-sr", "squish2")}
  {numbox("코스닥 (20일)", "▼3.33%", COL2[0], 900, 1.4, BLUE)}
  {numbox("원/달러 (20일)", "1,328.1원", COL2[1], 900, 1.6, L)}
  <div class="abs a-pop" style="left:{COL2[1][0]}px;top:1080px;width:{COL2[1][1]}px;text-align:center;font-size:36px;--d:1.8s">올해 최저 종가</div>
  <div class="abs a-pop" style="left:{COL2[0][0]}px;top:1080px;width:{COL2[0][1]}px;text-align:center;font-size:36px;--d:1.7s">800선 아래로</div>
</div>
''', "#4A3E78"))

# 5 ── 작전판 (오늘의 체크)
items = [("🤖", "AI 의구심, 누그러질까", f"나스닥 <span style='color:#1D4ED8'>▼0.02%</span> · 미국 기술주 숨 고르기"),
         ("🙋", "외국인·기관 매도 멈출까", f"20일 코스피 <span style='color:#1D4ED8'>▼3.73%</span>"),
         ("🛢️", "유가, 진정될까", f"WTI 101.79달러 <span style='color:#1D4ED8'>▼1.80%</span>")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{.7+i*.4:.1f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none;font-size:60px;width:70px;text-align:center">{ic}</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
BOARD = (f'<div class="abs" style="left:{P}px;top:40px;width:470px;height:380px;background:#2F7A48;border:6px solid #8A5A3B;border-radius:20px">'
         f'<div class="abs" style="left:232px;top:0;width:4px;height:368px;background:rgba(255,255,255,.6)"></div>'
         f'<div class="abs a-pop" style="left:60px;top:60px;--d:.2s;font-size:70px;color:#fff">X</div>'
         f'<div class="abs a-pop" style="left:330px;top:220px;--d:.35s;font-size:70px;color:#FFE36E">O</div>'
         f'<svg class="abs" style="left:0;top:0;overflow:visible" width="470" height="380"><path d="M110 120 Q240 60 330 250" fill="none" stroke="#fff" stroke-width="7" stroke-dasharray="14 12" stroke-linecap="round"/></svg>'
         f'<div class="abs" style="left:0;right:0;bottom:12px;text-align:center;font-size:40px;color:#fff">오늘의 작전</div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("작전판 · 오늘 한국장", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFF8E1;--d:0s">
  {BOARD}
  {ch(mascot("bamtol", "normal", "point", HEADSET), 560, 90, 280, .1, "a-sr", "squish")}
  {bub("급락 다음 날,<br>볼 것은 <b>셋</b>!", 520, 20, .3, "t-down", "40%", "font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:1.8s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 이데일리, 서울경제, 뉴스1, SBS Biz, 로이터</div>
''', "#FFE1CC"))

# 6 ── 다음 경기 일정
S[6] = (1, page(FX + f'''
{head("밤사이 중계석 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 경기 · 오늘 밤 (미국 현지 21일)</div>
  <div class="abs" style="left:44px;top:100px;font-size:72px;line-height:1.2">테슬라·메타<br>실적 발표</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.3s;font-size:44px">22일엔 <span style="color:#FFC08A">한은 금리 결정</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave", HEADSET), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("결과는 내일 아침 8시,<br><b>밤사이 중계석</b>에서!", 260, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 이데일리, 서울경제, 뉴스1, SBS Biz, 로이터, CNBC · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.7, 1.3), 2: (3.7, 1.5), 3: (4.4, 1.5), 4: (3.6, 1.5), 5: (4.2, 1.5), 6: (3.4, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "whistle", .9), (1, .05, "thud", .8), (1, .2, "pop", .5), (1, .45, "thud", 1), (1, .5, "cheer", .8), (1, .6, "whoosh", .5), (1, 1.0, "ding", .6),
 (2, .05, "whoosh", .5), (2, .1, "pop", .8), (2, .3, "STEPS_FAST", .6), (2, .6, "boing", .5), (2, 1.1, "whoosh", .4), (2, 1.3, "pop", .8), (2, 1.7, "sparkle", .6), (2, 1.9, "sparkle", .5), (2, 2.1, "blip_down", .8),
 (3, .1, "pop", .8), (3, .3, "boing", .6), (3, .45, "boing", .6), (3, .8, "whoosh", .6), (3, 1.0, "question", .6), (3, 1.3, "tick", 1), (3, 1.8, "thud", 1), (3, 1.8, "cheer", .6), (3, 2.3, "tick", .9),
 (4, .05, "whoosh", .5), (4, .1, "thud", .9), (4, .15, "slidedown", .6), (4, .5, "pop", .8), (4, .8, "sad", .5), (4, 1.4, "blip_down", .8), (4, 1.6, "pop", .6),
 (5, .05, "whoosh", .5), (5, .2, "whistle", .5), (5, .3, "pop", .8), (5, .7, "CHECK1", 1), (5, 1.1, "CHECK2", 1), (5, 1.5, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
