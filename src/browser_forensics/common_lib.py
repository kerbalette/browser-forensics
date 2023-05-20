import sqlite3

def fetch_db(db, command):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(command)
    return cursor.fetchall()