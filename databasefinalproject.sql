-- Active: 1744224929379@@127.0.0.1@3306@hostelsystem
create database HostelSystem;

CREATE Table Managers(
    `Manager_ID` int NOT NULL PRIMARY KEY,
    `Name` VARCHAR(255),
    `PhoneNo.` VARCHAR(13)
);

CREATE Table Hostels(
<<<<<<< HEAD
    Hostel_ID VARCHAR(6) NOT NULL PRIMARY KEY,
=======
    Hostel_ID int NOT NULL PRIMARY KEY,
>>>>>>> 22084186b8875dc07f2c476f9df3a316d6b9d07f
    Name VARCHAR(255),
    Location VARCHAR(255),
    Manager_ID int,
    FOREIGN KEY(Manager_ID) REFERENCES managers(manager_ID));

CREATE Table RoomTypes(
<<<<<<< HEAD
    TypeID VARCHAR(10) NOT NULL PRIMARY KEY,
=======
    TypeID int NOT NULL PRIMARY KEY,
>>>>>>> 22084186b8875dc07f2c476f9df3a316d6b9d07f
    Hostel_ID int,
    FOREIGN KEY(Hostel_ID) REFERENCES Hostels(Hostel_ID),
    Name VARCHAR(255),
    Price int,
    Total_Rooms int,
    Booked_Rooms int,
<<<<<<< HEAD
    Available_Rooms int as (`Total_Rooms`-`Booked_Rooms`)
=======
    Available_Rooms int
>>>>>>> 22084186b8875dc07f2c476f9df3a316d6b9d07f
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
<<<<<<< HEAD
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
=======
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
>>>>>>> 22084186b8875dc07f2c476f9df3a316d6b9d07f


INSERT INTO roomtypes(TypeID, Hostel_ID, `Name`, Price, Total_Rooms, Booked_Rooms) VALUES
("DUF_A2","DUF_A","Dufie Annex 2 in a Room",7100,50,50),
("DUF_G2","DUF_G","Dufie Gold 2 in a Room",6800,24,24),
("DUF_P2","DUF_P","Dufie Prestige 2 in a Room",6800,10,10),
("DUF_PL31","DUF_PL","Dufie 3 in a Room w 1 bathroom",5700,15,15),
("DUF_PL32","DUF_PL","Dufie 3 in a Room w 2 bathroom",5900,15,15),
("OLD_H2","OLD_H","Old Hosanna 2 in a Room",6400,0,0),
("OLD_H3","OLD_H","Old Hosanna 3 in a Room",5600,0,0),
("NEW_H2","NEW_H","New Hosanna 2 in a Room",6900,0,0),
("NEW_H3","NEW_H","New Hosanna 3 in a Room",5000,0,0),
("OLD_M2","OLD_M","Old Masere 2 in a Room",6800,18,10),
("OLD_M3","OLD_M","Old Masere 3 in a Room",5800,5,3),
("NEW_M2","NEW_M","New Masere 2 in a Room",7000,30,28),
("NEW_M3","NEW_M","New Masere 3 in a Room",6000,9,8),
("CEE_C1","CEE_C","Ceewus 1 in a Room",9000,0,0),
("CEE_C2","CEE_C","Ceewus 2 in a Room w AC",7000,0,0),
("CEE_C2","CEE_C","Ceewus 2 in a Room w/out AC",6000,0,0),
("CEE_C3","CEE_C","Ceewus 3 in a Room",,0,0),
("TAN_T2","TAN_T","Tanko 2 in a Room",8000,16,15),
("CHA_C1","CHA_C","Charlotte 1 in a Room",8000,50,10),
("CHA_C2B","CHA_C","Charlotte 2 in a Room Big",6800,50,10),
("CHA_C2S","CHA_C","Charlotte 2 in a Room Small",5200,50,10),
("CHA_C3","CHA_C","Charlotte 3 in a Room",4600,50,10),
("CHA_C4","CHA_C","Charlotte 4 in a Room",2500,50,10);

