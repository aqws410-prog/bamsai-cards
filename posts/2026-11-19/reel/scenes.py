"""2026-11-19 릴스 · 탐정 추리(detective) v8 — '결론 먼저' 훅, 장면 1 '용의자 라인업실 — 키 눈금 벽 + 번호판 든 실루엣 셋 + 흔들리는 천장 전등' 새 구도 (검수 전).
그날 상황: "성적은 좋았는데 엔비디아는 왜 내렸을까?" 원인 찾기가 핵심 → 상황표 첫 칸(큰 지표·급변: 3대 지수 ▼1.11~▲0.42%, 의사록은 금리 결정 아님) 해당 없음,
          둘째 칸 1순위 detective(마지막 11-12, 최근 3일 11-16 chat·11-17 news·11-18 delivery 미사용).
흐름: 1 결론(엔비디아 ▼2.89% '호실적에도 주가는 뚝!', 라인업실) → 2 수상한 점(매출 1,158억$·전망 1,300억$ 모두 예상 상회)
      → 3 용의자 둘(출처들이 공통으로 꼽은 이유만): 비유 '짐 가득 실은 배, 선장(황)은 내렸다 → 앞으로 항로는?' + 'AI 순풍은 언제까지?'
      → 4 서울 현장(18일 코스피 ▲1.99%, 하루 먼저 웃음) + 또 하나의 바람(의사록 '추가 인상 적절') → 5 수사 노트(체크 3) → 6 다음 사건 예고(앤트로픽 상장).
숫자·사실은 posts/2026-11-19 카드·sources.md에 있는 것만 쓴다. 다른 요인을 '무죄'로 단정하지 않는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes swing{0%{transform:rotate(-14deg)}50%{transform:rotate(12deg)}100%{transform:rotate(-14deg)}}
@keyframes beam{0%,100%{opacity:.55}50%{opacity:.85}}
@keyframes rise2{from{transform:translateY(40px);opacity:0}to{transform:none;opacity:1}}
@keyframes sail{0%{transform:translateX(-30px) rotate(-2deg)}50%{transform:translateX(0) rotate(2deg)}100%{transform:translateX(-30px) rotate(-2deg)}}
@keyframes wave{to{background-position:-200px 0}}
.swing{transform-origin:50% 0;animation:swing 1.1s ease-in-out infinite}
.beam{animation:beam .9s ease-in-out infinite}
.sail{animation:sail 2.4s ease-in-out infinite}
.wave{background:repeating-linear-gradient(90deg,#5AA9FF 0 100px,#7DBBFF 100px 200px);animation:wave 1.2s linear infinite}
</style>"""

def sil(x, y, h, no, q, d):
    """라인업 실루엣 — 번호판 + 물음표."""
    w = int(h * .48)
    return (f'<div class="abs a-pop" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;--d:{d}s">'
            f'<div class="abs" style="left:{int(w*.26)}px;top:0;width:{int(w*.48)}px;height:{int(w*.48)}px;border-radius:50%;background:#3B3A63;border:5px solid {L}"></div>'
            f'<div class="abs" style="left:0;top:{int(w*.42)}px;width:{w}px;height:{h-int(w*.42)}px;border-radius:{int(w*.4)}px {int(w*.4)}px 10px 10px;background:#3B3A63;border:5px solid {L};box-sizing:border-box"></div>'
            f'<div class="abs" style="left:{int(w*.1)}px;top:{int(h*.45)}px;width:{int(w*.8)}px;box-sizing:border-box;background:#FFFDF5;border:4px solid {L};border-radius:8px;text-align:center;font-size:{int(w*.26)}px;line-height:1.2">{no}</div>'
            f'<div class="abs" style="left:0;width:{w}px;top:{int(w*.02)}px;text-align:center;font-size:{int(w*.36)}px;color:#FFE36E">{q}</div></div>')

def ship(w=420, captain=False):
    cap = (f'<circle cx="250" cy="60" r="22" fill="#F6EEE4" stroke="{L}" stroke-width="5"/>' if captain else
           f'<rect x="226" y="40" width="48" height="44" rx="8" fill="none" stroke="#FFE36E" stroke-width="5" stroke-dasharray="10 7"/>'
           f'<text x="250" y="76" text-anchor="middle" font-size="34" font-family="Jua" fill="#FFE36E">?</text>')
    boxes = "".join(f'<rect x="{60+i*46}" y="{100 - (i%2)*28}" width="42" height="{40 + (i%2)*28}" rx="4" fill="{c}" stroke="{L}" stroke-width="4"/>'
                    for i, c in enumerate(["#FFB27F", "#9AD3FF", "#FFD84D", "#C9B8FF"]))
    return (f'<svg viewBox="0 0 320 200" width="{w}" height="{w*.625:.0f}">'
            f'<rect x="216" y="28" width="68" height="112" rx="8" fill="#F6EEE4" stroke="{L}" stroke-width="5"/>{cap}'
            f'{boxes}'
            f'<path d="M14 140 L306 140 L270 190 L50 190 Z" fill="#E05A5A" stroke="{L}" stroke-width="6" stroke-linejoin="round"/>'
            f'<rect x="40" y="152" width="160" height="22" rx="6" fill="#FFFDF5" stroke="{L}" stroke-width="3"/>'
            f'<text x="120" y="170" text-anchor="middle" font-size="18" font-family="Jua" fill="{L}">엔비디아호</text></svg>')

