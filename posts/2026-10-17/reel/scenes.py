"""형식: 밤사이 병원 진료 (검수 전 · 2026-10-17 처음 제작) — 밤톨이 의사, 솜부엉 간호사, 달떡이 환자(나스닥), 별콩이 보호자.
내용: 2026-10-17 (나스닥 16일 ▼2.14% · AI 빚 걱정 + 유가 100달러, 코스피 16일 ▲2.05% 반등). 비유: 할부로 큰 공장 짓기(빚 몸살) + 기름값 열.
장면 1 시그니처: 병원 간판(초록 십자) + 진료 차트 클립보드(질문) + 심박 모니터 + 청진기 든 의사 클로즈업.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"
GREEN = "#2FA36B"

# 청진기 (캐릭터 좌표계 소품)
STETH = (f'<path d="M112 222 Q108 268 150 274 Q192 268 188 222" fill="none" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<circle cx="112" cy="220" r="6" fill="#5B6B8C"/><circle cx="188" cy="220" r="6" fill="#5B6B8C"/>'
         f'<path d="M150 274 L150 292" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<circle cx="150" cy="300" r="14" fill="#C9D3E6" stroke="{L}" stroke-width="4"/>')
# 머리 거울 (의사 표시)
MIRROR = f'<circle cx="150" cy="118" r="20" fill="#E8F1FF" stroke="{L}" stroke-width="4"/><circle cx="150" cy="118" r="7" fill="#9FB7E0"/>'

def ecg(w, h, color="#5BF29B", drop=True):
    """심박 모니터 선: 평탄 → 뛰고 → 아래로 주르륵."""
    pts = f"M0 {h*.45} L{w*.18} {h*.45} L{w*.24} {h*.15} L{w*.30} {h*.70} L{w*.36} {h*.45} L{w*.50} {h*.45} L{w*.56} {h*.22} L{w*.62} {h*.62} L{w*.70} {h*.50}"
    pts += f" L{w*.80} {h*.62} L{w*.90} {h*.78} L{w} {h*.92}" if drop else f" L{w} {h*.45}"
    return f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible"><path d="{pts}" fill="none" stroke="{color}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/></svg>'

# 1 ── 응급 접수 (훅) — 0초에 간판·차트(질문)·모니터·의사가 모두 보인다 (핵심 요소에 등장 애니메이션 없음)
S[1] = (1, page(f'''
{stars(14, 41, 0, 300)}
{head("밤사이 병원 · 10.17 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:44px;top:186px;width:982px;height:118px;box-sizing:border-box;background:#FFFFFF;border:6px solid {L};border-radius:24px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;gap:24px">
  <div style="width:78px;height:78px;position:relative"><div class="abs" style="left:26px;top:0;width:26px;height:78px;background:{GREEN};border-radius:6px"></div><div class="abs" style="left:0;top:26px;width:78px;height:26px;background:{GREEN};border-radius:6px"></div></div>
  <div style="font-size:66px">밤사이 병원</div>
  <div style="background:#E8484A;color:#fff;border:4px solid {L};border-radius:14px;padding:2px 18px;font-size:44px;animation:beam .8s steps(1) infinite">응급실</div>
</div>
<div class="abs" style="left:44px;top:350px;width:982px;height:560px;box-sizing:border-box;background:#C99A62;border:6px solid {L};border-radius:30px;box-shadow:0 8px 0 rgba(0,0,0,.25)">
  <div class="abs" style="left:371px;top:-28px;width:240px;height:66px;background:#B8C2D6;border:5px solid {L};border-radius:16px"></div>
  <div class="abs" style="left:30px;top:52px;width:910px;height:480px;box-sizing:border-box;background:#FFFDF6;border:4px solid {L};border-radius:14px;padding:26px 34px">
    <div style="display:flex;justify-content:space-between;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;border-bottom:3px dashed #D6CBB8;padding-bottom:12px"><span>진료 차트 · 환자: <b style="color:{L}">나스닥</b></span><span>16일 밤 접수</span></div>
    <div class="hook" style="font-size:68px;margin-top:22px;color:#4A3838">코스피는 반등했는데,</div>
    <div class="hook" style="font-size:92px;margin-top:6px;color:#2B2140">나스닥은 왜</div>
    <div class="hook" style="font-size:92px;color:#C2410C">또 빠졌을까?</div>
  </div>
</div>
<div class="abs" style="left:4px;top:950px;width:500px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="squish">{mascot("bamtol", "surprised", "point", STETH + MIRROR)}</div></div>
<div class="abs" style="left:530px;top:960px;width:496px;height:340px;box-sizing:border-box;background:#14202A;border:6px solid {L};border-radius:26px;overflow:hidden;box-shadow:0 8px 0 rgba(0,0,0,.25)">
  <div class="abs" style="left:24px;top:18px;font-size:32px;color:#5BF29B">♥ 나스닥 (16일)</div>
  <div class="abs" style="left:24px;top:80px;width:440px;height:150px">{ecg(440, 150)}</div>
  <div class="abs" style="left:0;right:0;top:230px;text-align:center;font-size:84px;color:#7DBBFF">▼2.14%</div>
</div>
{bub("<span style='font-size:48px'>응급 환자예요!</span><br>나스닥이 하루에<br><b>2% 넘게</b> 빠졌어요", 530, 1330, .15, "t-left", style="font-size:38px;padding:18px 28px")}
''', "#262B55"))

# 2 ── 증상 확인 (간호사 솜부엉, 환자 달떡이)
bed = (f'<div class="abs" style="left:{P}px;top:600px;width:440px;height:60px;background:#FFFFFF;border:5px solid {L};border-radius:18px"></div>'
       f'<div class="abs" style="left:{P}px;top:520px;width:30px;height:200px;background:#9AA7C7;border:5px solid {L};border-radius:10px"></div>'
       f'<div class="abs" style="left:{P + 420}px;top:570px;width:30px;height:150px;background:#9AA7C7;border:5px solid {L};border-radius:10px"></div>')
S[2] = (1, page(f'''
{head("증상 확인", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#E6F0FA;--d:.05s">
  {cbub("환자 <b>나스닥</b>, 어디가 아파요?", 36, .2, "t-down", style="font-size:42px")}
  {bed}
  {ch(mascot("moon", "teary", "down"), P + 80, 300, 300, .4, "a-pop", "shiver")}
  <div class="abs a-pop" style="left:{P + 120}px;top:670px;--d:.5s"><span class="tag" style="position:relative;background:#7B6FD6">환자 · 나스닥</span></div>
  {ch(mascot("owl", "worried", "hold", p_tablet()), 590, 290, 320, .6, "a-sr", "squish2")}
  {bub("<b>AI·반도체</b> 쪽이<br>특히 아프대요", 520, 170, 1.0, "t-down", "70%", "font-size:38px")}
  {nar("증상: 3대 지수 모두 하락, 기술주가 많은 나스닥이 가장 아팠어요", P, 770, 1.5, f"font-size:34px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("다우", "▼0.34%", COL3[0], 900, 2.0)}
  {numbox("S&P500", "▼1.09%", COL3[1], 900, 2.2)}
  {numbox("나스닥", "▼2.14%", COL3[2], 900, 2.4)}
</div>
''', "#2B3060"))

# 3 ── 원인 진단 (엑스레이 두 장) — 비유: 할부로 큰 공장 짓기 + 기름값 열
def film(icon, title, sub, col, d):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:250px;width:{w}px;height:330px;box-sizing:border-box;--d:{d}s;background:#1C2633;border:5px solid {L};border-radius:22px;text-align:center;color:#EAF2FF;padding-top:18px">'
            f'<div style="font-size:92px;line-height:1.1">{icon}</div><div style="font-size:42px;margin-top:8px;color:#FFE59A">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:26px;line-height:1.4;margin-top:8px;color:#C9D6EA">{sub}</div></div>')
S[3] = (1, page(f'''
{head("원인 진단", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#F3EEFF;--d:.05s">
  {cbub("엑스레이를 보니<br>원인이 <b>두 가지</b>예요", 40, .2, "t-down", style="font-size:42px")}
  {film("🏗️", "① 빚 몸살", "빚내서 AI 데이터센터를<br>지은 기업들, 갚을 수 있을까?", COL2[0], .6)}
  {film("🌡️", "② 기름값 열", "WTI 101.41달러 ▲3.5%<br>중동 불안에 100달러 넘음", COL2[1], 1.0)}
  {nar("<b>할부</b>로 큰 공장을 지었는데 <b>이자</b>까지 비싸면?<br>갚을 걱정에 몸이 무거워지죠", P, 640, 1.6, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("bamtol", "normal", "point", STETH + MIRROR), P, 780, 330, 2.2, "a-sl", "squish")}
  <div class="stamp a-stamp" style="left:400px;top:820px;--d:2.5s;--r:-6deg;font-size:56px;white-space:nowrap;text-align:center;line-height:1.25">진단<br>빚 걱정 + 기름값</div>
</div>
''', "#30366E"))

# 4 ── 보호자 상담 (한국)
c0 = COL2[0][0] + COL2[0][1] // 2; c1 = COL2[1][0] + COL2[1][1] // 2
S[4] = (1, page(f'''
{head("한국은요?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#E2F6EA;--d:.05s">
  <div class="abs" style="left:0;right:0;top:760px;height:370px;background:#CBE9D6;border-top:5px solid {L}"></div>
  {bub("선생님, 한국은요?<br>어제 좀 나아졌던데…", P, 60, .5, "t-down", f"{c0 - P - 15}px")}
  {bub("16일 코스피는<br><b>8거래일 만에 반등</b>!<br>반도체 걱정은 다시 와요", 0, 230, 1.2, "t-down", "60%", f"font-size:36px;left:auto;right:{P}px")}
  {ch(mascot("star", "worried"), c0 - 150, 470, 300, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "normal", "hold", STETH + MIRROR), c1 - 150, 470, 300, .4, "a-sr", "squish2")}
  {numbox("코스피 (16일)", "▲2.05%", COL2[0], 900, 2.0, RED)}
  {numbox("원/달러 1,331.4원 (16일)", "▼13.2원", COL2[1], 900, 2.3, BLUE)}
</div>
''', "#4A3E78"))

# 5 ── 처방전 (월요일 체크 3)
PILL = lambda c: f'<svg viewBox="0 0 80 80" width="70"><g transform="rotate(-35 40 40)"><rect x="8" y="26" width="64" height="28" rx="14" fill="#fff" stroke="{L}" stroke-width="4"/><path d="M40 26 h18 a14 14 0 0 1 0 28 h-18z" fill="{c}" stroke="{L}" stroke-width="4"/></g></svg>'
items = [(PILL("#BFD3FF"), "반도체, 반등 이어갈까?", f"미국 AI·반도체주 다시 약세 · 나스닥 <span style='color:#1D4ED8'>▼2.14%</span>"),
         (PILL("#FFB27F"), "기름값 100달러 돌파", f"WTI 101.41달러 <span style='color:#C92A2A'>▲3.5%</span> · 더 오르면 물가 부담"),
         (PILL("#FFE59A"), "외국인·환율은?", f"원/달러 1,331.4원 <span style='color:#1D4ED8'>▼13.2원</span> · 외국인 매수 이어질까")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{1.0+i*.5:.1f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ic}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("처방전 · 월요일 한국장", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFFDF6;--d:.05s">
  <div class="abs" style="left:{P}px;top:30px;font-size:60px;color:{GREEN}">℞ 처방전</div>
  <div class="abs" style="left:{P}px;top:110px;width:520px;border-top:4px dashed #D6CBB8"></div>
  {bub("월요일 한국장은<br>이 <b>세 가지</b>를<br>챙겨 보세요!", P, 150, .4, "t-right", style="font-size:42px")}
  {ch(mascot("bamtol", "happy", "point", STETH + MIRROR), 620, 110, 290, .2, "a-sr", "squish")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.2s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: AP, 뉴스핌, 뉴스1, 서울경제, SBS</div>
''', "#FFE1CC"))

# 6 ── 다음 진료 예약 (아침)
S[6] = (1, page(f'''
{head("밤사이 병원 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 진료 예약</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">내일(일) 아침 8시<br>지난주 성적표</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.35s;font-size:42px">다음 주엔 실적 발표 · <span style="color:#FFC08A">27~28일 FOMC</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.2s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("moon", "sleep", cap=True), 40, 240, 260, .35, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave", STETH), 620, 210, 290, .45, "a-sr", "hop")}
  {bub("푹 쉬고 오세요!<br><b>밤사이 병원</b>이었습니다", 300, 30, .75, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.1s">출처: AP, 뉴스핌, 뉴스1, 서울경제, CNBC, SBS · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (3.0, 1.3), 2: (4.0, 1.6), 3: (4.4, 1.6), 4: (3.6, 1.6), 5: (4.0, 1.6), 6: (3.2, 1.2)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "beep", 1), (1, .02, "whoosh", .4), (1, .15, "pop", .9), (1, .6, "slidedown", .5), (1, 1.0, "beep", .7),
 (2, .1, "whoosh", .5), (2, .2, "pop", .8), (2, .4, "sad", .5), (2, .6, "whoosh", .4), (2, 1.0, "pop", .8), (2, 1.5, "tick", 1), (2, 2.0, "blip_down", .7), (2, 2.2, "blip_down", .8), (2, 2.4, "blip_down", 1),
 (3, .2, "pop", .8), (3, .6, "shutter", .7), (3, 1.0, "shutter", .7), (3, 1.6, "tick", 1), (3, 2.2, "whoosh", .5), (3, 2.5, "thud", 1), (3, 2.5, "ding", .7),
 (4, .3, "whoosh", .6), (4, .5, "question", .8), (4, 1.2, "pop", .8), (4, 2.0, "sparkle", .6), (4, 2.3, "blip_down", .8),
 (5, .2, "whoosh", .5), (5, .4, "pop", .8), (5, 1.0, "CHECK1", 1), (5, 1.5, "CHECK2", 1), (5, 2.0, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .35, "whoosh", .5), (6, .45, "boing", .7), (6, .75, "pop", .8), (6, 1.0, "jingle", .9),
]
