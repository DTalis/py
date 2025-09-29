DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS customers;

CREATE TABLE items (
 item_id SERIAL PRIMARY KEY,
 item VARCHAR (50) NOT NULL,
 price INT NOT NULL
);

INSERT INTO items (item, price)
VALUES ('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);


CREATE TABLE customers (
customer_id SERIAL PRIMARY KEY,
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (100) NOT NULL
);

INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

SELECT * FROM items;
SELECT * FROM items WHERE price > 80;
SELECT * FROM items WHERE price <= 300;
SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE last_name = 'Jones';
SELECT * FROM CUSTOMERS WHERE first_name <> 'Scott';

 