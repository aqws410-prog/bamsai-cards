"""2026-10-15 릴스 — 물가 쇼크와 AI·반도체 하락.

규칙: S[n] = (아무 숫자, page(...))  ·  PLAN[n] = (화면 길이 초, 재생 배속)  ·  CUES = (장면, 장면 안 시각(배속 전), 효과음, 볼륨)
"""
from lib import *

S = {}

# 1 ── 한국이 잠든 사이
S[1] = (7.5, page(f'''
{stars(30, 3)}
{head("밤사이 · 10.15 THU", 1, "#F6EEE4")}
<div class="abs hook" style="left:44px;top:190px;font-size:66px;color:#F6EEE4">물가는 고작 0.1%p 더 올랐는데</div>
<div class="abs hook" style="left:44px;top:272px;font-size:86px;color:#FFC08A">나스닥은 왜 1.88%나?</div>
<div class="sfx a-stamp" style="left:905px;top:240px;font-size:110px;--d:.05s;--r:12deg;color:#FFF0B3">?!</div>
<div class="panel a-pop" style="left:44px;top:430px;width:982px;height:560px;background:#3C4485;--d:.25s">
  {stars(14, 9, 20, 300, 20, 950)}{moon(850, 30, 96)}
  {nar("한국이 잠든 사이…", 30, 30, .45)}
  <div class="abs" style="left:56px;top:430px;width:320px;height:70px;border-radius:40px;background:#F6EEE4;border:4px solid {L}"></div>
  {ch(mascot("star", "sleep", cap=True), 80, 200, 270, .45, "a-fade", "squish")}
  <div class="abs sfx" style="left:300px;top:170px;font-size:60px;color:#C9D6FF;animation:zzz 1.8s ease-out infinite">Z</div>
  <div class="abs sfx" style="left:340px;top:140px;font-size:46px;color:#C9D6FF;animation:zzz 1.8s ease-out .9s infinite">z</div>
  {ch(mascot("owl", "surprised", "hold", p_tablet()), 640, 190, 290, .7, "a-sr", "squish2")}
  {sfx("두둥!", 420, 360, 92, 1.1, -10, "#FFC08A")}
  {bub("앗! 미국 주식시장에<br>일이 생겼어!", 380, 90, 1.3, "t-down", "350px", "font-size:38px;padding:16px 26px")}
</div>
<div class="panel a-pop" style="left:44px;top:1030px;width:982px;height:520px;background:#4B529A;--d:2.3s">
  {ch(mascot("star", "surprised"), 60, 170, 280, 2.5, "a-sl", "squish")}
  {sfx("!!", 320, 220, 110, 2.7, 8, "#FFF0B3")}
  {bub("자는 동안<br>무슨 일 있었어?!", 40, 40, 2.8, "t-down", "130px")}
  {ch(mascot("bamtol", "happy", "wave"), 640, 160, 290, 3.2, "a-sr", "hop")}
  {bub("나 밤톨이가<br><b>1분</b>만에 알려줄게!", 520, 36, 3.5, "t-down", "250px", "font-size:38px")}
</div>
''', "#262B55"))

# 2 ── 물가 성적표
crowd = (ch(mascot("owl", "normal"), 40, 300, 170, 2.9, "a-rise", "squish")
         + ch(mini("#D9F2E6"), 190, 330, 140, 3.0, "a-rise", "squish2")
         + ch(mascot("star", "normal"), 320, 300, 170, 3.1, "a-rise", "squish"))
