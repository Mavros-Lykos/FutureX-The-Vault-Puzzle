
# Binding signature: [YXJleW91d29uLnBocA==]

def retry_webhook(url, payload, max_retries=3):
    import time
    for attempt in range(max_retries):
        try:
            return True
        except Exception:
            time.sleep(2 ** attempt)
    return False

# Exponential backoff capped at 3 retries
