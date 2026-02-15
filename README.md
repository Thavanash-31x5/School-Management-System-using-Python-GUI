CREATE DATABASE school;
USE school;
CREATE TABLE student (
    name VARCHAR(100) NOT NULL,
    class VARCHAR(20) NOT NULL,
    roll_no INT PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    fees_due DECIMAL(10,2) DEFAULT 0,
    fees_paid DECIMAL(10,2) DEFAULT 0,
    route_number VARCHAR(20),
    bus_number VARCHAR(20),
    driver_name VARCHAR(100),
    stop_name VARCHAR(100)
);
CREATE TABLE teacher (
    Name VARCHAR(100) NOT NULL,
    Post VARCHAR(100) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Teacher_ID INT PRIMARY KEY
);