# 1 ── 결론 먼저 (용의자 라인업실): 0초에 숫자·결론·탐정(클로즈업, 놀람)·라인업 벽이 모두 보인다
#      0~1초: 숫자 펀치(0) → 전등 흔들림(계속) → 실루엣 셋 톡톡(.1/.2/.3) → '수사 착수' 도장 쾅(.4) → '뚝!'(.6) → 탐정 떨림(.6)
S[1] = (1, page(FX + f'''
{stars(12, 77, 0, 180)}
{head("밤사이 탐정 · 11.19 THU", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:196px;text-align:center;font-size:46px;color:#C9D6FF">실적 발표 다음 날 · 엔비디아 주가</div>
<div class="abs" style="left:0;width:1080px;top:252px;text-align:center"><span class="punch" style="--d:0s;font-size:236px;line-height:1;color:#6FB6FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼2.89%</span></div>
<div class="abs" style="left:0;width:1080px;top:504px;text-align:center;font-size:86px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">호실적에도 <span style="color:#FFE36E">주가는 뚝!</span></div>
<div class="panel" style="left:44px;top:660px;width:982px;height:760px;background:#26264A">
  <div class="abs" style="left:0;right:0;top:0;bottom:0;background-image:repeating-linear-gradient(180deg,transparent 0 78px,#4A4A7A 78px 82px)"></div>
  {''.join(f'<div class="abs" style="left:{P}px;top:{80 + i*80 - 18}px;font-size:26px;color:#8D8DC0">{200 - i*20}</div>' for i in range(8))}
  <div class="abs" style="left:{P}px;top:22px;background:#FFD84D;border:5px solid {L};border-radius:12px;padding:2px 18px;font-size:36px">🔦 용의자 라인업</div>
  <div class="abs swing" style="left:420px;top:0;width:140px;height:520px">
    <div class="abs" style="left:66px;top:0;width:8px;height:60px;background:{L}"></div>
    <div class="abs" style="left:30px;top:56px;width:80px;height:46px;border-radius:40px 40px 6px 6px;background:#3A3A48;border:5px solid {L}"></div>
    <div class="abs beam" style="left:-110px;top:100px;width:360px;height:420px;background:linear-gradient(180deg,rgba(255,236,150,.55),rgba(255,236,150,0));clip-path:polygon(40% 0,60% 0,100% 100%,0 100%)"></div>
  </div>
  {sil(80, 250, 360, "No.1", "?", .1)}{sil(250, 280, 330, "No.2", "?", .2)}{sil(410, 260, 350, "No.3", "?", .3)}
  <div class="abs" style="left:490px;top:220px;width:430px;animation:zoomIn .6s cubic-bezier(.2,.9,.3,1) both"><div class="shiver" style="animation-delay:.6s">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
  <div class="abs" style="left:30px;top:620px"><div class="stamp a-stamp" style="position:relative;--d:.4s;--r:-8deg;font-size:64px;white-space:nowrap">수사 착수!</div></div>
  {sfx("뚝!", 120, 110, 96, .6, -8, "#6FB6FF")}
</div>
''', "#262B55"))

# 2 ── 수상한 점: 실적·전망 모두 예상 위
S[2] = (1, page(FX + f'''
{head("사건 개요 · 수상한 점", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cbub("실적은 <b>시장 예상보다</b><br>좋았는데…", 36, .1, "t-down", style="font-size:48px")}
  {numbox("3분기 매출", "1,158억$", COL2[0], 270, .4, L)}
  {numbox("4분기 전망", "1,300억$", COL2[1], 270, .6, L)}
  <div class="abs a-fade" style="left:{P}px;top:478px;width:{IW}px;--d:.8s;text-align:center;font-size:36px;color:#E6E9FF">둘 다 <b style="font-weight:400;color:#FFE36E">시장 예상 위</b> ✔</div>
  <div class="abs a-pop" style="left:{P}px;top:560px;width:{IW}px;--d:1.1s;text-align:center">
    <div style="font-size:40px;color:#E6E9FF">다음 날 정규장 주가</div>
    <div style="font-size:170px;line-height:1.05"><span class="thump" style="--d:1.3s;color:#6FB6FF;-webkit-text-stroke:7px {L};paint-order:stroke fill">▼2.89%</span></div></div>
  {ch(mascot("star", "surprised", "up"), P, 830, 260, 1.7, "a-sl", "hop")}
  {bub("숫자는 좋은데<br><b>왜 내렸지?!</b>", 340, 880, 1.9, "t-left", style="font-size:48px")}
</div>
''', "#2B3060"))

