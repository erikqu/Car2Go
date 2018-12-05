import sys
import psycopg2
import pprint

'''
enter the correct info and I can define the schema for ya
'''

dbname = 'project'
host = 'localhost'
user = 'postgres'
password = 'root'
conn = psycopg2.connect(host=host, dbname = dbname, user = user, password = password)
cursor = conn.cursor()
print ("Connected to " + dbname + "!")
print ("Any numbers that come up are error codes.")
### begin commands

###read ME
### constraints to be added in later....

cleantables = 0
if cleantables:
    command = '''
                drop table Orders;
                drop table Supply;
                drop table Plant_supply;
                drop table Vehicles;
                drop table Model_parts;
                drop table Models;
                drop table Parts;
                drop table Brands;
                drop table Dealers;
                drop table Options;
                drop table Plants;
                drop table Customers;
                drop table Suppliers;

                '''
    cursor.execute(command)
    conn.commit()

try:
    command = '''CREATE TABLE Options (
		  oid char(4) NOT NULL,
		  color varchar(10),
		  engine varchar(10),
		  transmission varchar(10),
		  PRIMARY KEY (oid)
		);
                '''
    cursor.execute(command)
    conn.commit()
except:
    "Options failed! This is the first table.  Clean tables?"

try:
    command = '''CREATE TABLE Customers (
		  cid char(4) NOT NULL,
		  name varchar(30),
		  address varchar(30),
		  phone char(10),
		  gender char(1),
		  income numeric(10,2),
		  PRIMARY KEY (cid)
		); '''
    cursor.execute(command)
except:
    print ("Customers failed!")

try:
    command =    '''
            CREATE TABLE Brands (
		  bid char(4) NOT NULL,
		  brand_name varchar(20),
		  PRIMARY KEY (bid)
		); '''
    cursor.execute(command)
except:
    print("Brands failed!")

try:

    command=    '''
                CREATE TABLE Models (
		  mid char(4) NOT NULL,
		  model_name varchar(20),
		  brand_name varchar(20),
		  style varchar(10),
		  bid char(4) NOT NULL,
		  PRIMARY KEY (mid),
		  FOREIGN KEY (bid) REFERENCES Brands (bid)
		);
                '''
    cursor.execute(command)
except:
    print("Models failed!")
try:
    command=            '''
                CREATE TABLE Suppliers (
		  sid char(4) NOT NULL,
		  model_name varchar(20),
		  PRIMARY KEY (sid)
		);
                '''
    cursor.execute(command)
except:
    print ("Suppliers failed!")

'''in reality either the first one fails or not.'''

command=            '''
            CREATE TABLE Plants (
		  pid char(4) NOT NULL,
		  model_name varchar(20),
		  PRIMARY KEY (pid)
		);'''
cursor.execute(command)
command=            '''
	    CREATE TABLE Parts (
		  partId char(4) NOT NULL,
		  part_name varchar(20),
		  PRIMARY KEY (partId)
		);
            '''
cursor.execute(command)
command=            '''
            CREATE TABLE Supply (
			  sid char(4),
			  partId char(4),
			  PRIMARY KEY (sid, partId),
			  FOREIGN KEY (sid) REFERENCES Suppliers (sid),
			  FOREIGN KEY (partId) REFERENCES Parts (partId)
			);
'''

cursor.execute(command)
command=            '''
	    CREATE TABLE Plant_supply (
			  pid char(4) NOT NULL,
			  partId char(4) NOT NULL,
			  PRIMARY KEY (pid, partId),
			  FOREIGN KEY (pid) REFERENCES Plants (pid),
			  FOREIGN KEY (partId) REFERENCES Parts (partId)
			);
'''
cursor.execute(command)
command=            '''
            CREATE TABLE Dealers (
			  did char(4) NOT NULL,
			  dealer_name varchar(20),
			  purchase_date date,
			  brand_name varchar(10),
			  model_name varchar(10),
			  price numeric(12,2),
			  color varchar(10),
			  max_cars int,
			  current_cars int,
			  total_sold int,
			  CHECK (current_cars <= max_cars),
			  PRIMARY KEY (did)
			);
'''
cursor.execute(command)

command=            '''
	    CREATE TABLE Vehicles (
			  vin varchar(17) NOT NULL,
			  pid char(4) NOT NULL,
			  oid char(4) NOT NULL,
			  bid char(4) NOT NULL,
			  mid char(4) NOT NULL,
			  did char(4) NOT NULL,
			  PRIMARY KEY (vin),
			  FOREIGN KEY (pid) REFERENCES Plants (pid),
			  FOREIGN KEY (oid) REFERENCES Options (oid),
			  FOREIGN KEY (bid) REFERENCES Brands (bid),
			  FOREIGN KEY (mid) REFERENCES Models (mid),
			  FOREIGN KEY (did) REFERENCES Dealers (did)
			);
'''
cursor.execute(command)
command=            '''
	    CREATE TABLE Orders (
		  did char(4) NOT NULL,
		  cid char(4) NOT NULL,
		  vin varchar(17) NOT NULL,
		  PRIMARY KEY (did, cid, vin),
		  FOREIGN KEY (did) REFERENCES Dealers (did),
		  FOREIGN KEY (cid) REFERENCES Customers (cid),
		  FOREIGN KEY (vin) REFERENCES Vehicles (vin)
		);
'''
cursor.execute(command)
try:
    command =       '''
            CREATE TABLE Model_parts (
		  partId char(4),
		  mid char(4),
		  PRIMARY KEY (partId, mid),
		  FOREIGN KEY (partId) REFERENCES Parts (partId),
		  FOREIGN KEY (mid) REFERENCES Models (mid)
		);'''
    cursor.execute(command)
except:
    print("Model_parts Failed!")


#this line commits the actual schema!
conn.commit()
print ("Done!")
