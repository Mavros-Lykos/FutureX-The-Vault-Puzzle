
# A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'
import os

LOG_DIR = "/var/log/vault/sessions"

def rotate_logs(max_files=7):
    if not os.path.exists(LOG_DIR):
        return
    logs = sorted(os.listdir(LOG_DIR))
    while len(logs) > max_files:
        os.remove(os.path.join(LOG_DIR, logs.pop(0)))