# 3 ── 용의자 둘: 선장 없는 배 + 순풍은 언제까지 (출처들이 공통으로 꼽은 이유)
S[3] = (1, page(FX + f'''
{head("결정적 단서 · 용의자 둘", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#EEF0FF;--d:0s">
  {cbub("짐은 <b>가득</b> 실었는데<br>선장이 배에서 내렸어요", 30, .1, "t-down", style="font-size:46px")}
  <div class="abs a-pop" style="left:{P}px;top:250px;width:{IW}px;height:330px;box-sizing:border-box;--d:.3s;background:#BFE3FF;border:5px solid {L};border-radius:24px;overflow:hidden">
    <div class="abs wave" style="left:0;right:0;bottom:0;height:70px;border-top:5px solid {L}"></div>
    <div class="abs sail" style="left:60px;top:30px">{ship(420)}</div>
    <div class="abs a-pop" style="left:560px;top:40px;--d:.7s;background:#fff;border:4px solid {L};border-radius:14px;padding:6px 16px;font-size:34px;line-height:1.3">선장실 비었음<br><span style="color:#E8590C">앞으로 항로는?</span></div>
  </div>
  <div class="abs a-fade" style="left:{P}px;top:596px;--d:.9s;font-size:30px;color:#6B5A50">배 = 엔비디아 · 선장 = 물러난 젠슨 황</div>
  <div class="abs a-sl" style="left:{P}px;top:650px;width:{IW}px;height:200px;box-sizing:border-box;--d:1.2s;background:#fff;border:5px solid {L};border-radius:22px;padding:20px 28px">
    <div style="font-size:44px">🔍 용의자 1 · <span style="color:#E8590C">리더십 공백</span></div>
    <div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#5B5070;margin-top:8px">이사회 "황의 CEO 복귀 계획 없다"</div></div>
  <div class="abs a-sl" style="left:{P}px;top:880px;width:{IW}px;height:200px;box-sizing:border-box;--d:1.8s;background:#fff;border:5px solid {L};border-radius:22px;padding:20px 28px">
    <div style="font-size:44px">🔍 용의자 2 · <span style="color:#E8590C">AI 순풍은 언제까지?</span></div>
    <div style="font-family:Noto Sans CJK KR,sans-serif;font-size:30px;color:#5B5070;margin-top:8px">AI 붐이 얼마나 더 갈지 의문이 다시 커짐</div></div>
</div>
''', "#30366E"))

# 4 ── 서울 현장 + 또 하나의 바람(의사록)
S[4] = (1, page(FX + f'''
{head("서울 현장 · 또 하나의 바람", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  <div class="abs" style="left:0;right:0;top:30px;text-align:center;font-size:42px">🇰🇷 서울은 하루 먼저 웃었다 (18일 코스피)</div>
  <div class="abs" style="left:0;right:0;top:90px;text-align:center;font-size:160px;line-height:1"><span class="punch" style="--d:.15s;color:{RED};-webkit-text-stroke:6px {L};paint-order:stroke fill">▲1.99%</span></div>
  <div class="stamp a-stamp" style="left:290px;top:270px;--d:.5s;--r:-6deg;font-size:48px;padding:0 18px;white-space:nowrap">5,000선 되찾음</div>
  {numbox("SK하이닉스", "▲4.19%", COL2[0], 380, .8, RED)}
  {numbox("삼성전자", "▲2.31%", COL2[1], 380, .95, RED)}
  {ch(mascot("star", "worried", "up"), P, 600, 230, 1.3, "a-sl", "shiver")}
  {bub("그런데 밤사이<br>엔비디아는 <b>▼2.89%</b>…", 300, 630, 1.5, "t-left", style="font-size:44px")}
  <div class="abs a-pop" style="left:{P}px;top:870px;width:{IW}px;height:250px;box-sizing:border-box;--d:2.0s;background:#3A3460;color:#FFF6EA;border:5px solid {L};border-radius:26px;text-align:center;padding-top:22px">
    <div style="font-size:38px;color:#FFC08A">💨 또 하나의 바람 · 연준 의사록</div>
    <div style="font-size:64px;margin-top:6px">거의 모두 <span class="thump" style="--d:2.3s;color:#FFE36E">"추가 인상 적절"</span></div>
    <div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#D9D3F0;margin-top:6px">일부는 12월 더 큰 폭 인상 거론</div></div>
</div>
''', "#4A3E78"))

