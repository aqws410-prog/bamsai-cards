"""2026-10-29 릴스 · 뉴스 속보(news) — '결론 먼저' 훅, 장면 1 '서울↔뉴욕 이원 생중계' 새 구도 (검수 전).
그날 상황: 연준 금리 결정(동결 3.75~4.00%) = 큰 지표·금리 결정 → 1순위 news (최근 3일 chat·delivery·recipe 미사용).
흐름: 1 결론(코스피 ▲6.63% → 뉴욕도 따라 올랐다) → 2 뉴욕 전광판(3대 지수·SK하이닉스 ADR) → 3 연준 기자회견(브레이크 비유, 10 대 2)
      → 4 장 마감 뒤 속보(알파벳 시간외 급락 vs MS 상승) → 5 한국장 체크 3 → 6 오늘 밤 예고.
숫자·사실은 posts/2026-10-29 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes linedraw{from{stroke-dashoffset:900}to{stroke-dashoffset:0}}
.uline{stroke-dasharray:900;animation:linedraw .6s ease-out both}
@keyframes flick{0%,100%{opacity:1}50%{opacity:.55}}
.flick{animation:flick .5s steps(1) infinite}
@keyframes press{0%,100%{transform:translateY(0)}50%{transform:translateY(14px)}}
.press{animation:press .8s ease-in-out infinite}
@keyframes dotin{0%{opacity:0;transform:scale(.3)}100%{opacity:1;transform:scale(1)}}
.dotin{animation:dotin .3s cubic-bezier(.2,1.4,.4,1) both}
</style>"""

def up_line(w, h, d, color="#FF6B6B"):
    pts = (f"M0 {h*.86} L{w*.14} {h*.78} L{w*.26} {h*.82} L{w*.40} {h*.60} L{w*.52} {h*.64} L{w*.66} {h*.40} "
           f"L{w*.78} {h*.44} L{w*.90} {h*.18} L{w} {h*.10}")
    return (f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;overflow:visible">'
            f'<path class="uline" style="animation-delay:{d}s" d="{pts}" fill="none" stroke="{color}" stroke-width="11" stroke-linejoin="round" stroke-linecap="round"/></svg>')

def mini_screen(city, sub, x, y, w, h, d, color):
    # 이원 중계 작은 화면 (0초부터 보임, 선만 그려짐)
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#14202A;border:5px solid {L};border-radius:18px;overflow:hidden">'
            f'<div class="abs" style="left:14px;top:8px;font-size:34px;color:#FFE59A">{city}</div>'
            f'<div class="abs" style="right:14px;top:12px;font-size:28px;color:#9FB7E0">{sub}</div>'
            f'<div class="abs" style="left:22px;top:66px;width:{w-44}px;height:{h-90}px">{up_line(w-44, h-90, d, color)}</div></div>')

# 1 ── 결론 먼저: 0초에 배너·숫자·결론·앵커가 모두 보인다. 이원 생중계(서울↔뉴욕) 두 화면 사이에 앵커 클로즈업
S[1] = (1, page(FX + f'''
{stars(12, 29, 0, 180)}
{head("밤사이 뉴스 · 10.29 THU", 1, "#F6EEE4")}
{alert_banner("이원 생중계", 186)}
<div class="abs" style="left:0;width:1080px;top:300px;text-align:center;font-size:48px;color:#FFD84D">28일 서울 · 코스피</div>
<div class="abs" style="left:0;width:1080px;top:360px;text-align:center"><span class="punch" style="--d:0s;font-size:224px;line-height:1;color:{RED};-webkit-text-stroke:10px {L};paint-order:stroke fill">▲6.63%</span></div>
<div class="abs" style="left:0;width:1080px;top:604px;text-align:center;font-size:86px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">뉴욕도 <span style="color:#FFD84D">따라 올랐다!</span></div>
<div class="panel" style="left:44px;top:740px;width:982px;height:650px;background:#3C4485">
  {mini_screen("🇰🇷 서울", "6,000 탈환", P, 30, 431, 200, .2, "#FF6B6B")}
  {mini_screen("🇺🇸 뉴욕", "3대 지수 ▲", COL2[1][0], 30, 431, 200, .55, "#FF6B6B")}
  <div class="abs" style="left:{491-60}px;top:80px;font-size:90px;color:#FFD84D;-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="flick">⇄</span></div><div style="display:none">⇄</div>
  <div class="abs" style="left:{491-250}px;top:150px;width:500px"><div class="squish">{mascot("bamtol", "surprised", "point")}</div></div>
  <div class="abs" style="left:0;right:0;top:540px;height:110px;background:#5B5FA8;border-top:6px solid {L};text-align:center;color:#FFE59A;font-size:44px;line-height:100px">🌙 밤사이 뉴스</div>
  <div class="live" style="right:{P}px;top:250px"><i></i>LIVE</div>
  {stamp("SK하이닉스 효과", 20, 300, .3, -8)}
  {sfx("들썩!", 730, 330, 92, .8, 10, "#FFD84D")}
</div>
{ticker("코스피 6,012.44 ▲6.63% · 다우 ▲0.19% · S&P500 ▲0.28% · 나스닥 ▲0.27% · 연준 금리 동결", 1420)}
''', "#262B55"))

