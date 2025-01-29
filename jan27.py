#Using the SQLite3 to interact with a database
import sqlite3 

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)''')

#Insert data
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("Laptop", 999.99))
connection.commit()

#ftech data
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

connection.close()