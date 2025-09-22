# src/drivers.py
import os
from appium import webdriver
from dotenv import load_dotenv, find_dotenv
from appium.options.android import UiAutomator2Options  # ★ 추가

def _to_bool(val: str, default: bool = True) -> bool:
    if val is None:
        return default
    return str(val).strip().lower() in {"1","true","yes","y","on"}

def make_android_driver():
    """
    Create and return an Android driver using env vars from .env
    """
    # .env 로드
    load_dotenv(find_dotenv(), override=True)
    server = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

    # 기본 캡스
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": os.getenv("ANDROID_DEVICE_NAME", "Android"),
        "udid": os.getenv("ANDROID_UDID"),
        "newCommandTimeout": int(os.getenv("NEW_COMMAND_TIMEOUT", "180")),
        "noReset": _to_bool(os.getenv("NO_RESET", "true"), True),
        "autoGrantPermissions": True,
    }

    # 비어있지 않을 때만 추가 (깔끔)
    pkg = os.getenv("APP_PACKAGE")
    act = os.getenv("APP_ACTIVITY")
    if pkg: caps["appPackage"] = pkg
    if act: caps["appActivity"] = act

    app_path = os.getenv("ANDROID_APP_PATH")
    if app_path and app_path.strip():
        caps["app"] = app_path.strip()

    chromedir = os.getenv("CHROMEDRIVER_DIR")
    if chromedir and chromedir.strip():
        caps["chromedriverExecutableDir"] = chromedir.strip()

    # ★ Appium 4.x 방식: options 사용
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(server, options=options)
    return driver