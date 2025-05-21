import sqlite3
import json


def adapt_array(array):
    """Convert Python list to JSON string."""
    return json.dumps(array)


def convert_array(text):
    """Convert JSON string to Python list."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return []


def array(connection: sqlite3.Connection):
    """
    Register array adapters and converters for the connection.
    Should be called right after connecting to the database.
    """
    sqlite3.register_adapter(list, adapt_array)
    sqlite3.register_converter("ARRAY", convert_array)

    connection.create_function("json_array_length", 1, lambda x: len(json.loads(x)) if x else 0)
    connection.create_function("json_array_contains", 2, lambda x, val: val in json.loads(x) if x else False)
    connection.create_function("json_array_get", 2, lambda x, i: json.loads(x)[int(i)] if x else None)
