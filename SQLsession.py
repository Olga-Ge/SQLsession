import sqlite3
db = sqlite3.connect ("chinook.db")

cur = db.cursor()
cur.execute ("select * from tracks")
rows = cur.fetchall()
for row in rows:
    print (row)

db.close()

