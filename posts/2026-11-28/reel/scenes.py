"""2026-11-28 릴스 · 탐정 추리(detective) v9 — '결론 먼저' 훅, 장면 1 '증거물 감식대 — 지퍼 증거물 봉투 속에서 그려지는 상승 차트 + 증거 번호표 + 지문 + 감식 도장' 새 구도 (검수 전).
그날 상황: "롤러코스터 탄 미국 증시, 이번 주는 어떻게 끝났을까?" — 블랙프라이데이 단축장 3대 지수 상승(나스닥 ▲2.31%), 1년여 만의 최고의 한 주.
          '왜 마지막 날 또 올랐지?'(AI주 저가 매수) 원인 찾기가 핵심 → 첫 칸(큰 지표 발표 없음, 급변 아님) 해당 없음, 둘째 칸 1순위 detective(마지막 11-19, 최근 3일 11-25 news·11-26 recipe·11-27 homeshop 미사용).
흐름: 1 결론(나스닥 ▲2.31% '1년여 만의 최고의 한 주!', 감식대) → 2 사건 개요(롤러코스터 한 주, 주간 다우 ▲5.5%·S&P ▲5.6%·나스닥 ▲6.7%)
      → 3 결정적 단서: 비유 '블랙프라이데이 세일 매대에 몰린 손님 = 많이 내린 AI주를 싸게 담는 저가 매수'(반도체지수 ▲4.69%·마이크론 7%+·앤트로픽 10%+)
      → 4 서울 현장(27일 코스피 ▲4.34%, 미국 반도체 반등은 서울 마감 뒤) → 5 수사 노트(월요일 체크 3) → 6 다음 사건 예고(이번 주 성적표 내일 8시, 29일 OPEC+).
숫자·사실은 posts/2026-11-28 카드·sources.md에 있는 것만 쓴다. 다른 요인을 '무죄'로 단정하지 않는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes zip{from{width:0}to{width:100%}}
@keyframes swingtag{0%,100%{transform:rotate(-6deg)}50%{transform:rotate(6deg)}}
@keyframes scan{0%{top:10px}100%{top:300px}}
@keyframes cart{0%{transform:translateX(-14px)}50%{transform:translateX(14px)}100%{transform:translateX(-14px)}}
.tagsw{transform-origin:50% 0;animation:swingtag 1s ease-in-out infinite}
.scan{animation:scan .9s ease-in-out infinite alternate}
.cart{animation:cart 1.2s ease-in-out infinite}
</style>"""

def chart_line(w, h, d, color="#E03131"):
    """롤러코스터처럼 오르내리다 끝에 쑥 오르는 선 (그리기 애니메이션)."""
    pts = "10,150 60,95 105,160 150,70 195,175 240,120 285,150 330,40"
    return (f'<svg viewBox="0 0 340 200" width="{w}" height="{h}" style="overflow:visible">'
            f'<polyline points="{pts}" fill="none" stroke="{L}" stroke-width="16" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round" '
            f'style="--len:900;stroke-dasharray:900;animation:draw .8s ease-out {d}s both"/>'
            f'<circle cx="330" cy="40" r="13" fill="{color}" stroke="{L}" stroke-width="5" class="a-pop" style="--d:{d+.7}s"/></svg>')

def fingerprint(s=150):
    rings = "".join(f'<ellipse cx="75" cy="80" rx="{12+i*11}" ry="{16+i*13}" fill="none" stroke="#7C6FB0" stroke-width="4" stroke-dasharray="{30+i*6} 9"/>' for i in range(5))
    return f'<svg viewBox="0 0 150 160" width="{s}" height="{s*1.07:.0f}" style="opacity:.75">{rings}</svg>'

