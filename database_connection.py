import sqlite3

conn = sqlite3.connect("employee.db")

cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee(
               id INTEGER PRIMARY KEY,
               name VARCHAR(50),
               age INTEGER,
               salary INTEGER)
               ''')

cursor.execute("INSERT INTO employee (id,name,age,salary) VALUES (?, ?, ?,?)", (2,"Ram", 15, "56000"))
conn.commit() # used in CUD

cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()
for row in rows:
    print(row)