chart = f'''<svg class="abs" style="left:560px;top:120px" width="380" height="300" viewBox="0 0 380 300">
 <rect x="4" y="4" width="372" height="292" rx="26" fill="#fff" stroke="{L}" stroke-width="5"/>
 <path d="M30 80 L110 70 L170 110 L230 150 L290 200 L340 250" fill="none" stroke="#5B8DEF" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" style="stroke-dasharray:420;--len:420;animation:draw 1s ease-in both;animation-delay:3.6s"/>
 <path d="M318 238 L346 256 L344 222" fill="none" stroke="#5B8DEF" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" style="opacity:0;animation:fade .2s both;animation-delay:4.5s"/>
</svg>'''
S[2] = (8.0, page(f'''
{stars(12, 5, 0, 400)}
{head("밤사이 · 미국 물가", 2, "#F6EEE4")}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:640px;background:#E3EEFF;--d:.1s">
  {nar("미국 <b>물가 성적표(CPI)</b>가 나왔어요", 30, 28, .4)}
  <div class="tag a-pop" style="left:110px;top:150px;--d:.8s">미국 물가 역할</div>
  {ch(mascot("moon", "happy", "hold", p_card("9월 물가", "3.7%")), 60, 200, 380, .7, "a-pop", "squish")}
  {sfx("앗 뜨거!", 400, 160, 90, 1.2, -12, "#FFC08A")}
  {bub("예상(3.6%)보다<br><b>조금 더 뜨거워요!</b>", 490, 250, 1.5, "t-left")}
  <div class="abs a-pop" style="left:520px;top:480px;--d:1.9s;font-size:32px;background:#fff;border:4px solid {L};border-radius:16px;padding:8px 18px">근원물가도 2.6% (예상 2.5%)</div>
</div>
<div class="panel a-pop" style="left:44px;top:880px;width:982px;height:670px;background:#FFE9EF;--d:2.5s">
  {think("금리를 또<br>올리면 어쩌지…", 40, 50, 3.1)}
  {crowd}
  {chart}
  {sfx("주르륵", 640, 400, 82, 4.2, 6, "#C9E4FF")}
  {nar("<b>금리 인상 걱정</b> → AI·반도체부터 팔았어요", 30, 545, 4.6)}
  <div class="num a-pop" style="left:690px;top:24px;--d:5.0s"><div class="k">나스닥</div><div class="v">▼1.88%</div></div>
</div>
<div class="src a-fade" style="top:1580px;color:#B8BCD8;--d:5.2s">출처: AP, 연합뉴스, 뉴스핌, 서울경제 · 2026.10.14 뉴욕 마감</div>
''', "#2B3060"))

# 3 ── 1분 공부: 금리와 미래 기대
S[3] = (8.0, page(f'''
{head("1분 주식 공부", 3, "#EDEAF8")}
<div class="abs hook a-rise" style="left:44px;top:196px;font-size:72px;color:#F6EEE4;--d:.1s">금리가 오르면 <span style="color:#FFC08A">'미래 기대'</span>가 식어요</div>
<div class="panel a-pop" style="left:44px;top:330px;width:472px;height:620px;background:#FFF6D2;--d:.4s">
  <div class="tag" style="left:24px;top:24px">① 10년 뒤 큰 용돈!</div>
  {ch(mascot("star", "happy", "hold", p_paper("용돈!")), 60, 200, 330, .7, "a-pop", "hop")}
  {sfx("야호!", 250, 110, 84, 1.2, 10, "#FFC08A")}
</div>
<div class="panel a-pop" style="left:554px;top:330px;width:472px;height:620px;background:#ECE7FF;--d:2.0s">
  <div class="tag" style="left:24px;top:24px">② 은행 이자가 오르면?</div>
  {think("지금 은행에 넣어도<br><b style='color:#E8590C;font-weight:400'>이자 쏠쏠</b>한데?", 26, 90, 2.4)}
  {ch(mini("#D9F2E6"), 330, 300, 120, 2.3, "a-rise", "squish")}
  {ch(mascot("star", "teary", "hold", p_paper("용돈!")), 40, 270, 280, 2.8, "a-fade", "shiver")}
  {sfx("시들", 270, 500, 60, 3.1, 6, "#C9D6FF")}
</div>
<div class="panel a-pop" style="left:44px;top:990px;width:982px;height:560px;background:#FFFFFF;--d:3.8s">
  {ch(mascot("bamtol", "normal", "point"), 30, 160, 320, 4.1, "a-sl", "squish")}
  {bub("금리가 오르면 <b>먼 미래 기대</b>로<br>오른 주식이 먼저 흔들려!", 340, 70, 4.6, "t-left", style="font-size:46px")}
  {nar("AI·반도체주가 딱 이런 '기대주'예요", 390, 380, 5.4)}
</div>
''', "#30366E"))

