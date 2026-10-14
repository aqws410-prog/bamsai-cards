# bamsai-cards

인스타그램 **밤사이 (@bamsai.daily)** 카드 이미지 저장소.
매일 아침 8시(KST) 발행되는 카드뉴스 원본과 이미지가 `posts/날짜/`에 쌓입니다.

- 제작 규칙: [CLAUDE.md](CLAUDE.md)
- 기준 디자인: `template/example/`
- 렌더링: `python3 render.py posts/YYYY-MM-DD --sheet /tmp/sheet.jpg`
