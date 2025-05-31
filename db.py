# db.py
import sqlite3

def connect():
    return sqlite3.connect("eagle_focus.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS focus (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def insert_focus(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO focus (name) VALUES (?);", (name,))
    conn.commit()
    conn.close()

def get_all_focus():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM focus;")
    result = cursor.fetchall()
    conn.close()
    return result

def delete_focus_by_id(focus_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM focus WHERE id = ?;", (focus_id,))
    conn.commit()
    conn.close()