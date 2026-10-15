import sqlite3
import datetime
from typing import List, Dict, Any, Optional
from src import config

def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Get an SQLite connection with Row factory."""
    path = db_path or config.DB_PATH
    conn = sqlite3.connect(path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: Optional[str] = None) -> None:
    """Initialize database tables for mood entries and screening logs."""
    conn = get_connection(db_path)
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS mood_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                mood_score INTEGER NOT NULL CHECK(mood_score BETWEEN 1 AND 5),
                stress_level INTEGER NOT NULL CHECK(stress_level BETWEEN 1 AND 5),
                sleep_hours REAL NOT NULL,
                sleep_quality INTEGER NOT NULL CHECK(sleep_quality BETWEEN 1 AND 5),
                activities TEXT,
                journal_text TEXT,
                sentiment_label TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS screening_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                instrument TEXT NOT NULL,
                total_score INTEGER NOT NULL,
                max_score INTEGER NOT NULL,
                severity TEXT NOT NULL,
                safety_alert INTEGER NOT NULL DEFAULT 0
            )
        """)
    conn.close()

def save_mood_entry(
    mood_score: int,
    stress_level: int,
    sleep_hours: float,
    sleep_quality: int,
    activities: str = "",
    journal_text: str = "",
    sentiment_label: str = "",
    timestamp: Optional[str] = None,
    db_path: Optional[str] = None
) -> int:
    """Insert a new mood & wellness entry using parameterized SQL."""
    ts = timestamp or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_connection(db_path)
    with conn:
        cursor = conn.execute("""
            INSERT INTO mood_logs (
                timestamp, mood_score, stress_level, sleep_hours, sleep_quality,
                activities, journal_text, sentiment_label
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (ts, mood_score, stress_level, sleep_hours, sleep_quality, activities, journal_text, sentiment_label))
        new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_all_mood_entries(limit: int = 100, db_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieve mood entries sorted by timestamp descending."""
    conn = get_connection(db_path)
    cursor = conn.execute("""
        SELECT id, timestamp, mood_score, stress_level, sleep_hours, sleep_quality,
               activities, journal_text, sentiment_label
        FROM mood_logs
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows

def delete_mood_entry(entry_id: int, db_path: Optional[str] = None) -> bool:
    """Delete a single mood entry by ID."""
    conn = get_connection(db_path)
    with conn:
        cursor = conn.execute("DELETE FROM mood_logs WHERE id = ?", (entry_id,))
        success = cursor.rowcount > 0
    conn.close()
    return success

def delete_all_data(db_path: Optional[str] = None) -> None:
    """Wipe all user records from SQLite database."""
    conn = get_connection(db_path)
    with conn:
        conn.execute("DELETE FROM mood_logs")
        conn.execute("DELETE FROM screening_logs")
    conn.close()

def save_screening_result(
    instrument: str,
    total_score: int,
    max_score: int,
    severity: str,
    safety_alert: bool = False,
    db_path: Optional[str] = None
) -> int:
    """Optionally record a screening aggregate summary."""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_connection(db_path)
    with conn:
        cursor = conn.execute("""
            INSERT INTO screening_logs (
                timestamp, instrument, total_score, max_score, severity, safety_alert
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (ts, instrument, total_score, max_score, severity, 1 if safety_alert else 0))
        new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_screening_history(limit: int = 50, db_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieve previous screening summaries."""
    conn = get_connection(db_path)
    cursor = conn.execute("""
        SELECT id, timestamp, instrument, total_score, max_score, severity, safety_alert
        FROM screening_logs
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return rows
