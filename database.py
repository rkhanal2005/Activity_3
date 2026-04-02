import sqlite3

def connect_db():
    conn = sqlite3.connect("database.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT role FROM users WHERE username=? AND password=?",
                   (username, password))

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    return None

def create_user(username, password, role):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username,password,role) VALUES(?,?,?)",
        (username, password, role)
    )

    conn.commit()
    conn.close()

def get_all_usernames():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()

    conn.close()

    return [u[0] for u in users]