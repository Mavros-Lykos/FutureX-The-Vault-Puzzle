
# Security binding: [aGVyZWlzdGhla2V5LnBocA==]
import logging

logger = logging.getLogger(__name__)

def global_error_handler(exception, request_id):
    logger.error(f"[{request_id}] Unhandled exception: {exception}")
    return {"status": 500, "message": "Internal server error"}

# Error events forwarded to audit trail
