import os
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv, find_dotenv

def go_home(d, timeout: int = 5):
    load_dotenv(find_dotenv(), override=False)

    pkg = os.getenv("APP_PACKAGE", "io.appium.android.apis")
    act = os.getenv("APP_ACTIVITY", ".ApiDemos")

    # 1) 일반 방법 시도
    try:
        d.start_activity(pkg, act)  # 일부 환경에서만 제공
    except AttributeError:
        # 2) 폴백: Appium 2+ 공통 Mobile 명령
        d.execute_script("mobile: startActivity", {
            "appPackage": pkg,
            "appActivity": act
        })

    WebDriverWait(d, timeout).until(
        lambda x: len(x.find_elements(AppiumBy.ACCESSIBILITY_ID, "Views")) > 0
    )

def _at_root(d) -> bool:
    return len(d.find_elements(AppiumBy.ACCESSIBILITY_ID, "Views")) > 0

def back_to_root(d, tries: int = 7):
    for _ in range(tries):
        if _at_root(d):
            return
        d.press_keycode(4)