# 1 ── 결론 먼저 (증거물 감식대): 0초에 숫자·결론·탐정(클로즈업, 놀람)·증거물 봉투가 모두 보인다
#      0~1초: 숫자 펀치(0) → 봉투 속 차트 선 그리기(.05~.85) → 번호표 흔들(계속) → '감식 완료' 도장 쾅(.4) → '쑥!'(.6) → 탐정 떨림(.6) → 스캔 빛(계속)
S[1] = (1, page(FX + f'''
{stars(12, 128, 0, 180)}
{head("밤사이 탐정 · 11.28 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">블랙프라이데이 단축장 · 나스닥</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#FF6B6B;-webkit-text-stroke:10px {L};paint-order:stroke fill">▲2.31%</span></div>
<div class="abs" style="left:0;width:1080px;top:504px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">1년여 만의 <span style="color:#FFE36E">최고의 한 주!</span></div>
<div class="panel" style="left:44px;top:660px;width:982px;height:760px;background:#2E2A52">
  <div class="abs" style="left:0;right:0;top:0;bottom:0;background-image:linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(0deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:60px 60px"></div>
  <div class="abs" style="left:{P}px;top:22px;background:#FFD84D;border:5px solid {L};border-radius:12px;padding:2px 18px;font-size:36px">🧪 증거물 감식대</div>
  <div class="abs" style="left:{P}px;top:110px;width:520px;height:380px;box-sizing:border-box;background:rgba(220,236,255,.88);border:6px solid {L};border-radius:18px;overflow:hidden">
    <div class="abs" style="left:0;right:0;top:0;height:34px;background:#E03131;border-bottom:5px solid {L}"><div class="abs" style="left:0;top:12px;height:6px;background:#FFE36E;animation:zip .5s ease-out both"></div></div>
    <div class="abs" style="left:18px;top:48px;font-size:30px;color:#3B3560">이번 주 미국 증시</div>
    <div class="abs" style="left:40px;top:96px">{chart_line(430, 253, .05)}</div>
    <div class="abs scan" style="left:0;right:0;height:10px;background:rgba(255,236,150,.55)"></div>
  </div>
  <div class="abs tagsw" style="left:250px;top:470px;width:200px"><div style="width:6px;height:40px;background:{L};margin:0 auto"></div>
    <div style="background:#FFFDF5;border:5px solid {L};border-radius:10px;text-align:center;font-size:34px;line-height:1.25;padding:6px 0">증거물<br><span style="color:#E8590C">#1127</span></div></div>
  <div class="abs" style="left:60px;top:520px">{fingerprint(170)}</div>
  <div class="abs" style="left:470px;top:220px;width:410px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.6s">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
  <div class="abs" style="left:240px;top:640px"><div class="stamp a-stamp" style="position:relative;--d:.4s;--r:-8deg;font-size:62px;white-space:nowrap">감식 착수!</div></div>
  {sfx("쑥!", 560, 110, 96, .6, 8, "#FF6B6B")}
</div>
''', "#262B55"))

# 2 ── 사건 개요: 롤러코스터 한 주, 끝은 최고의 한 주
S[2] = (1, page(FX + f'''
{head("사건 개요 · 롤러코스터 한 주", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cbub("한 주 내내 <b>오르락내리락</b>…<br>그런데 결과는?", 36, .1, "t-down", style="font-size:48px")}
  <div class="abs" style="left:0;right:0;top:250px;text-align:center;font-size:40px;color:#E6E9FF">이번 주 성적 (27일 마감 기준)</div>
  {numbox("다우", "▲5.5%", COL3[0], 320, .4, RED)}
  {numbox("S&amp;P500", "▲5.6%", COL3[1], 320, .55, RED)}
  {numbox("나스닥", "▲6.7%", COL3[2], 320, .7, RED)}
  <div class="abs a-pop" style="left:{P}px;top:560px;width:{IW}px;--d:1.0s;text-align:center">
    <div style="font-size:40px;color:#E6E9FF">S&amp;P500 주간 오름폭</div>
    <div style="font-size:92px;line-height:1.2"><span class="thump" style="--d:1.2s;color:#FFE36E;-webkit-text-stroke:5px {L};paint-order:stroke fill">2025년 4월 이후 최대</span></div></div>
  {ch(mascot("star", "surprised", "up"), P, 830, 260, 1.6, "a-sl", "hop")}
  {bub("마지막 날엔<br><b>왜 또 올랐지?!</b>", 340, 880, 1.8, "t-left", style="font-size:48px")}
</div>
''', "#2B3060"))

