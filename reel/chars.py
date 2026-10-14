"""밤사이 마스코트 v3 — 말랑 손그림풍 (밤톨이·별콩이·솜부엉·달떡이) + 소품."""
L = "#4A3838"
def st(w=3.6): return f'stroke="{L}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'
BODY = "M60 250 C50 180 70 100 150 100 C230 100 250 180 240 250 C236 272 210 277 150 277 C90 277 64 272 60 250 Z"
FILTER = ('<defs><filter id="w" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4"/>'
          '<feDisplacementMap in="SourceGraphic" scale="2.6"/></filter></defs>')

def face(mood, ey=192, sp=34, beak=False):
    xl, xr, my = 150 - sp, 150 + sp, ey + 18
    s = (f'<ellipse cx="{xl-22}" cy="{ey+14}" rx="14" ry="8" fill="#FFB7C5" opacity=".85"/>'
         f'<ellipse cx="{xr+22}" cy="{ey+14}" rx="14" ry="8" fill="#FFB7C5" opacity=".85"/>')
    dot = lambda x, rx=6.5, ry=8.5, h=2.3: (f'<ellipse cx="{x}" cy="{ey}" rx="{rx}" ry="{ry}" fill="{L}"/>'
                                            f'<circle cx="{x+2}" cy="{ey-3}" r="{h}" fill="#fff"/>')
    mouth = ""
    if mood == "normal":
        s += dot(xl) + dot(xr)
        mouth = f'<path d="M143 {my} Q150 {my+7} 157 {my}" fill="none" {st(3.2)}/>'
    elif mood == "happy":
        for x in (xl, xr):
            s += f'<path d="M{x-9} {ey+3} Q{x} {ey-8} {x+9} {ey+3}" fill="none" {st(3.6)}/>'
        mouth = f'<path d="M140 {my-3} Q150 {my+13} 160 {my-3} Z" fill="#F27A7A" {st(3)}/>'
    elif mood == "surprised":
        s += dot(xl, 8, 10, 3) + dot(xr, 8, 10, 3)
        mouth = f'<ellipse cx="150" cy="{my+3}" rx="6" ry="7.5" fill="#F27A7A" {st(3)}/>'
    elif mood == "teary":
        for x in (xl, xr):
            s += (f'<ellipse cx="{x}" cy="{ey}" rx="10" ry="12" fill="{L}"/>'
                  f'<circle cx="{x+3}" cy="{ey-4}" r="4.2" fill="#fff"/><circle cx="{x-3}" cy="{ey+5}" r="2" fill="#fff"/>')
        mouth = f'<path d="M141 {my+2} q4.5 -5 9 0 q4.5 5 9 0" fill="none" {st(3)}/>'
        s += f'<path d="M{xr+6} {ey+12} q6 10 0 16 q-6 -6 0 -16z" fill="#A9DCFF" {st(2.4)}/>'
    elif mood == "worried":
        s += dot(xl) + dot(xr)
        s += (f'<path d="M{xl-10} {ey-16} L{xl+6} {ey-20}" {st(3)}/><path d="M{xr+10} {ey-16} L{xr-6} {ey-20}" {st(3)}/>'
              f'<path d="M{xr+44} {ey-36} q7 12 0 19 q-7 -7 0 -19z" fill="#A9DCFF" {st(2.4)}/>')
        mouth = f'<path d="M141 {my+2} q4.5 -5 9 0 q4.5 5 9 0" fill="none" {st(3)}/>'
    elif mood == "sleep":
        for x in (xl, xr):
            s += f'<path d="M{x-9} {ey} Q{x} {ey+8} {x+9} {ey}" fill="none" {st(3.6)}/>'
        mouth = f'<ellipse cx="150" cy="{my+3}" rx="5" ry="4" fill="#F27A7A"/>'
    if beak and mood != "happy":
        mouth = f'<path d="M144 {ey+12} L156 {ey+12} L150 {ey+21} Z" fill="#FFB25E" {st(2.6)}/>'
    return s + mouth

