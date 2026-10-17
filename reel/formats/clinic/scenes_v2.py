"""형식: 밤사이 병원 진료 v2 (검수 전 · 2026-10-17 '결론 먼저' 시안) — 10/17 내용으로 다시 짠 예시.
원칙: 장면 1에 결론(숫자+원인)을 큼직하게 → 장면 2~3 이유 하나씩 → 장면 4 한국 → 5 체크 → 6 예고.
0~1초 안에 숫자 펀치·심전도 하강·'진단' 도장이 연달아 움직인다(핵심 요소는 0초부터 보임).
"""
from lib import *

S = {}
RED, BLUE, GREEN = "#E03131", "#2F6BD8", "#2FA36B"

# 청진기 (목에 건 모양 — 눈·입 아래에만)
STETH = (f'<path d="M80 236 Q150 286 220 236" fill="none" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<path d="M80 236 Q74 224 82 216 M220 236 Q226 224 218 216" fill="none" stroke="#5B6B8C" stroke-width="6" stroke-linecap="round"/>'
         f'<path d="M196 254 Q206 266 204 276" fill="none" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<circle cx="204" cy="284" r="12" fill="#C9D3E6" stroke="{L}" stroke-width="4"/>')
MIRROR = f'<circle cx="150" cy="118" r="20" fill="#E8F1FF" stroke="{L}" stroke-width="4"/><circle cx="150" cy="118" r="7" fill="#9FB7E0"/>'

# 큼직한 움직임 (0초부터 보이되 계속 움직임)
FX = """<style>
@keyframes punch{0%{transform:scale(1)}12%{transform:scale(1.13)}24%{transform:scale(.97)}34%{transform:scale(1.03)}46%,100%{transform:scale(1)}}
@keyframes jolt{0%,100%{transform:translateX(0)}20%{transform:translateX(-14px)}40%{transform:translateX(12px)}60%{transform:translateX(-8px)}80%{transform:translateX(5px)}}
@keyframes ecgdraw{from{stroke-dashoffset:1400}to{stroke-dashoffset:0}}
@keyframes fever{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.06)}}
@keyframes heat{from{height:30%}to{height:88%}}
.punch{display:inline-block;transform-origin:50% 60%;animation:punch 1.1s ease-out both, jolt .45s ease-out .05s both}
.punch2{display:inline-block;transform-origin:50% 60%;animation:punch 1.1s ease-out var(--d,0s) both}
.ecg path{stroke-dasharray:1400;animation:ecgdraw .9s linear both}
</style>"""

def ecg(w, h, color="#5BF29B"):
    pts = (f"M0 {h*.45} L{w*.18} {h*.45} L{w*.24} {h*.12} L{w*.30} {h*.72} L{w*.36} {h*.45} L{w*.50} {h*.45} "
           f"L{w*.56} {h*.2} L{w*.62} {h*.62} L{w*.70} {h*.50} L{w*.80} {h*.64} L{w*.90} {h*.82} L{w} {h*.96}")
    return (f'<svg class="ecg" width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<path d="{pts}" fill="none" stroke="{color}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/></svg>')

# 1 ── 결론 먼저 (0초에 숫자·원인·의사 모두 보임)
S[1] = (1, page(FX + f'''
{stars(12, 41, 0, 300)}
{head("밤사이 응급실 · 10.17 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:44px;top:186px;width:982px;height:104px;box-sizing:border-box;background:#E8484A;border:6px solid {L};border-radius:22px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;gap:20px;color:#fff">
  <div style="width:64px;height:64px;position:relative;flex:none"><div class="abs" style="left:21px;top:0;width:22px;height:64px;background:#fff;border-radius:5px"></div><div class="abs" style="left:0;top:21px;width:64px;height:22px;background:#fff;border-radius:5px"></div></div>
  <div style="font-size:60px">응급 환자 <span style="animation:beam .6s steps(1) infinite">●</span> 나스닥</div>
</div>
<div class="abs" style="left:0;width:1080px;top:316px;text-align:center"><span class="punch" style="font-size:250px;line-height:1;color:#7DBBFF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼2.14%</span></div>
<div class="abs" style="left:44px;top:600px;width:982px;box-sizing:border-box;background:#FFD84D;border:6px solid {L};border-radius:26px;box-shadow:0 8px 0 rgba(0,0,0,.25);text-align:center;padding:14px 10px 18px">
  <div style="font-size:46px;color:#6B4A1A">진단 결과, 원인은 딱 2가지</div>
  <div style="font-size:88px;line-height:1.15;color:{L}">AI 빚 걱정<br><span style="color:#C2410C">+ 기름값 100달러</span></div>
</div>
<div class="abs" style="left:-20px;top:930px;width:600px"><div class="squish">{mascot("bamtol", "surprised", "point", STETH + MIRROR)}</div></div>
<div class="abs" style="left:560px;top:960px;width:466px;height:300px;box-sizing:border-box;background:#14202A;border:6px solid {L};border-radius:26px;overflow:hidden;box-shadow:0 8px 0 rgba(0,0,0,.25)">
  <div class="abs" style="left:22px;top:14px;font-size:34px;color:#5BF29B">♥ 나스닥 16일</div>
  <div class="abs" style="left:24px;top:80px;width:416px;height:180px">{ecg(416, 180)}</div>
</div>
<div class="stamp a-stamp" style="left:600px;top:1300px;--d:.45s;--r:-8deg;font-size:76px;white-space:nowrap">진단 완료!</div>
''', "#262B55"))

