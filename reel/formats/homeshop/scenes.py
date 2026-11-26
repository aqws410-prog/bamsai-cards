"""2026-11-27 릴스 · 홈쇼핑(homeshop) v1 — 처음 만든 플롯 (검수 전). 장면 1 '홈쇼핑 스튜디오 — ON AIR 간판 + 흔들리는 대형 가격표(3.25%) + 회전 진열대 + 인상 도장 + 주문 전화 따르릉'.
그날 상황: 어젯밤 미국장 추수감사절 휴장 + 26일 한은 기준금리 3.00→3.25% 인상(점도표 중간값 3.50%).
          첫 칸(금리 결정) 1순위 news(11-25)·2순위 talkshow(11-24) 모두 최근 3일 사용 → 아래 칸 중 원인 찾기·원인 여럿·이슈 나란히·개념 핵심·발언 핵심은
          꼭 맞지 않음 → '조용한 날·미국 휴장 다음 날' 1순위 homeshop(개념 하나 소개 = 점도표, 처음 사용).
흐름: 1 결론(3.25%, '한 번 더 올릴 수도!') → 2 가격표 교체(3.00% → 3.25%, 올해 세 번째) + 이유(성장률 전망 3.9%·4.1%, 물가 목표 위)
      → 3 오늘의 상품 '점도표'(6개월 뒤 금리 중간값 3.50%) · 장점/주의점(확정 아님, 7명 중 2명 동결)
      → 4 한국 매장 반응(26일 코스피 ▲0.29%, 장중 4,817.77 → 반납 · 원/달러 ▼0.5원) → 5 체크 3 → 6 오늘 밤 미국 단축장 · 내일 8시.
숫자·사실은 posts/2026-11-27 카드·sources.md에 있는 것만 쓴다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes swing{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
@keyframes spin{from{transform:rotateY(0)}to{transform:rotateY(360deg)}}
@keyframes ring{0%,100%{transform:rotate(0)}20%{transform:rotate(-16deg)}40%{transform:rotate(14deg)}60%{transform:rotate(-10deg)}80%{transform:rotate(8deg)}}
@keyframes beamlight{0%,100%{opacity:.35}50%{opacity:.6}}
@keyframes strike{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:.3}}
@keyframes slap{0%{opacity:0;transform:scale(1.8) rotate(var(--r,6deg))}60%{opacity:1;transform:scale(.94) rotate(var(--r,6deg))}100%{opacity:1;transform:scale(1) rotate(var(--r,6deg))}}
.swing{transform-origin:50% 0;animation:swing 1.3s ease-in-out infinite}
.ring{display:inline-block;animation:ring .5s ease-in-out infinite}
.blink{animation:blink .7s steps(1) infinite}
.slap{animation:slap .4s ease-out var(--d,0s) both}
</style>"""

def onair(top, d=0):
    return (f'<div class="abs" style="left:44px;top:{top}px;width:982px;height:92px;box-sizing:border-box;background:#E8484A;border:6px solid {L};'
            f'border-radius:22px;box-shadow:0 8px 0 rgba(0,0,0,.25);display:flex;align-items:center;justify-content:space-between;padding:0 28px;color:#fff;font-size:50px">'
            f'<span><span class="blink">●</span> ON AIR · 밤사이 홈쇼핑</span><span style="font-size:34px;background:#fff;color:{L};border-radius:999px;padding:4px 18px">미국장 휴장</span></div>')

def curtain(w, h):
    folds = "".join(f'<div class="abs" style="left:{x}px;top:0;width:24px;height:{h}px;background:rgba(0,0,0,.12);border-radius:12px"></div>' for x in range(20, w, 60))
    return f'<div class="abs" style="left:0;top:0;width:{w}px;height:{h}px;background:#C2416B">{folds}</div>'

def podium(x, y, w, label):
    """회전 진열대 + 상품 상자."""
    return (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px">'
            f'<div style="margin:0 auto;width:{w*.62:.0f}px;height:{w*.5:.0f}px;perspective:600px"><div style="width:100%;height:100%;animation:spin 2.4s linear infinite;'
            f'background:#FFE36E;border:6px solid {L};border-radius:18px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;font-size:{w*.1:.0f}px;text-align:center;line-height:1.15">{label}</div></div>'
            f'<div style="margin:-6px auto 0;width:{w}px;height:46px;border-radius:50%;background:#A8B4E8;border:6px solid {L};box-sizing:border-box"></div>'
            f'<div style="margin:-14px auto 0;width:{w*.8:.0f}px;height:90px;background:#7B88C9;border:6px solid {L};border-top:none;border-radius:0 0 20px 20px;box-sizing:border-box"></div></div>')

