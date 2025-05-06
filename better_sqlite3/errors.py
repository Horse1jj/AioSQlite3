class BetterSQLiteError(Exception):
    """Base exception for better-sqlite3."""


class DatabaseConnectionError(BetterSQLiteError):
    """Raised when a connection to the database fails."""


class QueryExecutionError(BetterSQLiteError):
    """Raised when executing a SQL query fails."""


class TransactionError(BetterSQLiteError):
    """Raised when a transaction operation fails."""


class RecordNotFoundError(BetterSQLiteError):
    """Raised when a requested record does not exist."""


class InvalidQueryError(BetterSQLiteError):
    """Raised when a malformed or unsupported query is passed."""