# 2 ── 이유 ① 빚 몸살
S[2] = (1, page(FX + f'''
{head("이유 ① 빚 몸살", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E6F0FA;--d:0s">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:170px;line-height:1"><span class="punch2" style="--d:.1s">🏗️💸</span></div>
  <div class="abs a-pop" style="left:0;right:0;top:240px;--d:.15s;text-align:center;font-size:84px;line-height:1.15">빚내서 지은<br><span style="color:#C2410C">AI 데이터센터</span></div>
  {bub("<b>할부</b>로 큰 공장 지었는데<br>갚을 수 있을까?", P, 480, .7, "t-down", "70%", "font-size:46px")}
  {ch(mascot("bamtol", "worried", "point", STETH + MIRROR), P, 660, 330, .5, "a-sl", "squish")}
  {ch(mascot("moon", "teary", "down"), 560, 680, 300, .9, "a-sr", "shiver")}
  {bub("몸이<br>무거워요…", 600, 560, 1.2, "t-down", "40%", "font-size:42px")}
  {numbox("다우", "▼0.34%", COL3[0], 1010, 1.8)}
  {numbox("S&P500", "▼1.09%", COL3[1], 1010, 2.0)}
  {numbox("나스닥", "▼2.14%", COL3[2], 1010, 2.2)}
</div>
''', "#2B3060"))

# 3 ── 이유 ② 기름값 열
thermo = (f'<div class="abs" style="left:{P+30}px;top:60px;width:110px;height:520px">'
          f'<div class="abs" style="left:25px;top:0;width:60px;height:440px;background:#fff;border:6px solid {L};border-radius:30px;overflow:hidden">'
          f'<div class="abs" style="left:0;right:0;bottom:0;background:#E8484A;animation:heat 1s cubic-bezier(.2,.9,.3,1) .1s both"></div></div>'
          f'<div class="abs" style="left:0;top:400px;width:110px;height:110px;border-radius:50%;background:#E8484A;border:6px solid {L};box-sizing:border-box"></div></div>')
S[3] = (1, page(FX + f'''
{head("이유 ② 기름값 열", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFF1E6;--d:0s">
  {thermo}
  <div class="abs" style="left:230px;top:70px;font-size:56px;color:#6B4A1A">국제유가 WTI</div>
  <div class="abs" style="left:230px;top:140px;font-size:150px;line-height:1"><span class="punch2" style="--d:.15s;color:{L}">101.41</span></div>
  <div class="abs" style="left:230px;top:300px;font-size:64px">달러 <span style="color:{RED}">▲3.5%</span></div>
  {nar("중동 불안에 <b>100달러</b>를 넘었어요", 230, 410, .6, "font-size:42px")}
  {ch(mascot("star", "surprised", "up"), 560, 640, 330, .9, "a-sr", "shiver")}
  {bub("기름값 더 오르면<br><b>물가 부담</b>도 커져요", P, 680, 1.3, "t-right", style="font-size:46px")}
  {sfx("후끈!", 120, 1000, 110, 1.0, -10, "#FFB27F")}
</div>
''', "#30366E"))