def phone(x, y, d, s=120):
    return (f'<div class="abs" style="left:{x}px;top:{y}px"><span class="ring" style="font-size:{s}px">☎️</span></div>')

def bar(text, right=""):
    return (f'<div class="abs" style="left:0;right:0;top:0;height:88px;background:#FFD9E4;border-bottom:4px solid {L};font-size:40px;line-height:88px;padding-left:30px">{text}'
            f'<span style="position:absolute;right:30px;font-size:32px">{right}</span></div>')

def tagbox(inner, x, y, w, d, bg="#fff", rot=-3, anim="a-pop"):
    """가격표 모양 상자 (왼쪽 구멍)."""
    return (f'<div class="abs {anim}" style="left:{x}px;top:{y}px;width:{w}px;--d:{d}s"><div style="position:relative;transform:rotate({rot}deg);background:{bg};border:6px solid {L};'
            f'border-radius:20px 34px 34px 20px;box-shadow:0 8px 0 rgba(0,0,0,.2);padding:14px 20px 14px 70px;box-sizing:border-box">'
            f'<div style="position:absolute;left:22px;top:50%;margin-top:-16px;width:32px;height:32px;border-radius:50%;background:#262B55;border:5px solid {L};box-sizing:border-box"></div>{inner}</div></div>')

# 1 ── 결론 먼저 (홈쇼핑 스튜디오): 0초에 대형 가격표 3.25% · 결론 · 놀란 쇼호스트 밤톨이(클로즈업) · ON AIR 간판이 모두 보인다
#      0~1초: 숫자 펀치(0) → '따르릉!' 쾅(.15) → '인상' 도장 쾅(.35) → '▲0.25%p' 스티커 철썩(.6) → 밤톨이 리액션 '헉!'(.85)
S[1] = (1, page(FX + f'''
{stars(12, 127, 0, 170)}
{head("밤사이 홈쇼핑 · 11.27 FRI", 1, "#F6EEE4")}
{onair(176)}
<div class="abs" style="left:150px;top:290px;width:780px"><div class="swing">
  <div style="margin:0 auto;width:6px;height:30px;background:{L}"></div>
  <div style="position:relative;background:#FFF6EA;border:8px solid {L};border-radius:36px;box-shadow:0 10px 0 rgba(0,0,0,.25);text-align:center;padding:6px 0 10px">
    <div style="font-size:44px">한국 기준금리</div>
    <div style="font-size:228px;line-height:1"><span class="punch" style="--d:0s;color:{RED};-webkit-text-stroke:10px {L};paint-order:stroke fill">3.25%</span></div>
  </div></div></div>
<div class="abs" style="left:0;width:1080px;top:668px;text-align:center;font-size:84px;color:#fff;-webkit-text-stroke:6px {L};paint-order:stroke fill">한 번 더 <span style="color:#FFE36E">올릴 수도!</span></div>
<div class="panel" style="left:44px;top:790px;width:982px;height:600px;background:#FFF0F4">
  {curtain(982, 600)}
  <div class="abs" style="left:300px;top:0;width:380px;height:600px;background:linear-gradient(#FFF6D6,rgba(255,246,214,0));animation:beamlight 1.2s ease-in-out infinite"></div>
  {podium(40, 250, 330, "기준<br>금리")}
  <div class="abs" style="left:430px;top:110px;width:520px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver">{mascot("bamtol", "surprised", "up")}</div></div>
  {phone(40, 30, 0, 110)}
  {sfx("따르릉!", 165, 50, 80, .15, -10, "#FFE36E")}
  {stamp("인상!", 120, 150, .35, -10)}
  {bub("<b>헉!</b> 가격표가 바뀌었어요", 470, 20, .85, "t-down", "60%", "font-size:40px")}
</div>
<div class="abs slap" style="left:790px;top:330px;--d:.6s;--r:10deg;background:#FFE36E;border:6px solid {L};border-radius:20px;padding:6px 18px;font-size:56px;color:{RED};box-shadow:0 6px 0 rgba(0,0,0,.2)">▲0.25%p</div>
''', "#262B55"))

