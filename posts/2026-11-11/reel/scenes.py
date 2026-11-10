"""2026-11-11 릴스 · 토크쇼(talkshow) v3 — '결론 먼저' 훅, 장면 1 'ON AIR 스튜디오 + 대형 물가 성적표 채점판' 새 구도 (검수 전).
그날 상황: 미국 10월 CPI 전월비 ▲0.4%(예상 0.3%), 월러 연준 이사 '0.5%p(빅스텝)도 고려' → 큰 지표 발표 칸.
          1순위 news는 11-10에 써서(최근 3일) 2순위 talkshow(마지막 11-06, 최근 3일 밖). '한 인물의 발언이 핵심' 칸과도 맞음.
흐름: 1 결론(▲0.4% '물가, 예상보다 뜨거웠다!', 성적표 채점판) → 2 게스트 토크(달떡이가 '연준 이사' 역: 12월 인상, 0.5%p도)
      → 3 1분 해설: 비유 '안 식는 라면 국물 — 연준은 후~ 불어 식히는 사람, 빅스텝 = 두 배 세게 후~~' + 3대 지수
      → 4 방청객 질문: 한국은?(어제 코스피 ▲4.39%, 밤사이 엔비디아 ▼5.47%) → 5 오늘 체크 3(자막 카드) → 6 예고(금요일 밤 PPI).
숫자는 posts/2026-11-11 카드·sources.md에 있는 것만 쓴다. 게스트 대사는 기사로 확인된 내용을 쉬운 말로 옮긴 역할극이다(실제 발언 인용 아님).
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes onair{0%,49%{opacity:1;box-shadow:0 0 22px #FF4D4D}50%,100%{opacity:.55;box-shadow:none}}
.onair{animation:onair .5s steps(1) infinite}
@keyframes circ{from{stroke-dashoffset:900}to{stroke-dashoffset:0}}
.circ{stroke-dasharray:900;animation:circ .5s ease-out both;animation-delay:var(--d,0s)}
@keyframes steam{0%{transform:translateY(10px) scaleX(1);opacity:0}30%{opacity:.9}100%{transform:translateY(-60px) scaleX(1.2);opacity:0}}
.steam{animation:steam 1.2s ease-out infinite;animation-delay:var(--d,0s)}
@keyframes blow{0%{transform:scaleX(.2);opacity:0}40%{opacity:1}100%{transform:scaleX(1);opacity:0}}
.blow{transform-origin:0 50%;animation:blow .9s ease-out infinite;animation-delay:var(--d,0s)}
@keyframes heads{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
</style>"""

def p_mic():
    """마이크 (캐릭터 오른손 쪽)."""
    return (f'<path d="M204 222 L188 266" stroke="{L}" stroke-width="13" stroke-linecap="round"/>'
            f'<path d="M204 222 L188 266" stroke="#2F2F3A" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="212" cy="196" r="19" fill="#3A3A48" stroke="{L}" stroke-width="5"/>'
            f'<path d="M200 190 h24 M198 198 h28 M202 206 h20" stroke="#8C92AE" stroke-width="2.5"/>')

def audience(y, n=9, w=982, seed=0):
    """방청객 뒷머리 실루엣 줄 (통통 움직임)."""
    out = ""
    for i in range(n):
        x = 20 + i * (w - 40) // n
        c = ["#4B4380", "#5A5196", "#433B74"][(i + seed) % 3]
        out += (f'<div class="abs" style="left:{x}px;top:{y + (i % 2) * 14}px;width:96px;height:110px;border-radius:48px 48px 20px 20px;'
                f'background:{c};border:4px solid {L};animation:heads {0.7 + (i % 3) * .15}s ease-in-out infinite"></div>')
    return out

def bowl(x, y, w=360, d=0):
    """김 나는 라면 그릇."""
    h = int(w * .55)
    st = "".join(f'<path class="steam" style="--d:{d + k * .35}s;transform-box:fill-box" d="M{w*.3 + k*w*.2} {40} q-18 -30 0 -60 q18 -30 0 -60" stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round" opacity=".9"/>' for k in range(3))
    return (f'<svg class="abs" style="left:{x}px;top:{y - 120}px" width="{w}" height="{h + 160}" viewBox="0 -120 {w} {h + 160}">{st}'
            f'<path d="M10 60 H{w-10} Q{w-30} {h+20} {w/2} {h+20} Q30 {h+20} 10 60 Z" fill="#F4A64A" stroke="{L}" stroke-width="6"/>'
            f'<ellipse cx="{w/2}" cy="60" rx="{w/2-10}" ry="26" fill="#E8590C" stroke="{L}" stroke-width="6"/>'
            f'<path d="M{w*.25} 58 q20 -14 40 0 t40 0 t40 0 t40 0" stroke="#FFE59A" stroke-width="7" fill="none"/>'
            f'<text x="{w/2}" y="{h-10}" text-anchor="middle" font-family="Jua" font-size="44" fill="#fff" stroke="{L}" stroke-width="2">물가</text></svg>')

