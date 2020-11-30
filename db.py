import sqlite3

con = sqlite3.connect('database.db')
print("Opened database successfully");

con.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
cur = con.cursor()
cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)", ("Ivan","Ivan","Ivan","Ivan"))
con.commit()
con.close()