# 2 ── 가격표 교체 (3.00% → 3.25%, 올해 세 번째) + 왜? 성장률 전망 ▲ · 물가 목표 위
S[2] = (1, page(FX + f'''
{head("가격표 교체", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#FFFDF6;--d:0s">
  {bar("🏷 오늘의 가격 변경", '<span class="blink" style="color:#E8484A">● 26일 한은 발표</span>')}
  <div class="abs" style="left:0;right:0;top:118px;text-align:center;font-size:56px">돈 빌리는 값의 <span style="color:#E8590C">기준 가격표</span></div>
  {tagbox(f'<div style="font-size:30px">이전</div><div style="font-size:92px;line-height:1;position:relative">3.00%<div style="position:absolute;left:-8px;right:-8px;top:46%;height:12px;background:{RED};border-radius:6px;transform-origin:0 50%;animation:strike .3s ease-out .5s both"></div></div>', P, 220, 400, .1, "#fff", -4)}
  <div class="abs a-pop" style="left:448px;top:280px;--d:.6s;font-size:90px">➜</div>
  {tagbox(f'<div style="font-size:30px">지금</div><div style="font-size:100px;line-height:1;color:{RED}"><span class="thump" style="--d:1.1s">3.25%</span></div>', 540, 210, 402, .8, "#FFE36E", 3, "slap")}
  <div class="abs a-pop" style="left:0;right:0;top:420px;--d:1.2s;text-align:center"><span style="display:inline-block;background:{L};color:#FFF6EA;border-radius:999px;padding:8px 30px;font-size:40px">올해 세 번째 인상</span></div>
  {ch(mascot("star", "surprised", "up"), P, 520, 230, 1.5, "a-sl", "squish")}
  {bub("왜 또 <b>올렸어요?</b>", 290, 560, 1.7, "t-left", style="font-size:46px")}
  <div class="abs a-fade" style="left:{P}px;top:780px;--d:2.0s;width:{IW}px;text-align:center;font-size:44px">경제가 쑥쑥 · 물가는 목표(2%) 위 전망</div>
  {numbox("올해 성장률 전망", "3.9% <span style='font-size:30px;color:#6B5A50'>(8월 3.3%)</span>", COL2[0], 860, 2.2, RED)}
  {numbox("내년 성장률 전망", "4.1% <span style='font-size:30px;color:#6B5A50'>(8월 2.9%)</span>", COL2[1], 860, 2.4, RED)}
  {nar("쌩쌩 달리는 차에 <b>살짝 브레이크</b>", P, 1050, 2.7, f"font-size:42px;width:{IW}px;box-sizing:border-box;text-align:center")}
</div>
''', "#2B3060"))

