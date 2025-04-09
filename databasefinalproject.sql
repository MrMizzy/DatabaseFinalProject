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

CREATE Table RoomTypes(
    TypeID int NOT NULL PRIMARY KEY,
    Hostel_ID int,
    FOREIGN KEY(Hostel_ID) REFERENCES Hostels(Hostel_ID),
    Name VARCHAR(255),
    Price int,
    Total_Rooms int,
    Booked_Rooms int,
    Available_Rooms int
);

CREATE Table Rooms(
    Room_ID int NOT NULL PRIMARY KEY,
    Room_Type int,
    Foreign Key (Room_Type) REFERENCES RoomTypes(TypeID),
    Available_Beds int
);