# 4 ── 반도체 미끄럼
speed = "".join(f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:8px;border-radius:5px;background:{L};opacity:.45"></div>'
                for x, y, w in [(20, 90, 110), (50, 140, 80), (0, 190, 130)])
S[4] = (8.5, page(f'''
{head("밤사이 · AI·반도체", 4, "#F6EEE4")}
<div class="abs hook a-rise" style="left:44px;top:196px;font-size:68px;color:#F6EEE4;--d:.1s">한국 반도체도 괜찮을까?</div>
<div class="panel a-pop" style="left:44px;top:320px;width:982px;height:640px;background:#E2F6EA;--d:.4s">
  <div class="abs" style="left:0;right:0;top:480px;height:170px;background:#F6C9A8;border-top:5px solid {L}"></div>
  <div class="abs" style="left:0;right:0;top:556px;height:7px;background:repeating-linear-gradient(90deg,#fff 0 60px,transparent 60px 110px)"></div>
  {nar("금리 걱정 바람에<br>미국 <b>AI·반도체주가 와르르</b>", 26, 26, .7)}
  <div class="abs" style="left:590px;top:250px;width:240px"><div class="a-sr" style="--d:1.0s"><div class="jog">{chip("#BFD3FF", "tired")}</div></div></div>
  <div class="tag a-pop" style="left:620px;top:536px;--d:1.3s">한국 반도체</div>
  <div class="abs" style="left:40px;top:250px;width:240px;--dx:240px;animation:run 3s ease-out both;animation-delay:1.8s">
     {speed}<div class="jog">{chip("#FFD9A8", "tired")}</div>
     <div class="tag" style="left:40px;top:286px">미국 반도체</div>
  </div>
  {bub("와르르~!", 290, 160, 2.4, "t-down", "90px", "font-size:40px;padding:14px 24px")}
  {sfx("헉, 나도?", 790, 200, 56, 2.8, 10, "#C9E4FF")}
</div>
<div class="panel a-pop" style="left:44px;top:1000px;width:982px;height:550px;background:#F3EEFF;--d:4.0s">
  {ch(mascot("bamtol", "worried"), 20, 180, 300, 4.3, "a-sl", "squish")}
  {bub("미국 반도체가 흔들리면<br><b>한국 반도체도</b> 영향 받기 쉬워!", 300, 40, 4.8, "t-left")}
  <div class="num a-pop" style="left:340px;top:290px;--d:5.6s"><div class="k">어제 코스피</div><div class="v">▼0.44%</div></div>
  <div class="num a-pop" style="left:650px;top:290px;--d:6.0s"><div class="k">6거래일 연속</div><div class="v">▼하락</div></div>
  {sfx("뚝!", 570, 420, 80, 6.3, -8, "#C9E4FF")}
</div>
<div class="src a-fade" style="top:1580px;color:#D6CCE8;--d:6.2s">출처: 연합뉴스, AP, 뉴스핌, 뉴스1, 아주경제 · 2026.10.14</div>
''', "#4A3E78"))

