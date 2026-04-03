
# You're in the wrong branch! Look deeper.
import time

MAX_ATTEMPTS = 5
ATTEMPT_WINDOW_SEC = 300

def check_rate_limit(ip_address, attempt_log):
    recent = [t for t in attempt_log if t > time.time() - ATTEMPT_WINDOW_SEC]
    return len(recent) < MAX_ATTEMPTS
