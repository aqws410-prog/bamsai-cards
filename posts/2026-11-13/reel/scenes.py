"""2026-11-13 릴스 · 스포츠 중계(sports) v2 — '결론 먼저' 훅, 장면 1 '벤치 옆 교체판(LED) + 빈 감독석' 새 구도 (검수 전).
그날 상황: 젠슨 황 엔비디아 CEO 사임 → 엔비디아 ▼4.34% vs AMD ▲5.86%·브로드컴 ▲5.54% 엇갈림(대결 구도).
          상황표: 첫 칸(급변) 아님(3대 지수 0.3%대 약보합), 원인은 한 가지로 분명(원인 찾기·원인 여럿 아님) → '대결 구도' 1순위 sports(마지막 10-21).
흐름: 1 결론(▼4.34% '감독 퇴장, 라이벌 득점!', 교체판·빈 감독석) → 2 하이라이트(스코어: 엔비디아 vs AMD·브로드컴, 3대 지수 약보합)
      → 3 해설: 비유 '관중(투자금)은 경기장에 그대로, 응원석만 옆 팀으로' — AI 칩 수요는 그대로라는 시각 → 4 한국 팀 상황(12일 삼성전자 ▲ vs SK하이닉스 ▼)
      → 5 작전판(체크 3) → 6 다음 경기(오늘 밤 PPI).
숫자는 posts/2026-11-13 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

# 중계 헤드셋 (캐릭터 좌표계)
HEADSET = (f'<path d="M66 186 Q66 96 150 92 Q234 96 234 186" fill="none" stroke="#2B2B3A" stroke-width="10" stroke-linecap="round"/>'
           f'<rect x="50" y="168" width="30" height="50" rx="12" fill="#E8484A" stroke="{L}" stroke-width="4"/>'
           f'<rect x="220" y="168" width="30" height="50" rx="12" fill="#E8484A" stroke="{L}" stroke-width="4"/>'
           f'<path d="M66 214 Q80 252 124 250" fill="none" stroke="#2B2B3A" stroke-width="6" stroke-linecap="round"/>'
           f'<circle cx="128" cy="250" r="10" fill="#2B2B3A"/>')

FX = """<style>
@keyframes boardin{0%{transform:translateY(-40px) rotate(-6deg)}60%{transform:translateY(6px) rotate(2deg)}100%{transform:none}}
@keyframes ledblink{0%,49%{opacity:1}50%,100%{opacity:.35}}
@keyframes chairspin{0%{transform:rotate(0)}30%{transform:rotate(-14deg)}60%{transform:rotate(9deg)}100%{transform:rotate(0)}}
@keyframes move{0%{transform:translateX(0)}100%{transform:translateX(var(--dx))}}
@keyframes ball{0%{transform:translate(0,0)}100%{transform:translate(var(--dx),var(--dy))}}
.boardin{animation:boardin .6s cubic-bezier(.2,.9,.3,1) both}
.led{animation:ledblink .5s steps(1) infinite}
.chair{transform-origin:50% 90%;animation:chairspin .9s ease-out .3s both}
.move{animation:move 1s cubic-bezier(.3,.9,.3,1) var(--d,0s) both}
.ball{animation:ball .5s cubic-bezier(.3,.9,.3,1) var(--d,0s) both}
</style>"""

def turf(w, h):
    stripes = "".join(f'<div class="abs" style="left:{i*w//8}px;top:0;width:{w//16}px;height:{h}px;background:rgba(255,255,255,.07)"></div>' for i in range(8))
    return f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;background:#3E9C5A">{stripes}</div>'

# 교체판 (4번째 심판이 드는 LED 보드)
def subboard(x, y, w, d=0, cls="boardin"):
    return (f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s">'
            f'<div style="background:#14181F;border:6px solid {L};border-radius:20px;padding:18px 22px;box-shadow:0 8px 0 rgba(0,0,0,.3)">'
            f'<div style="display:flex;align-items:center;gap:16px;font-size:46px;color:#FF6B6B"><span class="led">◀</span> OUT · 젠슨 황</div>'
            f'<div style="height:4px;background:#333;margin:12px 0"></div>'
            f'<div style="display:flex;align-items:center;gap:16px;font-size:46px;color:#5BF29B"><span class="led" style="animation-delay:.25s">▶</span> IN · 임시 크레스</div></div>'
            f'<div style="margin:0 auto;width:40px;height:90px;background:#3A3A48;border:5px solid {L};border-top:none;border-radius:0 0 14px 14px"></div></div>')

CHAIR = (f'<svg viewBox="0 0 200 220" width="200" height="220" class="chair">'
         f'<rect x="30" y="10" width="140" height="120" rx="22" fill="#2F6BD8" stroke="{L}" stroke-width="6"/>'
         f'<text x="100" y="82" text-anchor="middle" font-size="34" fill="#fff" font-family="Jua">감독</text>'
         f'<rect x="20" y="126" width="160" height="40" rx="14" fill="#2558B5" stroke="{L}" stroke-width="6"/>'
         f'<path d="M100 166 V200 M60 210 H140" stroke="{L}" stroke-width="8" stroke-linecap="round"/></svg>')

# 1 ── 결론 먼저: 0초에 숫자·결론·캐스터(클로즈업)·교체판·빈 감독석이 모두 보인다
#      0~1초: 숫자 펀치(0) → 교체판 흔들며 내려옴(0~.6) + OUT/IN 깜빡임 → '삐익!'(.2) → 빈 의자 빙글(.3~1.2) → '감독 교체!' 도장(.45) → 캐스터 떨림(.5~)
S[1] = (1, page(FX + f'''
{stars(12, 52, 0, 170)}
{head("밤사이 중계석 · 11.13 FRI", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">엔비디아 · 12일 뉴욕</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#6FB0FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼4.34%</span></div>
<div class="abs" style="left:0;width:1080px;top:504px;text-align:center;font-size:86px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">감독 퇴장, <span style="color:#FFE36E">라이벌 득점!</span></div>
<div class="panel" style="left:44px;top:660px;width:982px;height:760px;background:#3E9C5A">
  {turf(982, 760)}
  <div class="abs" style="left:0;top:0;width:982px;height:150px;background:#2A2F4A;border-bottom:5px solid {L}"></div>
  {"".join(f'<div class="abs" style="left:{20 + i*60}px;top:{30 + (i%2)*40}px;width:44px;height:44px;border-radius:50%;background:{["#FFB27F","#9FC2FF","#FFE36E","#C9B8FF"][i%4]};border:3px solid {L}"></div>' for i in range(16))}
  {subboard(P, 120, 470)}
  <div class="abs" style="left:190px;top:510px">{CHAIR}</div>
  <div class="abs" style="left:440px;top:230px;width:470px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.5s">{mascot("bamtol", "surprised", "point", HEADSET)}</div></div>
  <div class="abs" style="left:30px;top:410px"><div class="stamp a-stamp" style="position:relative;--d:.45s;--r:-8deg;font-size:64px;white-space:nowrap;background:rgba(255,255,255,.92)">감독 교체!</div></div>
  {sfx("삐익!", 560, 160, 90, .2, 8, "#FFE36E")}
</div>
''', "#262B55"))

# 2 ── 하이라이트: 같은 경기장, 결과는 정반대
S[2] = (1, page(FX + f'''
{head("오늘의 하이라이트", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E6F0FA;--d:0s">
  {cbub("같은 반도체 리그,<br>결과는 <b>정반대</b>!", 36, .1, "t-down", style="font-size:50px")}
  <div class="abs a-pop" style="left:{P}px;top:250px;width:{IW}px;height:330px;box-sizing:border-box;--d:.3s;background:#14181F;border:6px solid {L};border-radius:24px">
    <div class="abs" style="left:0;width:451px;top:30px;text-align:center;font-size:44px;color:#9FC2FF">엔비디아</div>
    <div class="abs" style="left:451px;width:451px;top:30px;text-align:center;font-size:44px;color:#FFB27F">AMD</div>
    <div class="abs" style="left:445px;top:40px;width:6px;height:240px;background:#333"></div>
    <div class="abs" style="left:0;width:451px;top:110px;text-align:center;font-size:110px;line-height:1"><span class="thump" style="--d:.5s;color:#6FB0FF">▼4.34%</span></div>
    <div class="abs" style="left:451px;width:451px;top:110px;text-align:center;font-size:110px;line-height:1"><span class="thump" style="--d:.7s;color:#FF7A7F">▲5.86%</span></div>
    <div class="abs" style="left:0;width:902px;top:250px;text-align:center;font-size:34px;color:#FFE36E">브로드컴도 ▲5.54% 득점</div>
  </div>
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P + 20, 640, 230, 1.0, "a-sl", "squish")}
  {bub("3대 지수는<br><b>약보합</b> 마감!", 320, 690, 1.2, "t-left", style="font-size:46px")}
  {numbox("다우", "▼0.36%", COL3[0], 1000, 1.6, BLUE)}
  {numbox("S&amp;P500", "▼0.35%", COL3[1], 1000, 1.75, BLUE)}
  {numbox("나스닥", "▼0.39%", COL3[2], 1000, 1.9, BLUE)}
</div>
''', "#2B3060"))

# 3 ── 해설: 관중(투자금)은 그대로, 응원석만 옆 팀으로
def stand(label, bg, x, w, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:250px;width:{w}px;height:300px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};border-radius:22px">'
            f'<div class="abs" style="left:0;right:0;top:16px;text-align:center;font-size:42px">{label}</div></div>')
fans = "".join(f'<div class="abs move" style="left:{P + 40 + (i%4)*90}px;top:{360 + (i//4)*80}px;--dx:470px;--d:{.9 + i*.05:.2f}s;font-size:60px">🙋</div>' for i in range(8))
S[3] = (1, page(FX + f'''
{head("1분 해설 · 응원석 이동", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("관중(투자금)은 그대로,<br><b>응원석만 옆 팀</b>으로!", 36, .1, "t-down", style="font-size:48px")}
  {stand("엔비디아 석", "#BFD3FF", COL2[0][0], COL2[0][1], .3)}
  {stand("AMD·브로드컴 석", "#FFD3C2", COL2[1][0], COL2[1][1], .45)}
  {fans}
  {nar("감독(CEO)이 떠나도 <b>AI 칩 경기 인기</b>는 그대로", P, 600, 1.6, f"font-size:42px;width:{IW}px;box-sizing:border-box;text-align:center")}
  <div class="abs a-fade" style="left:{P}px;top:680px;width:{IW}px;--d:1.8s;text-align:center;font-size:32px;color:#5B5070">= AI 칩 수요는 줄지 않는다는 시각 · 그래서 경쟁사가 반사이익</div>
  {ch(mascot("moon", "worried", "down"), P + 20, 760, 250, 2.1, "a-sl", "shiver")}
  {bub("임시 감독은<br><b>크레스 CFO</b>예요", 320, 820, 2.3, "t-left", style="font-size:44px")}
  <div class="abs a-fade" style="left:{P}px;top:1110px;--d:2.3s;font-size:28px;color:#6B5A50">역: 달떡이 = 엔비디아 임시 감독(CFO = 최고재무책임자)</div>
</div>
''', "#30366E"))

# 4 ── 한국 팀 상황 (12일 서울)
S[4] = (1, page(FX + f'''
{head("한국 팀 상황", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:50px">그 전날(12일) 서울도 엇갈렸다</div>
  {numbox("삼성전자", "▲0.97%", COL2[0], 130, .3, RED)}
  {numbox("SK하이닉스", "▼1.80%", COL2[1], 130, .45, BLUE)}
  <div class="abs" style="left:{COL2[1][0]}px;top:300px;width:{COL2[1][1]}px;text-align:center;font-size:150px;line-height:1"><span class="thump" style="--d:.8s">📉</span></div>
  <div class="abs" style="left:{COL2[0][0]}px;top:300px;width:{COL2[0][1]}px;text-align:center;font-size:150px;line-height:1"><span class="thump" style="--d:.7s">📈</span></div>
  {cbub("엔비디아에 <b>HBM</b>(AI용 메모리)을<br>많이 대는 쪽이 더 흔들렸어요", 490, 1.0, "t-down", style="font-size:42px")}
  {ch(mascot("bamtol", "worried", "hold", HEADSET), COL2[1][0] + 100, 680, 280, 1.3, "a-sr", "squish2")}
  {ch(mascot("star", "surprised", "up"), COL2[0][0] + 60, 700, 260, 1.4, "a-sl", "shiver")}
  {numbox("코스피 (12일)", "▼0.61%", COL2[0], 1000, 1.7, BLUE)}
  {numbox("원/달러 (12일)", "1,330.7원", COL2[1], 1000, 1.85, L)}
</div>
''', "#4A3E78"))

# 5 ── 작전판 (오늘 한국장 체크)
items = [("💾", "반도체, 또 엇갈릴까", "엔비디아 납품 비중 큰 쪽엔 부담 가능성"),
         ("🛢️", "유가, 다시 오름세 탈까", f"WTI 88.74달러 <span style='color:#C92A2A'>▲2.55%</span>"),
         ("💱", "환율, 1,330원대 지킬까", "미 국채금리 오르면 상승 압력 가능성")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{660+i*200}px;width:982px;height:176px;background:#fff;--d:{.6+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:44px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none;font-size:60px;width:70px;text-align:center">{ic}</div>'
    f'<div><div style="font-size:52px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("작전판 · 오늘 한국장", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#FFF8E1;--d:0s">
  <div class="abs" style="left:{P}px;top:40px;width:470px;height:340px;background:#2F7A48;border:6px solid #8A5A3B;border-radius:20px">
    <div class="abs" style="left:232px;top:0;width:4px;height:328px;background:rgba(255,255,255,.6)"></div>
    <div class="abs" style="left:0;right:0;top:110px;text-align:center;font-size:80px;color:#fff"><span class="punch" style="--d:.1s">체크 3</span></div>
    <div class="abs" style="left:0;right:0;bottom:12px;text-align:center;font-size:38px;color:#fff">오늘의 작전</div></div>
  {ch(mascot("bamtol", "normal", "point", HEADSET), 580, 110, 270, .2, "a-sr", "squish")}
  {bub("엇갈린 날,<br>볼 것은 <b>셋</b>!", 540, 20, .35, "t-down", "40%", "font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:1.8s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 서울신문, 이투데이, 파이낸셜뉴스, 한국경제, 서울경제, 뉴스1</div>
''', "#FFE1CC"))

# 6 ── 다음 경기 일정 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 중계석 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 경기 · 오늘(금) 밤 22:30</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:72px;line-height:1.2">미국 10월<br>생산자물가(PPI)</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">다음 주엔 <span style="color:#FFC08A">앤트로픽 상장(19일 목표)</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave", HEADSET), 600, 210, 280, .4, "a-sr", "hop")}
  {bub("결과는 내일 아침 8시,<br><b>밤사이 중계석</b>에서!", 260, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: 서울신문, 이투데이, 파이낸셜뉴스, 뉴스1, 한국경제, 서울경제, 헤럴드경제<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.6, 1.5), 3: (4.6, 1.5), 4: (4.0, 1.5), 5: (4.0, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "whistle", .9), (1, .05, "thud", .8), (1, .2, "pop", .5), (1, .3, "whoosh", .5), (1, .45, "thud", 1), (1, .6, "cheer", .8), (1, 1.0, "ding", .6),
 (2, .05, "whoosh", .5), (2, .1, "pop", .8), (2, .3, "thud", .6), (2, .5, "blip_down", .8), (2, .7, "sparkle", .7), (2, 1.0, "boing", .5), (2, 1.2, "pop", .8), (2, 1.6, "blip_down", .5), (2, 1.75, "blip_down", .5), (2, 1.9, "blip_down", .5),
 (3, .1, "pop", .8), (3, .3, "boing", .6), (3, .45, "boing", .6), (3, .9, "STEPS_FAST", .6), (3, 1.0, "cheer", .5), (3, 1.6, "tick", 1), (3, 2.1, "whoosh", .5), (3, 2.3, "pop", .8),
 (4, .05, "whoosh", .5), (4, .3, "pop", .7), (4, .45, "blip_down", .7), (4, .7, "sparkle", .5), (4, .8, "slidedown", .5), (4, 1.0, "pop", .8), (4, 1.3, "boing", .5), (4, 1.7, "pop", .6), (4, 1.85, "pop", .6),
 (5, .05, "whoosh", .5), (5, .1, "whistle", .5), (5, .35, "pop", .8), (5, .6, "CHECK1", 1), (5, 1.05, "CHECK2", 1), (5, 1.5, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