# 1 ── 결론 먼저 (ON AIR 스튜디오 + 대형 물가 성적표 채점판): 0초에 숫자·결론·MC(클로즈업, 놀람)·성적표가 모두 보인다
#      0~1초: 숫자 펀치(0) → 빨간 펜 동그라미 그리기(.1~.6) → '예상 초과' 도장 쾅(.4) → 말풍선(.25) → '헉!' 효과 글자(.7) → MC 떨림·방청객 들썩(상시)
S[1] = (1, page(FX + f'''
{stars(12, 77, 0, 180)}
{head("밤사이 토크쇼 · 11.11 WED", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:192px;text-align:center;font-size:46px;color:#C9D6FF">미국 10월 소비자물가 (전월비)</div>
<div class="abs" style="left:0;width:1080px;top:250px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#FF6B6B;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲0.4%</span></div>
<div class="abs" style="left:0;width:1080px;top:500px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">물가, <span style="color:#FFE36E">예상보다 뜨거웠다!</span></div>
<div class="panel" style="left:44px;top:640px;width:982px;height:780px;background:#2C2450">
  <div class="abs onair" style="left:{P}px;top:26px;background:#E8484A;color:#fff;border:5px solid {L};border-radius:14px;padding:4px 20px;font-size:38px">● ON AIR</div>
  <div class="abs" style="right:{P}px;top:40px;width:520px;height:340px;box-sizing:border-box;background:#FFFDF5;border:6px solid {L};border-radius:18px;transform:rotate(2deg);
       background-image:repeating-linear-gradient(0deg,transparent 0 58px,#E6E1F2 58px 61px)">
    <div class="abs" style="left:28px;top:16px;font-size:40px">📋 10월 물가 성적표</div>
    <div class="abs" style="left:28px;top:96px;font-size:44px;color:#6B5A50">예상 &nbsp;<span style="font-size:60px;color:{L}">0.3%</span></div>
    <div class="abs" style="left:28px;top:186px;font-size:44px;color:#6B5A50">실제 &nbsp;<span style="font-size:80px;color:{RED}">0.4%</span></div>
    <svg class="abs" style="left:100px;top:168px" width="270" height="140" viewBox="0 0 260 140"><ellipse class="circ" style="--d:.1s" cx="135" cy="70" rx="128" ry="58" fill="none" stroke="{RED}" stroke-width="8"/></svg>
  </div>
  <div class="stamp a-stamp" style="left:640px;top:340px;--d:.4s;--r:-10deg;font-size:56px;padding:2px 20px">예상 초과</div>
  {audience(630, 9)}
  <div class="abs" style="left:-30px;top:300px;width:440px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver">{mascot("bamtol", "surprised", "hold", p_mic())}</div></div>
  {bub("예상보다 0.1%p<br>높을 뿐인데 <b>술렁!</b>", P, 100, .25, "t-down", "60%", "font-size:38px;padding:14px 20px")}
  {sfx("헉!", 390, 440, 110, .7, 10, "#FFE36E")}
</div>
''', "#262B55"))

