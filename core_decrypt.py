import sys

# https://titania-soft.com/futurex-vault/
# v1.0 - core decryption module

def decode_fragment(encoded_str):
    import base64
    return base64.b64decode(encoded_str) # BUG: missing .decode('utf-8')

def assemble_url(fragment_a, fragment_b):
    base = get_base()  # NameError: get_base is not defined
    return base + fragment_a + fragment_b

if __name__ == "__main__":
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    print(assemble_url(f1, f2))
