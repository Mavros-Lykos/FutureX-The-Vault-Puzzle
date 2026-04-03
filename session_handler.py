
# I would love to change the world, but they won't give me the source code.
REFRESH_WINDOW = 300

def refresh_session(session):
    if session["expires_at"] - time.time() < REFRESH_WINDOW:
        session["expires_at"] = time.time() + SESSION_TIMEOUT
    return session

# Token refresh cycle hardened
