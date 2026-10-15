"""형식: 밤사이 단톡방 — 캐릭터들이 메신저로 대화하며 뉴스를 푼다. 화면 대부분이 채팅창.
예시 내용: 2026-10-15. 새 날짜에는 구조만 참고하고 대화·비유·카드는 그날 이야기에 맞게 새로 짠다.
메시지가 하나씩 올라오는 리듬(0.6~0.9초 간격)이 핵심. 한 장면에 메시지 3~4개까지.
"""
from lib import *

S = {}
BG = "#20244A"
CH_X, CH_W = 44, 982

def room(n, inner, d=0, h=1200, title="🌙 밤사이 단톡방 (4)"):
    return chat(title, CH_X, 260, CH_W, h, d, inner)

def bar(cpi_exp, cpi_act):
    return (f'<div style="font-size:30px;margin-bottom:8px">📊 미국 9월 물가(CPI)</div>'
            f'<div style="display:flex;align-items:flex-end;gap:30px;height:200px;padding-left:20px">'
            f'<div style="text-align:center"><div style="width:120px;height:{cpi_exp}px;background:#B9C7E6;border:4px solid {L};border-radius:10px 10px 0 0"></div><div style="font-size:30px">예상 3.6%</div></div>'
            f'<div style="text-align:center"><div style="width:120px;height:{cpi_act}px;background:#FF8A8A;border:4px solid {L};border-radius:10px 10px 0 0"></div><div style="font-size:30px;color:#E03131">실제 3.7%</div></div></div>')

# 1 ── 단톡 알림 (훅)
S[1] = (1, page(f'''
{head("밤사이 · 10.15 THU", 1, "#F6EEE4")}
{big("물가 0.1%p에 나스닥 <span style='color:#7DBBFF'>▼1.88%</span>?!", 44, 176, 62, 0, "#FFC08A", "")}
{room(1, f"""
  {msg("owl", "🚨 속보!! 나스닥 <b style='color:#2F6BD8;font-weight:400'>▼1.88%</b>", 120, .15, mood="surprised")}
  {msg("star", "자고 일어났는데<br>무슨 일이야?!", 330, 1.0, side="r", mood="surprised")}
  {msg("owl", "미국 물가가 예상보다<br><b style='color:#E03131;font-weight:400'>뜨겁게</b> 나왔어 🔥", 520, 1.8)}
  {typing(780, 2.5, until=3.3)}
  {msg("bamtol", "내가 1분 만에 정리해 줄게!", 780, 3.4, mood="happy")}
""")}
''', BG))

# 2 ── 사진 공유 + 질문
S[2] = (1, page(f'''
{head("밤사이 단톡방", 2, "#F6EEE4")}
{room(2, f"""
  {msg("owl", "📷 사진", 120, .1)}
  {msg_card(bar(150, 172), 300, .4)}
  {msg("star", "0.1%p 차이인데<br>그게 그렇게 커? 🤔", 640, 1.3, side="r", mood="worried")}
  {typing(850, 2.0, until=2.7)}
  {msg("bamtol", "물가가 뜨거우면 미국이<br><b style='color:#E8590C;font-weight:400'>금리를 올릴 수도</b> 있거든!", 850, 2.8)}
""")}
''', BG))

# 3 ── 비유 설명 (1분 공부)
def row(label, w0, w1, c, note):
    b = lambda w: f'<div style="width:{w}px;height:44px;background:{c};border:4px solid {L};border-radius:22px"></div>'
    return (f'<div style="display:grid;grid-template-columns:200px 150px 50px 260px;align-items:center;font-size:30px;margin:10px 0">'
            f'<div>{label}</div>{b(w0)}<div style="text-align:center">→</div><div style="display:flex;gap:10px;align-items:center">{b(w1)}<span>{note}</span></div></div>')
compare = (f'<div style="font-size:30px;margin-bottom:6px">🍦 사람들이 서는 줄로 비유하면</div>'
           + row("은행 예금 줄", 90, 150, "#BFE3C8", "")
           + row("미래 기대주 줄", 140, 70, "#FFD9A8", ""))
S[3] = (1, page(f'''
{head("밤사이 단톡방", 3, "#F6EEE4")}
{room(3, f"""
  {msg("bamtol", "금리가 오르면 은행에만 넣어도<br>이자가 쏠쏠해지잖아?", 120, .1)}
  {msg_card(compare, 330, .9, w=720)}
  {msg("bamtol", "그래서 '나중에 클 것 같은'<br><b style='color:#E8590C;font-weight:400'>AI·반도체주</b> 줄에서 빠져나가!", 660, 1.8, mood="normal")}
  {msg("star", "아하! 그래서 기술주 많은<br>나스닥이 더 빠졌구나 💡", 900, 2.8, side="r", mood="happy")}
""")}
''', BG))

