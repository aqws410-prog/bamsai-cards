"""형식: 밤사이 탐정 추리 v3 (검수 전 · 2026-10-24) — 장면 1을 '용의자 라인업 벽(키 눈금)' 구도로 새로 짠 버전.
내용: 2026-10-24 (23일 뉴욕 — 다우 ▼1.23%로 3대 지수 중 가장 크게 하락, WTI 배럴당 100달러 돌파). 비유: 기름값 = 모든 물건에 붙는 '배송비'.
흐름: 1 사건 해결 선언(결론: 다우 ▼1.23% + '범인은 기름값!') → 2 용의자 셋(수배 전단) → 3 단서·주범(배송비 비유) → 4 한국 현장 조사(V자 반등) → 5 수사 수첩(월요일 체크 3) → 6 다음 사건 예고.
숫자는 2026-10-24 카드·sources.md에 있는 것만 쓴다. 다른 용의자를 '무죄'로 단정하지 않는다.
"""
from lib import *

S = {}
RED, BLUE = "#E03131", "#2F6BD8"

FX = """<style>
@keyframes grow{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes linedraw{from{stroke-dashoffset:var(--len)}to{stroke-dashoffset:0}}
@keyframes tapeMove{from{transform:translateX(0)}to{transform:translateX(-520px)}}
@keyframes spotSweep{0%{transform:translateX(-120px)}100%{transform:translateX(0)}}
@keyframes up{0%{transform:translateY(0)}100%{transform:translateY(-34px)}}
.tape-run{animation:tapeMove 3s linear both}
.grow{transform-origin:50% 0;animation:grow .55s cubic-bezier(.2,.9,.3,1) both;animation-delay:var(--d,0s)}
.spot{animation:spotSweep .8s cubic-bezier(.2,.9,.3,1) both}
.lift{animation:up .5s ease-out both;animation-delay:var(--d,0s)}
</style>"""

TAPE = "출입 금지 · 밤사이 탐정 · 사건 현장 · " * 5

def tape(top, rot):
    return (f'<div class="abs" style="left:-80px;top:{top}px;width:1240px;height:76px;background:#FFD84D;border-top:6px solid {L};border-bottom:6px solid {L};'
            f'transform:rotate({rot}deg);overflow:hidden;box-shadow:0 8px 0 rgba(0,0,0,.25)">'
            f'<div class="tape-run" style="position:absolute;left:0;top:7px;white-space:nowrap;font-size:42px;line-height:54px;padding-left:20px">{TAPE}</div></div>')

# 1 ── 결론 먼저 (라인업 벽): 0초에 숫자·결론·탐정(클로즈업)·라인업 벽이 모두 보인다
#      0~1초: 숫자 펀치(0) → 지수 막대 아래로 쭉(0.15~0.55) → '주범 확보' 도장(.45) → 스포트라이트 쓸기(0~.8) → 탐정 흔들림
def lineup_bar(name, val, h, x, d):
    return (f'<div class="abs" style="left:{x}px;top:150px;width:120px;text-align:center;font-size:34px;color:#F6EEE4">{name}</div>'
            f'<div class="abs grow" style="left:{x + 20}px;top:200px;width:80px;height:{h}px;background:#5B8DEF;border:5px solid {L};border-radius:0 0 14px 14px;--d:{d}s"></div>'
            f'<div class="abs" style="left:{x - 10}px;top:{214 + h}px;width:140px;text-align:center;font-size:40px;color:#9EC2FF">{val}</div>')
