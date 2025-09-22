# tests/test_basic01.py
from appium.webdriver.common.appiumby import AppiumBy
from src.utils.actions import tap_menu, click, type_text, get_text

def test_views_controls_toggle_checkbox(driver):
    d = driver

    # "Views" → "Controls" → "1. Light Theme" 화면으로 이동
    tap_menu(d, "Views")
    tap_menu(d, "Controls")
    tap_menu(d, "1. Light Theme")

    # 체크박스 토글 검증
    cb = d.find_element(AppiumBy.ID, "io.appium.android.apis:id/check1")
    before = cb.get_attribute("checked")
    cb.click()
    after = cb.get_attribute("checked")

    assert before != after, "체크박스 상태가 토글되어야 합니다."
