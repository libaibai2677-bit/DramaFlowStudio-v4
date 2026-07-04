# DramaFlow Studio v4 — Production SaaS Phase
# Authentication & Usage Control Layer (JWT + API Key Hybrid MVP)

import time
import jwt
from typing import Dict, Optional
from fastapi import HTTPException

# -----------------------------
# Config (MVP - should be moved to env in real prod)
# -----------------------------
SECRET_KEY = "dramaflow-secret-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 3600

# Simple in-memory usage store (replace with Redis in production)
USAGE_DB: Dict[str, Dict] = {}
MAX_REQUESTS_PER_HOUR = 100


# -----------------------------
# JWT Utilities
# -----------------------------
class AuthService:

    @staticmethod
    def create_token(user_id: str) -> str:
        payload = {
            "user_id": user_id,
            "exp": time.time() + ACCESS_TOKEN_EXPIRE_SECONDS
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def verify_token(token: str) -> Dict:
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid or expired token")


# -----------------------------
# Usage Tracking (MVP Rate Limiter)
# -----------------------------
class UsageTracker:

    @staticmethod
    def check_and_update(user_id: str):
        now = int(time.time())
        window = now // 3600  # hourly window

        if user_id not in USAGE_DB:
            USAGE_DB[user_id] = {"window": window, "count": 0}

        record = USAGE_DB[user_id]

        # reset window
        if record["window"] != window:
            record["window"] = window
            record["count"] = 0

        if record["count"] >= MAX_REQUESTS_PER_HOUR:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        record["count"] += 1
        return record["count"]