# 2 ── 현장 연결 · 뉴욕 전광판: 3대 지수 모두 ▲, 주인공은 SK하이닉스 ADR
def board_row(name, val, pct, y, d):
    return (f'<div class="abs a-sl" style="left:{P}px;top:{y}px;width:{IW}px;height:96px;--d:{d}s;background:#0B1220;border:4px solid {L};border-radius:16px;'
            f'display:flex;align-items:center;justify-content:space-between;padding:0 30px;box-sizing:border-box;font-size:48px;color:#F6EEE4">'
            f'<span>{name}</span><span style="display:flex;gap:30px"><span style="color:#C9D6FF">{val}</span><span style="color:#FF6B6B;width:180px;text-align:right">{pct}</span></span></div>')
S[2] = (1, page(f'''
{head("현장 연결 · 뉴욕", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:640px;background:#2A2F5E;--d:.0s">
  <div class="abs" style="left:{P}px;top:30px;font-size:40px;color:#FFE59A">🗽 28일 뉴욕 마감 전광판</div>
  {board_row("다우", "52,475.10", "▲0.19%", 100, .15)}
  {board_row("S&amp;P 500", "7,743.98", "▲0.28%", 214, .3)}
  {board_row("나스닥", "26,549.85", "▲0.27%", 328, .45)}
  {nar("3대 지수 <b>모두 상승!</b> S&amp;P500은 <b>사흘 연속</b>", P, 460, .9, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
<div class="panel a-pop" style="left:44px;top:870px;width:982px;height:520px;background:#FFF8E1;--d:1.3s">
  {ch(mascot("owl", "happy", "hold", p_tablet()), P, 60, 300, 1.4, "a-sl", "squish")}
  {lower_third("솜부엉 기자", "뉴욕 현장", P, 400, 1.6)}
  {bub("SK하이닉스 실적에<br>미국 반도체도 <b>들썩!</b>", 380, 40, 1.7, "t-left", style="font-size:42px")}
  <div class="num a-pop" style="left:380px;top:250px;width:522px;box-sizing:border-box;text-align:center;--d:2.3s"><div class="k">미국에 상장된 SK하이닉스(ADR)</div><div class="v" style="color:{RED}"><span class="thump" style="--d:2.6s">▲13% 넘게</span></div></div>
</div>
{ticker("오라클 ▲10% 넘게 · 반도체주 강세 · 3대 지수 모두 상승", 1420, "현장")}
''', "#2B3060"))

# 3 ── 연준 기자회견: 금리 = 브레이크. 지난달 밟고, 이번엔 그대로. 2명은 "더 밟자"
def pedal(d):
    return (f'<svg viewBox="0 0 260 220" width="240" overflow="visible">'
            f'<rect x="20" y="170" width="220" height="30" rx="10" fill="#9C8CC4" stroke="{L}" stroke-width="5"/>'
            f'<g class="press" style="transform-box:fill-box;transform-origin:50% 100%;animation-delay:{d}s">'
            f'<rect x="60" y="40" width="140" height="120" rx="22" fill="#E8484A" stroke="{L}" stroke-width="6"/>'
            f'<text x="130" y="118" text-anchor="middle" font-size="46" font-family="Jua" fill="#fff">금리</text></g></svg>')
