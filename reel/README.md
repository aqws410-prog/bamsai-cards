# 밤사이 릴스 도구

- `make_reel.py` — 장면 파일 → 영상(프레임 렌더 + 효과음·테마곡 믹스 + 음량 -14 LUFS)
- `lib.py` — 공통 스타일과 부품(컷, 말풍선, 내레이션, 효과음 글자, 별, 달, 아이콘). 인스타 안전 영역 자동 배치
- `chars.py` — 캐릭터 4종(밤톨이·별콩이·솜부엉·달떡이)과 소품
- `audio.py` — 밤사이 테마곡과 효과음 21종(모두 코드로 합성한 오리지널)
- `formats/<형식>/scenes.py` — 이야기 형식별 기준 예시(qa·news·quiz·chat·detective). 매일 형식을 돌려 쓴다
- `history.md` — 날짜별로 쓴 형식·비유 기록(반복 방지)
- `fonts/Jua-Regular.ttf` — 주아체(SIL Open Font License, OFL.txt 동봉)

규칙은 저장소 루트의 CLAUDE.md "릴스" 절을 따른다.
