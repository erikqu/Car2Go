from flask import Flask, render_template, request,redirect, url_for
import random 
import psycopg2
import string
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

app=Flask(__name__)

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
			return redirect(url_for('account'))
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
def account():
	return render_template('account.html')
	
@app.route('/employeelogin')
def employeelogin():
	return render_template('employeelogin.html')

@app.route('/purchasehistory', methods=['POST'])
def purchasehistory():
	try:
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		name = request.form['name']
		cid = request.form['cid']
		command = '''select "color", brand_name", "model_name" from "Customers" natural join "Order" natural join "Vehicles" natural join "Brands" natural join "Models" natural join "Options" where "name"='%s' and "cid"='%s';'''%(name,cid)
		cur.execute(command)
		conn.commit()
	except:
		conn.rollback()
		print("No purchase history")
	return render_template("purchasehistory.html")

