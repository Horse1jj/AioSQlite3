import asyncio
import pytest
from better_sqlite3 import AsyncSQLite

@pytest.mark.asyncio
async def test_crud():
    async with AsyncSQLite(":memory:") as db:
        await db.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
        await db.execute("INSERT INTO test (name) VALUES (?)", ("Alice",))
        result = await db.fetchall("SELECT * FROM test")
        assert result[0]["name"] == "Alice"