# 3 ── 오늘의 상품: 점도표 (6개월 뒤 금리 중간값 3.50%) · 장점 / 주의점
S[3] = (1, page(FX + f'''
{head("오늘의 상품", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {bar("🛍 오늘의 상품 · 점도표")}
  <div class="abs" style="left:0;right:0;top:112px;text-align:center;font-size:44px">위원들이 <span style="color:#7048E8">6개월 뒤 금리</span>를 점으로 콕!</div>
  <div class="abs a-pop" style="left:{P}px;top:190px;--d:.2s;width:{IW}px;height:330px;box-sizing:border-box;background:#fff;border:5px solid {L};border-radius:26px">
    <div class="abs" style="left:30px;top:22px;font-size:30px;color:#6B5A50">6개월 뒤 금리, 중간값은?</div>
    <div class="abs" style="left:60px;right:60px;top:200px;height:6px;background:#D6CCF5;border-radius:3px"></div>
    <div class="abs a-pop" style="left:360px;top:116px;--d:.6s;text-align:center"><div style="width:110px;height:110px;margin:0 auto;border-radius:50%;background:{RED};border:6px solid {L};box-sizing:border-box"></div></div>
    <div class="abs a-pop" style="left:0;right:0;top:250px;--d:.8s;text-align:center;font-size:62px;line-height:1"><span class="punch" style="--d:.8s;color:{RED}">3.50%</span></div>
    <div class="abs a-fade" style="left:30px;top:250px;--d:1.0s;font-size:30px;color:#6B5A50">지금 3.25%</div>
  </div>
  {sfx("콕!", 600, 200, 90, .6, 8, "#FFE36E")}
  <div class="abs a-pop" style="left:{COL2[0][0]}px;top:560px;width:{COL2[0][1]}px;height:250px;box-sizing:border-box;--d:1.3s;background:#E2F6EA;border:5px solid {L};border-radius:26px;padding:18px 22px">
    <div style="font-size:38px;color:#2B8A3E">👍 장점</div><div style="font-size:40px;line-height:1.3;margin-top:8px">한은 생각을<br>미리 엿보기</div></div>
  <div class="abs a-pop" style="left:{COL2[1][0]}px;top:560px;width:{COL2[1][1]}px;height:250px;box-sizing:border-box;--d:1.6s;background:#FFE3E3;border:5px solid {L};border-radius:26px;padding:18px 22px">
    <div style="font-size:38px;color:{RED}">⚠ 주의점</div><div style="font-size:40px;line-height:1.3;margin-top:8px">약속 아닌 전망<br>물가·성장 보고 결정</div></div>
  {ch(mascot("moon", "normal", "point"), P, 860, 220, 2.0, "a-sl", "squish")}
  {bub("7명 중 <b>2명</b>은<br>'그대로 두자'(동결)", 290, 900, 2.2, "t-left", style="font-size:44px")}
</div>
''', "#30366E"))

# 4 ── 한국 매장 반응 (26일 서울)
S[4] = (1, page(FX + f'''
{head("한국 매장 반응", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {bar("🇰🇷 26일 서울 매장")}
  {ch(mascot("owl", "normal", "hold", p_tablet()), P, 110, 220, .1, "a-sl", "squish")}
  {bub("가격표 바뀐 날,<br>코스피는 <b>강보합</b> 마감", 290, 140, .3, "t-left", style="font-size:42px")}
  <div class="abs a-pop" style="left:{P}px;top:390px;width:{IW}px;--d:.6s;text-align:center">
    <div style="font-size:40px">코스피 (26일 종가 4,711.21)</div>
    <div style="font-size:150px;line-height:1.05"><span class="thump" style="--d:.8s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲0.29%</span></div></div>
  {nar("장중 <b>4,817.77</b>까지 갔다가 대부분 반납", P, 640, 1.1, f"font-size:42px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {numbox("SK하이닉스", "▲2.23%", COL2[0], 760, 1.5, RED)}
  {numbox("원/달러", "▼0.5원", COL2[1], 760, 1.7, BLUE)}
  <div class="abs a-sl" style="left:{P}px;top:960px;--d:2.1s;width:{IW}px;height:150px;box-sizing:border-box;background:#FFF8E1;border:5px solid {L};border-radius:26px;display:flex;align-items:center;gap:24px;padding:0 30px">
    <div style="font-size:70px">🗽</div><div style="font-size:46px;line-height:1.25">어젯밤 미국은 <span style="color:#E8590C">휴장</span><br><span style="font-size:34px">추수감사절 · 새 신호 없음</span></div></div>
</div>
''', "#4A3E78"))

# 5 ── 오늘 체크 3 (복숭아빛)
checks = [("'한 번 더' 신호", "금리에 민감한 업종은 부담 가능성"),
          ("미국 신호 없는 날, 반도체", "새 재료 적어 수급 따라 움직일 가능성"),
          ("호르무즈와 유가", "유조선 2척 폭발 주장 · 확인 안 됨")]
