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
    cursor.execute('''CREATE OR REPLACE FUNCTION drop_all ()
   RETURNS VOID  AS
   $$
   DECLARE rec RECORD;
   BEGIN
       -- Get all the schemas
        FOR rec IN
        select distinct schemaname
         from pg_catalog.pg_tables
         -- You can exclude the schema which you don't want to drop by adding another condition here
         where schemaname not like 'pg_catalog'
           LOOP
             EXECUTE 'DROP SCHEMA ' || rec.schemaname || ' CASCADE';
           END LOOP;
           RETURN;
       END;
       $$ LANGUAGE plpgsql;

    select drop_all();''')

try:
    command = '''CREATE TABLE "Model_parts" (
                  "partId" char(4),
                  "mid" char(4)
                );
                '''
    cursor.execute(command)
except:
    "Model_parts failed! This is the first table.  Clean tables?"

try:
    command = '''CREATE TABLE "Plants" (
                  "pid" char(4),
                  "model_name" varchar(20),
                  PRIMARY KEY ("pid")
                ); '''
    cursor.execute(command)
except:
    print ("Plants failed!")

try:
    command =    '''
            CREATE TABLE "Options" (
              "oid" char(4),
              "color" varchar(10),
              "engine" varchar(10),
              "transmission" varchar(10),
              PRIMARY KEY ("oid")
            ); '''
    cursor.execute(command)
except:
    print("Options failed!")

try:

    command=    '''
                CREATE TABLE "Customers" (
                  "cid" char(4),
                  "name" varchar(30),
                  "address" varchar(30),
                  "phone" char(10),
                  "gender" char(1),
                  "income" numeric(10,2),
                  PRIMARY KEY ("cid")
                );
                '''
    cursor.execute(command)
except:
    print("Customers failed!")
try:
    command=            '''
                CREATE TABLE "Models" (
                  "mid" char(4),
                  "name" varchar(20),
                  "brand" varchar(20),
                  "style" varchar(10),
                  "bid" char(4),
                  PRIMARY KEY ("mid")
                );
                '''
    cursor.execute(command)
except:
    print ("Models failed!")

'''in reality either the first one fails or not.'''

command=            '''
            CREATE TABLE "Suppliers" (
              "sid" char(4),
              "model_name" varchar(20),
              PRIMARY KEY ("sid")
            );'''

command=            '''
            CREATE TABLE "Supply" (
              "sid" char(4),
              "partId" char(4)
            );'''
cursor.execute(command)
command=            '''
            CREATE TABLE "Plant_supply" (
              "pid" char(4),
              "partId" char(4)
            );'''

cursor.execute(command)
command=            '''CREATE TABLE "Order" (
              "did" char(4),
              "cid" char(4),
              "vin" varchar(17)
            );'''
cursor.execute(command)
command=            '''CREATE TABLE "Parts" (
              "partId" char(4),
              "name" varchar(20),
              "sid" char(4),
              PRIMARY KEY ("partId")
            );'''
cursor.execute(command)

command=            '''CREATE TABLE "Brands" (
              "bid" char(4),
              "name" varchar(10),
              PRIMARY KEY ("bid")
            );'''
cursor.execute(command)
command=            '''CREATE TABLE "Dealers" (
              "did" char(4),
              "name" varchar(20),
              "date" date,
              "brand_name" varchar(10),
              "model_name" varchar(10),
              "price" numeric(12,2),
              "color" varchar(10),
              "max_cars" int,
              "current_cars" int,
              "total_sold" int,
              PRIMARY KEY ("did")
            );'''
cursor.execute(command)
try:
    command =       '''
            CREATE TABLE "Vehicles" (
              "vin" varchar(17),
              "pid" char(4),
              "oid" char(4),
              "bid" char(4),
              "mid" char(4),
              "did" char(4),
              PRIMARY KEY ("vin")
            );'''
except:
    print("Vehicles Failed!")

cursor.execute(command)
#this line commits the actual schema!
conn.commit()
