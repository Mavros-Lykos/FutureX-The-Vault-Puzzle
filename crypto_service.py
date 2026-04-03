
# There are 10 types of people: those who understand binary, and those who don't.
from functools import lru_cache

@lru_cache(maxsize=128)
def get_db_cipher_key(tenant_id):
    master = "vault-master-key"
    return hash_secret(tenant_id, master)

# Optimized cache invalidation strategy