# 2 ── 게스트 토크 (달떡이가 '연준 이사' 역) — 기사로 확인된 내용만 쉬운 말로
S[2] = (1, page(FX + f'''
{head("게스트 토크", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3E3570;--d:0s">
  <div class="abs" style="left:{P}px;top:36px;width:{IW}px;box-sizing:border-box;background:#FFF8E1;border:5px solid {L};border-radius:22px;text-align:center;padding:10px 0">
    <div style="font-size:32px;color:#8A5A3B">오늘의 게스트 (역: 달떡이)</div>
    <div style="font-size:60px"><span style="color:#E8590C">연준 이사</span> 월러</div></div>
  {ch(mascot("moon", "normal", "point"), P, 250, 300, .15, "a-sl", "squish")}
  {bub("12월엔 금리를<br><b>올려야죠</b>", 360, 260, .4, "t-left", style="font-size:46px")}
  {bub("물가가 계속 높으면<br><b>0.5%p</b>도 생각해요", 360, 440, 1.0, "t-left", style="font-size:46px")}
  {ch(mascot("bamtol", "surprised", "hold", p_mic()), 680, 620, 200, 1.5, "a-sr", "shiver")}
  <div class="abs a-pop" style="left:{P}px;top:660px;width:600px;--d:1.7s;text-align:center">
    <div style="font-size:42px;color:#FFE59A">이걸 부르는 말</div>
    <div style="font-size:150px;line-height:1.05;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="thump" style="--d:1.9s">빅스텝</span></div></div>
  {nar("<b>빅스텝</b> = 금리를 한 번에 0.5%p 올리기", P, 900, 2.2, f"font-size:44px;width:{IW}px;box-sizing:border-box;text-align:center")}
  <div class="abs a-fade" style="left:0;width:982px;top:1080px;text-align:center;font-family:Noto Sans CJK KR,sans-serif;font-size:26px;color:#CFC4E0;--d:2.4s">기사 내용을 쉬운 말로 옮긴 역할극입니다</div>
</div>
''', "#2B3060"))

# 3 ── 1분 해설: 안 식는 라면 국물 (연준 = 후~ 불어 식히는 사람)
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("물가는 <b>안 식는 라면 국물!</b><br>후~ 불어 식히는 게 연준이에요", 30, .1, "t-down", style="font-size:44px")}
  {bowl(80, 400, 360, .2)}
  {ch(mascot("owl", "worried", "point"), 520, 230, 260, .5, "a-sr", "squish")}
  <svg class="abs" style="left:400px;top:330px" width="140" height="80" viewBox="0 0 140 80"><path class="blow" style="--d:.9s" d="M130 20 H20 M130 40 H10 M130 60 H30" stroke="#7EC8FF" stroke-width="9" stroke-linecap="round"/></svg>
  {sfx("후~~", 760, 300, 90, .9, -6, "#9AD3FF")}
  <div class="abs a-pop" style="left:{P}px;top:640px;width:{IW}px;box-sizing:border-box;--d:1.3s;background:#fff;border:5px solid {L};border-radius:26px;padding:20px 30px;font-size:42px;line-height:1.5;text-align:center">
    후~ = <b style="color:#6A4FD8">금리 인상</b> · 후~~ 두 배 세게 = <b style="color:{RED}">빅스텝</b><br>
    <span style="font-size:36px;color:#6B5A50">세게 불면 돈 빌리기가 비싸져 주식엔 부담</span></div>
  {numbox("다우", "▼0.30%", COL3[0], 880, 1.9, BLUE)}
  {numbox("S&amp;P500", "▼0.38%", COL3[1], 880, 2.05, BLUE)}
  {numbox("나스닥", "▼0.74%", COL3[2], 880, 2.2, BLUE)}
  <div class="abs a-fade" style="left:0;width:982px;top:1060px;text-align:center;font-size:40px;--d:2.5s">근원 물가도 <span style="color:{RED}">0.3%</span> (예상 0.2%)</div>
