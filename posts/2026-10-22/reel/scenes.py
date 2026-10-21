"""2026-10-22 릴스 · 병원 진료(clinic) — '결론 먼저' 훅. 환자 나스닥이 '실적 비타민 주사'로 기운을 되찾은 날.
장면 1: 진료 차트(클립보드) + 상승 심전도 + 의사 밤톨이 클로즈업 + '기운 회복' 도장 (10-17 응급실 배너 구도와 다르게).
숫자·사실은 posts/2026-10-22 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE, GREEN = "#E03131", "#2F6BD8", "#2FA36B"

STETH = (f'<path d="M80 236 Q150 286 220 236" fill="none" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<path d="M80 236 Q74 224 82 216 M220 236 Q226 224 218 216" fill="none" stroke="#5B6B8C" stroke-width="6" stroke-linecap="round"/>'
         f'<path d="M196 254 Q206 266 204 276" fill="none" stroke="#5B6B8C" stroke-width="7" stroke-linecap="round"/>'
         f'<circle cx="204" cy="284" r="12" fill="#C9D3E6" stroke="{L}" stroke-width="4"/>')
MIRROR = f'<circle cx="150" cy="118" r="20" fill="#E8F1FF" stroke="{L}" stroke-width="4"/><circle cx="150" cy="118" r="7" fill="#9FB7E0"/>'

FX = """<style>
@keyframes ecgdraw{from{stroke-dashoffset:1600}to{stroke-dashoffset:0}}
@keyframes inject{0%{transform:translateX(0)}40%{transform:translateX(-46px)}100%{transform:translateX(-46px)}}
@keyframes glow{0%,100%{filter:drop-shadow(0 0 0 #FFD84D)}50%{filter:drop-shadow(0 0 22px #FFD84D)}}
@keyframes barup{from{height:12%}to{height:86%}}
.ecg path{stroke-dasharray:1600;animation:ecgdraw .8s linear both}
.inject{animation:inject .7s cubic-bezier(.2,.9,.3,1) .35s both}
.glow{animation:glow 1s ease-in-out infinite}
</style>"""

def ecg_up(w, h, color="#5BF29B"):
    # 처음엔 낮고 약하다가 오른쪽으로 갈수록 힘차게 올라가는 심전도
    pts = (f"M0 {h*.80} L{w*.14} {h*.80} L{w*.19} {h*.66} L{w*.24} {h*.88} L{w*.29} {h*.78} L{w*.42} {h*.70} "
           f"L{w*.48} {h*.36} L{w*.54} {h*.80} L{w*.60} {h*.56} L{w*.72} {h*.48} L{w*.78} {h*.06} L{w*.84} {h*.62} L{w*.90} {h*.30} L{w} {h*.18}")
    return (f'<svg class="ecg" width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<path d="{pts}" fill="none" stroke="{color}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/></svg>')

SYRINGE = (f'<svg viewBox="0 0 300 90" width="300" height="90" overflow="visible">'
           f'<rect x="70" y="22" width="170" height="46" rx="10" fill="#E8F7FF" stroke="{L}" stroke-width="5"/>'
           f'<rect x="76" y="28" width="110" height="34" rx="6" fill="#FFD84D"/>'
           f'<rect x="240" y="38" width="42" height="14" fill="#C9D3E6" stroke="{L}" stroke-width="4"/>'
           f'<rect x="276" y="14" width="14" height="62" rx="4" fill="#C9D3E6" stroke="{L}" stroke-width="4"/>'
           f'<path d="M70 45 H10" stroke="{L}" stroke-width="5" stroke-linecap="round"/>'
           f'<path d="M100 30 v12 M130 30 v12 M160 30 v12" stroke="{L}" stroke-width="3"/></svg>')

# 1 ── 결론 먼저: 0초에 숫자·결론·의사·차트가 모두 보임
S[1] = (1, page(FX + f'''
{stars(12, 22, 0, 260)}
{head("밤사이 진료실 · 10.22 THU", 1, "#F6EEE4")}
<div class="abs" style="left:44px;top:186px;width:982px;text-align:center;font-size:52px;color:#FFD84D">환자 나스닥 · 21일 뉴욕</div>
<div class="abs" style="left:0;width:1080px;top:250px;text-align:center"><span class="punch" style="font-size:250px;line-height:1;color:#FF6B6B;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲1.05%</span></div>
<div class="abs" style="left:44px;top:540px;width:982px;box-sizing:border-box;background:#FFFDF6;border:6px solid {L};border-radius:26px;box-shadow:0 8px 0 rgba(0,0,0,.25);text-align:center;padding:12px 10px 16px">
  <div style="font-size:44px;color:#6B4A1A">기운 없던 AI주, 처방은 단 하나</div>
  <div style="font-size:86px;line-height:1.15;color:{L}"><span style="color:#C2410C">스페이스X 실적</span> 주사!</div>
</div>
<div class="abs" style="left:44px;top:830px;width:560px;height:520px;box-sizing:border-box;background:#F2E3C9;border:6px solid {L};border-radius:26px;box-shadow:0 8px 0 rgba(0,0,0,.25)">
  <div class="abs" style="left:190px;top:-28px;width:170px;height:56px;background:#9AA6BF;border:5px solid {L};border-radius:14px"></div>
  <div class="abs" style="left:28px;top:44px;right:28px;bottom:28px;background:#fff;border:4px solid {L};border-radius:14px;overflow:hidden">
    <div class="abs" style="left:24px;top:14px;font-size:40px">진료 차트 · 나스닥</div>
    <div class="abs" style="left:20px;top:84px;width:452px;height:160px;background:#14202A;border-radius:12px;overflow:hidden">
      <div class="abs" style="left:14px;top:12px;width:424px;height:136px">{ecg_up(424, 136)}</div>
    </div>
    <div class="abs" style="left:24px;top:262px;font-size:38px;line-height:1.35">AI 투자 걱정 <span style="color:{BLUE}">▼ 누그러짐</span><br>3대 지수 <span style="color:{RED}">▲ 모두 상승</span></div>
  </div>
</div>
<div class="abs" style="left:600px;top:760px;width:470px"><div class="hop">{mascot("bamtol", "surprised", "point", STETH + MIRROR)}</div></div>
<div class="abs" style="left:640px;top:1250px;width:300px"><div class="inject">{SYRINGE}</div></div>
<div class="stamp a-stamp" style="left:250px;top:1380px;--d:.3s;--r:-8deg;font-size:84px;white-space:nowrap">기운 회복!</div>
''', "#262B55"))

# 2 ── 이유 ①: 스페이스X 실적 주사
S[2] = (1, page(FX + f'''
{head("처방 ① 스페이스X 실적", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E6F0FA;--d:0s">
  <div class="abs" style="left:0;right:0;top:34px;text-align:center;font-size:52px">스페이스X 3분기 매출 · 1년 새</div>
  <div class="abs" style="left:0;right:0;top:100px;text-align:center;font-size:210px;line-height:1"><span class="punch" style="--d:.1s;color:{RED};-webkit-text-stroke:8px {L};paint-order:stroke fill">▲161%</span></div>
  <div class="abs a-pop" style="left:0;right:0;top:330px;--d:.4s;text-align:center;font-size:60px">주가는 하루 <span class="thump" style="--d:.9s;color:{RED}">▲7.79%</span></div>
  {ch(mascot("star", "surprised", "up"), P, 470, 300, .6, "a-sl", "shiver")}
  {bub("AI에 돈 계속<br>쓸 수 있을까 <b>걱정</b>이…", 330, 470, .9, "t-left", style="font-size:44px")}
  {ch(mascot("bamtol", "happy", "point", STETH), 640, 640, 280, 1.2, "a-sr", "squish")}
  {bub("실적이 좋으니<br><b>누그러졌어요!</b>", 250, 720, 1.4, "t-right", style="font-size:44px")}
  {numbox("다우", "▲0.69%", COL3[0], 1000, 1.9, RED)}
  {numbox("S&P500", "▲0.58%", COL3[1], 1000, 2.05, RED)}
  {numbox("나스닥", "▲1.05%", COL3[2], 1000, 2.2, RED)}
</div>
''', "#2B3060"))

# 3 ── 이유 ②: 형제 회사 테슬라 + 장 마감 뒤 검사 결과
S[3] = (1, page(FX + f'''
{head("처방 ② 테슬라 · 메타", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFF1E6;--d:0s">
  <div class="abs" style="left:0;right:0;top:40px;text-align:center;font-size:56px;color:#6B4A1A">스페이스X와 합병 검토 위원회</div>
  <div class="abs" style="left:0;right:0;top:120px;text-align:center;font-size:96px;line-height:1.1">테슬라 <span class="punch" style="--d:.15s;color:{RED};font-size:170px;-webkit-text-stroke:7px {L};paint-order:stroke fill">▲3.41%</span></div>
  {nar("장 마감 뒤엔 <b>실적 검사</b> 결과도 나왔어요", P, 360, .6, "font-size:42px")}
  {ch(mascot("moon", "happy", "hold", p_card("실적 검사", "양호!")), P, 470, 300, .9, "a-sl", "hop")}
  {bub("테슬라·메타<br><b>매출, 예상 넘었다!</b>", 360, 500, 1.2, "t-left", style="font-size:48px")}
  {ch(mascot("star", "happy", "up"), 620, 720, 260, 1.5, "a-sr", "hop")}
  {numbox("테슬라 시간외", "▲ 상승", COL2[0], 1000, 1.9, RED)}
  {numbox("메타 3분기 매출", "예상 상회", COL2[1], 1000, 2.1, RED)}
</div>
''', "#30366E"))

# 4 ── 한국은?
S[4] = (1, page(FX + f'''
{head("그럼 한국은?", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:52px">21일 코스피 · 하루 만에 반등</div>
  <div class="abs" style="left:0;right:0;top:106px;text-align:center;font-size:210px;line-height:1"><span class="punch" style="--d:.1s;color:{RED};-webkit-text-stroke:8px {L};paint-order:stroke fill">▲3.29%</span></div>
  {cbub("외국인·기관이 함께 사서<br><b>매수 사이드카</b>까지 켜졌어요", 350, .5, "t-down", "50%", "font-size:44px")}
  {ch(mascot("star", "happy", "up"), 120, 560, 300, .8, "a-sl", "hop")}
  {ch(mascot("owl", "happy", "wave"), 560, 560, 300, 1.0, "a-sr", "squish2")}
  {numbox("삼성전자", "▲5.67%", COL2[0], 900, 1.4, RED)}
  {numbox("SK하이닉스", "▲5.81%", COL2[1], 900, 1.6, RED)}
  {numbox("원/달러 1,325.2원 · 올해 최저", "▼2.9원", (P, IW), 1040, 1.9, BLUE)}
</div>
''', "#4A3E78"))

# 5 ── 처방전 (오늘 체크 3)
PILL = lambda c: f'<svg viewBox="0 0 80 80" width="76"><g transform="rotate(-35 40 40)"><rect x="8" y="26" width="64" height="28" rx="14" fill="#fff" stroke="{L}" stroke-width="4"/><path d="M40 26 h18 a14 14 0 0 1 0 28 h-18z" fill="{c}" stroke="{L}" stroke-width="4"/></g></svg>'
items = [(PILL("#BFD3FF"), "오늘 한은 금리 결정", "연 3% 동결 전망 우세 · 11월 인상 언급이 관건"),
         (PILL("#FFB27F"), "반도체 온기, 이어질까", f"나스닥 <span style='color:#C92A2A'>▲1.05%</span> · 미국 AI주 반등"),
         (PILL("#FFE59A"), "외국인 매수 이어질까", f"21일 코스피 <span style='color:#C92A2A'>▲3.29%</span> · 외국인·기관 동반 순매수")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{560+i*230}px;width:982px;height:200px;background:#fff;--d:{.4+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 30px;box-sizing:border-box">'
    f'<div style="flex:none;width:84px;height:84px;border-radius:50%;background:#FFB27F;border:5px solid {L};font-size:52px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ic}</div>'
    f'<div><div style="font-size:58px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("처방전 · 오늘 한국장", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:320px;background:#FFFDF6;--d:0s">
  <div class="abs" style="left:{P}px;top:34px;font-size:96px;color:{GREEN}">℞ 처방전</div>
  <div class="abs" style="left:{P}px;top:160px;font-size:52px">오늘은 이 <span class="thump" style="color:#E8590C">3가지</span>!</div>
  {ch(mascot("bamtol", "happy", "point", STETH + MIRROR), 640, 30, 280, .1, "a-sr", "squish")}
</div>
{cards}
<div class="src a-fade" style="top:1260px;color:#6B5A50;--d:1.6s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 서울경제, 뉴스1, SBS Biz, CNBC</div>
''', "#FFE1CC"))

# 6 ── 다음 진료 예약
S[6] = (1, page(FX + f'''
{head("밤사이 진료실 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:40px;color:#FFC08A">다음 진료 예약</div>
  <div class="abs" style="left:44px;top:100px;font-size:72px;line-height:1.2">내일(금) 아침 8시<br>한은 금리 결정 결과</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.3s;font-size:42px">그다음은 <span style="color:#FFC08A">27~28일 FOMC</span></div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 240, 260, .3, "a-sl", "hop")}
  {ch(mascot("bamtol", "happy", "wave", STETH), 620, 210, 290, .4, "a-sr", "squish")}
  {bub("기운 차렸네요!<br><b>밤사이 진료실</b>이었습니다", 290, 30, .65, "t-down", "75%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: 뉴스핌, 서울경제, 뉴스1, SBS Biz, CNBC, 메타 실적 발표 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.8, 1.3), 2: (4.0, 1.6), 3: (3.8, 1.6), 4: (4.0, 1.6), 5: (4.6, 1.6), 6: (3.4, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "beep", 1), (1, .05, "thud", .8), (1, .3, "thud", 1), (1, .35, "whoosh", .5), (1, .6, "sparkle", .7), (1, 1.0, "beep", .6),
 (2, .05, "whoosh", .5), (2, .1, "thud", .8), (2, .4, "pop", .7), (2, .6, "question", .6), (2, .9, "pop", .8), (2, 1.2, "boing", .6), (2, 1.4, "ding", .8), (2, 1.9, "pop", .6), (2, 2.05, "pop", .7), (2, 2.2, "pop", .8),
 (3, .05, "whoosh", .5), (3, .15, "thud", .8), (3, .6, "tick", 1), (3, .9, "boing", .6), (3, 1.2, "pop", .8), (3, 1.5, "yay", .5), (3, 1.9, "pop", .7), (3, 2.1, "pop", .7),
 (4, .05, "whoosh", .5), (4, .1, "thud", .8), (4, .15, "sparkle", .7), (4, .5, "pop", .8), (4, .8, "yay", .6), (4, 1.4, "pop", .7), (4, 1.6, "pop", .7), (4, 1.9, "blip_down", .8),
 (5, .05, "whoosh", .5), (5, .1, "pop", .7), (5, .4, "CHECK1", 1), (5, .85, "CHECK2", 1), (5, 1.3, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
