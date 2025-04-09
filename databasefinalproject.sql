-- Active: 1744224929379@@127.0.0.1@3306@hostelsystem
create database HostelSystem;

CREATE Table Managers(
    `Manager_ID` int NOT NULL PRIMARY KEY,
    `Name` VARCHAR(255),
    `PhoneNo.` VARCHAR(13)
);

CREATE Table Hostels(
    Hostel_ID int NOT NULL PRIMARY KEY,
    Name VARCHAR(255),
    Location VARCHAR(255),
    Manager_ID int,
    FOREIGN KEY(Manager_ID) REFERENCES managers(manager_ID));
select * from hostels;