# 4 ── 한국 이야기
S[4] = (1, page(f'''
{head("밤사이 단톡방", 4, "#F6EEE4")}
{room(4, f"""
  {msg("moon", "(코스피 역) 나 벌써<br><b style='color:#2F6BD8;font-weight:400'>6일 연속</b> 내리막이야 🥲", 120, .1, mood="teary")}
  {msg_card('<div style="font-size:30px">🇰🇷 코스피 (14일)</div><div style="font-size:64px;color:#2F6BD8">6,008.81 ▼0.44%</div><div style="font-family:Noto Sans CJK KR,sans-serif;font-size:24px;color:#6B5A50">6거래일 연속 하락</div>', 340, .8)}
  {msg("star", "오늘은 뭘 봐야 해?", 640, 1.6, side="r")}
  {typing(830, 2.1, until=2.7)}
  {msg("bamtol", "① 반도체 — 미국 약세 이어지나<br>② 환율 — 원/달러 1,338원대<br>③ 기름값 — WTI 95.09달러 <span style='color:#E03131'>▲1.01%</span>", 830, 2.8)}
""")}
<div class="src a-fade" style="top:1480px;color:#B8BCD8;--d:3.0s">특정 종목 매수·매도 권유가 아닙니다 · 판단과 책임은 본인에게 · 출처: 뉴스핌, 뉴스1, 머니투데이, 파이낸셜뉴스</div>
''', BG))

# 5 ── 마무리
S[5] = (1, page(f'''
{head("밤사이 단톡방", 5, "#F6EEE4")}
{room(5, f"""
  {msg("owl", "오늘 밤엔 PPI·소매판매·<br>TSMC 실적 나와! 👀", 120, .1)}
  {msg("bamtol", "결과는 내일 아침 8시에<br>단톡에 올릴게 🌅", 330, .9, mood="happy")}
  {msg("star", "알림 설정 완료! 🔔", 540, 1.7, side="r", mood="happy")}
  {ch(mascot("bamtol", "happy", "wave"), 340, 720, 300, 2.3, "a-pop", "hop")}
""", h=1100)}
<div class="abs a-pop" style="left:0;right:0;top:1390px;--d:2.6s;text-align:center"><span style="display:inline-block;background:#FFB27F;border:5px solid {L};border-radius:999px;padding:12px 44px;font-size:46px">팔로우 @bamsai.daily</span></div>
<div class="src a-fade" style="top:1490px;color:#B8BCD8;--d:2.8s">출처: AP, 연합뉴스, 뉴스핌, 서울경제, 아시아경제 · 정보 제공용이며 투자 권유가 아닙니다</div>
''', BG))

PLAN = {1: (5.2, 1.2), 2: (5.2, 1.2), 3: (6.0, 1.2), 4: (5.6, 1.3), 5: (4.6, 1.3)}
CUES = [
 (1, .0, "dundun", .9), (1, .15, "msg", 1), (1, 1.0, "msg", .9), (1, 1.8, "msg", .9), (1, 2.5, "typing", .8), (1, 3.4, "msg", 1), (1, 3.5, "boing", .5),
 (2, .1, "msg", .9), (2, .4, "shutter", .8), (2, .6, "slidedown", .5), (2, 1.3, "msg", .9), (2, 1.4, "question", .6), (2, 2.0, "typing", .8), (2, 2.8, "msg", 1),
 (3, .1, "msg", .9), (3, .9, "pop", .8), (3, 1.0, "whoosh", .5), (3, 1.8, "msg", .9), (3, 2.8, "msg", .9), (3, 2.9, "ding", .9),
 (4, .1, "msg", .9), (4, .3, "sad", .5), (4, .8, "blip_down", 1), (4, 1.6, "msg", .9), (4, 2.1, "typing", .8), (4, 2.8, "msg", 1), (4, 2.9, "CHECK1", .6), (4, 3.1, "CHECK2", .6), (4, 3.3, "CHECK3", .6),
 (5, .1, "msg", .9), (5, .9, "msg", .9), (5, 1.7, "msg", .9), (5, 2.3, "boing", .7), (5, 2.6, "jingle", .9),
]
