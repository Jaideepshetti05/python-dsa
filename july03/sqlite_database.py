import sqlite3

conn=sqlite3.connect("demo.db")

cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER,name TEXT)")

cur.execute("INSERT INTO student VALUES(1,'Alice')")

conn.commit()

for row in cur.execute("SELECT * FROM student"):
    print(row)

conn.close()