#!/usr/bin/env python3
"""밤사이 사운드: 전용 테마곡 + 효과음 라이브러리 (모두 코드로 합성한 오리지널)."""
import numpy as np, wave, pathlib
from scipy.signal import butter, lfilter

SR = 44100
rng = np.random.default_rng(7)

def t_(d): return np.arange(int(d * SR)) / SR
def env(n, a=.005, r=.2, curve=6):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-curve * t / max(r, 1e-4) * .2)
    return e
def adsr(n, a=.01, d=.1, s=.6, r=.1):
    e = np.ones(n) * s
    A, D, R = int(a*SR), int(d*SR), int(r*SR)
    e[:A] = np.linspace(0, 1, A) if A else e[:A]
    e[A:A+D] = np.linspace(1, s, len(e[A:A+D]))
    if R: e[-R:] *= np.linspace(1, 0, len(e[-R:]))
    return e
def lp(x, f, o=2): b, a = butter(o, f / (SR/2), 'low'); return lfilter(b, a, x)
def hp(x, f, o=2): b, a = butter(o, f / (SR/2), 'high'); return lfilter(b, a, x)
def bp(x, lo, hi, o=2): b, a = butter(o, [lo/(SR/2), hi/(SR/2)], 'band'); return lfilter(b, a, x)
def mtof(m): return 440 * 2 ** ((m - 69) / 12)
def sweep(f0, f1, d, shape="exp"):
    t = t_(d)
    f = f0 * (f1/f0) ** (t/d) if shape == "exp" else f0 + (f1-f0) * t/d
    return np.sin(2*np.pi*np.cumsum(f)/SR)
def norm(x, p=.9): m = np.max(np.abs(x)) or 1; return x / m * p

# ─────────────── 효과음 ───────────────
def sfx_pop():        # 말풍선 뿅
    d = .12; s = sweep(380, 1250, d) * np.exp(-t_(d)*28)
    return norm(s + .3*sweep(760, 2500, d)*np.exp(-t_(d)*40), .55)
def sfx_tick():       # 내레이션 툭
    d = .08; return norm(np.sin(2*np.pi*1800*t_(d)) * np.exp(-t_(d)*70), .35)
def sfx_whoosh(d=.45):
    n = rng.standard_normal(int(d*SR)); t = t_(d)
    sh = np.sin(np.pi * t/d) ** 2
    out = np.zeros_like(n)
    for i, (lo, hi) in enumerate([(300, 900), (700, 2000), (1500, 4000)]):
        out += bp(n, lo, hi) * np.sin(np.pi * np.clip(t/d*1.2 - i*.08, 0, 1)) ** 2
    return norm(out * sh, .32)
def sfx_boing():      # 통통
    d = .35; t = t_(d)
    f = 180 + 220 * np.exp(-t*14) + 25*np.sin(2*np.pi*14*t)*np.exp(-t*6)
    return norm(np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t*9), .5)
def sfx_dundun():     # 두둥!
    out = np.zeros(int(1.1*SR))
    for k, (st, m) in enumerate([(0, 40), (.28, 39)]):
        d = .75 if k else .3; t = t_(d)
        tone = sum(np.sin(2*np.pi*mtof(m+o)*t)*g for o, g in [(0, 1), (12, .5), (19, .25), (24, .2)])
        boom = np.sin(2*np.pi*np.cumsum(70*np.exp(-t*8)+45)/SR)
        s = (tone*.6 + boom) * np.exp(-t*(5 if k else 12))
        i = int(st*SR); out[i:i+len(s)] += s
    return norm(lp(out, 2500), .75)
def sfx_sparkle():    # 짠! 반짝
    out = np.zeros(int(1.0*SR))
    for i, m in enumerate([84, 88, 91, 96, 100]):
        d = .6; t = t_(d)
        s = (np.sin(2*np.pi*mtof(m)*t) + .3*np.sin(2*np.pi*mtof(m)*3.01*t)) * np.exp(-t*7)
        j = int(i*.06*SR); out[j:j+len(s)] += s
    return norm(out, .45)
def sfx_slidedown():  # 주르륵
    d = 1.0; t = t_(d)
    f = 1300 * (260/1300) ** (t/d) * (1 + .03*np.sin(2*np.pi*7*t))
    s = np.sin(2*np.pi*np.cumsum(f)/SR) + .25*np.sin(2*np.pi*np.cumsum(2*f)/SR)
    return norm(s * adsr(len(t), .03, .1, .9, .25), .4)
