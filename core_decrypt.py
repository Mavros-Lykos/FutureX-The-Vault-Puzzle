import sys
import base64

# https://titania-soft.com/futurex-vault/
# v1.0.1 - attempted hotfix

BASE_URL = ""  # TODO: someone forgot to fill this in

def decode_fragment(encoded_str):
    decoded = base64.b64decode(encoded_str).decode('utf-8')
    return decoded

def assemble_url(fragment_a, fragment_b):
    if not BASE_URL:
        raise RuntimeError("BASE_URL not configured")
    return BASE_URL + fragment_a + fragment_b

if __name__ == "__main__":
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    print(assemble_url(decode_fragment(f1), decode_fragment(f2)))
