
DROP DATABASE IF EXISTS mockInjection;

CREATE DATABASE IF NOT EXISTS mockInjection;

USE mockInjection;
CREATE TABLE users(
	username varchar(255) NOT NULL,
	password varchar(255) NOT NULL
);
INSERT INTO users 
VALUES 
('lnwza007', '123'), 
('eiei123','123'),
('Emma', 'u8N6tK9g'),
('Noah', 'p7H5jM6z'),
('Olivia', 'h9L8kQ2t'),
('Liam', 'z5T8gP9u'),
('Ava', 'b8K6tH7m'),
('Mason', 'y2Q9uH5t'),
('Sophia', 'm6J8hK7z'),
('Jacob', 'w8T6pH9g'),
('Isabella', 'x5P9uN8t'),
('William', 'g8K7tZ9h'),
('Mia', 't8J6pH7u'),
('Ethan', 'y9L8kQ5t'),
('Charlotte', 'm7H9jK8z'),
('James', 'w6T7pH5g'),
('Amelia', 'x8P6uN7t'),
('Alexander', 'g7K9tZ8h'),
('Abigail', 't6J8pH9u'),
('Michael', 'y5L7kQ8t'),
('Emily', 'm8H6jK9z'),
('Benjamin', 'w7T9pH6g'),
('Elizabeth', 'x6P8uN5t'),
('Matthew', 'g9K7tZ7h'),
('Avery', 't8J9pH6u'),
('Daniel', 'y7L8kQ9t'),
('Sofia', 'm6H7jK8z'),
('Joseph', 'w5T6pH7g'),
('Evelyn', 'x9P7uN8t'),
('Samuel', 'g7K8tZ9h'),
('Aubrey', 't7J6pH8u'),
('Christopher', 'y8L9kQ7t'),
('Harper', 'm9H7jK6z'),
('Nathan', 'w6T8pH5g'),
('Aria', 'x7P9uN7t'),
('Ryan', 'g8K7tZ9h'),
('Adalynn', 't6J8pH9u'),
('Andrew', 'y5L7kQ8t'),
('Ellie', 'm8H6jK9z'),
('Oliver', 'w7T9pH6g'),
('Scarlett', 'x6P8uN5t'),
('Henry', 'g9K7tZ7h'),
('Aaliyah', 't8J9pH6u'),
('Jaxon', 'y7L8kQ9t'),
('Audrey', 'm6H7jK8z'),
('Julian', 'w5T6pH7g'),
('Natalie', 'x9P7uN8t'),
('Levi', 'g7K8tZ9h'),
('Hazel', 't7J6pH8u');

CREATE TABLE employee(
	employee_id varchar(255) NOT NULL,
    prefixname varchar(255) NOT NULL,
    fname varchar(255) NOT NULL,
    lname varchar(255) NOT NULL,
    nickname varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    tel char(10) NOT NULL,
    work_background varchar(255) NOT NULL,
    graduation_certificate varchar(255) NOT NULL,
    address varchar(255) NOT NULL,
    id_card varchar(255) NOT NULL,
    house_registration varchar(255) NOT NULL,
    PRIMARY KEY (employee_id)
);

INSERT INTO employee
VALUES ('E001', 'Mr.', 'bobo1', 'two1', 'baba1', 'E001@gmail.com', 0123456781 , 'companyA, companyB', 'XAU', '123 r.xxxxx 50200', 1530302340921, '123 r.xxxxx 54000'), 
       ('E002', 'Mr.', 'bobo2', 'two2', 'baba2', 'E002@gmail.com', 0123456782 , 'companyA, companyB', 'XAU', '123 r.xxxxx 50200', 1530302340922, '123 r.xxxxx 54000'), 
       ('E003', 'Mr.', 'bobo3', 'two3', 'baba3', 'E003@gmail.com', 0123456783 , 'companyA, companyB', 'XAU', '123 r.xxxxx 50200', 1530302340923, '123 r.xxxxx 54000'), 
       ('E004', 'Mr.', 'bobo4', 'two4', 'baba4', 'E004@gmail.com', 0123456784 , 'companyA, companyB', 'XAU', '123 r.xxxxx 50200', 1530302340924, '123 r.xxxxx 54000'), 
       ('E005', 'Mr.', 'bobo5', 'two5', 'baba5', 'E005@gmail.com', 0123456785 , 'companyA, companyB', 'XAU', '123 r.xxxxx 50200', 1530302340925, '123 r.xxxxx 54000');

CREATE TABLE customer(
	customer_id varchar(255) NOT NULL PRIMARY KEY,
    fname varchar(255) NULL,
    lname varchar(255) NULL,
    email varchar(255) NULL,
    tel char(10) NOT NULL
);

INSERT INTO customer
VALUES ('C001', 'memo1', 'one1', 'E001@gmail.com', 0123456781),
        ('C002', 'memo2', 'one2', 'E002@gmail.com', 0123456782);

CREATE TABLE service(
    name varchar(255) NOT NULL PRIMARY KEY,
    price int(11) UNSIGNED NOT NULL);

INSERT INTO service
VALUES ('A', 100), ('B',200), ('C',300), ('D',400);