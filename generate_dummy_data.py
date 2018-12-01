import psycopg2



dbname = 'project'
host = 'localhost'
user = 'postgres'
password = 'root' #postgres on laptop, root on desktop
conn = psycopg2.connect(host=host, dbname = dbname, user = user, password = password)
cursor = conn.cursor()




command = '''
			insert into "Model_parts" values ( '4318', '6743');
			insert into "Model_parts" values ( '4319', '6744');
			insert into "Model_parts" values ('4320', '6745');
			insert into "Model_parts" values ('4321', '6746');
			'''
cursor.execute(command)

command = '''
			insert into "Plants" values ('5001', 'CTS');
			insert into "Plants" values ('5002','XTS');
			insert into "Plants" values ('5003', 'Enclave');
			insert into "Plants" values ('5004', 'Bolt EV');
			insert into "Plants" values ('5005', 'Impala');
			'''

cursor.execute(command)

command = '''
			insert into "Options" values ('9001', 'blue','V6','manual');
			insert into "Options" values ('9002','red','V6','automatic');
			insert into "Options" values ('9003', 'white','V4','automatic');
			insert into "Options" values ('9004', 'beige','V4','automatic');
			insert into "Options" values ('9005', 'black','V4','automatic');
			'''
cursor.execute(command)

command = '''
			insert into "Customers" values ('2001', 'John', '190 Dickinson St.', '9324920010', 'M', 21000.30);
			insert into "Customers" values ('2002', 'Mary', '500 Van Dyke St.', '9993354924','F', 190000.21);
			insert into "Customers" values ('2003', 'George', '800 George Ave.', '4154581859', 'M', 50000.90);
			'''
cursor.execute(command)

command = '''
			insert into "Models" values ('6743', 'Enclave', 'Buick','SUV','0001');
			insert into "Models" values ('6744','CTS', 'Cadillac', 'sedan', '0002');
			insert into "Models" values ('6745', 'Acadia', 'GMC','SUV','0004');
			'''

cursor.execute(command)

command = '''
			insert into "Suppliers" values ('3001','Acadia');
			insert into "Suppliers" values ('3002', 'Enclave');
			insert into "Suppliers" values ('3003', 'CTS');
			'''

cursor.execute(command)

command = '''
			insert into "Supply" values ('3001', '9001');
			insert into "Supply" values ('3002', '9002');
			insert into "Supply" values ('3003', '9003');
			'''
cursor.execute(command)


command = '''
			insert into "Plant_supply" values ('5001', '9001');
			insert into "Plant_supply" values ('5002', '9002');
			insert into "Plant_supply" values ('5003', '9003');
			insert into "Plant_supply" values ('5004', '9004');
			insert into "Plant_supply" values ('5005', '9005');
			'''
cursor.execute(command)

command = '''
			insert into "Order" values ('0010', '2001', 'WAUFFAFM3CA000000');
			insert into "Order" values ('0012', '2002', 'FAHJBVCALEIQ90019');
			insert into "Order" values ('0011', '2003', 'POQJJA023NKVLNVO3');
			'''
cursor.execute(command)

command = '''
			insert into "Parts" values ('9001', 'Motor');
			insert into "Parts" values ('9002', 'Transmission');
			insert into "Parts" values ('9003', 'Transmission');
			insert into "Parts" values ('9004', 'Motor');
			'''
cursor.execute(command)


command = '''
			insert into "Brands" values ('0001', 'Buick');
			insert into "Brands" values ('0002', 'Cadillac');
			insert into "Brands" values ('0003', 'Chevrolet');
			insert into "Brands" values ('0004', 'GMC');
			'''
cursor.execute(command)

command = '''
			insert into "Dealers" values('0010', 'Bens Buick', '2017-03-14', 'Buick', 'Enclave', 25000.00, 'red', 25,5,30);
			insert into "Dealers" values('0011', 'Kens Cadillac', '2017-09-14', 'Cadillac', 'CTS', 55000.00, 'silver', 155,65,500);
			insert into "Dealers" values('0012', 'Gills GMC', '2017-12-14', 'GMC', 'Acadia', 35000.00, 'black', 65,15,50);
			'''
cursor.execute(command)

command = '''
			insert into "Vehicles" values ('WAUFFAFM3CA000000', '5001', '9001', '0001', '6473', '0010');
			insert into "Vehicles" values ('FAHJBVCALEIQ90019', '5002', '9005', '0004', '6745', '0012');
			insert into "Vehicles" values ('POQJJA023NKVLNVO3', '5003', '9004', '0002', '6744', '0011');
			'''
cursor.execute(command)
conn.commit()
