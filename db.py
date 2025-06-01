import sqlite3
from datetime import datetime

def connect():
    return sqlite3.connect("/Users/danielzunarelli/data/eagle_focus.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # Tabela de Focus (nomes únicos)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS focus (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """)

    # Tabela de sessões de foco
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS focus_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            focus_name TEXT NOT NULL,
            duration INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

def insert_focus(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO focus (name) VALUES (?);", (name,))
    conn.commit()
    conn.close()

def get_all_focus_total_time():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT f.name, 
               COALESCE(SUM(fs.duration), 0) as total_duration
        FROM focus f
        LEFT JOIN focus_sessions fs ON f.name = fs.focus_name
        GROUP BY f.name;
    """)
    result = cursor.fetchall()
    conn.close()
    return result

def delete_focus_by_name(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM focus WHERE name = ?;", (name,))
    cursor.execute("DELETE FROM focus_sessions WHERE focus_name = ?;", (name,))
    conn.commit()
    conn.close()

def insert_focus_session(name, seconds):
    conn = connect()
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO focus_sessions (focus_name, duration, timestamp) VALUES (?, ?, ?);", (name, seconds, timestamp))
    conn.commit()
    conn.close()

def reset_focus_time(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM focus_sessions WHERE focus_name = ?;", (name,))
    conn.commit()
    conn.close()