def arms(col, pose):
    E = lambda cx, cy, rx, ry, r, cls="": (f'<g class="{cls}"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" {st()} '
                                          f'transform="rotate({r} {cx} {cy})"/></g>')
    if pose == "up":
        return E(54, 176, 10, 14, -30) + E(246, 176, 10, 14, 30)
    if pose == "point":
        return E(60, 226, 13, 10, -25) + E(252, 196, 16, 10, -30)
    if pose == "wave":
        return E(60, 226, 13, 10, -25) + E(248, 170, 10, 14, 25, "wave")
    if pose == "hold":
        return E(84, 236, 12, 10, 60) + E(216, 236, 12, 10, -60)
    return E(60, 226, 13, 10, -25) + E(240, 226, 13, 10, 25)

def feet(col):
    return (f'<ellipse cx="118" cy="278" rx="18" ry="10" fill="{col}" {st()}/>'
            f'<ellipse cx="182" cy="278" rx="18" ry="10" fill="{col}" {st()}/>')

def nightcap():
    return (f'<path d="M84 136 Q110 52 214 70 Q196 92 214 126 Q150 112 84 136Z" fill="#8FA2F0" {st()}/>'
            f'<circle cx="222" cy="70" r="14" fill="#fff" {st()}/>')

def mascot(kind, mood="normal", pose="down", prop="", cap=False):
    if kind == "bamtol":
        col = "#FFF3E0"
        top = (f'<path d="M62 176 C66 112 100 92 150 92 C200 92 234 112 238 176 C206 160 94 160 62 176 Z" fill="#B57D55" {st()}/>'
               f'<path d="M138 95 Q150 62 162 95" fill="#B57D55" {st()}/>'
               f'<path d="M96 124 q8 -6 16 -2 M184 120 q8 2 14 8" fill="none" stroke="#D9A57E" stroke-width="5" stroke-linecap="round"/>')
        pre, f_ = "", face(mood, 206)
    elif kind == "moon":
        col = "#F4EFFF"
        pre = (f'<path d="M150 101 Q148 88 152 80" fill="none" {st()}/>'
               f'<path d="M140 70 a16 16 0 1 0 22 -10 a12 12 0 1 1 -22 10z" fill="#FFE38A" {st(3.2)}/>')
        top, f_ = "", face(mood)
    elif kind == "owl":
        col = "#DCD5F2"
        pre = f'<path d="M84 128 Q70 92 102 108" fill="{col}" {st()}/><path d="M216 128 Q230 92 198 108" fill="{col}" {st()}/>'
        top = (f'<ellipse cx="150" cy="246" rx="48" ry="26" fill="#F8F4FF"/>'
               f'<path d="M134 104 q6 -10 12 0 q6 -10 12 0 q6 -10 12 0" fill="none" {st(3)}/>')
        f_ = face(mood, beak=True)
    else:  # star
        col = "#FFF4C2"
        pre = (f'<path d="M150 101 Q144 84 152 70" fill="none" {st()}/>'
               f'<path transform="translate(152 62)" d="M0 -14 L4 -4 L14 -3 L6 4 L9 14 L0 8 L-9 14 L-6 4 L-14 -3 L-4 -4Z" fill="#FFD84D" {st(3)}/>')
        top, f_ = "", face(mood)
    fc = "#FFC57A" if kind == "owl" else col
    capsvg = nightcap() if cap else ""
    inner = f'{feet(fc)}{pre}<path d="{BODY}" fill="{col}" {st()}/>{top}{f_}{capsvg}{prop}{arms(col, pose)}'
    return (f'<svg viewBox="30 40 240 260" xmlns="http://www.w3.org/2000/svg" overflow="visible">{FILTER}'
            f'<g filter="url(#w)">{inner}</g></svg>')

# ── 소품 (캐릭터 앞에 들고 있는 것, 캐릭터 좌표계) ──
def p_card(text1, text2):
    return (f'<g transform="rotate(-4 150 236)"><rect x="86" y="212" width="128" height="74" rx="10" fill="#fff" {st()}/>'
            f'<text x="150" y="242" text-anchor="middle" font-size="20" fill="{L}" font-family="Jua">{text1}</text>'
            f'<text x="150" y="272" text-anchor="middle" font-size="23" fill="#E8590C" font-family="Jua">{text2}</text></g>')

