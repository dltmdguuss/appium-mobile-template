import os
import pytest
from dotenv import load_dotenv
from src.drivers import make_android_driver
from src.utils.nav import back_to_root

@pytest.fixture(scope="session", autouse=True)
def load_env():
    # Load .env before any tests
    load_dotenv()

@pytest.fixture(scope="session")
def driver():
    d = make_android_driver()
    yield d
    d.quit()

@pytest.fixture(autouse=True)
def _before_each(driver, request):
    if request.node.get_closest_marker("no_home"):
        yield
        return
    back_to_root(driver)   # ← 홈 복귀 (ADB 호출 없음)
    yield