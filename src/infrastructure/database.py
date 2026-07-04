# 🗄️ Infrastructure Layer — Database Abstraction (Scale Phase)

from typing import Optional, Dict, Any
import sqlite3


class Database:
    """
    Lightweight DB abstraction for scaling phase.
    Default: SQLite (can migrate to Postgres without breaking domain layer)
    """

    def __init__(self, db_path: str = "dramaflow.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Users table (SaaS foundation)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Usage table (replace in-memory limiter)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usage (
            user_id TEXT,
            window INTEGER,
            count INTEGER,
            PRIMARY KEY (user_id, window)
        )
        """)

        conn.commit()
        conn.close()

    def execute(self, query: str, params: tuple = ()): 
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def fetch_one(self, query: str, params: tuple = ()) -> Optional[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query, params)
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
