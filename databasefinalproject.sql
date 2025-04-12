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

INSERT into Managers(`Manager_ID`,`Name`,`PhoneNo.`) VALUES
(1,"Victoria Kudjoe", "+233543958700"),
(2,"Joyce Gyekye", "+233201323058"),
(3,"Simon","+233542601827"),
(4,"Safia Tanko","+233202252859"),
(5,"Carlos Ayi-Bonte","+233242781788"),
(6,"Francisca Frimpong","+233244370272"),
(7,"Bernard Olu Sawyerr","+233244329320"),
(8,"Roger Jackson","+23327884440");

INSERT into hostels(`Hostel_ID`,`Name`,`Location`,`Manager_ID`) VALUES
(1,"Dufie Platinum","3rd Turn, University Avenue", 2),
(2,"Dufie Annex","4th Turn, University Avenue", 2),
(3,"New Masere","2nd Turn, University Avenue", 1),
(4,"Old Masere","4th Turn, University Avenue", 6),
(5,"Tanko","University Avenue", 4),
(6,"Queenstar","University Avenue", 7),
(7,"Charlotte's Court","1st Turn, University Avenue", 8),
(8,"Old Hosanna","3rd Turn, University Avenue", 3),
(9,"New Hosanna","University Avenue", 3),
(10,"Columbiana","4th Turn, University Avenue", 5);

