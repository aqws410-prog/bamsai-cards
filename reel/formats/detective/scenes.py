"""형식: 밤사이 탐정 추리 (검수 전 · 2026-10-16 처음 제작, 같은 날 피드백으로 장면 1 훅을 탐정 전용 레이아웃으로 교체) — 밤톨이 탐정, 별콩이 의뢰인, 솜부엉 조수.
내용: 2026-10-16 (코스피 15일 ▼7.57% · 미국 3대 지수 상승, AI → 헬스케어 갈아타기). 비유: 놀이공원 롤러코스터 줄 → 회전목마 줄.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

# 1 ── 사건 발생 (훅) — 탐정 시그니처: 사선 폴리스 라인 + 사건 파일 폴더 + 스포트라이트 속 탐정 클로즈업
#      (뉴스 속보 장면 1의 '배너 → 헤드라인 2줄 → 캐릭터 컷 → 티커' 구조를 쓰지 않는다)
TAPE = "사건 현장 · 출입 금지 · 밤사이 탐정 · " * 4
S[1] = (1, page(f'''
{stars(16, 31, 0, 400)}
<div class="abs" style="left:-120px;top:780px;width:1320px;height:1100px;background:radial-gradient(circle at 30% 50%,rgba(255,236,170,.30) 0,rgba(255,236,170,.10) 22%,transparent 40%)"></div>
{head("밤사이 탐정 · 10.16 FRI", 1, "#F6EEE4")}
<div class="abs" style="left:-80px;top:250px;width:1240px;height:86px;background:repeating-linear-gradient(135deg,#FFD84D 0 46px,#2A2A2A 46px 64px);border-top:6px solid {L};border-bottom:6px solid {L};transform:rotate(-3deg);overflow:hidden;box-shadow:0 8px 0 rgba(0,0,0,.25)">
  <div style="position:absolute;left:0;right:0;top:12px;height:56px;background:#FFD84D;font-size:44px;line-height:56px;white-space:nowrap;padding-left:30px">{TAPE}</div></div>
<div class="abs" style="left:44px;top:440px;width:360px;height:70px;background:#D9B06A;border:5px solid {L};border-bottom:none;border-radius:20px 20px 0 0;font-size:36px;line-height:66px;text-align:center">사건 파일 No.1016</div>
<div class="abs" style="left:44px;top:504px;width:982px;height:500px;box-sizing:border-box;background:#E9C98A;border:5px solid {L};border-radius:0 26px 26px 26px;box-shadow:0 8px 0 rgba(0,0,0,.22)">
  <div class="abs" style="left:{P}px;top:34px;font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B4A2A">의뢰인: 코스피 · 사건: 15일 하루 ▼7.57%</div>
  <div class="abs hook" style="left:{P}px;top:100px;font-size:96px;color:#2B2140">미국은<br>왜 올랐을까?</div>
  <div class="abs" style="left:{P}px;top:350px;font-size:44px;color:#5A3A1A">코스피가 무너진 바로 그 밤</div>
  <div class="abs" style="left:620px;top:80px;width:300px;transform:rotate(5deg)"><div class="pola" style="position:relative"><div class="pin"></div>
    <div style="height:200px;background:#E7ECFA;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:34px">코스피 (15일)</div><div style="font-size:84px;color:#2F6BD8">▼7.57%</div></div>
    <div style="margin-top:4px">증거물 1</div></div></div>
</div>
<div class="abs" style="left:20px;top:1070px;width:500px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="squish">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
{bub("<span style='font-size:50px'>사건 접수!</span><br>그날 밤 미국은<br><b>3대 지수 모두 상승</b>", 540, 1120, .2, "t-left", style="font-size:40px;padding:22px 30px")}
<div class="abs a-stamp" style="left:560px;top:1420px;--d:.6s;--r:-5deg;background:#fff;border:5px solid {L};border-radius:16px;padding:8px 22px;font-size:40px;box-shadow:0 6px 0 rgba(0,0,0,.2)">증거 2 · 다우 <span style="color:#E03131">▲1.08%</span></div>
''', "#262B55"))

# 2 ── 용의자 셋 (코르크 보드)
def suspect(icon, name, note, col, d, rot, ncol):
    x, w = col
    return (pola(f'<div style="height:170px;font-size:110px;line-height:170px;background:#EEF1FA">{icon}</div>', name, x, 250, w, d, rot)
            + f'<div class="abs a-pop" style="left:{x}px;top:540px;width:{w}px;text-align:center;--d:{d + .3:.1f}s"><span class="tag" style="position:relative;background:{ncol}">{note}</span></div>')
S[2] = (1, page(f'''
{head("용의자 셋", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#3A4080;--d:.05s">
  {cork(P, 200, IW, 470, .1)}
  {cbub("어젯밤 미국장을 <b>끌어올린 범인</b>은<br>이 셋 중 누구일까요?", 40, .3, "t-down", style="font-size:40px")}
  {suspect("🏥", "헬스케어주", "강세", COL3[0], .9, -4, RED)}
  {suspect("💾", "반도체주", "장중 약세", COL3[1], 1.3, 3, BLUE)}
  {suspect("🌡️", "생산자물가", "1.3% 급등", COL3[2], 1.7, -3, "#7B6FD6")}
  {ch(mascot("owl", "worried", "hold", p_tablet()), P, 720, 300, 2.2, "a-sl", "squish")}
  {bub("물가가 4년 반 만에<br>가장 크게 뛰었는데<br>주가가 올랐다고요?", 370, 760, 2.5, "t-left", style="font-size:38px")}
</div>
''', "#2B3060"))

# 3 ── 단서로 주범 지목 (비유: 롤러코스터 줄 → 회전목마 줄)
S[3] = (1, page(f'''
{head("단서 분석", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#F3EEFF;--d:.05s">
  {cbub("단서를 보면 범인은…<br><b>'줄 바꾸기'</b>예요!", 30, .25, "t-down", style="font-size:42px")}
  <div class="abs a-pop" style="left:{COL2[0][0]}px;top:230px;width:{COL2[0][1]}px;height:340px;box-sizing:border-box;background:#E7ECFA;border:4px solid {L};border-radius:26px;text-align:center;--d:.6s">
     <div style="font-size:96px;margin-top:20px">🎢</div><div style="font-size:38px">롤러코스터 줄</div><div style="font-size:30px;color:{BLUE}">AI·반도체</div></div>
  <div class="abs a-pop" style="left:{COL2[1][0]}px;top:230px;width:{COL2[1][1]}px;height:340px;box-sizing:border-box;background:#FFECEC;border:4px solid {L};border-radius:26px;text-align:center;--d:.9s">
     <div style="font-size:96px;margin-top:20px">🎠</div><div style="font-size:38px">회전목마 줄</div><div style="font-size:30px;color:{RED}">헬스케어 등 방어주</div></div>
  {string(300, 530, 680, 530, 1.3)}
  {stamp("주범: 갈아타기", 220, 600, 1.8, -6)}
  {nar("무서워진 사람들이 <b>짜릿한 AI 줄</b>을 떠나<br><b>얌전한 회전목마 줄</b>로 옮겨 섰어요", P, 740, 2.4, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("다우", "▲1.08%", COL2[0], 900, 3.0, RED)}
  {numbox("나스닥 (기술주 많음)", "▲0.08%", COL2[1], 900, 3.3, RED)}
</div>
''', "#30366E"))

# 4 ── 한국 피해 조사
S[4] = (1, page(f'''
{head("한국 피해 조사", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#E2F6EA;--d:.05s">
  <div class="abs" style="left:0;right:0;top:760px;height:370px;background:#CBE9D6;border-top:5px solid {L}"></div>
  {bub("탐정님, 한국은요?<br>너무 많이 빠졌어요…", P, 60, .6, "t-down", "120px")}
  {bub("15일 코스피·코스닥 모두<br><b>서킷브레이커</b>(거래 일시 정지)!<br>7거래일 연속 하락이에요", 0, 250, 1.3, "t-down", "70%", f"font-size:36px;left:auto;right:{P}px")}
  {ch(mascot("star", "teary"), COL2[0][0] + 65, 470, 300, .3, "a-sl", "shiver")}
  {ch(mascot("bamtol", "worried", "hold", p_mag()), COL2[1][0] + 65, 470, 300, .4, "a-sr", "squish2")}
  {numbox("코스피 (15일)", "▼7.57%", COL2[0], 900, 2.3, BLUE)}
  {numbox("원/달러 (15일)", "▲6.3원", COL2[1], 900, 2.6, RED)}
</div>
{ticker("코스피 5,554.22 ▼7.57% · 원/달러 1,344.6원 ▲6.3원 · 삼성전자·SK하이닉스 10% 안팎 급락", 1380, "한국")}
''', "#4A3E78"))

# 5 ── 수사 노트 (오늘의 체크)
KOSPI_ICON = (f'<svg viewBox="0 0 80 80" width="70"><rect x="8" y="10" width="64" height="60" rx="12" fill="#FFE3E3" stroke="{L}" stroke-width="4"/>'
              f'<path d="M18 30 l14 14 l10 -8 l20 20" stroke="{BLUE}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
items = [(KOSPI_ICON, "코스피, 하락 멈출까?", f"미국 3대 지수는 상승 마감 · 다우 <span style='color:#C92A2A'>▲1.08%</span>"),
         (ICONS["chip"], "반도체, 숨 고를까?", "미국 반도체주는 장중 약세"),
         (ICONS["won"], "외국인·환율은?", f"원/달러 1,344.6원 <span style='color:#C92A2A'>▲6.3원</span>")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{1.2+i*.5:.1f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ic}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 노트 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFF8E1;--d:.05s">
  {ch(mascot("bamtol", "normal", "point"), 600, 120, 290, .2, "a-sr", "squish")}
  {bub("오늘 한국장은<br>이 <b>세 가지</b>를<br>수사하세요!", P, 90, .5, "t-right", style="font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.6s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 로이터, 뉴스핌, 서울경제, 뉴스1, 아시아경제</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(f'''
{head("밤사이 탐정 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 사건 (미국 시간 10/16 금요일)</div>
  <div class="abs" style="left:44px;top:100px;font-size:66px;line-height:1.2">금요일 미국장,<br>폭풍 같은 한 주의 마감</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.35s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.2s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .35, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .45, "a-sr", "hop")}
  {bub("사건 종결!<br><b>밤사이 탐정</b>이었습니다", 300, 30, .75, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.1s">출처: 로이터, 뉴스핌, 서울경제, 뉴스1, 아시아경제 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.9, 1.3), 2: (4.0, 1.6), 3: (4.6, 1.6), 4: (3.8, 1.6), 5: (4.1, 1.7), 6: (3.2, 1.2)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .7), (1, .02, "whoosh", .4), (1, .2, "pop", .9), (1, .6, "thud", .7), (1, .7, "question", .5),
 (2, .1, "whoosh", .5), (2, .3, "pop", .8), (2, .9, "shutter", .7), (2, 1.3, "shutter", .7), (2, 1.7, "shutter", .7), (2, 2.2, "whoosh", .5), (2, 2.5, "pop", .7),
 (3, .25, "pop", .8), (3, .6, "pop", .6), (3, .9, "pop", .6), (3, 1.3, "whoosh", .6), (3, 1.8, "thud", 1), (3, 1.8, "reveal", .8), (3, 2.4, "tick", 1), (3, 3.0, "ding", .8), (3, 3.3, "ding", .6),
 (4, .3, "whoosh", .6), (4, .6, "pop", .8), (4, .7, "sad", .5), (4, 1.3, "pop", .8), (4, 2.3, "blip_down", 1), (4, 2.6, "pop", .6),
 (5, .2, "whoosh", .5), (5, .5, "pop", .8), (5, 1.2, "CHECK1", 1), (5, 1.7, "CHECK2", 1), (5, 2.2, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .35, "whoosh", .5), (6, .45, "boing", .7), (6, .75, "pop", .8), (6, 1.0, "jingle", .9),
]
