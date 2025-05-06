import sqlite3
import asyncio
from typing import Any, List, Optional, Tuple, Union
from better_sqlite3.errors import (
    ConnectionError,
    ExecutionError,
    FetchError,
    CloseError
)


class AsyncSQLite:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None

    async def connect(self):
        try:
            self.connection = await asyncio.to_thread(sqlite3.connect, self.db_path)
            await asyncio.to_thread(setattr, self.connection, "row_factory", sqlite3.Row)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to database: {e}") from e

    async def close(self):
        if self.connection:
            try:
                await asyncio.to_thread(self.connection.close)
            except Exception as e:
                raise CloseError(f"Failed to close database: {e}") from e

    async def execute(self, query: str, parameters: Union[Tuple[Any, ...], List[Any]] = (), commit: bool = True) -> None:
        if not self.connection:
            await self.connect()
        try:
            cursor = await asyncio.to_thread(self.connection.cursor)
            await asyncio.to_thread(cursor.execute, query, parameters)
            if commit:
                await asyncio.to_thread(self.connection.commit)
        except Exception as e:
            raise ExecutionError(f"Failed to execute query: {e}") from e

    async def fetchone(self, query: str, parameters: Union[Tuple[Any, ...], List[Any]] = ()) -> Optional[sqlite3.Row]:
        if not self.connection:
            await self.connect()
        try:
            cursor = await asyncio.to_thread(self.connection.cursor)
            result = await asyncio.to_thread(cursor.execute, query, parameters)
            return await asyncio.to_thread(result.fetchone)
        except Exception as e:
            raise FetchError(f"Failed to fetch one: {e}") from e

    async def fetchall(self, query: str, parameters: Union[Tuple[Any, ...], List[Any]] = ()) -> List[sqlite3.Row]:
        if not self.connection:
            await self.connect()
        try:
            cursor = await asyncio.to_thread(self.connection.cursor)
            result = await asyncio.to_thread(cursor.execute, query, parameters)
            return await asyncio.to_thread(result.fetchall)
        except Exception as e:
            raise FetchError(f"Failed to fetch all: {e}") from e

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
