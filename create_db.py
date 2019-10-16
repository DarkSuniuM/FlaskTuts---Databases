from app import create_db

db = create_db()
cur = db.cursor()

cur.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
)''')

print("Done")