LINEUP = "".join(f'<div class="abs" style="left:0;right:0;top:{y}px;height:3px;background:rgba(255,255,255,.18)"></div>' for y in range(200, 640, 55))
S[1] = (1, page(FX + f'''
{stars(14, 24, 0, 260)}
{head("밤사이 탐정 · 10.24 SAT", 1, "#F6EEE4")}
<div class="abs" style="left:0;width:1080px;top:205px;text-align:center;font-size:46px;color:#C9D6FF">다우존스 · 23일 뉴욕 마감</div>
<div class="abs" style="left:0;width:1080px;top:262px;text-align:center"><span class="punch" style="--d:0s;font-size:250px;line-height:1;color:#7DB0FF;-webkit-text-stroke:10px {L};paint-order:stroke fill">▼1.23%</span></div>
<div class="abs" style="left:0;width:1080px;top:512px;text-align:center;font-size:96px;color:#fff;-webkit-text-stroke:5px {L};paint-order:stroke fill">범인은 <span style="color:#FFE36E">기름값!</span></div>
<div class="panel" style="left:44px;top:680px;width:982px;height:740px;background:#1D2348">
  <div class="abs spot" style="left:330px;top:-120px;width:760px;height:980px;background:radial-gradient(ellipse at 50% 70%,rgba(255,236,170,.34) 0,rgba(255,236,170,.10) 45%,transparent 68%)"></div>
  {LINEUP}
  <div class="abs" style="left:{P}px;top:40px;font-size:40px;color:#FFD84D">지수 라인업 · 23일</div>
  {lineup_bar("다우", "▼1.23%", 330, P, .15)}
  {lineup_bar("S&amp;P", "▼0.52%", 140, P + 150, .3)}
  {lineup_bar("나스닥", "▼0.21%", 56, P + 300, .45)}
  <div class="abs" style="left:400px;top:190px;width:520px"><div class="shiver" style="animation-delay:.6s">{mascot("bamtol", "surprised", "hold", p_mag())}</div></div>
</div>
{tape(1336, -5).replace("width:1240px","width:760px").replace("left:-80px","left:-60px")}
<div class="stamp a-stamp" style="left:560px;top:706px;--d:.45s;--r:-9deg;font-size:62px;white-space:nowrap">주범 확보!</div>
''', "#262B55"))

# 2 ── 용의자 셋 (수배 전단 세로 목록) — 다른 용의자를 '무죄'로 단정하지 않는다
def wanted(icon, name, note, top, d, ncol):
    return (f'<div class="abs a-sl" style="left:{P}px;top:{top}px;width:{IW}px;height:200px;box-sizing:border-box;background:#F4E6C6;border:5px solid {L};border-radius:22px;--d:{d}s;display:flex;align-items:center;gap:26px;padding:0 30px;box-shadow:0 6px 0 rgba(0,0,0,.2)">'
            f'<div style="flex:none;width:140px;height:140px;border:4px solid {L};border-radius:16px;background:#fff;font-size:96px;line-height:140px;text-align:center">{icon}</div>'
            f'<div style="flex:1"><div style="font-size:30px;color:#8A5A3B">용의자</div><div style="font-size:58px">{name}</div></div>'
            f'<div style="flex:none;background:{ncol};color:#fff;border:4px solid {L};border-radius:999px;padding:8px 22px;font-size:36px">{note}</div></div>')
S[2] = (1, page(FX + f'''
{head("용의자 셋", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#3A4080;--d:0s">
  {cbub("다우를 <b>끌어내린 범인</b>은<br>이 셋 중 누구일까요?", 40, .1, "t-down", style="font-size:44px")}
  {wanted("🛢️", "기름값", "100달러 돌파", 250, .4, RED)}
  {wanted("💾", "반도체", "오히려 반등", 480, .7, "#7B6FD6")}
  {wanted("📡", "스페이스X 소식", "통신주만 급락", 710, 1.0, "#8A6A3A")}
  {ch(mascot("owl", "surprised", "hold", p_tablet()), P, 930, 260, 1.5, "a-sl", "squish")}
  {bub("반도체는 오히려<br><b>올랐</b>는데요?", 330, 990, 1.8, "t-left", style="font-size:46px")}
</div>
''', "#2B3060"))

# 3 ── 단서·주범 지목 (비유: 기름값 = 모든 물건에 붙는 '배송비')
def parcel(label, x, d):
    return (f'<div class="abs a-pop" style="left:{x}px;top:110px;width:250px;--d:{d}s">'
            f'<div style="height:150px;background:#D9A877;border:5px solid {L};border-radius:14px;position:relative">'
            f'<div style="position:absolute;left:50%;top:0;bottom:0;width:30px;margin-left:-15px;background:#F0D9A8;border-left:4px solid {L};border-right:4px solid {L}"></div></div>'
            f'<div style="text-align:center;font-size:36px;margin-top:8px">{label}</div>'
            f'<div class="a-pop" style="--d:{d + .9:.1f}s;margin:16px auto 0;width:200px;text-align:center;background:#fff;border:4px solid {L};border-radius:12px;font-size:34px;color:{RED}">배송비 ▲</div></div>')
