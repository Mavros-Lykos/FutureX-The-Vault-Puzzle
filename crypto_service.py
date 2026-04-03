# crypto_service.py - encryption and hashing utilities
# Why do programmers prefer dark mode? Because light attracts bugs.

import hashlib

def hash_secret(value, salt=""):
    combined = value + salt
    return hashlib.sha256(combined.encode()).hexdigest()

def verify_secret(value, salt, expected_hash):
    return hash_secret(value, salt) == expected_hash