# 3 ── 결정적 단서: 블랙프라이데이 세일 매대 = 저가 매수 (출처들이 공통으로 꼽은 이유)
def tag(name, val, x, y, d, rot):
    return (f'<div class="abs a-drop" style="left:{x}px;top:{y}px;width:250px;--d:{d}s"><div style="transform:rotate({rot}deg);background:#FFFDF5;border:5px solid {L};border-radius:14px;text-align:center;padding:10px 0;box-shadow:0 6px 0 rgba(0,0,0,.15)">'
            f'<div style="font-size:30px;color:#5B5070">{name}</div><div style="font-size:52px;color:{RED}">{val}</div></div></div>')
S[3] = (1, page(FX + f'''
{head("결정적 단서 · 세일 매대", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#EEF0FF;--d:0s">
  {cbub("많이 내린 AI주,<br><b>세일할 때 담자!</b>", 30, .1, "t-down", style="font-size:48px")}
  <div class="abs a-pop" style="left:{P}px;top:250px;width:{IW}px;height:400px;box-sizing:border-box;--d:.3s;background:#FFE9C2;border:5px solid {L};border-radius:24px;overflow:hidden">
    <div class="abs" style="left:0;right:0;top:0;height:70px;background:repeating-linear-gradient(90deg,#E03131 0 60px,#FFFDF5 60px 120px);border-bottom:5px solid {L}"></div>
    <div class="abs" style="left:0;right:0;top:78px;text-align:center;font-size:54px;color:{L}">BLACK FRIDAY · AI주 매대</div>
    {tag("반도체지수", "▲4.69%", 36, 160, .6, -4)}
    {tag("마이크론", "▲7%+", 326, 175, .8, 3)}
    {tag("앤트로픽", "▲10%+", 616, 160, 1.0, -3)}
    <div class="abs cart" style="left:330px;top:318px;font-size:64px">🛒🛒🛒</div>
  </div>
  <div class="abs a-fade" style="left:{P}px;top:666px;--d:1.2s;font-size:30px;color:#6B5A50">세일 매대 = 많이 내린 주식 · 손님 = 싸게 사려는 투자자</div>
  <div class="abs a-sl" style="left:{P}px;top:720px;width:{IW}px;height:200px;box-sizing:border-box;--d:1.5s;background:#fff;border:5px solid {L};border-radius:22px;padding:20px 28px">
    <div style="font-size:46px">🔍 주요 원인 · <span style="color:#E8590C">AI주 저가 매수</span></div>
    <div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#5B5070;margin-top:8px">메모리 반도체로 매수가 몰렸다 (여러 매체 공통)</div></div>
  {ch(mascot("bamtol", "happy", "point"), 600, 920, 220, 1.9, "a-sr", "squish")}
  {bub("범인은<br><b>‘싸게 사자’!</b>", 260, 950, 2.1, "t-right", style="font-size:44px")}
</div>
''', "#30366E"))

