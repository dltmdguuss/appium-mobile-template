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

def test_views_controls_edit(driver):
    d = driver

    tap_menu(d, "Views")
    tap_menu(d, "Controls")
    tap_menu(d, "1. Light Theme")
    edit = (AppiumBy.ID, "io.appium.android.apis:id/edit")
    type_text(d, edit, "hellow appium")

    shown = get_text(d, edit) or d.find_elemnet(edit).get_attribute("value")
    assert "hellow appium" in shown

def test_views_controls_spinner(driver):
    d = driver

    tap_menu(d, "Views")
    tap_menu(d, "Controls")
    tap_menu(d, "1. Light Theme")
    spinner = (AppiumBy.ID, "io.appium.android.apis:id/spinner1")
    click(d, spinner)
    Jupiter = (AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().resourceId("android:id/text1").text("Jupiter")')
    click(d, Jupiter)

    container = d.find_element(*spinner)
    text_el = container.find_element(AppiumBy.CLASS_NAME, "android.widget.TextView")
    shown = text_el.text or text_el.get_attribute("text")
    assert shown == "Jupiter"

def test_app_alert_ok_cancel(driver):
    d = driver

    tap_menu(d, "App")
    tap_menu(d, "Alert Dialogs")
    btn = (AppiumBy.ACCESSIBILITY_ID,"OK Cancel dialog with a message")
    click(d, btn)
    alert = (AppiumBy.ID,"android:id/parentPanel")

    okbtn = (AppiumBy.ID,"android:id/button1")
    click(d, okbtn)

    assert not d.find_elements(*alert)

