import sqlite3


db_connector = sqlite3.connect('SQL/SQLite/my_learning.db')
cursor = db_connector.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')


db_connector.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())