</div>
''', "#30366E"))

# 4 ── 방청객 질문: 한국은?
S[4] = (1, page(FX + f'''
{head("방청객 질문", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {ch(mascot("star", "surprised", "up"), P, 40, 230, .1, "a-sl", "hop")}
  {bub("한국 증시는<br><b>어땠어요?</b>", 300, 70, .3, "t-left", style="font-size:46px")}
  <div class="abs" style="left:{P}px;top:330px;width:{IW}px;text-align:center">
    <div class="a-fade" style="--d:.6s;font-size:40px">어제(10일) 코스피</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.7s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲4.39%</span></div></div>
  {numbox("삼성전자", "▲4.74%", COL2[0], 560, 1.0, RED)}
  {numbox("SK하이닉스", "▲6.69%", COL2[1], 560, 1.15, RED)}
  <div class="abs a-drop" style="left:{P}px;top:760px;width:{IW}px;box-sizing:border-box;--d:1.6s;background:#1B2040;border:5px solid {L};border-radius:24px;color:#fff;text-align:center;padding:12px 0">
    <div style="font-size:36px;color:#FFE59A">그런데 밤사이 엔비디아</div>
    <div style="font-size:84px;line-height:1.15"><span class="punch" style="--d:1.8s;color:#7DBBFF">▼5.47%</span></div></div>
  {ch(mascot("bamtol", "worried", "hold", p_mic()), P, 990, 170, 2.2, "a-sl", "squish2")}
  {bub("어제 급등 뒤,<br>오늘은 <b>숨 고르기</b>일지 봐요", 240, 1010, 2.4, "t-left", style="font-size:38px")}
</div>
''', "#4A3E78"))

# 5 ── 오늘의 체크 (방송 자막 띠 3줄)
def strip(n, title, sub, y, d, col):
    return (f'<div class="abs a-sl" style="left:0;top:{y}px;width:982px;height:170px;--d:{d}s">'
            f'<div class="abs" style="left:0;top:0;width:150px;height:170px;background:{col};border:5px solid {L};border-left:none;border-radius:0 0 0 0;color:#fff;font-size:90px;line-height:160px;text-align:center">{n}</div>'
            f'<div class="abs" style="left:150px;top:0;right:0;height:170px;box-sizing:border-box;background:#fff;border:5px solid {L};border-right:none;padding:18px 30px">'
            f'<div style="font-size:48px">{title}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#5B5070;margin-top:6px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFF8E1;--d:0s">
  <div class="abs onair" style="left:{P}px;top:34px;background:#E8484A;color:#fff;border:5px solid {L};border-radius:14px;padding:4px 20px;font-size:34px">● 자막</div>
  <div class="abs" style="left:0;right:0;top:110px;text-align:center;font-size:64px"><span class="punch" style="--d:.1s">오늘 한국장, 볼 것은 셋</span></div>
  {strip(1, "금리 걱정, 외국인은?", "금리 인상 전망 커지면 외국인 매수엔 부담 가능성", 240, .45, "#7E5BB8")}
  {strip(2, "반도체, 엔비디아 이틀째 급락", "약세 이어지면 반도체 업종엔 부담 가능성", 440, .9, "#2F6BD8")}
  {strip(3, "환율, 다시 오를까", "美 물가 높아 원/달러엔 상승 압력 가능성", 640, 1.35, "#E8590C")}
  {ch(mascot("bamtol", "normal", "point"), 680, 840, 200, 1.9, "a-sr", "squish")}
  {bub("세 줄, <b>꼭 챙겨요!</b>", 330, 890, 2.1, "t-right", style="font-size:44px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.3s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: 한국경제, SBS Biz, 뉴스1, 서울신문, 이투데이</div>
''', "#FFE1CC"))

# 6 ── 다음 회 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 토크쇼 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 회 예고 · 금요일 밤 10시 30분</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:72px;line-height:1.2">물가 2탄<br>10월 생산자물가</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">오늘 밤 미국장은 <span style="color:#FFC08A">내일 아침 8시</span>에</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("moon", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 590, 220, 270, .4, "a-sr", "hop")}
  {bub("오늘 토크쇼는 여기까지!<br><b>박수~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: 한국경제, 한국경제TV, SBS Biz, 뉴스1, 이투데이, 서울신문, 머니투데이<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.0, 1.5), 3: (4.4, 1.5), 4: (4.2, 1.5), 5: (4.0, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "applause", .5), (1, .0, "mic", .5), (1, .1, "whoosh", .5), (1, .25, "pop", .8), (1, .4, "thud", 1), (1, .5, "hmm", .6), (1, .7, "thud", .8),
 (2, .0, "mic", .7), (2, .15, "whoosh", .5), (2, .4, "pop", .8), (2, 1.0, "pop", .8), (2, 1.5, "boing", .6), (2, 1.7, "dundun", .7), (2, 2.2, "tick", .8),
 (3, .1, "pop", .8), (3, .2, "sizzle", .4), (3, .5, "whoosh", .5), (3, .9, "whoosh", .7), (3, 1.3, "ding", .7), (3, 1.9, "blip_down", .6), (3, 2.05, "blip_down", .6), (3, 2.2, "blip_down", .7), (3, 2.5, "tick", .7),
 (4, .1, "whoosh", .5), (4, .3, "question", .7), (4, .7, "sparkle", .7), (4, 1.0, "pop", .6), (4, 1.15, "pop", .6), (4, 1.6, "whoosh", .5), (4, 1.8, "blip_down", .9), (4, 2.2, "boing", .5), (4, 2.4, "pop", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .6), (5, .45, "CHECK1", 1), (5, .9, "CHECK2", 1), (5, 1.35, "CHECK3", 1), (5, 2.1, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "applause", .6), (6, .9, "jingle", .9),
]
