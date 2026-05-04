"""
database.py — SQLite Persistence Layer
Manages search history and bookmarked repositories.
"""

import sqlite3
import json
from datetime import datetime
from config import DATABASE_PATH


def _get_conn():
    """Create and return a new database connection."""
    return sqlite3.connect(DATABASE_PATH)


def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = _get_conn()
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS searches (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            query       TEXT    NOT NULL,
            domain      TEXT    NOT NULL,
            timestamp   TEXT    NOT NULL,
            results_json TEXT   NOT NULL,
            ai_insights TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS bookmarks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_name   TEXT    NOT NULL,
            repo_url    TEXT    NOT NULL,
            stars       INTEGER DEFAULT 0,
            language    TEXT    DEFAULT 'Unknown',
            description TEXT,
            added_at    TEXT    NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("[DB] Database initialized successfully.")


def save_search(query: str, domain: str, results: list, ai_insights: str) -> int:
    """Persist a search and its results. Returns the new row ID."""
    conn = _get_conn()
    c = conn.cursor()
    c.execute(
        'INSERT INTO searches (query, domain, timestamp, results_json, ai_insights) VALUES (?,?,?,?,?)',
        (query, domain, datetime.now().strftime('%Y-%m-%d %H:%M'), json.dumps(results), ai_insights)
    )
    conn.commit()
    row_id = c.lastrowid
    conn.close()
    return row_id


def get_recent_searches(limit: int = 10) -> list:
    """Fetch the most recent searches ordered by newest first."""
    conn = _get_conn()
    c = conn.cursor()
    c.execute(
        'SELECT id, query, domain, timestamp FROM searches ORDER BY timestamp DESC LIMIT ?',
        (limit,)
    )
    rows = c.fetchall()
    conn.close()
    return [{'id': r[0], 'query': r[1], 'domain': r[2], 'timestamp': r[3]} for r in rows]


def get_search_by_id(search_id: int) -> dict | None:
    """Retrieve a single search record by its ID."""
    conn = _get_conn()
    c = conn.cursor()
    c.execute('SELECT * FROM searches WHERE id = ?', (search_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0], 'query': row[1], 'domain': row[2],
            'timestamp': row[3], 'results': json.loads(row[4]), 'ai_insights': row[5]
        }
    return None


def add_bookmark(repo_name: str, repo_url: str, stars: int,
                 language: str, description: str):
    """Save a repository to the bookmarks table."""
    conn = _get_conn()
    c = conn.cursor()
    c.execute(
        'INSERT INTO bookmarks (repo_name, repo_url, stars, language, description, added_at) VALUES (?,?,?,?,?,?)',
        (repo_name, repo_url, stars, language, description,
         datetime.now().strftime('%Y-%m-%d %H:%M'))
    )
    conn.commit()
    conn.close()


def get_bookmarks() -> list:
    """Retrieve all bookmarked repositories."""
    conn = _get_conn()
    c = conn.cursor()
    c.execute('SELECT * FROM bookmarks ORDER BY added_at DESC')
    rows = c.fetchall()
    conn.close()
    return [
        {'id': r[0], 'repo_name': r[1], 'repo_url': r[2],
         'stars': r[3], 'language': r[4], 'description': r[5], 'added_at': r[6]}
        for r in rows
    ]


def delete_bookmark(bookmark_id: int):
    """Remove a bookmark by ID."""
    conn = _get_conn()
    c = conn.cursor()
    c.execute('DELETE FROM bookmarks WHERE id = ?', (bookmark_id,))
    conn.commit()
    conn.close()
