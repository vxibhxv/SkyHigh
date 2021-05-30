create database SkyHigh;
use SkyHigh;

create table AirportStaff(empId varchar(10) NOT NULL,
staff_name varchar(30) NOT NULL,age int,
gender char(7) ,address varchar(50) NOT NULL,phone varchar(15) NOT NULL,
role varchar(50),
Primary Key(empId));

create table Passenger(passengerId varchar(15) NOT NULL,
passengerName varchar(30) NOT NULL,
covidTestResult char(10),
address varchar(50) NOT NULL,
phone varchar(15) NOT NULL,
Primary Key (passengerId));

create table Airlines(flightId varchar(10) NOT NULL,
airlineName varchar(30) NOT NULL,
Primary Key(flightId));

create table GovernmentEmployee(empId varchar(10) NOT NULL ,
empName varchar(30) NOT NULL,
shiftTiming Time,
assignedLocation varchar(50), empPassword varchar(20) NOT NULL,
Primary Key(empID));

create table CleaningCompany(empId varchar(10) NOT NULL,
empName varchar(30),
shiftTiming Time,
assignedLocation varchar(50),
Primary Key(empId));

create table StoresAndRestaurants(storeName varchar(50) NOT NULL,
ownerName varchar(30) NOT NULL,
contact varchar(15) NOT NULL,
email varchar(50), 
openTime Time,
closeTime Time,
generalGuidelines varchar(200),
Primary Key(storeName));

create table MedicalTeam(empId varchar(10) NOT NULL,
teamId varchar(10) NOT NULL,
empName varchar(30) NOT NULL,
address varchar(50) NOT NULL,
phone varchar(15) NOT NULL,
Primary Key(empID));

create table SecurityTeam(empId varchar(10) NOT NULL,
teamId varchar(10) NOT NULL,
empName varchar(30) NOT NULL,
address varchar(50) NOT NULL,
phone varchar(15) NOT NULL,
Primary Key(empID));

create table Transport(transportId varchar(10) NOT NULL, 
exitGateNoAssigned int NOT NULL,
Primary Key(transportID));

create table AirlineCleaned(flightId varchar(10) NOT NULL,
empId varchar(10) NOT NULL,
cleaned boolean,
timings datetime,
Foreign Key(flightId) REFERENCES Airlines(flightId)  ON DELETE cascade ON UPDATE  cascade,
Foreign Key(empId) REFERENCES CleaningCompany(empId));

create table StoreCleaned(storeName varchar(50) NOT NULL,
Empid varchar(10) NOT NULL,
cleaned boolean,
timings datetime,
Foreign Key(storeName) REFERENCES StoresAndRestaurants(storeName) ON DELETE cascade ON UPDATE  cascade,
Foreign Key(empId) REFERENCES CleaningCompany(empId));

create table MedicalTests(empId varchar(10) NOT NULL, 
passengerId varchar(15) NOT NULL,
testResult char(10) ,
testDate date NOT NULL,
testTime time NOT NULL,
Foreign Key(passengerId) REFERENCES Passenger(passengerID),
Foreign Key(empId) REFERENCES MedicalTeam(empId));

create table MedicalTeamshift(teamId varchar(10)  NOT NULL,
shiftDate date  NOT NULL,
shiftTime time  NOT NULL,
location varchar(50)  NOT NULL);

create table SecurityTeamshift(teamId varchar(10)  NOT NULL,
shiftDate date  NOT NULL,
shiftTime time  NOT NULL,
location varchar(50)  NOT NULL);

create table Govtcheck(empId varchar(10)  NOT NULL,
passengerId varchar(15)  NOT NULL,
checkDate date  NOT NULL,
checkTime time  NOT NULL,
Foreign Key(passengerId) REFERENCES Passenger(passengerID),
Foreign Key(empId) REFERENCES GovernmentEmployee(empId));


create table TravellingAirline(passengerId varchar(15)  NOT NULL, 
flightId varchar(10)  NOT NULL,
Foreign Key(passengerId) REFERENCES Passenger(passengerID),
Foreign Key(flightId) REFERENCES Airlines(flightId)  ON DELETE cascade ON UPDATE  cascade);

create table TravelsToFrom(flightId varchar(10) NOT NULL,
trDate date NOT NULL,trTime time NOT NULL,
trFrom char(3) NOT NULL,
trTo char(3) NOT NULL, 
gates int,
Foreign Key(flightId) REFERENCES Airlines(flightId)  ON DELETE cascade ON UPDATE  cascade);

create table ExternalEmployee (empId varchar(10) NOT NULL, 
empName varchar(30) NOT NULL, 
flightId varchar(10),
storeName varchar(50), 
transportId varchar(10), 
phone varchar(15) NOT NULL,
address varchar(50) NOT NULL,
Primary key (empId));

CREATE VIEW airlineCleaninginfo AS
SELECT *
FROM airlineCleaned natural join cleaningCompany;

CREATE VIEW airlineinfo AS
SELECT *
FROM airlines natural join travelsToFrom;

CREATE VIEW governmentcheckinfo AS
SELECT *
FROM governmentemployee natural join govtcheck natural join passenger;

CREATE VIEW medicalTeaminfo AS
SELECT *
FROM medicalTeam natural join medicalTeamShift natural join medicalTests; 

CREATE VIEW storeCleaninginfo AS
SELECT *
FROM storeCleaned natural join cleaningCompany;

CREATE INDEX airlinecleanedIndex
ON airlineCleaned (flightId, empId);

CREATE UNIQUE INDEX airlineIndex
ON airlines (flightId);
 
CREATE UNIQUE INDEX airportStaffIndex
ON airportStaff (empId);

CREATE UNIQUE INDEX cleaningCompanyIndex
ON cleaningCompany (empId);

CREATE UNIQUE INDEX externalEmployeeIndex
ON externalEmployee (empId);

CREATE UNIQUE INDEX governmentEmployeeIndex
ON governmentEmployee (empId);

CREATE UNIQUE INDEX govtCheckIndex
ON govtCheck (empId,pssengerID);

CREATE UNIQUE INDEX medicalTeamIndex
ON medicalTeam(teamID,empId);

CREATE UNIQUE INDEX medicalTeamShiftIndex
ON medicalTeamShift(teamID);

CREATE UNIQUE INDEX medicalTestsIndex
ON medicalTests(empId,passengerID);

CREATE UNIQUE INDEX passengerIndex
ON passenger(passengerID);

CREATE UNIQUE INDEX securityTeamIndex
ON securityTeam(teamID,empId);

CREATE UNIQUE INDEX securityTeamShiftIndex
ON securityTeamShift(teamID);

CREATE INDEX storeCleanedIndex
ON storeCleaned(storeName,empId);

CREATE UNIQUE INDEX StoresAndRestaurantsIndex
ON StoresAndRestaurants(storeName);

CREATE UNIQUE INDEX transportIndex
ON transport(transportID);

CREATE UNIQUE INDEX travellingAirlineIndex
ON travellingAirline(flightID,passengerID);

CREATE INDEX travelsToFrom
ON travelsToFrom(flightID,trDate);