rows = "".join(
    f'<div class="abs a-sl" style="left:{P}px;top:{300+i*180}px;width:{IW}px;height:158px;box-sizing:border-box;--d:{.6+i*.45:.2f}s;background:#fff;border:4px solid {L};border-radius:24px;display:flex;align-items:center;gap:22px;padding:0 26px">'
    f'<div style="flex:none;width:76px;height:76px;border-radius:14px;background:#FFF6EA;border:4px solid {L};font-size:54px;line-height:70px;text-align:center;color:{RED}">✔</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50">{s}</div></div></div>'
    for i, (t, s) in enumerate(checks))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("오늘의 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFDF6;--d:0s">
  {bar("✅ 오늘 한국장 장바구니", '<span style="color:#E8590C">3개</span>')}
  <div class="abs" style="left:0;right:0;top:130px;text-align:center;font-size:84px;line-height:1"><span class="punch" style="--d:.1s">담을 건 <span style="color:#E8590C">딱 셋</span></span></div>
  {rows}
  {ch(mascot("bamtol", "normal", "point"), 60, 830, 200, 2.0, "a-sl", "squish")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.2s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: 이데일리, 헤럴드경제, 아시아경제, 파이낸셜뉴스, 서울신문, 로이터, VOA, 뉴스1</div>
''', "#FFE1CC"))

# 6 ── 다음 방송 예고 · 마무리
def daycard(day, date, t, col, d, hi=False):
    x, w = col
    bg = "#FFD84D" if hi else "#fff"
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:{w}px;height:280px;box-sizing:border-box;--d:{d}s;background:{bg};border:5px solid {L};'
            f'border-radius:26px;box-shadow:0 6px 0 rgba(0,0,0,.15);text-align:center;padding:14px 8px;color:{L}">'
            f'<div style="font-size:32px;color:#6B5A50">{day}</div><div style="font-size:88px;line-height:1.05">{date}</div>'
            f'<div style="font-size:32px;line-height:1.2;margin-top:6px">{t}</div></div>')
S[6] = (1, page(FX + f'''
{head("다음 방송 예고", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:30px;font-size:42px;color:#FFC08A">📺 다음 방송 편성표</div>
  {daycard("오늘 밤 11:30", "27", "미국장<br>단축 거래", COL3[0], .15, True)}
  {daycard("토 새벽 3시", "28", "미국장<br>조기 폐장", COL3[1], .3)}
  {daycard("일요일", "29", "OPEC+<br>회의", COL3[2], .45)}
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:540px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:320px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("bamtol", "happy", "wave"), 40, 230, 260, .3, "a-sl", "hop")}
  {ch(mascot("star", "happy", "wave"), 680, 230, 260, .4, "a-sr", "squish")}
  {bub("단축장 결과는 내일 8시,<br><b>또 소개해 드릴게요!</b>", 300, 40, .65, "t-down", "50%", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1260px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:52px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1385px;color:#6B5A50;--d:1.0s">출처: 이투데이, 아시아경제, 서울신문, 파이낸셜뉴스, 한국경제TV, 연합인포맥스, 콕스뉴스, 로이터<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (4.4, 1.6), 3: (4.2, 1.6), 4: (4.0, 1.6), 5: (3.3, 1.45), 6: (3.0, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "ring", .9), (1, .15, "thud", .8), (1, .35, "thud", .9), (1, .6, "pop", .8), (1, .85, "pop", .7), (1, .95, "question", .5),
 (2, .05, "whoosh", .5), (2, .1, "pop", .7), (2, .5, "slidedown", .6), (2, .6, "whoosh", .5), (2, .8, "chaching", .8), (2, 1.2, "ding", .6), (2, 1.5, "boing", .5), (2, 1.7, "question", .7), (2, 2.2, "pop", .6), (2, 2.4, "pop", .6), (2, 2.7, "tick", .8),
 (3, .05, "whoosh", .5), (3, .2, "pop", .6), (3, .6, "thud", .8), (3, .8, "sparkle", .7), (3, 1.3, "pop", .7), (3, 1.6, "pop", .7), (3, 2.0, "boing", .5), (3, 2.2, "pop", .8),
 (4, .05, "whoosh", .5), (4, .1, "boing", .5), (4, .3, "pop", .8), (4, .6, "ding", .6), (4, 1.1, "tick", .8), (4, 1.5, "pop", .6), (4, 1.7, "blip_down", .6), (4, 2.1, "whoosh", .5),
 (5, .05, "whoosh", .5), (5, .1, "thud", .7), (5, .6, "CHECK1", 1), (5, 1.05, "CHECK2", 1), (5, 1.5, "CHECK3", 1), (5, 2.0, "boing", .5),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .15, "pop", .5), (6, .3, "pop", .5), (6, .45, "pop", .6), (6, .65, "pop", .5), (6, .9, "jingle", .9),
]
