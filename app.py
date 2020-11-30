from flask import Flask, request, render_template
import sqlite3 as sql


app = Flask(__name__)
con = sql.connect('database.db')
print("Opened database successfully");

con.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
	return 'COPYRIGHT Ruslan Isaev @ AIU 2020'


@app.route('/enternew')
def new_student():
   return render_template('student.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	msg = ""
	if request.method == 'POST':
		try:
			nm = request.form['nm']
			addr = request.form['add']
			city = request.form['city']
			pin = request.form['pin']
			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)", (nm,addr,city,pin))
				con.commit()
			msg = "Record successfully added"
		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("result.html", msg=msg)
			con.close()


@app.route('/list')
def list():
	con = sql.connect("database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from students")
	rows = cur.fetchall();
	return render_template("list.html", rows=rows)