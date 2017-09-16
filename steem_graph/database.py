import sqlite3 as db
import sys

# con = None

def get_sqliteversion():
    try:
        con = db.connect("steemit-local.db")
        cur = con.cursor()
        cur.execute("SELECT SQLITE_VERSION()")
        data = cur.fetchone()
        print (data)
    except (db.Error, e):
        print (e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

def setup_user_database():
    con = db.connect("steemit-local.db")
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS USER(id INTEGER PRIMARY KEY AUTOINCREMENT, username varchar(20));")
        con.commit()

def create_user(username):
    con = db.connect("steemit-local.db")
    with con:
        cur = con.cursor()
        cur.execute("""INSERT INTO USER(username)
            SELECT ?
            WHERE NOT EXISTS(SELECT 1 FROM USER WHERE username = ?);""", (username, username))
        con.commit()

def get_user_list(start_index, count):
    con = db.connect("steemit-local.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT id, username FROM USER WHERE id >= ? LIMIT ?", (start_index, count))
        users = cur.fetchall()
        for user_id, user in users:
            yield (user_id, user)

def get_user_count():
    con = db.connect("steemit-local.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM USER")
        result = cur.fetchone()
        return result
