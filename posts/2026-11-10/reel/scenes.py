"""2026-11-10 릴스 · 뉴스 속보(news) v4 — '결론 먼저' 훅, 장면 1 '증권거래소 시세 전광판(다 빨강 속 한 칸만 파랑)' 새 구도 (검수 전).
그날 상황: 다우 하루 1,104p ▲·미국 반도체 ▲6.8%대 급반등, 엔비디아만 ▼4.27%, 유가 급락 → 첫 칸(급변) 1순위 news
          (같은 칸 직전 사용 11-06 talkshow(2순위) 다음이라 1순위 차례, 최근 3일 detective·weather·chat 미사용).
흐름: 1 결론(▼4.27% '다 올랐는데 엔비디아만 뚝!', 시세 전광판) → 2 현장 연결(3대 지수, 저가 매수) → 3 1분 해설: 비유 '에이스가 벤치에 앉아도 팀은 대승'
      → 4 기름값 급락(주유소 가격판) + 어제 서울 → 5 오늘 체크 3 → 6 예고(오늘 밤 10시 30분 CPI).
숫자·사실은 posts/2026-11-10 카드·sources.md에 있는 것만 쓴다. 엔비디아 하락 이유는 'CEO 관련 조사 → 불확실성'까지만(사생활 세부 언급 금지).
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes flick{0%{opacity:.35}30%{opacity:1}45%{opacity:.3}60%,100%{opacity:1}}
@keyframes blinkb2{0%,49%{opacity:1}50%,100%{opacity:.35}}
@keyframes ring{0%{transform:scale(1.6);opacity:0}100%{transform:scale(1);opacity:1}}
@keyframes ball{0%{transform:translate(0,0)}100%{transform:translate(var(--bx),var(--by))}}
@keyframes drip{0%{transform:translateY(-30px);opacity:0}30%{opacity:1}100%{transform:translateY(0)}}
.flick{animation:flick .45s steps(4) both;animation-delay:var(--d,0s)}
.blb{animation:blinkb2 .5s steps(1) infinite}
.ring{animation:ring .35s ease-out both;animation-delay:var(--d,0s)}
</style>"""

def tile(name, val, col, y, d, up=True, w=None):
    """시세 전광판 한 칸 (켜질 때 깜빡)."""
    x, cw = col
    bg, fg = ("#3A1418", "#FF8A8F") if up else ("#0F2547", "#7DBBFF")
    return (f'<div class="abs flick" style="left:{x}px;top:{y}px;width:{cw}px;height:150px;--d:{d}s;box-sizing:border-box;background:{bg};border:5px solid {L};border-radius:16px;text-align:center">'
            f'<div style="font-size:32px;color:#E9E4F5;margin-top:12px">{name}</div>'
            f'<div style="font-size:58px;color:{fg};line-height:1.25">{val}</div></div>')

