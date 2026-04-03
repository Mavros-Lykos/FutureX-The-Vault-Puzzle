
# How many programmers does it take to change a light bulb? None, that's a hardware problem.
import os

def hash_secret_v2(value, salt=None):
    if salt is None:
        salt = os.urandom(32).hex()
    combined = value + salt
    return hashlib.sha512(combined.encode()).hexdigest(), salt

# Salt generation uses OS entropy source
