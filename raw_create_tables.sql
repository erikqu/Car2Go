CREATE TABLE "Model_parts" (
  "partId" char(4),
  "mid" char(4)
);

CREATE INDEX "FK" ON  "Model_parts" ("partId", "mid");

CREATE TABLE "Plants" (
  "pid" char(4),
  "model_name" varchar(20),
  PRIMARY KEY ("pid")
);

CREATE TABLE "Options" (
  "oid" char(4),
  "color" varchar(10),
  "engine" varchar(10),
  "transmission" varchar(10),
  PRIMARY KEY ("oid")
);

CREATE TABLE "Customers" (
  "cid" char(4),
  "name" varchar(30),
  "address" varchar(30),
  "phone" char(10),
  "gender" char(1),
  "income" numeric(10,2),
  PRIMARY KEY ("cid")
);

CREATE TABLE "Models" (
  "mid" char(4),
  "model_name" varchar(20),
  "brand_name" varchar(20),
  "style" varchar(10),
  "bid" char(4),
  PRIMARY KEY ("mid")
);

CREATE INDEX "FK" ON  "Models" ("bid");

CREATE TABLE "Suppliers" (
  "sid" char(4),
  "model_name" varchar(20),
  PRIMARY KEY ("sid")
);

CREATE TABLE "Supply" (
  "sid" char(4),
  "partId" char(4)
);

CREATE INDEX "FK" ON  "Supply" ("sid", "partId");

CREATE TABLE "Plant_supply" (
  "pid" char(4),
  "partId" char(4)
);

CREATE INDEX "FK" ON  "Plant_supply" ("pid", "partId");

CREATE TABLE "Order" (
  "did" char(4),
  "cid" char(4),
  "vin" varchar(17)
);

CREATE INDEX "FK" ON  "Order" ("did", "cid", "vin");

CREATE TABLE "Parts" (
  "partId" char(4),
  "part_name" varchar(20),
  PRIMARY KEY ("partId")
);

CREATE TABLE "Brands" (
  "bid" char(4),
  "brand_name" varchar(20),
  PRIMARY KEY ("bid")
);

CREATE TABLE "Dealers" (
  "did" char(4),
  "dealer_name" varchar(20),
  "date" date,
  "brand_name" varchar(10),
  "model_name" varchar(10),
  "price" numeric(12,2),
  "color" varchar(10),
  "max_cars" int,
  "current_cars" int,
  "total_sold" int,
  PRIMARY KEY ("did")
);

CREATE TABLE "Vehicles" (
  "vin" varchar(17),
  "pid" char(4),
  "oid" char(4),
  "bid" char(4),
  "mid" char(4),
  "did" char(4),
  PRIMARY KEY ("vin")
);

CREATE INDEX "FK" ON  "Vehicles" ("pid", "oid", "bid", "mid", "did");