# 5 ── 오늘 체크 3
icons = {
    "chip": f'<svg viewBox="0 0 80 80" width="70"><rect x="14" y="14" width="52" height="52" rx="14" fill="#BFD3FF" stroke="{L}" stroke-width="4"/><path d="M26 6v8M40 6v8M54 6v8M26 66v8M40 66v8M54 66v8" stroke="{L}" stroke-width="4" stroke-linecap="round"/><path d="M28 46 l9 -10 l8 7 l10 -12" stroke="{L}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "won": f'<svg viewBox="0 0 80 80" width="70"><circle cx="40" cy="40" r="30" fill="#FFE59A" stroke="{L}" stroke-width="4"/><text x="40" y="53" text-anchor="middle" font-size="36" fill="{L}" font-family="Jua">$</text></svg>',
    "oil": f'<svg viewBox="0 0 80 80" width="70"><path d="M40 8 Q64 40 60 52 A20 20 0 0 1 20 52 Q16 40 40 8Z" fill="#8A7BC8" stroke="{L}" stroke-width="4"/><path d="M30 50 Q32 58 38 60" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/></svg>',
}
items = [("chip", "반도체, 또 흔들릴까?", "미국 AI·반도체 급락이 한국으로 번지는지"),
         ("won", "외국인, 매도 멈출까?", "코스피 6거래일 연속 하락 · 외국인 수급과 환율"),
         ("oil", "기름값은?", "WTI 95.09달러 <span style='color:#C92A2A'>▲1.01%</span> · 정유엔 도움, 항공엔 부담")]
cards = "".join(
    f'<div class="panel a-sl" style="left:44px;top:{690+i*200}px;width:982px;height:170px;background:#fff;--d:{2.4+i*.8:.1f}s;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box">'
    f'<div style="flex:none;width:70px;height:70px;border-radius:50%;background:#FFB27F;border:4px solid {L};font-size:42px;display:flex;align-items:center;justify-content:center">{i+1}</div>'
    f'<div style="flex:none">{ICONS[k]}</div>'
    f'<div><div style="font-size:48px">{t}</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:28px;color:#6B5A50;margin-top:4px;line-height:1.35">{d}</div></div></div>'
    for i, (k, t, d) in enumerate(items))
S[5] = (8.5, page(f'''
<div class="abs" style="right:-170px;top:-170px;width:520px;height:520px;border-radius:50%;background:#FFC6A0"></div>
{head("오늘 한국장 체크", 5, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:450px;background:#FFF8E1;--d:.1s">
  {ch(mascot("star", "surprised", "down", p_mag()), 40, 130, 270, .4, "a-sl", "squish")}
  {bub("그럼 오늘은<br>뭘 보면 돼?", 330, 40, .9, "t-left")}
  {ch(mascot("bamtol", "happy", "up"), 680, 140, 260, 1.4, "a-sr", "hop")}
  {bub("딱 <b>세 가지</b>만!", 620, 40, 1.8, "t-down", "150px", "font-size:40px;padding:14px 24px")}
</div>
{cards}
<div class="src a-fade" style="top:1300px;color:#6B5A50;--d:5.0s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게<br>출처: AP, 연합뉴스, 뉴스핌, 이투데이</div>
''', "#FFE1CC"))

