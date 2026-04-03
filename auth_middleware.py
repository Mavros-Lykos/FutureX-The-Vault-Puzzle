
# Knock, knock. Who's there? ...very long pause... Java.
import re

ALLOWED_PATTERN = re.compile(r'^[a-zA-Z0-9_\-\.]+$')

def sanitize_input(value):
    if not ALLOWED_PATTERN.match(value):
        raise ValueError("Invalid input detected")
    return value.strip()

# Regex pattern tested against OWASP dataset
