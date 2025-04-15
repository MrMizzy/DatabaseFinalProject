-- Active: 1744224929379@@127.0.0.1@3306@hostelsystem
create database HostelSystem;

CREATE Table Managers(
    `Manager_ID` int NOT NULL PRIMARY KEY,
    `Name` VARCHAR(255),
    `PhoneNo.` VARCHAR(13)
);

CREATE Table Hostels(
    Hostel_ID VARCHAR(6) NOT NULL PRIMARY KEY,
    Name VARCHAR(255),
    Location VARCHAR(255),
    Manager_ID int,
    FOREIGN KEY(Manager_ID) REFERENCES managers(manager_ID));

CREATE Table RoomTypes(
    TypeID VARCHAR(10) NOT NULL PRIMARY KEY,
    Hostel_ID int,
    FOREIGN KEY(Hostel_ID) REFERENCES Hostels(Hostel_ID),
    Name VARCHAR(255),
    Price int,
    Total_Rooms int,
    Booked_Rooms int,
    Available_Rooms int as (`Total_Rooms`-`Booked_Rooms`)
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
(8,"Roger Jackson","+23327884440"),
(9,"Cynthia","+233265563074");

INSERT into hostels(`Hostel_ID`,`Name`,`Location`,`Manager_ID`) VALUES
("DUF_A","Dufie Annex","4th Turn, University Avenue", 2),
("DUF_G","Dufie Gold","3rd Turn, University Avenue", 2),
("DUF_P","Dufie Prestige","3rd Turn, University Avenue", 2),
("DUF_PL","Dufie Platinum","3rd Turn, University Avenue", 2),
("NEW_M","New Masere","2nd Turn, University Avenue", 1),
("OLD_M","Old Masere","4th Turn, University Avenue", 6),
("TAN_T","Tanko","University Avenue", 4),
("QUE_Q","Queenstar","University Avenue", 7),
("CHA_C","Charlotte's Court","1st Turn, University Avenue", 8),
("OLD_H","Old Hosanna","3rd Turn, University Avenue", 3),
("NEW_H","New Hosanna","University Avenue", 3),
("COL_C","Columbiana","4th Turn, University Avenue", 5),
("CEE_C","CEEWUS","1st Turn, University Avenue",9);


INSERT INTO roomtypes(TypeID, Hostel_ID, `Name`, Price, Total_Rooms, Booked_Rooms, Available_Rooms) VALUES
(1, 1, '3-In-A-Room, One Washroom', 5700, 20, 4, 16),
(2, 1, '3-In-A-Room, Two Washroom', 5900, 20, 4, 16),
(3, 1, '2-In-A-Room', 6800, 20, 4, 16),
(4, 2, '2-In-A-Room', 7100, 20, 4, 16),
(5, 4, '2-In-A-Room', 6800, 10, 0, 10),
(6, 4, '3-In-A-Room', 5800, 10, 4, 6),
(7, 3, '2-In-A-Room', 7000, 15, 10, 5),
(8, 3, '3-In-A-Room', 6000, 10, 1, 9),
(9, 5, '2-In-A-Room, Balcony', 6900, 12, 3, 9),
(10, 5, '3-In-A-Room', 5700, 12, 5, 7),
(11, 6, 'Single Room, Ensuite', 8000, 8, 6, 2),
(12, 6, '2-In-A-Room', 7200, 10, 4, 6),
(13, 7, '3-In-A-Room', 5900, 15, 7, 8),
(14, 7, '2-In-A-Room', 7500, 10, 5, 5),
(15, 8, '2-In-A-Room', 7000, 10, 2, 8),
(16, 8, 'Single Room', 8500, 5, 1, 4),
(17, 9, '3-In-A-Room', 6100, 15, 6, 9),
(18, 9, '2-In-A-Room', 7300, 12, 7, 5),
(19, 10, 'Single Room', 8800, 6, 3, 3),
(20, 10, '3-In-A-Room', 6200, 9, 2, 7);




