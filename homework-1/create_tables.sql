-- SQL-команды для создания таблиц
CREATE TABLE employees
(employee_id serial PRIMARY KEY,
 first_name CHARACTER VARYING(30),
 last_name CHARACTER VARYING(30),
 title 	varchar(100) NOT NULL,
 birth_date varchar(30),
 notes text
);

CREATE TABLE customers
(customer_id varchar(50) PRIMARY KEY,
 company_name varchar(100) NOT NULL,
 contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(order_id int PRIMARY KEY,
 customer_id varchar(50) REFERENCES customers(customer_id) NOT NULL,
 employee_id int REFERENCES employees(employee_id) NOT NULL,
 order_date date,
 ship_city varchar(50)
);

SELECT * FROM employees
SELECT * FROM customers
SELECT * FROM orders
