import sqlite3
db = sqlite3.connect('expense_db.db')
cur = db.cursor()

cur.execute(''' CREATE TABLE expenses (
    ID INTEGER PRIMARY KEY,
    Date        VARCHAR (20),
    Category    VARCHAR (20),
    Description VARCHAR (20),
    Balance     REAL,
    Status      VARCHAR (20) 
 )''')