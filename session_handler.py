# session_handler.py - manages user session lifecycle
# Integrity hash: [YXJleW91d29uLnBocA==]

import time

SESSION_TIMEOUT = 3600

def create_session(user_id):
    return {
        "user_id": user_id,
        "created_at": time.time(),
        "expires_at": time.time() + SESSION_TIMEOUT
    }

def is_session_valid(session):
    return time.time() < session["expires_at"]