def sfx_hmm():        # 에이~ (구경꾼 웅성)
    d = .9; t = t_(d); out = np.zeros(len(t))
    for f0, ph in [(210, 0), (260, 1.3), (180, 2.1)]:
        f = f0 * (1 - .18*t/d) * (1 + .02*np.sin(2*np.pi*5*t + ph))
        out += sum(np.sin(2*np.pi*np.cumsum(f*h)/SR)/h for h in (1, 2, 3))
    return norm(lp(out, 1400) * adsr(len(t), .08, .1, .8, .3), .32)
def sfx_yay():        # 야호! 신나는 아르페지오
    out = np.zeros(int(.9*SR))
    for i, m in enumerate([72, 76, 79, 84]):
        d = .45; t = t_(d)
        s = (np.sin(2*np.pi*mtof(m)*t) + .4*np.sin(4*np.pi*mtof(m)*t)) * np.exp(-t*8)
        j = int(i*.08*SR); out[j:j+len(s)] += s
    return norm(out, .45)
def sfx_sad():        # 시무룩 (와와와~)
    out = np.zeros(int(1.6*SR))
    for i, (m, d) in enumerate([(62, .3), (61, .3), (60, .3), (59, .7)]):
        t = t_(d); f = mtof(m) * (1 + (.03*np.sin(2*np.pi*6*t) if i == 3 else 0))
        s = sum(np.sin(2*np.pi*np.cumsum(np.ones_like(t)*f*h)/SR) * g for h, g in [(1, 1), (2, .5), (3, .35), (4, .2)])
        wah = .5 + .5*np.sin(np.pi*np.minimum(t/.25, 1))
        s = lp(s * wah, 1800) * adsr(len(t), .02, .05, .9, .08)
        j = int(i*.3*SR); out[j:j+len(s)] += s
    return norm(out, .38)
def sfx_ding():       # 띵! (깨달음)
    d = 1.0; t = t_(d)
    s = sum(np.sin(2*np.pi*1568*r*t)*g*np.exp(-t*k) for r, g, k in [(1, 1, 4), (2.76, .4, 7), (5.4, .2, 10)])
    return norm(s, .4)
