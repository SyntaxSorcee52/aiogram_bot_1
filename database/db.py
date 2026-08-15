import aiosqlite

DB_NAME = 'bot.db'

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("PRAGMA journal_mode=WAL;")
        await db.execute("""
            CREATE TABLE IF NOT EXSIST users (
                id INTEGER PRIMARY KEY,
                user_name TEXT,
                name TEXT,

            )
""")
        await db.commit()