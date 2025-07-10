# 🤖 Python 자동화 실습 (with pyautogui)

이 프로젝트는 Python의 `pyautogui`, `pyperclip`, `shutil`, `os`, `logging` 등 다양한 라이브러리를 활용해  
**마우스/키보드 자동화, 이미지 인식, 윈도우 조작, 파일 시스템 관리** 등을 연습한 실습 코드 모음입니다.  

---

## 📌 주요 실습 내용

### 🖱️ 1. 마우스 & 키보드 제어
- `moveTo`, `move`, `click`, `doubleClick`, `drag`, `scroll` 등 다양한 마우스 제어
- `write`, `press`, `hotkey`, `keyDown/Up` 등 키보드 자동 입력

### 🎯 2. 이미지 인식 자동화
- `locateOnScreen`, `locateAllOnScreen`으로 이미지 탐지
- `confidence`, `region`, `grayscale` 옵션으로 정확도 및 속도 조정
- 일정 시간까지 대기하면서 이미지 탐색 (`Timeout`, `while` 루프)

### 🖼️ 3. 화면 캡쳐 & 픽셀 분석
- `screenshot()`을 통한 스크린샷 저장
- `pixel`, `pixelMatchesColor`로 특정 좌표의 색상 판별

### 🧩 4. 윈도우 창 조작
- `getWindowsWithTitle`로 창 핸들링
- 창 활성화, 최대화, 원복, 닫기 등 자동화 대상 창 제어

### 📝 5. 입력 자동화 응용 (그림판 예제)
- Win + R → 그림판 실행 → 버튼 인식 후 클릭 → 텍스트 자동 입력 → 종료
- 이미지 기반 버튼 탐색 (`btn_text.png`, `btn_brush.png` 등 필요)

### 📂 6. 파일 & 폴더 자동화
- `os`, `shutil` 활용: 폴더 생성, 삭제, 파일 복사, 이동, 경로 탐색
- `fnmatch`, `os.walk()`을 활용한 파일 검색 자동화

### 🧠 7. 로그 기록
- `logging`을 사용해 터미널과 파일 모두에 로그 남기기
- 로그 포맷: `[시간] [로그레벨] 메시지`

---

## 🔒 8. 팝업 및 보안 입력
- `alert`, `confirm`, `prompt`, `password` 함수로 GUI 팝업 다루기
- 암호 입력도 가능

---

## 🖼️ 예시: 그림판 자동화 실행 흐름

```plaintext
1. Win + R → mspaint 입력 → 실행
2. '텍스트 도구' 버튼 인식 및 클릭
3. 텍스트 영역 클릭 후 "참 잘했어요" 자동 입력
4. 5초 대기 후 프로그램 종료 (저장 안 함)
