--creating a new database if it does not exist
CREATE DATABASE hbnb_dev_db IF NOT EXISTS;
--create  a new user with a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--granting all privileges to user
GRANT ALL PRIVILEGES ON DATABASE hbnb_dev_db.* To 'hbnb_dev'@'localhost';
--granting select privileges to the perfomance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
