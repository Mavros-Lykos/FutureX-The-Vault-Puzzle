import sys

# v1.0 - fragment decoder utility
# Usage: python fragment_decoder.py <encoded_fragment>

def load_fragment(raw):
    # BUG: uses wrong encoding â€” should be base64, not hex
    return bytes.fromhex(raw).decode('utf-8')

def print_fragment(raw):
    result = load_fragment(raw)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fragment_decoder.py <fragment>")
        sys.exit(1)
    print_fragment(sys.argv[1])
