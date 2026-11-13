"""2026-11-14 릴스 · 병원 진료(clinic) v3 — '결론 먼저' 훅, 장면 1 '엑스레이 판독대(라이트박스 속 이틀 그래프 + 판독 도장)' 새 구도 (검수 전).
그날 상황: "어제 5% 넘게 뛴 AMD, 하루 만에 왜 8% 넘게 빠졌을까?" 원인 찾기가 핵심 → 둘째 칸 1순위 detective는 11-12에 써서(최근 3일)
          2순위 clinic(마지막 10-22). 첫 칸(큰 지표) PPI는 예상 하회로 시장 주인공이 아님.
흐름: 1 결론(AMD ▼8.75% '반짝 기대, 하루 만에 식었다', 엑스레이 판독대) → 2 증상: 반도체 병동(AMD·브로드컴·엔비디아) + 다우만 멀쩡
      → 3 진단: 비유 '옆 가게 사장님이 떠나자 손님이 몰릴 줄 알았는데, 상가 거리 전체가 썰렁해질까 걱정' + 차익 실현 풀이
      → 4 한국은?(SK하이닉스 ADR ▼4.30%, 13일 코스피·SK하이닉스) → 5 처방전(월요일 체크 3) → 6 다음 진료 예약(내일 주간 성적표).
숫자·사실은 posts/2026-11-14 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE, GREEN = "#E03131", "#2F6BD8", "#2FA36B"

# 청진기 (목에 건 모양)
STETH = (f'<path d="M80 236 Q150 286 220 236" fill="none" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<path d="M80 236 Q74 224 82 216 M220 236 Q226 224 218 216" fill="none" stroke="#5B6B8C" stroke-width="6" stroke-linecap="round"/>'
         f'<path d="M196 254 Q206 266 204 276" fill="none" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<circle cx="204" cy="284" r="12" fill="#C9D3E6" stroke="{L}" stroke-width="4"/>')
MIRROR = f'<circle cx="150" cy="118" r="20" fill="#E8F1FF" stroke="{L}" stroke-width="4"/><circle cx="150" cy="118" r="7" fill="#9FB7E0"/>'
NCAP = (f'<path d="M104 70 Q150 40 196 70 L190 96 Q150 84 110 96 Z" fill="#fff" stroke="{L}" stroke-width="4" stroke-linejoin="round"/>'
        f'<path d="M144 62 h12 M150 56 v12" stroke="#E8484A" stroke-width="5" stroke-linecap="round"/>')

FX = """<style>
@keyframes glow{0%,100%{box-shadow:0 0 0 rgba(160,210,255,0),0 8px 0 rgba(0,0,0,.25)}50%{box-shadow:0 0 46px rgba(160,210,255,.55),0 8px 0 rgba(0,0,0,.25)}}
@keyframes flickon{0%{opacity:.2}20%{opacity:1}30%{opacity:.4}45%,100%{opacity:1}}
@keyframes ringin{0%{transform:scale(1.7);opacity:0}100%{transform:scale(1);opacity:1}}
@keyframes cool{from{height:86%}to{height:22%}}
.glow{animation:glow 1.2s ease-in-out infinite}
.flickon{animation:flickon .5s steps(5) both;animation-delay:var(--d,0s)}
.ringin{animation:ringin .35s ease-out both;animation-delay:var(--d,0s)}
.xline path{animation:draw .8s ease-out both;animation-delay:var(--d,0s)}
</style>"""

def xray_chart(w, h, d=0.1):
    """이틀 그래프: 11일 → 12일 ▲(반짝) → 13일 ▼(급랭). 하얀 필름 선."""
    x0, x1, x2 = 60, w * .46, w - 70
    y0, y1, y2 = h * .55, h * .16, h * .92
    ln = 1600
    grid = "".join(f'<path d="M0 {h*k:.0f} H{w}" stroke="rgba(200,230,255,.18)" stroke-width="3"/>' for k in (.25, .5, .75))
    return (f'<svg class="xline" width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible">{grid}'
            f'<path d="M{x0} {y0} L{x1} {y1} L{x2} {y2}" fill="none" stroke="#EAF6FF" stroke-width="14" stroke-linejoin="round" stroke-linecap="round" '
            f'style="stroke-dasharray:{ln};--len:{ln};stroke-dashoffset:{ln};--d:{d}s;filter:drop-shadow(0 0 10px #9FD4FF)"/>'
            f'<circle cx="{x0}" cy="{y0}" r="12" fill="#EAF6FF"/></svg>')

# 1 ── 결론 먼저 (엑스레이 판독대): 0초에 숫자·결론·의사(클로즈업, 놀람)·판독대가 모두 보인다
#      0~1초: 숫자 펀치(0) → 판독대 불 깜빡 켜짐(.05) + 그래프 선 그리기(.1~.9) → 말풍선(.2) → 빨간 원(.4)+'급랭' 도장(.45) → '뚝!'(.7) → 의사 떨림(상시)
CW, CH = 902, 330
S[1] = (1, page(FX + f'''
{stars(12, 52, 0, 180)}
{head("밤사이 병원 · 11.14 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">어젯밤 뉴욕 · AMD</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#5AA9FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼8.75%</span></div>
<div class="abs" style="left:0;width:1080px;top:506px;text-align:center;font-size:76px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">반짝 기대, <span style="color:#FFE36E">하루 만에 식었다</span></div>
<div class="panel glow" style="left:44px;top:640px;width:982px;height:780px;background:#2E3550">
  <div class="abs" style="left:{P}px;top:18px;font-size:32px;color:#BFE3FF">● 엑스레이 판독대 · 환자 AMD</div>
  <div class="abs flickon" style="left:{P}px;top:74px;width:{CW}px;height:{CH + 60}px;--d:.05s;background:#0D1A2B;border:6px solid #9FD4FF;border-radius:20px;box-sizing:border-box;overflow:visible">
    <div class="abs" style="left:0;top:20px;width:{CW - 12}px;height:{CH}px">{xray_chart(CW - 12, CH)}</div>
    <div class="abs a-pop" style="left:{int((CW-12)*.46) - 130}px;top:-2px;--d:.35s;font-size:44px;color:#FF8A8F;-webkit-text-stroke:4px {L};paint-order:stroke fill">12일 ▲5.86%</div>
    <div class="abs" style="left:28px;top:{CH + 4}px;font-size:28px;color:#8FB4D8">11일</div>
  </div>
  <div class="abs ringin" style="left:{P + CW - 210}px;top:{74 + CH - 70}px;width:200px;height:120px;box-sizing:border-box;border:8px solid #FFE36E;border-radius:60px;--d:.4s"></div>
  <div class="abs a-pop" style="left:{P + CW - 300}px;top:{74 + CH + 80}px;--d:.5s;font-size:52px;color:#7DBBFF;-webkit-text-stroke:5px {L};paint-order:stroke fill">13일 ▼8.75%</div>
  <div class="stamp a-stamp" style="left:470px;top:640px;--d:.45s;--r:-8deg;font-size:64px;padding:2px 22px">판독: 급랭</div>
  {ch(mascot("bamtol", "surprised", "point", STETH + MIRROR), P - 10, 440, 330, 0, "", "shiver")}
  {bub("어제는 <b>펄펄</b>,<br>오늘은 꽁꽁!", 360, 470, .2, "t-left", style="font-size:42px;padding:16px 26px")}
  {sfx("뚝!", 640, 150, 110, .7, 10, "#7DBBFF")}
</div>
''', "#262B55"))

# 2 ── 증상: 반도체 병동 줄줄이 + 다우만 멀쩡
def bed(name, val, col, d):
    x, w = col
    return (f'<div class="abs a-pop" style="left:{x}px;top:250px;width:{w}px;height:260px;box-sizing:border-box;--d:{d}s;background:#fff;border:5px solid {L};border-radius:26px;text-align:center;padding-top:16px">'
            f'<div style="font-size:30px;color:#6B5A50">🛏 입원</div><div style="font-size:46px;margin-top:6px">{name}</div>'
            f'<div style="font-size:60px;color:{BLUE};line-height:1.3">{val}</div></div>')
S[2] = (1, page(FX + f'''
{head("증상 · 반도체 병동", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:640px;background:#E6F0FA;--d:0s">
  <div class="abs" style="left:0;width:982px;top:40px;text-align:center;font-size:76px">반도체주 <span class="thump" style="--d:.3s;color:{BLUE}">줄줄이 입원</span></div>
  <div class="abs a-fade" style="left:0;width:982px;top:150px;text-align:center;font-size:36px;color:#6B5A50;--d:.2s">13일(현지) 뉴욕 마감</div>
  {bed("AMD", "▼8.75%", COL3[0], .4)}
  {bed("브로드컴", "▼4.76%", COL3[1], .6)}
  {bed("엔비디아", "▼2.01%", COL3[2], .8)}
  {nar("엔비디아는 <b>이틀째</b> 하락", P, 540, 1.1, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
<div class="panel a-pop" style="left:44px;top:880px;width:982px;height:520px;background:#FFF8E1;--d:1.5s">
  {ch(mascot("owl", "normal", "hold", p_tablet()), P, 30, 230, 1.6, "a-sl", "squish")}
  {bub("다우만 <b>멀쩡</b>해요!", 300, 60, 1.8, "t-left", style="font-size:44px")}
  <div class="abs a-fade" style="left:300px;top:190px;width:640px;font-size:34px;color:#6B5A50;--d:2.0s">돈이 코카콜라 같은 전통 우량주로</div>
  {numbox("다우", "▲0.10%", COL3[0], 300, 2.2, RED)}
  {numbox("S&amp;P500", "▼0.40%", COL3[1], 300, 2.35, BLUE)}
  {numbox("나스닥", "▼0.91%", COL3[2], 300, 2.5, BLUE)}
</div>
''', "#2B3060"))

# 3 ── 진단: 옆 가게 사장님이 떠나자 → 손님 몰릴 줄 알았는데 → 상가 거리 전체가 썰렁해질까 걱정
def shop(label, x, y, w, color, d, closed=False):
    sign = '<div style="font-size:30px;color:#fff;background:#8A7F78;border-radius:10px;padding:2px 12px;display:inline-block;margin-top:10px">사장님 부재</div>' if closed else ''
    return (f'<div class="abs a-pop" style="left:{x}px;top:{y}px;width:{w}px;height:210px;--d:{d}s">'
            f'<div class="abs" style="left:0;top:0;width:{w}px;height:56px;background:repeating-linear-gradient(90deg,{color} 0 40px,#fff 40px 80px);border:4px solid {L};border-radius:14px 14px 0 0;box-sizing:border-box"></div>'
            f'<div class="abs" style="left:0;top:52px;width:{w}px;height:158px;background:#FFF6EA;border:4px solid {L};border-top:none;box-sizing:border-box;text-align:center">'
            f'<div style="font-size:40px;margin-top:12px">{label}</div>{sign}</div></div>')
S[3] = (1, page(FX + f'''
{head("진단 · 1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:600px;background:#F3EEFF;--d:0s">
  <div class="tag" style="left:{P}px;top:30px;font-size:34px">어제(12일)</div>
  {shop("엔비디아", P, 100, 260, "#9AA0B4", .15, True)}
  {shop("AMD", P + 300, 100, 260, "#FF8A8F", .3)}
  {ch(mascot("moon", "happy", "up"), 650, 60, 230, .5, "a-sr", "hop")}
  {bub("옆 가게 손님이<br>우리한테 <b>오겠지?</b>", 560, 320, .8, "t-up", "60%", "font-size:38px;padding:14px 22px")}
  <div class="abs" style="left:{P}px;top:350px;font-size:110px;line-height:1"><span class="punch" style="--d:.4s;color:{RED};-webkit-text-stroke:7px {L};paint-order:stroke fill">▲5.86%</span></div>
  {nar("사장님(CEO)이 떠난 옆 가게 → <b>반사이익</b> 기대", P, 500, 1.0, "font-size:36px")}
</div>
<div class="panel a-pop" style="left:44px;top:830px;width:982px;height:590px;background:#E8ECF4;--d:1.5s">
  <div class="tag" style="left:{P}px;top:30px;font-size:34px">오늘(13일)</div>
  <div class="abs a-fade" style="left:{P}px;top:100px;width:{IW}px;text-align:center;font-size:58px;--d:1.7s">“<span style="color:{BLUE}">AI 상가 거리</span> 전체가<br>썰렁해지면 어쩌지?”</div>
  {ch(mascot("moon", "worried", "down"), P, 290, 230, 2.0, "a-sl", "shiver")}
  {ch(mascot("bamtol", "normal", "point", STETH + MIRROR), 680, 270, 230, 2.2, "a-sr", "squish")}
  {bub("<b>차익 실현</b><br>= 오른 김에 팔기", 290, 330, 2.5, "t-right", style="font-size:40px;padding:14px 24px")}
  {sfx("썰렁~", 300, 470, 84, 2.9, -6, "#BFE3FF")}
</div>
''', "#30366E"))

# 4 ── 한국은?
c0 = COL2[0][0] + COL2[0][1] // 2
S[4] = (1, page(FX + f'''
{head("그럼 한국은?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1220px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:48px">미국에 상장된 <span style="color:#C2410C">SK하이닉스</span> 주식</div>
  <div class="abs" style="left:0;right:0;top:110px;text-align:center;font-size:200px;line-height:1"><span class="punch" style="--d:.15s;color:{BLUE};-webkit-text-stroke:8px {L};paint-order:stroke fill">▼4.30%</span></div>
  {ch(mascot("star", "surprised", "up"), P, 380, 300, .5, "a-sl", "shiver")}
  {bub("서울 반도체주도<br><b>긴장</b>하겠네!", 360, 420, .8, "t-left", style="font-size:44px")}
  <div class="abs a-pop" style="left:{P}px;top:740px;width:{IW}px;--d:1.3s;text-align:center;font-size:44px">그 전날(13일) 서울은?</div>
  {numbox("코스피", "▼0.98%", COL2[0], 820, 1.5, BLUE)}
  {numbox("SK하이닉스", "▼3.03%", COL2[1], 820, 1.7, BLUE)}
  {nar("장중 5,500선 넘었다가 <b>외국인 매도</b>에 밀렸어요", P, 1020, 2.1, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
''', "#4A3E78"))

# 5 ── 처방전 (월요일 체크 3)
PILL = lambda c: f'<svg viewBox="0 0 80 80" width="76"><g transform="rotate(-35 40 40)"><rect x="8" y="26" width="64" height="28" rx="14" fill="#fff" stroke="{L}" stroke-width="4"/><path d="M40 26 h18 a14 14 0 0 1 0 28 h-18z" fill="{c}" stroke="{L}" stroke-width="4"/></g></svg>'
items = [(PILL("#BFD3FF"), "반도체, 충격 흡수할까", "미국 반도체주 급락이 반영될지"),
         (PILL("#FFE59A"), "외국인, 다시 팔까", "13일 매도로 돌아선 외국인"),
         (PILL("#FFB27F"), "금리 인상 걱정", "미국 생산자물가 1년 새 <span style='color:#C92A2A'>▲6.5%</span>")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{580+i*230}px;width:982px;height:200px;background:#fff;--d:{.5+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 30px;box-sizing:border-box">'
    f'<div style="flex:none;width:84px;height:84px;border-radius:50%;background:#FFB27F;border:5px solid {L};font-size:52px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ic}</div>'
    f'<div><div style="font-size:56px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("처방전 · 월요일 한국장", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:340px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:{P}px;top:34px;font-size:96px;color:{GREEN}">℞ 처방전</div>
  <div class="abs" style="left:{P}px;top:160px;font-size:52px">월요일엔 이 <span style="color:#E8590C">3가지</span>!</div>
  {ch(mascot("bamtol", "happy", "point", STETH + MIRROR), 640, 40, 280, .15, "a-sr", "squish")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:1.8s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 파이낸셜뉴스, 서울신문, 미디어펜, 아시아경제, 서울경제, AP</div>
''', "#FFE1CC"))

# 6 ── 다음 진료 예약
S[6] = (1, page(FX + f'''
{head("밤사이 병원 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:40px;color:#FFC08A">다음 진료 예약</div>
  <div class="abs" style="left:44px;top:100px;font-size:72px;line-height:1.2">내일(일) 아침 8시<br>이번 주 성적표</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.3s;font-size:42px">다음 주엔 <span style="color:#FFC08A">19일 앤트로픽 상장 목표</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .3, "a-sl", "hop")}
  {ch(mascot("bamtol", "happy", "wave", STETH), 640, 210, 290, .4, "a-sr", "squish")}
  {bub("주말 푹 쉬세요!<br><b>밤사이 병원</b>이었습니다", 300, 30, .65, "t-down", "60%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 파이낸셜뉴스, 서울신문, 이투데이, MTN, 미디어펜, AP · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.2, 1.6), 3: (4.8, 1.6), 4: (4.2, 1.6), 5: (4.2, 1.6), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "beep", .9), (1, .05, "scan", .6), (1, .2, "pop", .9), (1, .4, "blip_down", .9), (1, .45, "thud", 1), (1, .7, "slidedown", .6), (1, 1.2, "beep", .5),
 (2, .05, "whoosh", .5), (2, .3, "thud", .7), (2, .4, "blip_down", .6), (2, .6, "blip_down", .7), (2, .8, "blip_down", .8), (2, 1.1, "tick", .8), (2, 1.5, "whoosh", .5), (2, 1.8, "pop", .8), (2, 2.2, "pop", .6), (2, 2.35, "pop", .6), (2, 2.5, "pop", .6),
 (3, .05, "whoosh", .5), (3, .15, "pop", .6), (3, .3, "pop", .6), (3, .4, "sparkle", .7), (3, .5, "boing", .6), (3, .8, "pop", .8), (3, 1.0, "tick", .8), (3, 1.5, "whoosh", .5), (3, 1.7, "hmm", .6), (3, 2.0, "sad", .5), (3, 2.5, "ding", .7), (3, 2.9, "slidedown", .5),
 (4, .05, "whoosh", .5), (4, .15, "blip_down", 1), (4, .2, "thud", .8), (4, .5, "boing", .6), (4, .8, "pop", .8), (4, 1.3, "whoosh", .4), (4, 1.5, "pop", .6), (4, 1.7, "pop", .6), (4, 2.1, "tick", .8),
 (5, .05, "whoosh", .5), (5, .15, "pop", .7), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
