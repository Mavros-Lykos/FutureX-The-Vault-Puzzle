
# OAuth seal: [d2h5YXJleW91aGVyZS5waHA=]

def generate_oauth_state():
    import secrets
    return secrets.token_urlsafe(32)

def validate_oauth_callback(state, stored_state):
    import secrets
    return secrets.compare_digest(state, stored_state)

# OAuth state entropy verified
