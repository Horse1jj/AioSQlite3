# better-sqlite3

**An async wrapper around SQLite3 using `asyncio.to_thread` for thread-safe and aiohttp-compatible usage.**

## Features

- Async/await interface
- Works with `aiohttp` and other async frameworks
- No external dependencies
- Built-in context manager support
- error handling 

## Installation

```bash
pip install aiosqlite3
```

## Usage

```python
import aiosqlite3

async def main():
    async with aiosqlite3 ("example.db") as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        await db.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
        users = await db.fetchall("SELECT * FROM users")
        print([dict(row) for row in users])
```
