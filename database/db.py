import os
import asyncpg

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_URL = f"postgresql://postgres:secret@{DB_HOST}:5432/bot_db"

async def init_db():
    async with asyncpg.connect(DB_URL) as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY,
                user_name TEXT,
                name TEXT
            )
        """)