dots = "".join(
    f'<div class="abs dotin" style="left:{P + i*74}px;top:900px;width:62px;height:62px;border-radius:50%;background:{"#8EC5FF" if i < 10 else "#FF8A8F"};'
    f'border:4px solid {L};animation-delay:{1.6 + i*.06:.2f}s"></div>' for i in range(12))
S[3] = (1, page(FX + f'''
{head("연준 발표 · 1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1190px;background:#F3EEFF;--d:.0s">
  <div class="abs" style="left:0;right:0;top:0;height:96px;background:#3A3460;border-bottom:4px solid {L};color:#FFE59A;font-size:42px;line-height:96px;text-align:center">🏛 미국 연준 금리 결정</div>
  <div class="abs" style="left:0;right:0;top:120px;text-align:center"><span class="punch" style="--d:.1s;font-size:120px;line-height:1.1">금리 <span style="color:#2F6BD8">동결</span></span></div>
  <div class="abs a-fade" style="left:0;right:0;top:256px;text-align:center;font-size:52px;--d:.3s">3.75~4.00% 그대로</div>
  {ch(mascot("moon", "normal", "point"), P, 340, 290, .4, "a-sl", "squish")}
  {lower_third("달떡이 의장", "연준 역할", P, 640, .5)}
  <div class="abs a-pop" style="left:690px;top:540px;width:240px;--d:.6s">{pedal(.9)}</div>
  {bub("금리는 경제의 <b>브레이크</b>!<br>지난달 한 번 밟았고<br>이번엔 그대로 둬요", 330, 360, .8, "t-right", style="font-size:36px;padding:16px 22px")}
  <div class="abs a-fade" style="left:{P}px;top:820px;width:{IW}px;font-size:40px;--d:1.4s">투표 결과 <span style="color:#2F6BD8">동결 10</span> : <span style="color:{RED}">인상 2</span></div>
  {dots}
  {nar("2명은 <b>“더 밟자(인상)”</b> — 시장은 추가 인상에 무게", P, 1010, 2.6, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
''', "#30366E"))

# 4 ── 장 마감 뒤 속보: 알파벳 시간외 ▼ vs MS 시간외 ▲ — 희비 갈린 성적
def tv(name, mood, arrow, word, color, x, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:431px;height:600px;--d:{d}s;background:#14202A;border:5px solid {L};border-radius:22px;overflow:hidden">'
            f'<div class="abs" style="left:0;right:0;top:0;height:80px;background:{color};border-bottom:4px solid {L};color:#fff;font-size:44px;line-height:80px;text-align:center">{name}</div>'
            f'<div class="abs" style="left:0;right:0;top:110px;text-align:center;font-size:120px;color:{color};-webkit-text-stroke:6px {L};paint-order:stroke fill"><span class="punch" style="--d:{d+.2}s">{arrow}</span></div>'
            f'<div class="abs" style="left:0;right:0;top:270px;text-align:center;font-size:56px;color:#F6EEE4">{word}</div>'
            f'<div class="abs" style="left:{431//2-120}px;top:350px;width:240px">{mascot("star" if mood=="teary" else "bamtol", mood)}</div></div>')
S[4] = (1, page(f'''
{head("장 마감 뒤 속보", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1190px;background:#3A3460;--d:.0s">
  <div class="abs" style="left:0;right:0;top:24px;text-align:center;font-size:46px;color:#FFE59A">🌙 빅테크 성적표, 시간외 거래</div>
  {tv("알파벳(구글)", "teary", "▼", "시간외 급락", "#2F6BD8", P, .15)}
  {tv("MS", "happy", "▲", "시간외 상승", "#E03131", COL2[1][0], .45)}
  {nar("알파벳: 주당순이익 <b>예상 못 미침</b> · AI 투자에 현금 흐름 <b>마이너스</b>", P, 750, 1.1, f"font-size:36px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {cbub("AI에 돈을 너무 많이 쓴다는<br>걱정이 <b>다시 커질까?</b>", 880, 1.8, style="font-size:42px", width=982)}
  {ch(mascot("owl", "worried"), 680, 1000, 200, 2.0, "a-sr", "shiver")}
</div>
{ticker("알파벳 실적 실망 · MS 예상 웃돌아 · 오늘 한국 반도체 영향 주목", 1420, "속보")}
''', "#4A3E78"))

