class aiosqlite3Error(Exception):
    """Base exception for aiosqlite3."""


class DatabaseConnectionError(aiosqlite3Error):
    """Raised when a connection to the database fails."""


class QueryExecutionError(aiosqlite3Error):
    """Raised when executing a SQL query fails."""


class TransactionError(aiosqlite3Error):
    """Raised when a transaction operation fails."""


class RecordNotFoundError(aiosqlite3Error):
    """Raised when a requested record does not exist."""


class InvalidQueryError(aiosqlite3Error):
    """Raised when a malformed or unsupported query is passed."""