# 1 ── 결론 먼저 (증권거래소 시세 전광판): 0초에 숫자·결론·앵커(클로즈업, 놀람)·전광판이 모두 보인다
#      0~1초: 숫자 펀치(0) → 전광판 칸 깜빡 켜짐(.05~.3) → 빨간 원 + '홀로 하락' 도장(.4) → 말풍선(.2) → '뚝!' 효과 글자(.7) → 앵커 떨림(상시)
S[1] = (1, page(FX + f'''
{stars(12, 31, 0, 180)}
{head("밤사이 뉴스 · 11.10 TUE", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">어젯밤 뉴욕 · 엔비디아</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#5AA9FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼4.27%</span></div>
<div class="abs" style="left:0;width:1080px;top:504px;text-align:center;font-size:80px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">다 올랐는데 <span style="color:#FFE36E">엔비디아만 뚝!</span></div>
<div class="panel" style="left:44px;top:640px;width:982px;height:780px;background:#1B2040">
  <div class="abs" style="left:{P}px;top:18px;font-size:30px;color:#FFE59A">● 뉴욕 증시 시세판</div>
  <div class="live" style="right:{P}px;top:14px"><i></i>LIVE</div>
  {tile("다우", "▲2.15%", COL3[0], 70, .05)}
  {tile("S&amp;P500", "▲2.35%", COL3[1], 70, .1)}
  {tile("나스닥", "▲2.74%", COL3[2], 70, .15)}
  {tile("반도체지수", "▲6.8%대", COL3[0], 240, .2)}
  {tile("AMD", "▲10%+", COL3[1], 240, .25)}
  <div class="blb abs" style="left:{COL3[2][0]}px;top:240px;width:{COL3[2][1]}px;height:150px">{tile("엔비디아", "▼4.27%", (0, COL3[2][1]), 0, .3, up=False)}</div>
  <div class="abs ring" style="left:{COL3[2][0] - 18}px;top:222px;width:{COL3[2][1] + 36}px;height:186px;box-sizing:border-box;border:8px solid #FFE36E;border-radius:30px;--d:.4s"></div>
  <div class="stamp a-stamp" style="left:{COL3[2][0] - 30}px;top:410px;--d:.45s;--r:-8deg;font-size:48px;padding:2px 18px">홀로 하락</div>
  {ch(mascot("bamtol", "surprised", "point"), P - 10, 410, 320, 0, "", "shiver")}
  {bub("다 같이 올랐는데<br><b>엔비디아만</b> 내렸어요!", 360, 520, .2, "t-left", style="font-size:40px;padding:18px 26px")}
  {sfx("뚝!", 420, 650, 96, .7, 10, "#7DBBFF")}
</div>
{ticker("다우 ▲2.15% · S&P500 ▲2.35% · 나스닥 ▲2.74% · 미국 반도체 ▲6.8%대 · 엔비디아 ▼4.27%", 1440)}
''', "#262B55"))

# 2 ── 현장 연결 (솜부엉 기자, 뉴욕)
bld = ''.join(f'<div class="abs" style="left:{x}px;bottom:150px;width:{w}px;height:{h}px;background:#3A4080;border:4px solid {L};border-radius:6px 6px 0 0"></div>'
              for x, w, h in [(20, 120, 260), (150, 90, 340), (700, 110, 300), (830, 120, 230)])
S[2] = (1, page(FX + f'''
{head("현장 연결 · 뉴욕", 2, "#F6EEE4")}
{screen(f"""
  <div class="abs" style="left:0;right:0;bottom:0;height:150px;background:#2A2F5E"></div>
  {bld}
  {ch(mascot("owl", "happy", "hold", p_tablet()), 330, 250, 320, .3, "a-pop", "squish")}
  {cbub("지난주 많이 떨어진 <b>반도체주</b>를<br>다시 사들였어요!", 60, .6, style="font-size:40px", width=968)}
""", 44, 200, 982, 660, .05, "● 월가 현장")}
{lower_third("솜부엉 기자", "뉴욕 월가", 44 + P, 800, .5)}
<div class="panel a-pop" style="left:44px;top:930px;width:982px;height:420px;background:#FFF8E1;--d:1.2s">
  <div class="abs" style="left:0;width:982px;top:24px;text-align:center;font-size:46px">다우 하루 <span class="thump" style="--d:2.2s;color:{RED};font-size:64px">1,104p ▲</span></div>
  {numbox("다우", "▲2.15%", COL3[0], 150, 1.5, RED)}
  {numbox("S&amp;P500", "▲2.35%", COL3[1], 150, 1.7, RED)}
  {numbox("나스닥", "▲2.74%", COL3[2], 150, 1.9, RED)}
  <div class="abs a-fade" style="left:0;width:982px;top:330px;text-align:center;font-size:34px;color:#6B5A50;--d:2.2s">유가 급락으로 물가 걱정도 덜었어요</div>
</div>
{ticker("저가 매수 + 유가 급락 → 3대 지수 일제히 상승", 1380, "현장")}
''', "#2B3060"))

