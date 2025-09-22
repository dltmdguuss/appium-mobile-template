# Appium Python Mobile Template

초보자용 최소 템플릿입니다. **Android 실기기/에뮬레이터 + Appium 2 + pytest** 기준입니다.

## 0) 요구사항
- Python 3.9+
- Node.js 18+ (Appium 2 설치용)
- ANDROID SDK / ADB (디바이스 연결 확인용)

## 1) Appium 2 설치 (터미널/PowerShell)
```bash
# Appium 서버와 Android 드라이버
npm i -g appium@latest
appium driver install uiautomator2

# 서버 실행 (새 창에서 계속 켜두세요)
appium -a 127.0.0.1 -p 4723
```
> 참고: Appium Inspector로 요소 확인을 원하면 별도 설치가 필요합니다.

## 2) 파이썬 환경 & 의존성
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

## 3) 환경변수(.env) 설정
`.env.example`을 복사해서 값을 채웁니다.
```bash
# Windows
copy .env.example .env
# macOS/Linux
cp .env.example .env
```

필수 값:
- `APPIUM_SERVER_URL` (기본: http://127.0.0.1:4723)
- `ANDROID_UDID` (`adb devices`로 확인되는 디바이스 UDID)
- `APP_PACKAGE` / `APP_ACTIVITY` (테스트 대상 앱의 패키지/액티비티)
- (선택) `ANDROID_APP_PATH` (.apk 경로를 넣으면 설치 후 실행)

## 4) 디바이스 연결 확인
```bash
adb devices
```

## 5) 테스트 실행
```bash
pytest
```
리포트: `reports/report.html` 생성

## 6) 구조
```
appium-mobile-template/
  src/
    drivers.py
    pages/
      login_page.py
    utils/
      waits.py
  tests/
    test_login_sample.py
  .env.example
  pytest.ini
  requirements.txt
  README.md
```

## 7) 다음 단계
- `src/pages/login_page.py`에 실제 앱의 접근자(Accessibility ID, resource-id 등)를 반영하세요.
- 요소 식별은 **Appium Inspector** 또는 **adb uiautomatorviewer**(구버전)로 확인 가능합니다.
- 안정성을 위해 **고유 AID(data-test-id 등)**를 앱 쪽에 추가해두면 좋아요.
