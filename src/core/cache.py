# DramaFlow Studio v4 - Simple Cache Layer (Phase 3)
# Provides in-memory + lightweight dedup caching for image search

import time
import hashlib
from typing import Any, Dict, Optional


class CacheItem:
    def __init__(self, value: Any, ttl: int):
        self.value = value
        self.expire_at = time.time() + ttl

    def is_expired(self) -> bool:
        return time.time() > self.expire_at


class SimpleCache:
    """
    Lightweight in-memory cache for MVP+.

    Features:
    - TTL-based expiration
    - Key normalization
    - Basic dedup support
    """

    def __init__(self):
        self._store: Dict[str, CacheItem] = {}

    def _normalize_key(self, key: str) -> str:
        key = key.strip().lower()
        return hashlib.md5(key.encode("utf-8")).hexdigest()

    def set(self, key: str, value: Any, ttl: int = 300):
        norm_key = self._normalize_key(key)
        self._store[norm_key] = CacheItem(value, ttl)

    def get(self, key: str) -> Optional[Any]:
        norm_key = self._normalize_key(key)
        item = self._store.get(norm_key)

        if not item:
            return None

        if item.is_expired():
            del self._store[norm_key]
            return None

        return item.value

    def exists(self, key: str) -> bool:
        return self.get(key) is not None

    def clear(self):
        self._store.clear()

    def cleanup(self):
        """Remove expired items."""
        keys_to_delete = [k for k, v in self._store.items() if v.is_expired()]
        for k in keys_to_delete:
            del self._store[k]