# 3 ── 1분 해설: 에이스가 벤치에 앉아도 팀은 대승
def player(name, val, col, d, up=True, bench=False):
    x, w = col
    c = RED if up else BLUE
    bg = "#E8ECF4" if bench else "#fff"
    tag = '<div style="font-size:26px;color:#6B5A50">벤치 · 에이스</div>' if bench else '<div style="font-size:26px;color:#6B5A50">⚽ 골!</div>'
    return (f'<div class="abs a-pop" style="left:{x}px;top:560px;width:{w}px;height:230px;box-sizing:border-box;--d:{d}s;background:{bg};border:4px solid {L};border-radius:26px;text-align:center;padding-top:14px">'
            f'{tag}<div style="font-size:42px;margin-top:4px">{name}</div><div style="font-size:52px;color:{c}">{val}</div></div>')
S[3] = (1, page(FX + f'''
{head("1분 해설", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1130px;background:#F3EEFF;--d:.05s">
  {ch(mascot("moon", "happy", "point"), P, 40, 280, .2, "a-sl", "squish")}
  {lower_third("달떡이 위원", "반도체 해설", 350, 50, .3)}
  {bub("에이스가 벤치에 앉아도<br>팀은 <b>대승</b>했어요!", 350, 150, .5, "t-left", style="font-size:42px")}
  <div class="abs a-drop" style="left:{P}px;top:370px;width:{IW}px;height:150px;box-sizing:border-box;--d:1.0s;background:#1B2040;border:5px solid {L};border-radius:24px;color:#fff;text-align:center">
    <div style="font-size:32px;color:#FFE59A;margin-top:10px">반도체 팀 점수 (필라델피아 반도체지수)</div>
    <div style="font-size:72px;line-height:1.2"><span class="thump" style="--d:1.4s;color:#FF8A8F">▲6.8%대</span></div></div>
  {player("엔비디아", "▼4.27%", COL3[0], 1.6, False, True)}
  {player("AMD", "▲10%+", COL3[1], 1.9)}
  {player("브로드컴", "▲약 9%", COL3[2], 2.1)}
  {nar("에이스 엔비디아는 <b>CEO 관련 조사</b> 소식에 주춤,<br>동료 칩주들이 골을 넣었어요", P, 830, 2.7, f"font-size:38px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {sfx("대승!", 330, 980, 100, 3.2, -6, "#FFB27F")}
</div>
''', "#30366E"))

# 4 ── 기름값 급락 + 어제 서울
S[4] = (1, page(FX + f'''
{head("기름값 · 그리고 서울", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:520px;background:#E2F6EA;--d:.05s">
  <div class="abs" style="left:{P}px;top:40px;width:420px;height:300px;box-sizing:border-box;background:#2A2F3E;border:6px solid {L};border-radius:24px;text-align:center;color:#fff">
    <div style="font-size:34px;color:#FFE59A;margin-top:18px">⛽ WTI 유가 (배럴당)</div>
    <div style="font-size:76px;line-height:1.3">86.85달러</div>
    <div style="font-size:64px;color:#7DBBFF"><span class="punch" style="--d:.4s">▼4.38%</span></div></div>
  {bub("트럼프 “이란 추가 공격<br>가능성 <b>낮다</b>”", 490, 40, .7, "t-down", "45%", "font-size:36px;padding:14px 24px")}
  {ch(mascot("star", "happy", "up"), 610, 175, 200, .9, "a-sr", "hop")}
  {nar("중동 공급 걱정 ↓ → 물가 걱정도 ↓", P, 400, 1.4, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
<div class="panel a-pop" style="left:44px;top:760px;width:982px;height:580px;background:#FFF8E1;--d:1.9s">
  <div class="abs" style="left:{P}px;top:30px;font-size:44px">🇰🇷 어제(9일) 서울은?</div>
  {ch(mascot("bamtol", "worried"), 700, 10, 220, 2.1, "a-sr", "squish2")}
  {bub("장중엔 올랐다가<br><b>밀렸어요</b>", 330, 110, 2.3, "t-right", style="font-size:36px;padding:14px 24px")}
  {numbox("코스피 5,018.85", "▼0.81%", COL2[0], 300, 2.6, BLUE)}
  {numbox("원/달러 1,347.1원", "▼9.5원", COL2[1], 300, 2.8, BLUE)}
  <div class="abs a-fade" style="left:0;width:982px;top:470px;text-align:center;font-size:34px;color:#6B5A50;--d:3.0s">삼성전자 <span style="color:{RED}">▲0.64%</span> · SK하이닉스 <span style="color:{RED}">▲0.35%</span></div>
</div>
''', "#4A3E78"))

