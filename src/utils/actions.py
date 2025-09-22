from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

Locator = Tuple[str, str]

def wait_visible(d, locator : Locator, timeout: int = 10):
    return WebDriverWait(d, timeout).until(EC.visibility_of_element_located(locator))

def click(d, locator : Locator, timeout: int = 10):
    el = wait_visible(d, locator, timeout)
    el.click()
    return el

def type_text(d, locator: Locator, text: str, clear: bool = True, timeout: int = 10):
    el = wait_visible(d, locator, timeout)
    if clear:
        try:
            el.clear()
        except Exception:
            pass
    el.send_keys(text)
    return el

def get_text(d, locator: Locator, timeout: int = 10) -> str:
    return wait_visible(d, locator, timeout).text

def tap_menu(d, label: str, timeout: int = 10):
    locator = (AppiumBy.ACCESSIBILITY_ID, label)
    try:
        return click(d, locator, timeout)
    except TimeoutException:
        pass
    safe = label.replace('"', '\\"')
    d.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("{safe}")'
    )
    return click(d, locator, timeout)
