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
	return render_template("registered.html",cid=cid)

@app.route('/registered')
def registered(name=None):
	return render_template("/templatesregistered.html",name=name)

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
			return redirect(url_for('employeeaccount', name=dealer,updatefail=False))
		else:
			print("Login Failed!")
			return render_template('employeelogin.html')
	except:
		conn.rollback()
		print("Failed to login!")
		return render_template('employeelogin.html')
		
		
@app.route('/employeeaccount')
@app.route('/employeeaccount/<name>')
def employeeaccount(name=None,updatefail=False):
	cars = None 
	#print(name)
	if name != None: 
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		comm = ''' select brand_name, model_name, current_cars from "Dealers" where "dealer_name"='%s';'''%(name)
		cur.execute(comm) 
		cars = cur.fetchall()
		#print (cars)
	return render_template('employeeaccount.html', name=name, cars = cars,updatefail=updatefail)
	
@app.route('/employeeaccount/<name>',methods=['POST'])
def employeeaccount_post(name=None):
	try:
		#fetch brand, model, and we name the dealer name so we can update....
		conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
		cur = conn.cursor()
		brand = request.form['brand']
		model = request.form['model']
		newcount = request.form['current']
		#check if brand already in, if not then add the car.
		#if the brand is already in the database then update the count. 
		#have something to print if the new inventory is too large. 
		com = '''select * from "Dealers" where "dealer_name"='%s' and "model_name"='%s' and "brand_name"='%s';'''%(name,model,brand)
		cur.execute(com)
		if cur.fetchall() !=[]:
			#actually update inventory
			com = '''update "Dealers" set "current_cars"=%s where "dealer_name"='%s' and "brand_name"='%s' and "model_name"='%s';'''%(newcount,name,brand,model)
			cur.execute(com)
			conn.commit()
			comm = ''' select brand_name, model_name, current_cars from "Dealers" where "dealer_name"='%s';'''%(name)
			cur.execute(comm) 
			cars = cur.fetchall()
			return render_template('employeeaccount.html', name=name, cars = cars, updatefail=False)
		else:
			#insert the vehicle into inventory
			did = id_generator(size=4)
			com = '''insert into "Dealers" values ('%s','%s',NULL,'%s','%s',NULL,NULL,500,%s,0);'''%(did,name,brand,model,newcount)
			cur.execute(com)
			conn.commit()
			comm = ''' select brand_name, model_name, current_cars from "Dealers" where "dealer_name"='%s';'''%(name)
			cur.execute(comm) 
			cars = cur.fetchall()
			return render_template('employeeaccount.html', name=name, cars = cars, updatefail=False)
			
	except:
		conn.rollback()
		comm = ''' select brand_name, model_name, current_cars from "Dealers" where "dealer_name"='%s';'''%(name)
		cur.execute(comm) 
		cars = cur.fetchall()
		return render_template('employeeaccount.html', name=name, cars = cars, updatefail=True)


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
	return render_template("/purchasehistory.html", name=name, cid=cid, history=history)

@app.route('/phoneUpdate', methods=['POST'])
def phoneUpdate(cid=None):
	conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
	cur = conn.cursor()
	phone = request.form['phone']
	cid = request.form['cid']
	cid=int(cid)
	command = '''update "Customers" set "phone" = '%s' where "cid"='%s';'''%(phone,cid)
	cur.execute(command)
	conn.commit()
	return render_template('account.html', name=name, cid=cid)

@app.route('/phoneUpdate', methods=['GET'])
def showphoneUpdate():
	return render_template('phoneUpdate.html')

@app.route('/addressUpdate', methods=['POST'])
def addressUpdate(cid=None):
	conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
	cur = conn.cursor()
	address = request.form['address']
	cid = request.form['cid']
	command = '''update "Customers" set "address" = '%s' where "cid"='%s';'''%(address,cid)
	cur.execute(command)
	conn.commit()
	return render_template('addressUpdate.html')

@app.route('/addressUpdate', methods=['GET'])
def showAddressUpdate():
	return render_template('addressUpdate.html')

@app.route('/salaryUpdate', methods=['POST'])
def salaryUpdate():
	conn = psycopg2.connect("dbname='project' user='postgres' host='localhost' password='root'")
	cur = conn.cursor()
	salary = request.form['salary']
	salary=float(salary)
	cid = request.form['cid']
	cid=int(cid)
	command = '''update "Customers" set "income" = '%s' where "cid"='%s';'''%(salary,cid)
	cur.execute(command)
	conn.commit()
	return render_template('salaryUpdate.html')
	
@app.route('/salaryUpdate', methods=['GET'])
def showSalaryUpdate():
	return render_template('salaryUpdate.html')
	# except:
	# 	return render_template('account.html')
	

if __name__ == "__main__":
	app.run(debug=True)