# 5 ── 수사 노트 (오늘 한국장 체크 3)
def note(n, title, sub, y, d):
    return (f'<div class="abs a-drop" style="left:{P}px;top:{y}px;width:{IW}px;--d:{d}s">'
            f'<div style="background:#FFFDF2;border:5px solid {L};border-radius:14px;padding:16px 28px 16px 120px;position:relative;box-shadow:0 6px 0 rgba(0,0,0,.18);'
            f'background-image:repeating-linear-gradient(0deg,transparent 0 46px,#F1E6C8 46px 49px)">'
            f'<div style="position:absolute;left:24px;top:50%;margin-top:-38px;width:76px;height:76px;border-radius:50%;background:#E8590C;border:5px solid {L};color:#fff;font-size:48px;line-height:72px;text-align:center">{n}</div>'
            f'<div style="font-size:46px">{title}</div>'
            f'<div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#5B5070;margin-top:4px">{sub}</div></div></div>')
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 노트 · 오늘 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#5E6BB8;--d:0s">
  <div class="abs" style="left:0;right:0;top:36px;text-align:center;font-size:62px;color:#FFF6EA;-webkit-text-stroke:3px {L};paint-order:stroke fill"><span class="punch" style="--d:.1s">오늘 한국장, 볼 것은 셋</span></div>
  {note(1, "반도체 상승분 지킬까", "엔비디아 반락이 이어지면 반도체 업종에 부담 가능성", 160, .5)}
  {note(2, "금리 인상 경계", "의사록이 추가 인상을 가리켜 성장주·환율 부담 가능성", 370, .95)}
  {note(3, "앤트로픽 상장 앞두고", "공모 흥행 여부가 AI 투자 심리의 가늠자라는 분석", 580, 1.4)}
  {ch(mascot("bamtol", "normal", "point"), 630, 800, 220, 2.0, "a-sr", "squish")}
  {bub("수사 노트 셋,<br><b>꼭 챙겨요!</b>", 320, 840, 2.2, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.4s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: AP, 이투데이, 파이낸셜뉴스, 뉴스핌, 서울경제</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 다음 사건", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:420px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:{P}px;top:40px;font-size:38px;color:#FFC08A">다음 사건 파일 · 미국 현지 19일</div>
  <div class="abs" style="left:{P}px;top:100px;font-size:76px;line-height:1.2">앤트로픽<br>나스닥 상장 첫날</div>
  <div class="abs a-rise" style="left:{P}px;top:300px;--d:.3s;font-size:44px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>에</div>
</div>
<div class="panel a-pop" style="left:44px;top:660px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("star", "happy", "wave"), 40, 250, 250, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 590, 220, 270, .4, "a-sr", "hop")}
  {bub("오늘 수사는 여기까지!<br><b>사건 해결~</b>", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1270px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:50px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1400px;color:#6B5A50;--d:1.0s">출처: AP, 이투데이, 파이낸셜뉴스, 이데일리, 뉴스핌, 서울경제, 한국경제<br>정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.6, 1.5), 3: (4.0, 1.5), 4: (4.4, 1.5), 5: (4.0, 1.5), 6: (3.2, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .5), (1, .1, "pop", .5), (1, .2, "pop", .5), (1, .3, "pop", .5), (1, .4, "thud", 1), (1, .6, "blip_down", .8), (1, .7, "question", .6),
 (2, .1, "pop", .8), (2, .4, "pop", .7), (2, .6, "pop", .7), (2, .8, "ding", .6), (2, 1.1, "whoosh", .5), (2, 1.3, "blip_down", .8), (2, 1.7, "boing", .5), (2, 1.9, "question", .8),
 (3, .1, "pop", .7), (3, .3, "whoosh", .5), (3, .7, "pop", .6), (3, .9, "tick", .6), (3, 1.2, "whoosh", .6), (3, 1.4, "dundun", .5), (3, 1.8, "whoosh", .6), (3, 2.0, "dundun", .5), 
 (4, .05, "whoosh", .5), (4, .15, "sparkle", .8), (4, .5, "thud", .8), (4, .8, "pop", .6), (4, .95, "pop", .6), (4, 1.3, "whoosh", .4), (4, 1.5, "pop", .8), (4, 2.0, "whoosh", .6), (4, 2.3, "dundun", .7),
 (5, .05, "whoosh", .5), (5, .1, "thud", .6), (5, .5, "CHECK1", 1), (5, .95, "CHECK2", 1), (5, 1.4, "CHECK3", 1), (5, 2.2, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .6), (6, .9, "jingle", .9),
]