# 5 ── 오늘 체크 (복숭아빛)
items = [("chip", "반도체, 바통 이어받을까?", "미국 반도체 <span style='color:#C92A2A'>▲6.8%대</span> 반영될지"),
         ("oil", "유가 하락, 이어질까?", "WTI <span style='color:#1D4ED8'>▼4.38%</span> · 수입 부담·물가"),
         ("won", "오늘 밤 물가 눈치 보기", "CPI 높으면 금리 인상 걱정 ↑")]
cards = "".join(
    f'<div class="panel a-sr" style="left:44px;top:{690+i*190}px;width:982px;height:164px;background:#fff;--d:{1.1+i*.45:.2f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ICONS[k]}</div>'
    f'<div><div style="font-size:46px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (k, t, d) in enumerate(items))
S[5] = (1, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("클로징 · 오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:450px;background:#FFF8E1;--d:.05s">
  {live(40, 34, "밤사이 뉴스", .1)}
  {ch(mascot("bamtol", "normal", "point"), 40, 110, 280, .2, "a-sl", "squish")}
  {bub("오늘 한국장은<br>딱 <b>세 가지</b>만 보세요!", 380, 150, .45, "t-left", style="font-size:42px")}
</div>
{cards}
<div class="src a-fade" style="top:1270px;color:#6B5A50;--d:2.3s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 뉴스핌, 이투데이, 서울신문, 국민일보, 아시아경제, 뉴스1</div>
{ticker("오늘 밤 10시 30분 미국 10월 소비자물가(CPI) 발표", 1380, "예고")}
''', "#FFE1CC"))

# 6 ── 예고·사인오프 (아침)
S[6] = (1, page(f'''
{head("밤사이 뉴스 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">오늘 밤 10시 30분</div>
  <div class="abs" style="left:44px;top:100px;font-size:66px;line-height:1.2">미국 10월<br>소비자물가(CPI)</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.35s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.2s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .35, "a-sl", "hop")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 210, 290, .45, "a-sr", "squish")}
  {bub("이상, <b>밤사이 뉴스</b>였습니다!", 330, 40, .75, "t-down", "60%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1280px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.1s">출처: 뉴스핌, 이투데이, 서울신문, 국민일보, SBS, 뉴스1 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.8, 1.5), 3: (4.6, 1.5), 4: (4.6, 1.6), 5: (3.8, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "news", .8), (1, .05, "beep", .5), (1, .2, "pop", .9), (1, .3, "blip_down", .9), (1, .45, "thud", 1), (1, .7, "slidedown", .6),
 (2, .05, "whoosh", .6), (2, .3, "pop", .6), (2, .5, "tick", .8), (2, .6, "pop", .8), (2, 1.2, "whoosh", .5), (2, 1.5, "pop", .6), (2, 1.7, "pop", .6), (2, 1.9, "pop", .6), (2, 2.2, "ding", .8),
 (3, .2, "whoosh", .6), (3, .3, "tick", .8), (3, .5, "pop", .8), (3, 1.0, "whistle", .6), (3, 1.4, "sparkle", .7), (3, 1.6, "sad", .5), (3, 1.9, "pop", .7), (3, 2.1, "pop", .7), (3, 2.7, "tick", .8), (3, 3.2, "cheer", .7),
 (4, .05, "whoosh", .5), (4, .4, "blip_down", 1), (4, .7, "pop", .8), (4, .9, "boing", .6), (4, 1.4, "ding", .7), (4, 1.9, "whoosh", .5), (4, 2.3, "pop", .7), (4, 2.6, "blip_down", .7), (4, 2.8, "pop", .6),
 (5, .05, "news", .5), (5, .2, "whoosh", .5), (5, .45, "pop", .8), (5, 1.1, "CHECK1", 1), (5, 1.55, "CHECK2", 1), (5, 2.0, "CHECK3", 1),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .35, "whoosh", .5), (6, .45, "boing", .7), (6, .75, "pop", .8), (6, .9, "news", .6), (6, 1.0, "jingle", .9),
]
