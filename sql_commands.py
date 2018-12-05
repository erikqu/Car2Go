# This file contains a list of all SQL commands used to running this program. 

# Lets look at all the commands it took to create the tables in sql

drop_command = '''
                drop table "Model_parts";
                drop table "Plants";
                drop table "Options";
                drop table "Customers";
                drop table "Models";
                drop table "Suppliers";
                drop table "Supply";
                drop table "Plant_supply";
                drop table "Orders" ;
                drop table "Parts";
                drop table "Brands";
                drop table "Dealers";
                drop table "Vehicles";

                '''
dealers =    '''CREATE TABLE "Dealers" (
              "did" char(4) NOT NULL,
              "dealer_name" varchar(20),
              "date" date,
              "brand_name" varchar(10),
              "model_name" varchar(10),
              "price" numeric(12,2),
              "color" varchar(10),
              "max_cars" int,
              "current_cars" int,
              "total_sold" int,
              PRIMARY KEY ("did"),
			  check (current_cars <= max_cars)
            );'''

model_parts = '''CREATE TABLE "Model_parts" (
                  "partId" char(4),
                  "mid" char(4)
                );
                '''
plants = '''CREATE TABLE "Plants" (
                  "pid" char(4) NOT NULL,
                  "model_name" varchar(20),
                  PRIMARY KEY ("pid")
                ); '''

Options =    '''
            CREATE TABLE "Options" (
              "oid" char(4) NOT NULL,
              "color" varchar(10),
              "engine" varchar(10),
              "transmission" varchar(10),
              PRIMARY KEY ("oid")
            ); '''
        
customer = '''
                CREATE TABLE "Customers" (
                  "cid" char(4) NOT NULL,
                  "name" varchar(30),
                  "address" varchar(30),
                  "phone" char(10),
                  "gender" char(1),
                  "income" numeric(10,2),
                  PRIMARY KEY ("cid")
                );
                '''
models =  '''
                CREATE TABLE "Models" (
                  "mid" char(4) NOT NULL,
                  "model_name" varchar(20),
                  "brand_name" varchar(20),
                  "style" varchar(10),
                  "bid" char(4) NOT NULL,
                  PRIMARY KEY ("mid")
                );
                '''
supplier =            '''
            CREATE TABLE "Suppliers" (
              "sid" char(4) NOT NULL,
              "model_name" varchar(20),
              PRIMARY KEY ("sid")
            );'''

plant_supply =            '''
            CREATE TABLE "Plant_supply" (
              "pid" char(4) NOT NULL,
              "partId" char(4) NOT NULL
            );'''

orders = '''CREATE TABLE "Orders" (
              "did" char(4) NOT NULL,
              "cid" char(4) NOT NULL,
              "vin" varchar(17) NOT NULL
            );'''

parts =            '''CREATE TABLE "Parts" (
              "partId" char(4) NOT NULL,
              "part_name" varchar(20),
              PRIMARY KEY ("partId")
            );'''
        
brands =  '''CREATE TABLE "Brands" (
              "bid" char(4) NOT NULL,
              "brand_name" varchar(20),
              PRIMARY KEY ("bid")
            );'''

vehicles =       '''
            CREATE TABLE "Vehicles" (
              "vin" varchar(17) NOT NULL,
              "pid" char(4),
              "oid" char(4) NOT NULL,
              "bid" char(4) NOT NULL,
              "mid" char(4) NOT NULL,
              "did" char(4),
              PRIMARY KEY ("vin")
            );'''


@app.route('/phoneUpdate', methods=['POST'])
def phoneUpdate(cid=None):
	conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='sumanand'")
	cur = conn.cursor()
	phone = request.form['phone']
	cid = request.form['cid']
	cid=int(cid)
	command = '''update "Customers" set "phone" = '%s' where "cid"=%s;'''%(phone,cid)
	cur.execute(command)
	conn.commit()
	return render_template('account.html', name=name, cid=cid)

@app.route('/phoneUpdate', methods=['GET'])
def showphoneUpdate():
	return render_template('phoneUpdate.html')

@app.route('/addressUpdate', methods=['POST'])
def addressUpdate(cid=None):
	conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='sumanand'")
	cur = conn.cursor()
	address = request.form['address']
	cid = request.form['cid']
	cid=int(cid)
	command = '''update "Customers" set "address" = '%s' where "cid"=%s;'''%(address,cid)
	cur.execute(command)
	conn.commit()
	return render_template('addressUpdate.html')

@app.route('/addressUpdate', methods=['GET'])
def showAddressUpdate():
	return render_template('addressUpdate.html')

@app.route('/salaryUpdate', methods=['POST'])
def salaryUpdate():
	conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='sumanand'")
	cur = conn.cursor()
	salary = request.form['salary']
	salary=float(salary)
	cid = request.form['cid']
	cid=int(cid)
	command = '''update "Customers" set "income" = CAST('%s' as NUMERIC(8,2) where "cid"=%s;'''%(salary,cid)
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