def sfx_steps(d=3.0, rate=7.0):  # 다다다 발소리
    out = np.zeros(int(d*SR)); step = int(SR/rate)
    for k in range(0, len(out) - 3000, step):
        n = int(.05*SR); t = t_(.05)
        s = (np.sin(2*np.pi*(240 if (k//step) % 2 else 200)*t) + .6*rng.standard_normal(n)) * np.exp(-t*90)
        out[k:k+n] += lp(s, 1600)
    return norm(out, .3)
def sfx_pant():       # 헉헉
    out = np.zeros(int(1.0*SR))
    for i in range(2):
        d = .28; n = rng.standard_normal(int(d*SR))
        s = bp(n, 900, 3200) * np.sin(np.pi*t_(d)/d)**1.5
        j = int(i*.42*SR); out[j:j+len(s)] += s
    return norm(out, .3)
def sfx_thud():       # 뚝!
    d = .5; t = t_(d)
    s = np.sin(2*np.pi*np.cumsum(140*np.exp(-t*10)+50)/SR) * np.exp(-t*9)
    s += lp(rng.standard_normal(len(t)), 900) * np.exp(-t*40) * .6
    return norm(s, .7)
def sfx_blip_down():  # 숫자 카드 (하락 뿅)
    d = .22; return norm(sweep(900, 420, d) * np.exp(-t_(d)*12), .4)
def sfx_question():   # 뾰잉?
    d = .4; t = t_(d)
    f = 500 + 500*(t/d)**2
    return norm(np.sin(2*np.pi*np.cumsum(f)/SR) * adsr(len(t), .01, .05, .8, .1), .4)
def sfx_check(m=79):  # 체크 띵
    d = .5; t = t_(d)
    s = (np.sin(2*np.pi*mtof(m)*t) + .5*np.sin(2*np.pi*mtof(m+7)*t)) * np.exp(-t*9)
    return norm(s, .42)
def sfx_snore(d=2.2):  # 쿨쿨
    out = np.zeros(int(d*SR)); cyc = 1.1
    for k in np.arange(0, d - .5, cyc):
        n = int(.55*SR); tt = t_(.55)
        f = 95 + 20*np.sin(np.pi*tt/.55)
        s = (np.sign(np.sin(2*np.pi*np.cumsum(f)/SR)) * .3 + rng.standard_normal(n)*.5)
        s = lp(s, 700) * np.sin(np.pi*tt/.55)**2
        j = int(k*SR); out[j:j+n] += s
    return norm(out, .2)
def sfx_yawn():       # 하암~
    d = 1.1; t = t_(d)
    f = 300 * (1 + .4*np.sin(np.pi*np.minimum(t/.35, 1))) * np.where(t > .35, (1 - .45*(t-.35)/(d-.35)), 1)
    s = sum(np.sin(2*np.pi*np.cumsum(f*h)/SR)/h**1.2 for h in range(1, 7))
    s = bp(s, 250, 1800) + .15*bp(rng.standard_normal(len(t)), 800, 2500)
    return norm(s * adsr(len(t), .1, .1, .8, .35), .3)
def sfx_sunrise():    # 해 뜨는 반짝 상승
    d = 1.8; t = t_(d); out = np.zeros(len(t))
    for i, m in enumerate([72, 76, 79, 83, 86, 88, 91]):
        dd = 1.0; tt = t_(dd); s = np.sin(2*np.pi*mtof(m)*tt) * np.exp(-tt*4)
        j = int(i*.15*SR); out[j:j+len(s)] += s[:len(out)-j]
    pad = sum(np.sin(2*np.pi*mtof(m)*t) for m in (60, 64, 67)) * np.sin(np.pi*t/d)**2 * .3
    return norm(out + pad, .4)
def sfx_jingle():     # 팔로우 마무리 징글
    out = np.zeros(int(1.4*SR))
    for st, m, d in [(0, 84, .18), (.14, 88, .18), (.28, 91, .9)]:
        t = t_(d); s = (np.sin(2*np.pi*mtof(m)*t) + .35*np.sin(2*np.pi*mtof(m)*2*t)) * np.exp(-t*(6 if d > .5 else 12))
        j = int(st*SR); out[j:j+len(s)] += s
    return norm(out, .5)

def sfx_news():        # 뉴스 시그널 (빰-빠밤!)
    out = np.zeros(int(1.3*SR))
    for st, ms, d in [(0, (67, 71, 74), .16), (.18, (67, 71, 74), .12), (.34, (72, 76, 79, 84), .9)]:
        t = t_(d); s = np.zeros(len(t))
        for m in ms:
            f = mtof(m); s += sum(np.sin(2*np.pi*f*h*t)/h**1.1 for h in range(1, 7))
        s = lp(s, 4200) * adsr(len(t), .01, .08, .7, .12)
        j = int(st*SR); out[j:j+len(s)] += s
    return norm(out, .55)
def sfx_correct():     # 딩동댕
    out = np.zeros(int(1.2*SR))
    for i, m in enumerate([72, 76, 79]):
        d = .7; t = t_(d); s = (np.sin(2*np.pi*mtof(m)*t) + .3*np.sin(2*np.pi*mtof(m)*2*t)) * np.exp(-t*5)
        j = int(i*.17*SR); out[j:j+len(s)] += s[:len(out)-j]
    return norm(out, .5)
def sfx_wrong():       # 삐빅 (오답)
    d = .45; t = t_(d)
    s = np.sign(np.sin(2*np.pi*150*t)) * .5 + np.sign(np.sin(2*np.pi*157*t)) * .5
    s *= (np.sin(2*np.pi*7*t) > -.3)
    return norm(lp(s, 1800) * adsr(len(t), .005, .05, .9, .05), .35)
def sfx_msg():         # 메신저 알림 띵동
    out = np.zeros(int(.5*SR))
    for st, m in [(0, 88), (.09, 93)]:
        d = .35; t = t_(d); s = np.sin(2*np.pi*mtof(m)*t) * np.exp(-t*14)
        j = int(st*SR); out[j:j+len(s)] += s[:len(out)-j]
    return norm(out, .4)
def sfx_typing(d=.8):  # 타닥타닥
    out = np.zeros(int(d*SR))
    for k in np.arange(0, d - .05, .085):
        n = int(.025*SR); s = hp(rng.standard_normal(n), 2500) * np.exp(-t_(.025)*220)
        j = int((k + rng.uniform(0, .02))*SR); out[j:j+n] += s * rng.uniform(.5, 1)
    return norm(out, .25)
def sfx_drumroll(d=1.2):  # 두구두구
    out = np.zeros(int(d*SR)); t0 = t_(d)
    for k in np.arange(0, d, .045):
        n = int(.06*SR); tt = t_(.06)
        s = (np.sin(2*np.pi*190*tt) * .5 + bp(rng.standard_normal(n), 200, 3000)) * np.exp(-tt*50)
        j = int(k*SR); out[j:j+n] += s[:len(out)-j] * (.4 + .6*k/d)
    return norm(out, .4)
def sfx_reveal():      # 짜잔! (공개)
    d = 1.0; t = t_(d)
    cym = hp(rng.standard_normal(len(t)), 5000) * np.exp(-t*4)
    ch = sum(np.sin(2*np.pi*mtof(m)*t) for m in (60, 64, 67, 72)) * np.exp(-t*3)
    return norm(cym*.5 + ch*.5, .55)
def sfx_shutter():     # 찰칵
    out = np.zeros(int(.25*SR))
    for st in (0, .07):
        n = int(.04*SR); s = bp(rng.standard_normal(n), 1500, 6000) * np.exp(-t_(.04)*120)
        j = int(st*SR); out[j:j+n] += s
    return norm(out, .45)
def sfx_tension():     # 띠용띠용 (긴장)
    d = .9; t = t_(d)
    f = 220 * (1 + .06*np.sin(2*np.pi*9*t))
    s = sum(np.sin(2*np.pi*np.cumsum(f*h)/SR)/h for h in (1, 2, 3))
    return norm(lp(s, 1500) * adsr(len(t), .05, .1, .8, .2), .3)
def sfx_rain():        # 빗소리 (짧게)
    d = 1.2; n = rng.standard_normal(int(d*SR))
    return norm(bp(n, 1200, 6000) * np.sin(np.pi*t_(d)/d)**.6, .22)

def sfx_beep():        # 삐-삐- (병원 심박 모니터, 병원 진료 플롯 시그니처)
    out = np.zeros(int(.9*SR))
    for st in (0, .42):
        d = .16; t = t_(d)
        s = (np.sin(2*np.pi*1000*t) + .25*np.sin(2*np.pi*2000*t)) * adsr(len(t), .004, .02, .85, .03)
        j = int(st*SR); out[j:j+len(s)] += s
    return norm(out, .32)

def sfx_thunder():     # 우르릉 쾅! (일기예보 플롯 — 번개)
    d = 1.3; t = t_(d); n = rng.standard_normal(len(t))
    crack = hp(n, 1800) * np.exp(-t*28) * .9
    rumble = lp(n, 160, 3) * (np.exp(-t*2.2) * (1 - np.exp(-t*30)))
    rumble *= 1 + .5*np.sin(2*np.pi*5*t)
    return norm(crack + rumble*3.5, .55)
def sfx_forecast():    # 띵-띵-띠링 (일기예보 플롯 시그니처 차임)
    out = np.zeros(int(.95*SR))
    for st, m in ((0, 84), (.16, 88), (.32, 91), (.32, 96)):
        d = .55; t = t_(d); f = mtof(m)
        s = (np.sin(2*np.pi*f*t) + .3*np.sin(2*np.pi*2*f*t)) * env(len(t), .003, d, 5)
        j = int(st*SR); out[j:j+len(s)] += s
    return norm(out, .38)

def sfx_whistle():     # 삐익-삑! 호루라기 (스포츠 중계 플롯 시그니처)
    out = np.zeros(int(.75*SR))
    for st, d in ((0, .34), (.42, .2)):
        t = t_(d); f = 2900 * (1 + .035*np.sin(2*np.pi*38*t))
        s = (np.sin(2*np.pi*np.cumsum(f)/SR) + .3*bp(rng.standard_normal(len(t)), 2500, 4200)) * adsr(len(t), .01, .03, .9, .04)
        j = int(st*SR); out[j:j+len(s)] += s
    return norm(out, .3)
def sfx_cheer():       # 와아아~ 관중 함성 (스포츠 중계 플롯)
    d = 1.4; t = t_(d); n = rng.standard_normal(len(t))
    crowd = bp(n, 350, 2400, 2) * (1 + .35*np.sin(2*np.pi*3.3*t) * np.sin(2*np.pi*.9*t))
    sh = np.minimum(1, t/.15) * np.exp(-np.maximum(0, t-.5)*2.2)
    return norm(crowd * sh, .3)

SFX = {k[4:]: v for k, v in globals().items() if k.startswith("sfx_")}

# ─────────────── 밤사이 테마 (오리지널) ───────────────
BPM = 96; BEAT = 60 / BPM
def musicbox(m, d):
    t = t_(d); f = mtof(m)
    s = (np.sin(2*np.pi*f*t) + .25*np.sin(2*np.pi*f*2.01*t)*np.exp(-t*6) + .12*np.sin(2*np.pi*f*3*t)*np.exp(-t*9))
    return s * np.minimum(1, t/.004) * np.exp(-t*3.2)
def epiano(ms, d):
    t = t_(d); s = np.zeros(len(t))
    for m in ms:
        f = mtof(m); s += np.sin(2*np.pi*f*t + .6*np.sin(2*np.pi*f*t)*np.exp(-t*3))
    return lp(s * adsr(len(t), .01, .4, .45, .3), 2200)
def bass(m, d):
    t = t_(d); return np.sin(2*np.pi*mtof(m)*t) * adsr(len(t), .01, .15, .7, .08)
def kick():
    d = .25; t = t_(d); return np.sin(2*np.pi*np.cumsum(110*np.exp(-t*30)+48)/SR) * np.exp(-t*14)
def shaker():
    d = .07; return hp(rng.standard_normal(int(d*SR)), 6000) * np.exp(-t_(d)*60)
def snap():
    d = .12; return bp(rng.standard_normal(int(d*SR)), 1500, 5000) * np.exp(-t_(d)*35)

# 진행: Fmaj7 – Em7 – Dm7 – C(add9) | Bbmaj7 – Am7 – Gm7 – C7sus  (각 1마디)
CH = [([53], [65, 69, 72, 76]), ([52], [64, 67, 71, 74]), ([50], [62, 65, 69, 72]), ([48], [64, 67, 72, 74]),
      ([46], [62, 65, 69, 70]), ([45], [64, 67, 69, 72]), ([43], [62, 65, 67, 70]), ([48], [65, 67, 70, 72])]
# 멜로디 (8분음표 단위, None=쉼표) — 밤사이 모티프: 도-레-파… 하늘이 밝아지는 느낌
MEL = [[81, None, 79, 77, None, 76, 77, None], [79, None, None, 76, 74, None, 72, None],
       [74, None, 77, 81, None, 79, 77, None], [76, None, None, None, 74, 76, 79, None],
       [77, None, 74, 70, None, 72, 74, None], [76, None, 72, 69, None, None, 72, 74],
       [74, None, 70, 67, None, 72, 74, 77], [79, None, None, 77, 76, None, None, None]]

def theme(total):
    out = np.zeros(int((total + 3) * SR)); bar = 4 * BEAT; nb = int(total / bar) + 1
    def put(x, st, g):
        i = int(st * SR); j = min(len(out), i + len(x)); out[i:j] += x[:j-i] * g
    for b in range(nb):
        bl, chord = CH[b % 8]; t0 = b * bar
        put(epiano(chord, bar * .98), t0, .10)
        for k, m in enumerate([bl[0], bl[0], bl[0]+7, bl[0]+12]):
            put(bass(m - 12 + 12, BEAT * .9), t0 + k*BEAT, .22)
        for k in range(4):
            put(kick(), t0 + k*BEAT, .30 if k in (0, 2) else .0)
            if k in (1, 3): put(snap(), t0 + k*BEAT, .06)
        for k in range(8):
            put(shaker(), t0 + k*BEAT/2 + (.02 if k % 2 else 0), .05 if k % 2 else .03)
        if b >= 1:  # 첫 마디는 반주만
            for k, m in enumerate(MEL[b % 8]):
                if m: put(musicbox(m, 1.2), t0 + k*BEAT/2 + (.012 if k % 2 else 0), .16)
    out = lp(out, 7000)
    # 페이드 인·아웃
    n = int(total * SR); out = out[:n]
    fi, fo = int(.8*SR), int(2.5*SR)
    out[:fi] *= np.linspace(0, 1, fi); out[-fo:] *= np.linspace(1, 0, fo)
    return out

def write(path, x):
    x = np.clip(x, -1, 1); st = np.stack([x, x], 1)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    import json, sys
    out = pathlib.Path(sys.argv[1]); out.mkdir(exist_ok=True)
    (out / "sfx").mkdir(exist_ok=True)
    for k, fn in SFX.items():
        write(out / "sfx" / f"{k}.wav", fn())
    loop = theme(8 * 4 * BEAT * 2)  # 2바퀴(약 40초) 루프용 샘플
    write(out / "bamsai_theme.wav", loop)
    print("sfx:", ", ".join(SFX))
