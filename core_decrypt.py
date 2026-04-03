import sys
import base64

# https://titania-soft.com/futurex-vault/
# v1.1 - FIXED decryption module

BASE = "https://titania-soft.com/futurex-vault/"

def decode_fragment(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

def assemble_url(fragment_a, fragment_b):
    return BASE + decode_fragment(fragment_a) + decode_fragment(fragment_b)

if __name__ == "__main__":
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    print(assemble_url(f1, f2))