S[3] = (1, page(FX + f'''
{head("단서 분석", 3, "#EDEAF8")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#F3EEFF;--d:0s">
  {cbub("기름값은 <b>모든 물건에 붙는<br>배송비</b> 같은 거예요", 26, .1, "t-down", style="font-size:44px")}
  <div class="abs" style="left:0;top:190px;width:982px;height:470px">
    {parcel("과자", COL3[0][0], .4)}{parcel("옷", COL3[1][0], .55)}{parcel("가전", COL3[2][0], .7)}
  </div>
  {nar("배송비가 오르면 → <b>물건값(물가)</b>도 ↑<br>→ 금리 걱정 ↑ → 대부분 업종 ↓", P, 640, 1.8, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {stamp("주범: 기름값", 230, 800, 2.4, -6)}
  {numbox("WTI (23일)", "100달러 돌파", COL2[0], 960, 2.9, RED)}
  {numbox("다우 (23일)", "▼1.23%", COL2[1], 960, 3.1, BLUE)}
</div>
''', "#30366E"))

# 4 ── 한국 현장 조사 (23일 코스피: 장중 4%대 급락 → 상승 마감)
VCH = (f'<svg width="{IW}" height="300" viewBox="0 0 902 300" style="overflow:visible">'
       f'<line x1="0" y1="70" x2="902" y2="70" stroke="#8FA39A" stroke-width="4" stroke-dasharray="14 12"/>'
       f'<text x="8" y="56" font-size="30" fill="#5E7268" font-family="Jua">전날 종가</text>'
       f'<path d="M20 74 L200 160 L330 250 L470 210 L620 120 L760 80 L880 50" fill="none" stroke="{RED}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" '
       f'style="stroke-dasharray:1000;--len:1000;stroke-dashoffset:1000;animation:linedraw 1.1s ease-out .4s both"/>'
       f'<text x="270" y="292" font-size="34" fill="{BLUE}" font-family="Jua">장중 4%대 급락</text>'
       f'<circle cx="880" cy="50" r="15" fill="{RED}" stroke="{L}" stroke-width="4"/></svg>')
S[4] = (1, page(FX + f'''
{head("한국 현장 조사", 4, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1180px;background:#E2F6EA;--d:0s">
  {cbub("그보다 앞서 23일 서울에선?<br>코스피가 <b>급락을 딛고</b> 올랐어요", 34, .15, "t-down", style="font-size:42px")}
  <div class="abs" style="left:{P}px;top:230px">{VCH}</div>
  {numbox("코스피 (23일)", "▲0.30%", COL2[0], 600, 1.4, RED)}
  {numbox("SK하이닉스", "▲4.42%", COL2[1], 600, 1.7, RED)}
  {nar("외국인은 <b>1조938억원</b> 순매도,<br>기관·개인이 사들여 받쳤어요", P, 800, 2.2, f"font-size:40px;width:{IW}px;box-sizing:border-box;text-align:center")}
  {ch(mascot("star", "happy", "up"), 120, 940, 250, 2.5, "a-sl", "hop")}
  {ch(mascot("bamtol", "normal", "hold", p_mag()), 600, 940, 250, 2.6, "a-sr", "squish2")}
</div>
''', "#4A3E78"))

# 5 ── 수사 수첩 (월요일 체크)
items = [("🛢️", "기름값 100달러, 버틸까", "더 오르면 물가·금리 걱정이 커질 가능성"),
         (ICONS["chip"], "반도체, 반등 이어갈까", "미국 반도체주 금요일 반등"),
         (ICONS["won"], "외국인이 돌아올까", "23일 1조938억원 순매도 · 원/달러 1,324.6원")]
rows = "".join(
    f'<div class="abs a-rise" style="left:{P}px;top:{210 + i*190}px;width:{IW}px;height:170px;--d:{.6 + i*.45:.2f}s;display:flex;align-items:center;gap:22px;border-bottom:4px dashed #C9B48A">'
    f'<div style="flex:none;width:64px;height:64px;border:5px solid {L};border-radius:12px;background:#fff;font-size:52px;line-height:60px;text-align:center;color:{RED}"><span class="a-stamp" style="display:inline-block;--d:{.9 + i*.45:.2f}s">✔</span></div>'
    f'<div style="flex:none;font-size:56px;width:70px;text-align:center">{ic}</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:29px;color:#6B5A50;margin-top:4px">{d}</div></div></div>'
    for i, (ic, t, d) in enumerate(items))
