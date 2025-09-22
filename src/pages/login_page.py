from appium.webdriver.common.appiumby import AppiumBy

class LoginPage:
    # ===== 샘플 접근자(예시) =====
    EMAIL = (AppiumBy.ACCESSIBILITY_ID, "email")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "password")
    SIGNIN = (AppiumBy.ACCESSIBILITY_ID, "signin")
    WELCOME = (AppiumBy.ACCESSIBILITY_ID, "welcome")

    def __init__(self, driver):
        self.d = driver

    def input_email(self, text: str):
        self.d.find_element(*self.EMAIL).send_keys(text)

    def input_password(self, text: str):
        self.d.find_element(*self.PASSWORD).send_keys(text)

    def tap_signin(self):
        self.d.find_element(*self.SIGNIN).click()

    def is_welcome_visible(self) -> bool:
        try:
            return self.d.find_element(*self.WELCOME).is_displayed()
        except Exception:
            return False