# 4 ── 한국은?
c0 = COL2[0][0] + COL2[0][1] // 2; c1 = COL2[1][0] + COL2[1][1] // 2
S[4] = (1, page(FX + f'''
{head("그럼 한국은?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:52px">16일 코스피 · 8거래일 만에 반등</div>
  <div class="abs" style="left:0;right:0;top:110px;text-align:center;font-size:200px;line-height:1"><span class="punch2" style="--d:.15s;color:{RED};-webkit-text-stroke:8px {L};paint-order:stroke fill">▲2.05%</span></div>
  {ch(mascot("star", "happy", "up"), c0 - 160, 470, 320, .5, "a-sl", "hop")}
  {bub("한국은<br>나아졌네!", P, 340, .8, "t-down", "45%", "font-size:44px")}
  {ch(mascot("bamtol", "worried", "hold", STETH + MIRROR), c1 - 160, 470, 320, 1.0, "a-sr", "squish2")}
  {bub("그런데 미국 반도체가<br>또 약해서 <b>방심 금물</b>", 0, 330, 1.4, "t-down", "70%", f"font-size:40px;left:auto;right:{P}px")}
  {numbox("원/달러 1,331.4원 (16일)", "▼13.2원", (P, IW), 1010, 2.0, BLUE)}
</div>
''', "#4A3E78"))

# 5 ── 처방전 (월요일 체크 3) — 제목만 큼직하게
PILL = lambda c: f'<svg viewBox="0 0 80 80" width="76"><g transform="rotate(-35 40 40)"><rect x="8" y="26" width="64" height="28" rx="14" fill="#fff" stroke="{L}" stroke-width="4"/><path d="M40 26 h18 a14 14 0 0 1 0 28 h-18z" fill="{c}" stroke="{L}" stroke-width="4"/></g></svg>'
items = [(PILL("#BFD3FF"), "반도체 반등, 이어질까?", f"나스닥 <span style='color:#1D4ED8'>▼2.14%</span> · 미국 AI·반도체주 약세"),
         (PILL("#FFB27F"), "기름값 100달러 넘을까", f"WTI 101.41달러 <span style='color:#C92A2A'>▲3.5%</span>"),
         (PILL("#FFE59A"), "외국인·환율 흐름", f"원/달러 1,331.4원 <span style='color:#1D4ED8'>▼13.2원</span>")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{560+i*230}px;width:982px;height:200px;background:#fff;--d:{.5+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 30px;box-sizing:border-box">'
    f'<div style="flex:none;width:84px;height:84px;border-radius:50%;background:#FFB27F;border:5px solid {L};font-size:52px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ic}</div>'
    f'<div><div style="font-size:58px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("처방전 · 월요일 한국장", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:320px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:{P}px;top:34px;font-size:96px;color:{GREEN}">℞ 처방전</div>
  <div class="abs" style="left:{P}px;top:160px;font-size:52px">월요일엔 이 <span style="color:#E8590C">3가지</span>!</div>
  {ch(mascot("bamtol", "happy", "point", STETH + MIRROR), 640, 30, 280, .15, "a-sr", "squish")}
</div>
{cards}
<div class="src a-fade" style="top:1260px;color:#6B5A50;--d:1.8s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: AP, 뉴스핌, 뉴스1, 서울경제, SBS</div>
''', "#FFE1CC"))

# 6 ── 다음 진료 예약
S[6] = (1, page(FX + f'''
{head("밤사이 병원 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:40px;color:#FFC08A">다음 진료 예약</div>
  <div class="abs" style="left:44px;top:100px;font-size:72px;line-height:1.2">내일(일) 아침 8시<br>지난주 성적표</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.3s;font-size:42px">다음 주엔 실적 발표 · <span style="color:#FFC08A">27~28일 FOMC</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("moon", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave", STETH), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("푹 쉬고 오세요!<br><b>밤사이 병원</b>이었습니다", 300, 30, .65, "t-down", "75%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: AP, 뉴스핌, 뉴스1, 서울경제, CNBC, SBS · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.8, 1.3), 2: (3.8, 1.6), 3: (3.4, 1.6), 4: (3.8, 1.6), 5: (4.4, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "beep", 1), (1, .05, "thud", .8), (1, .1, "slidedown", .6), (1, .45, "thud", 1), (1, .5, "ding", .6), (1, 1.2, "beep", .6),
 (2, .05, "whoosh", .5), (2, .1, "boing", .7), (2, .5, "whoosh", .4), (2, .7, "pop", .8), (2, .9, "sad", .5), (2, 1.2, "pop", .8), (2, 1.8, "blip_down", .7), (2, 2.0, "blip_down", .8), (2, 2.2, "blip_down", 1),
 (3, .05, "whoosh", .5), (3, .1, "tension", .5), (3, .15, "thud", .8), (3, .6, "tick", 1), (3, .9, "question", .7), (3, 1.0, "boing", .6), (3, 1.3, "pop", .8),
 (4, .05, "whoosh", .5), (4, .15, "sparkle", .8), (4, .5, "yay", .6), (4, .8, "pop", .8), (4, 1.4, "pop", .8), (4, 2.0, "blip_down", .8),
 (5, .05, "whoosh", .5), (5, .15, "pop", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