S[5] = (1, page(FX + f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("수사 수첩 · 월요일 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:1060px;background:#FFFBEF;--d:0s">
  <div class="abs" style="left:0;right:0;top:0;height:150px;background:#FFE9A8;border-bottom:5px solid {L}"></div>
  <div class="abs" style="left:{P}px;top:44px;font-size:58px">월요일 한국장, 볼 것은 셋</div>
  {rows}
  {ch(mascot("bamtol", "normal", "point"), 640, 790, 250, 2.2, "a-sr", "squish")}
  {bub("주말 동안<br><b>이 셋</b>을 지켜봐요!", 200, 830, 2.4, "t-right", style="font-size:42px")}
</div>
<div class="src a-fade" style="top:1290px;color:#6B5A50;--d:2.6s">투자 권유 아님 · 판단과 책임은 본인에게<br>출처: AP, 뉴스핌, 로이터, 서울경제, 뉴스1, SBS Biz</div>
''', "#FFE1CC"))

# 6 ── 다음 사건 예고 (아침)
S[6] = (1, page(FX + f'''
{head("밤사이 탐정 · 마침", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:440px;background:#3A3460;--d:0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">다음 사건 파일</div>
  <div class="abs" style="left:44px;top:100px;font-size:62px;line-height:1.25">내일(일) 이번 주 성적표<br>27~28일 FOMC</div>
  <div class="abs a-rise" style="left:44px;top:320px;--d:.3s;font-size:44px">내일 아침 <span style="color:#FFC08A">8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:680px;width:982px;height:560px;background:#FFE9C2;--d:.15s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 240, 260, .3, "a-sl", "squish")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .4, "a-sr", "hop")}
  {bub("사건 종결!<br><b>밤사이 탐정</b>이었습니다", 300, 30, .65, "t-down", "75%", "font-size:40px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:.9s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1410px;color:#6B5A50;--d:1.0s">출처: AP, 뉴스핌, 로이터, CNBC, 서울경제, 뉴스1, SBS Biz, 한국경제 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (2.6, 1.3), 2: (3.6, 1.5), 3: (4.2, 1.5), 4: (3.8, 1.5), 5: (3.8, 1.5), 6: (3.4, 1.3)}
CUES = [
 (1, .0, "dundun", 1), (1, .0, "tension", .6), (1, .05, "thud", .8), (1, .15, "slidedown", .6), (1, .45, "thud", .9), (1, .5, "reveal", .6), (1, .6, "whoosh", .5), (1, .8, "ding", .6),
 (2, .05, "whoosh", .5), (2, .1, "pop", .8), (2, .4, "shutter", .7), (2, .7, "shutter", .7), (2, 1.0, "shutter", .7), (2, 1.5, "whoosh", .5), (2, 1.8, "question", .6),
 (3, .1, "pop", .8), (3, .4, "boing", .5), (3, .55, "boing", .5), (3, .7, "boing", .5), (3, 1.3, "ding", .5), (3, 1.8, "tick", 1), (3, 2.4, "thud", 1), (3, 2.4, "reveal", .8), (3, 2.9, "ding", .8), (3, 3.1, "blip_down", .6),
 (4, .05, "whoosh", .5), (4, .15, "pop", .8), (4, .4, "slidedown", .5), (4, 1.0, "sparkle", .6), (4, 1.4, "pop", .7), (4, 1.7, "pop", .6), (4, 2.2, "tick", .9), (4, 2.5, "boing", .6),
 (5, .05, "whoosh", .5), (5, .9, "CHECK1", 1), (5, 1.35, "CHECK2", 1), (5, 1.8, "CHECK3", 1), (5, 2.4, "pop", .8),
 (6, .0, "pop", .6), (6, .05, "sunrise", .8), (6, .3, "whoosh", .5), (6, .4, "boing", .7), (6, .65, "pop", .8), (6, .9, "jingle", .9),
]