# 6 ── 예고 (압축)
S[6] = (3.8, page(f'''
{head("아침이 밝았어요", 6, L)}
<div class="panel a-pop" style="left:44px;top:200px;width:982px;height:430px;background:#3A3460;--d:.0s;color:#FFF6EA">
  <div class="abs" style="left:44px;top:40px;font-size:38px;color:#FFC08A">오늘 밤 (미국 시간 10/15)</div>
  <div class="abs" style="left:44px;top:100px;font-size:72px;line-height:1.2">생산자물가<span style="color:#FFE59A">(PPI)</span>·<br>소매판매 발표!</div>
  <div class="abs a-rise" style="left:44px;top:300px;--d:.35s;font-size:46px">결과는 <span style="color:#FFC08A">내일 아침 8시</span>, 밤사이에서</div>
</div>
<div class="panel a-pop" style="left:44px;top:670px;width:982px;height:560px;background:#FFE9C2;--d:.2s">
  <div class="abs" style="left:300px;top:330px;width:380px;height:380px;border-radius:50%;background:#FFC46B;border:5px solid {L};animation:sunrise 1s cubic-bezier(.2,.9,.3,1) both"></div>
  {ch(mascot("owl", "sleep", cap=True), 40, 230, 270, .35, "a-sl", "squish")}
  {sfx("쿨쿨", 60, 120, 60, .6, -8, "#C9D6FF")}
  {ch(mascot("bamtol", "happy", "wave"), 620, 210, 290, .45, "a-sr", "hop")}
  {bub("내일 아침에<br><b>또 만나!</b>", 560, 40, .75, "t-down", "200px", "font-size:42px")}
</div>
<div class="abs a-pop" style="left:0;right:0;top:1290px;--d:1.0s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};box-shadow:0 6px 0 rgba(0,0,0,.18);border-radius:999px;padding:14px 46px;font-size:48px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1420px;color:#6B5A50;--d:1.1s">출처: AP, 연합뉴스, 뉴스핌, SBS Biz 등 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', "#FFF6EA"))

PLAN = {1: (4.6, 1.3), 2: (5.2, 1.5), 3: (5.4, 1.5), 4: (5.6, 1.6), 5: (5.0, 1.6), 6: (3.8, 1.0)}

# (장면, 장면 안 시각(애니메이션 delay와 같은 기준), 효과음 이름, 볼륨)
CUES = [
 (1, .0, "dundun", 1), (1, .05, "question", .7), (1, .25, "pop", .6), (1, .45, "tick", 1), (1, .45, "SNORE", 1),
 (1, .7, "whoosh", .7), (1, 1.1, "thud", .6), (1, 1.3, "pop", .8),
 (1, 2.3, "pop", .6), (1, 2.5, "whoosh", .6), (1, 2.7, "question", 1), (1, 2.8, "pop", .8),
 (1, 3.2, "boing", .8), (1, 3.5, "pop", .8),
 (2, .1, "pop", .7), (2, .4, "tick", 1), (2, .7, "pop", .8), (2, 1.2, "boing", 1), (2, 1.5, "pop", .8),
 (2, 2.5, "pop", .7), (2, 3.0, "hmm", 1), (2, 3.1, "pop", .6), (2, 3.6, "slidedown", 1),
 (2, 4.6, "tick", 1), (2, 5.0, "blip_down", 1),
 (3, .1, "whoosh", .6), (3, .4, "pop", .7), (3, .75, "boing", .7), (3, 1.2, "yay", 1),
 (3, 2.0, "pop", .7), (3, 2.4, "pop", .8), (3, 3.0, "sad", 1),
 (3, 3.8, "pop", .7), (3, 4.1, "whoosh", .7), (3, 4.6, "pop", .8), (3, 5.4, "ding", 1),
 (4, .1, "whoosh", .6), (4, .4, "pop", .7), (4, .7, "tick", 1), (4, 1.0, "whoosh", .6),
 (4, 1.0, "STEPS_SLOW", 1), (4, 1.8, "slidedown", 1), (4, 2.4, "pop", .8), (4, 2.8, "question", .8),
 (4, 4.0, "pop", .7), (4, 4.3, "whoosh", .7), (4, 4.8, "pop", .8),
 (4, 5.6, "blip_down", 1), (4, 6.0, "blip_down", 1), (4, 6.3, "thud", 1),
 (5, .1, "pop", .7), (5, .4, "whoosh", .7), (5, .9, "question", 1), (5, 1.4, "boing", .8),
 (5, 2.3, "boing", .5), (5, 1.8, "pop", .8),
 (5, 2.4, "CHECK1", 1), (5, 3.2, "CHECK2", 1), (5, 4.0, "CHECK3", 1),
 (6, .0, "pop", .7), (6, .05, "sunrise", .8), (6, .35, "whoosh", .5), (6, .45, "boing", .7),
 (6, .6, "SNORE_SHORT", .8), (6, .75, "pop", .8), (6, 1.0, "jingle", 1),
]
