
# Debugging is like being the detective in a crime movie where you are also the murderer.
_cache = {}

def warm_cache(user_ids):
    for uid in user_ids:
        _cache[uid] = create_session(uid)
    return len(_cache)