def p_paper(score):
    return (f'<g transform="rotate(6 150 236)"><rect x="104" y="214" width="92" height="72" rx="8" fill="#fff" {st()}/>'
            f'<path d="M118 230 h64" stroke="#E9DFD2" stroke-width="6" stroke-linecap="round"/>'
            f'<text x="150" y="274" text-anchor="middle" font-size="32" fill="#E03131" font-family="Jua">{score}</text></g>')

def p_mag():
    return (f'<circle cx="214" cy="214" r="22" fill="#E6F6FF" {st()}/><path d="M230 230 L252 252" {st(9)}/>'
            f'<path d="M204 204 q6 -8 14 -6" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>')

def p_tablet():
    return (f'<rect x="100" y="222" width="100" height="62" rx="10" fill="#3B3F6B" {st()}/>'
            f'<path d="M112 236 L134 242 L152 256 L172 262 L186 272" fill="none" stroke="#8EC5FF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')

def chip(col, mood="normal"):
    """반도체 칩 친구 (말랑 버전)."""
    pins = "".join(f'<rect x="{x}" y="88" width="12" height="20" rx="5" fill="#E9E4DA" {st(3)}/>' for x in (108, 144, 180))
    legs = (f'<path d="M122 262 q-10 18 -30 18" fill="none" {st(8)}/><path d="M178 262 q14 12 8 30" fill="none" {st(8)}/>')
    if mood == "tired":
        fc = (f'<path d="M106 172 l14 8 l-14 8 M194 172 l-14 8 l14 8" fill="none" {st(3.6)}/>'
              f'<ellipse cx="150" cy="208" rx="9" ry="7" fill="#F27A7A" {st(3)}/>'
              f'<path d="M232 140 q7 12 0 19 q-7 -7 0 -19z" fill="#A9DCFF" {st(2.4)}/>'
              f'<path d="M246 176 q6 10 0 16 q-6 -6 0 -16z" fill="#A9DCFF" {st(2.4)}/>')
    else:
        fc = (f'<ellipse cx="116" cy="178" rx="6.5" ry="8.5" fill="{L}"/><circle cx="118" cy="175" r="2.3" fill="#fff"/>'
              f'<ellipse cx="184" cy="178" rx="6.5" ry="8.5" fill="{L}"/><circle cx="186" cy="175" r="2.3" fill="#fff"/>'
              f'<path d="M104 160 L124 166 M196 160 L176 166" {st(3)}/>'
              f'<path d="M140 198 Q150 210 160 198 Z" fill="#F27A7A" {st(3)}/>')
    return (f'<svg viewBox="30 60 240 250" xmlns="http://www.w3.org/2000/svg" overflow="visible">{FILTER}<g filter="url(#w)">'
            f'{legs}{pins}<rect x="76" y="104" width="148" height="160" rx="40" fill="{col}" {st()}/>'
            f'<ellipse cx="96" cy="196" rx="13" ry="8" fill="#FFB7C5" opacity=".85"/><ellipse cx="204" cy="196" rx="13" ry="8" fill="#FFB7C5" opacity=".85"/>'
            f'{fc}<ellipse cx="72" cy="196" rx="12" ry="9" fill="{col}" {st()}/><ellipse cx="230" cy="186" rx="12" ry="9" fill="{col}" {st()}/></g></svg>')

def mini(col, mood="meh"):
    """이름 없는 구경꾼 떡."""
    f = (f'<path d="M126 196 h12 M162 196 h12" {st(3.4)}/><path d="M143 216 h14" {st(3.2)}/>' if mood == "meh" else
         f'<ellipse cx="132" cy="196" rx="6" ry="8" fill="{L}"/><ellipse cx="168" cy="196" rx="6" ry="8" fill="{L}"/>')
    return (f'<svg viewBox="30 40 240 260" xmlns="http://www.w3.org/2000/svg" overflow="visible">{FILTER}<g filter="url(#w)">'
            f'<path d="{BODY}" fill="{col}" {st()}/><ellipse cx="104" cy="212" rx="13" ry="7" fill="#FFB7C5" opacity=".8"/>'
            f'<ellipse cx="196" cy="212" rx="13" ry="7" fill="#FFB7C5" opacity=".8"/>{f}</g></svg>')
