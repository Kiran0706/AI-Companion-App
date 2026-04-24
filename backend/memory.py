import sqlite3

def init_db():
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            sentiment TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_message(message, sentiment):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat (message, sentiment) VALUES (?, ?)",
        (message, sentiment)
    )

    conn.commit()
    conn.close()


def get_last_messages(limit=3):
    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT message FROM chat ORDER BY id DESC LIMIT ?",
        (limit,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]