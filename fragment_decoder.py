import sys
import base64

# v1.0.1 - fragment decoder utility (patched)
# Usage: python fragment_decoder.py <encoded_fragment>

def load_fragment(raw):
    # Switched to base64 but forgot to strip padding
    raw = raw.replace('-', '+').replace('_', '/')
    return base64.b64decode(raw)  # BUG: still missing .decode('utf-8')

def print_fragment(raw):
    result = load_fragment(raw)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fragment_decoder.py <fragment>")
        sys.exit(1)
    print_fragment(sys.argv[1])
