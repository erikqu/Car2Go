from flask import Flask, render_template, request,redirect, url_for
import random 
import psycopg2
import string
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

app=Flask(__name__)
global empdid
@app.route('/')
def indexLogin():
    return render_template('index.html')

	
@app.route('/', methods=['POST'])
def indexLogin_POST():
	try:
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		name = request.form['name']
		cid = request.form['cid'] 
		#print('''select * from "Customers" where 'name'='%s' and 'cid'='%s';'''%(name,cid))
		#COMMANDS ARE TO BE OF THIS FORM '''select * from "Customers" where "name"='erikq';'''
		command = '''select * from "Customers" where "name"='%s' and "cid"='%s';'''%(name,cid)
		cur.execute(command)
		if cur.rowcount is not 0:
			return redirect(url_for('account', name=name, cid=cid))
		else:
			print("Login Failed!")
			return render_template('index.html')
	except:
		conn.rollback()
		print("Failed to login!")
		return render_template('index.html')
	
@app.route('/register')
def register():
    return render_template('register.html')
	
	
@app.route('/register', methods=['POST'])
def register_post():
	try:
		#print ("Registering!")
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		name = request.form['name']
		address = request.form['address']
		phone = request.form['phone']
		gender = request.form['gender']
		income = request.form['income']
		cid =  id_generator(size=4)
		phone = int(phone) 
		income = float(income) 
		#print("('%s','%s','%s',%d,'%s',%.2f);"%(cid,name,address,phone,gender,income))
		cur.execute('''insert into "Customers" values ('%s','%s','%s',%d,'%s',%.2f);'''%(cid,name,address,phone,gender,income))
		conn.commit()
	except:
		conn.rollback()
		print("Cannot register!")
	return render_template("registered.html")

@app.route('/registered')
def registered():
	return render_template("registered.html")

@app.route('/account')
@app.route('/account/<name>/<cid>')
def account(name=None, cid=None):
	return render_template('account.html', name=name, cid=cid)
	
@app.route('/employeelogin')
def employeelogin():
	return render_template('employeelogin.html')
	
@app.route('/employeelogin', methods=['POST'])
def employeelogin_POST():
	try:
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		dealer = request.form['name']
		did = request.form['did']
		#print('''select * from "Dealers" where "dealer_name"='%s' and "did"='%s';'''%(dealer,did))
		command = '''select * from "Dealers" where "dealer_name"='%s' and "did"='%s';'''%(dealer,did)
		cur.execute(command)
		if cur.rowcount is not 0:
			global empdid
			empdid = did
			return redirect(url_for('employeeaccount', name=dealer))
		else:
			print("Login Failed!")
			return render_template('employeelogin.html')
	except:
		conn.rollback()
		print("Failed to login!")
		return render_template('employeelogin.html')
		
		
@app.route('/employeeaccount')
@app.route('/employeeaccount/<name>')
def employeeaccount(name=None):
	cars = None 
	#print(name)
	if name != None: 
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		comm = ''' select brand_name, model_name, current_cars from "Dealers" where "dealer_name"='%s';'''%(name)
		cur.execute(comm) 
		cars = cur.fetchall()
		#print (cars)
	return render_template('employeeaccount.html', name=name, cars = cars)

@app.route('/purchasehistory/<name>/<cid>')
def purchasehistory(name=None, cid=None):
	if name != None and cid != None:
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		#name = request.form['name']
		#cid = request.form['cid']
		command = '''select "color", "brand_name", "model_name", "price" 
		from "Customers" natural join "Orders" natural join "Vehicles" natural join "Dealers"
		where "name"='%s' and "cid"='%s';'''%(name,cid)
		#tab="<table style='border:1px solid black'>"
		cur.execute(command)
		history=cur.fetchall()
	return render_template("purchasehistory.html", name=name, cid=cid, history=history)

