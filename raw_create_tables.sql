
CREATE TABLE Options (
  oid char(4) NOT NULL,
  color varchar(10),
  engine varchar(10),
  transmission varchar(10),
  PRIMARY KEY (oid)
);

CREATE TABLE Customers (
  cid char(4) NOT NULL,
  name varchar(30),
  address varchar(30),
  phone char(10),
  gender char(1),
  income numeric(10,2),
  PRIMARY KEY (cid)
);

CREATE TABLE Brands (
  bid char(4) NOT NULL,
  brand_name varchar(20),
  PRIMARY KEY (bid)
);

CREATE TABLE Models (
  mid char(4) NOT NULL,
  model_name varchar(20),
  brand_name varchar(20),
  style varchar(10),
  bid char(4) NOT NULL,
  PRIMARY KEY (mid),
  FOREIGN KEY (bid) REFERENCES (Brands)
);

CREATE TABLE Suppliers (
  sid char(4) NOT NULL,
  model_name varchar(20),
  PRIMARY KEY (sid)
);

CREATE TABLE Plants (
  pid char(4) NOT NULL,
  model_name varchar(20),
  PRIMARY KEY (pid)
);

CREATE TABLE Parts (
  partId char(4) NOT NULL,
  part_name varchar(20),
  PRIMARY KEY (partId)
);

CREATE TABLE Supply (
  sid char(4),
  partId char(4),
  PRIMARY KEY (sid, partId),
  FOREIGN KEY (sid) REFERENCES (Suppliers),
  FOREIGN KEY (partId) REFERENCES (Parts)
);

CREATE TABLE Plant_supply (
  pid char(4) NOT NULL,
  partId char(4) NOT NULL,
  PRIMARY KEY (pid, partId),
  FOREIGN KEY (pid) REFERENCES (Plants),
  FOREIGN KEY (partId) REFERENCES (Parts)
);

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

CREATE TABLE Vehicles (
  vin varchar(17) NOT NULL,
  pid char(4) NOT NULL,
  oid char(4) NOT NULL,
  bid char(4) NOT NULL,
  mid char(4) NOT NULL,
  did char(4) NOT NULL,
  PRIMARY KEY (vin),
  FOREIGN KEY (pid) REFERENCES (Plants),
  FOREIGN KEY (oid) REFERENCES (Options),
  FOREIGN KEY (bid) REFERENCES (Brands),
  FOREIGN KEY (mid) REFERENCES (Models),
  FOREIGN KEY (did) REFERENCES (Dealers)
);

CREATE TABLE Orders (
  did char(4) NOT NULL,
  cid char(4) NOT NULL,
  vin varchar(17) NOT NULL,
  PRIMARY KEY (did, cid, vin),
  FOREIGN KEY (did) REFERENCES (Dealers),
  FOREIGN KEY (cid) REFERENCES (Customers),
  FOREIGN KEY (vin) REFERENCES (Vehicles)
);

CREATE TABLE Model_parts (
  partId char(4),
  mid char(4),
  PRIMARY KEY (partId, mid),
  FOREIGN KEY (partId) REFERENCES (Parts),
  FOREIGN KEY (mid) REFERENCES (Models)
);
