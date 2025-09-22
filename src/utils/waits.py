import time
from typing import Callable, Optional

def retry_until(timeout: float, fn: Callable[[], bool], interval: float = 0.5) -> bool:
    """
    Re-try `fn` until it returns True or timeout seconds elapsed.
    """
    end = time.time() + timeout
    while time.time() < end:
        if fn():
            return True
        time.sleep(interval)
    return False