# 4 ── 서울 현장: 하루 먼저 크게 웃었다
S[4] = (1, page(FX + f'''
{head("서울 현장 · 하루 먼저", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:30px;text-align:center;font-size:42px">🇰🇷 서울은 하루 먼저 (27일 코스피)</div>
  <div class="abs" style="left:0;right:0;top:90px;text-align:center;font-size:160px;line-height:1"><span class="punch" style="--d:.15s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲4.34%</span></div>
  <div class="stamp a-stamp" style="left:290px;top:270px;--d:.5s;--r:-6deg;font-size:48px;padding:0 18px;white-space:nowrap">4,900선 되찾음</div>
  {numbox("삼성전자", "▲4.55%", COL2[0], 380, .8, RED)}
  {numbox("SK하이닉스", "▲5.41%", COL2[1], 380, .95, RED)}
  <div class="abs a-fade" style="left:{P}px;top:580px;width:{IW}px;--d:1.2s;text-align:center;font-size:36px;color:#2F4A3A">증안펀드 기대 · 외국인 1조원 넘게 순매수</div>
  {ch(mascot("star", "happy", "up"), P, 660, 230, 1.5, "a-sl", "hop")}
  {bub("미국 반도체 반등은<br><b>서울 장 끝난 뒤!</b>", 300, 700, 1.7, "t-left", style="font-size:44px")}
  <div class="abs a-pop" style="left:{P}px;top:930px;width:{IW}px;height:200px;box-sizing:border-box;--d:2.2s;background:#3A3460;color:#FFF6EA;border:5px solid {L};border-radius:26px;text-align:center;padding-top:22px">
    <div style="font-size:38px;color:#FFC08A">📬 월요일로 넘어온 소식</div>
    <div style="font-size:60px;margin-top:6px">미국 반도체지수 <span class="thump" style="--d:2.5s;color:#FF8A8F">▲4.69%</span></div></div>
</div>
''', "#4A3E78"))

# 5 ── 수사 노트 (월요일 한국장 체크 3)
def note(n, title, sub, y, d):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="background:#FFFDF2;border:5px solid {L};border-radius:14px;padding:16px 28px 16px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#F1E6C8 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#E8590C;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:46px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 노트 · 월요일 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#5E6BB8;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:62px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill"><span class="punch" style="--d:.1s">월요일 한국장, 볼 것은 셋</span></div>
  {note(1, "반도체 훈풍 이어질까", "미국 반도체 반등이 월요일 반도체 업종에 우호적일 가능성", 160, .5)}
  {note(2, "증안펀드, 30일 긴급회의", "가동·확대 논의 결과에 따라 기대가 커지거나 실망 가능성", 370, .95)}
  {note(3, "젠슨 황 美 의회 청문회", "AI 칩 수출통제 발언에 따라 반도체 변동성 커질 가능성", 580, 1.4)}
  {ch(mascot("bamtol", "normal", "point"), 630, 800, 220, 2.0, "a-sr", "squish")}
  {bub("수사 노트 셋,<br><b>꼭 챙겨요!</b>", 320, 840, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: AP, 서울경제, 파이낸셜뉴스, 폴리뉴스, 이투데이, SBS Biz</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 다음 사건", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 사건 파일 · 일요일판</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:76px;line-height:1.2">이번 주 성적표<br>+ 29일 OPEC+</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>에</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 590, 220, 270, .4, "a-sr", "hop")}
  {bub("오늘 감식은 여기까지!<br><b>사건 해결~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: AP, 서울경제, 파이낸셜뉴스, EBN, 폴리뉴스, 재경일보, 이투데이<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.4, 1.5), 3: (4.0, 1.5), 4: (4.4, 1.5), 5: (4.0, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .5), (1, .05, "whoosh", .5), (1, .4, "thud", 1), (1, .6, "sparkle", .8), (1, .75, "boing", .6), (1, .9, "ding", .5),
 (2, .1, "pop", .8), (2, .4, "pop", .7), (2, .55, "pop", .7), (2, .7, "pop", .7), (2, 1.0, "whoosh", .5), (2, 1.2, "sparkle", .7), (2, 1.6, "boing", .5), (2, 1.8, "question", .8),
 (3, .1, "pop", .7), (3, .3, "whoosh", .5), (3, .6, "ding", .6), (3, .8, "ding", .6), (3, 1.0, "ding", .6), (3, 1.2, "tick", .6), (3, 1.5, "dundun", .6), (3, 1.9, "whoosh", .5), (3, 2.1, "pop", .8),
 (4, .05, "whoosh", .5), (4, .15, "sparkle", .8), (4, .5, "thud", .8), (4, .8, "pop", .6), (4, .95, "pop", .6), (4, 1.2, "tick", .5), (4, 1.5, "boing", .5), (4, 1.7, "pop", .8), (4, 2.2, "msg", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .6), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .6), (6, .9, "jingle", .9),
]