# 5 ── 오늘 한국장 체크 (복숭아빛)
items = [("chip", "급등 뒤 차익 실현?", "이틀 새 10% 가까이 오른 코스피"),
         ("chip", "알파벳 충격 vs MS 호실적", "AI 투자 걱정이 반도체로 번질지"),
         ("won", "원/달러 1,337.7원", "하루 <span style='color:#C92A2A'>▲14.0원</span> · 외국인 수급")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{700+i*190}px;width:982px;height:164px;background:#fff;--d:{1.0+i*.5:.1f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ICONS[k]}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (k, t, d) in enumerate(items))
S[5] = (1, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("한국은요? · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:460px;background:#FFF8E1;--d:.0s">
  {ch(mascot("star", "surprised"), P, 120, 280, .1, "a-sl", "squish")}
  {bub("코스피 <b>6,000</b> 다시 넘었는데<br>오늘은요?", 340, 40, .2, "t-left", style="font-size:40px")}
  {bub("딱 <b>세 가지</b>만 보세요!", 400, 270, .6, "t-right", style="font-size:40px")}
  {ch(mascot("bamtol", "normal", "point"), 720, 210, 220, .5, "a-sr", "squish2")}
</div>
{cards}
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: AP, 뉴스핌, 뉴시스, 한국일보, 파이낸셜뉴스</div>
''', "#FFE1CC"))

# 6 ── 오늘 밤 예고·마무리 (아침)
S[6] = (1, page(f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:36px;font-size:38px;color:#FFC08A">오늘 (10/29)</div>
  <div class="abs" style="left:{P}px;top:96px;font-size:58px;line-height:1.25">낮: 삼성전자 세부 실적<br>밤: 미국 GDP · PCE 물가<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ 아마존 실적</div>
  <div class="abs a-rise" style="left:{P}px;top:350px;--d:.4s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("이상, <b>밤사이 뉴스</b>였습니다!", 330, 40, .7, "t-down", "380px", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1420px;color:#6B5A50;--d:1.0s">출처: AP, 뉴스핌, 파이낸셜뉴스, 뉴스1, 한국경제, 연합인포맥스 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.8, 1.3), 2: (4.4, 1.6), 3: (5.0, 1.6), 4: (4.0, 1.5), 5: (4.0, 1.6), 6: (3.0, 1.2)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .9), (1, .05, "thud", .7), (1, .2, "whoosh", .4), (1, .3, "thud", .9), (1, .55, "whoosh", .4), (1, .8, "boing", .8),
 (2, .1, "whoosh", .5), (2, .15, "tick", .6), (2, .3, "tick", .6), (2, .45, "tick", .6), (2, .9, "ding", .8), (2, 1.3, "pop", .6), (2, 1.7, "pop", .8), (2, 2.3, "sparkle", .9),
 (3, .05, "news", .5), (3, .1, "thud", .9), (3, .4, "whoosh", .5), (3, .8, "pop", .8), (3, 1.6, "typing", .6), (3, 2.3, "ding", .7), (3, 2.6, "tick", 1),
 (4, .0, "news", .7), (4, .15, "pop", .7), (4, .35, "blip_down", 1), (4, .45, "pop", .7), (4, .65, "sparkle", .8), (4, 1.1, "tick", 1), (4, 1.8, "question", .9),
 (5, .1, "whoosh", .5), (5, .2, "pop", .8), (5, .6, "pop", .8), (5, 1.0, "CHECK1", 1), (5, 1.5, "CHECK2", 1), (5, 2.0, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .7, "pop", .8), (6, .9, "jingle", .9),
]
