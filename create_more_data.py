import psycopg2



dbname = 'project'
host = 'localhost'
user = 'postgres'
password = 'root' #postgres on laptop, root on desktop
conn = psycopg2.connect(host=host, dbname = dbname, user = user, password = password)
cursor = conn.cursor()



'''CREATE TABLE "Dealers" (
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
command = '''
			insert into "Dealers" values('9000', 'Bens Buick', '2017-03-14', 'Buick', 'Regal', 55000.00, 'red', 25,2,30);
			insert into "Dealers" values('9100', 'Bens Buick', '2017-03-14', 'Buick', 'Lacrosse', 15000.00, 'red', 250,50,30);
			'''
cursor.execute(command)
conn.commit()
