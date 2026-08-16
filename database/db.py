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
async def add_user(user_id: int, user_name: str, name: str):
    async with asyncpg.connect(DB_URL) as conn:
        await conn.execute("""
            INSERT INTO users (id, user_name, name)
            VALUES ($1, $2, $3)
            ON CONFLICT (id) DO NOTHING
        """, user_id, user_name, name)    