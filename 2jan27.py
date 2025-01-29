import sqlite3

connection= sqlite3.connect("store.db")
cursor= connection.cursor()

#Create a table for book
cursor.execute('''CREATE TABLE IF NOT EXISTS Book(
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               author TEXT NOT NULL,
               price REAL NOT NULL)
               ''')

#Insert data
cursor.execute("INSERT INTO Book (title, author, price) VALUES (?,?,?)", ("Animal Farm", "George Orwell", 999.99))
connection.commit()

cursor.execute("INSERT INTO Book (title, author, price) VALUES (?,?,?)", ("Pride and Prejudice", "Jane Austin", 1597.88))
connection.commit()

cursor.execute("INSERT INTO Book (title, author, price) VALUES (?,?,?)", ("And Then There Were None", "Agatha Christie", 999.99))
connection.commit()

#Fetch data
cursor.execute("SELECT * FROM Book")
for row in cursor.fetchall():
    print(row)

connection.close()

#Using SQLAlchemy for database interaction
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base= declarative_base()

class Books(Base):
    __tablename__ = 'Book'
    id= Column(Integer, primary_key=True)
    title= Column(String, nullable=False)
    author= Column(String, nullable=False)
    price= Column(Float, nullable=False)

#Create engine and session
engine= create_engine('sqlite:///store.db')
Base.metadata.create_all(engine)
Session= sessionmaker(bind=engine)
session= Session()

#Add a new book
new_book= Books(title="War and Peace", author= "Leo Tolstoy", price=1289.86)
session.add(new_book)
new_book= Books(title="The Metamorphosis", author= "Franz Kafka", price=1690.86)
session.add(new_book)
new_book= Books(title="Adventures of Huckleberry Finn", author= "Mark Twain", price=999.86)
session.add(new_book)
session.commit()

#Query products
for book in session.query(Books):
    print(book.title, book.author, book.price) 