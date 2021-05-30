import mysql.connector as mysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def governmentEmployee(cnx):
    c='y'
    while(c=='Y' or c=='y'):
        print("""
                1) Passenger details of current stay.\n
                2) Officials shift timing and assigned location For a given empId.\n
                3) Officials shift timing and assigned location For everyone.\n
                4) Assign a location to an employee.\n
                5) Passengers checked by an employee.\n
                6) Passengers checked at a particular date.\n
                7) List of all employees at a particular location on a particular day\n
                8) previous Menu\n""")
        choice = int(input("Select the query : "))
        if(choice == 1):
            query = "SELECT * FROM Passenger"
        elif(choice == 2):
            inp = input("Enter employee Id : ")
            query = "SELECT empId, empName, shiftTiming, assignedLocation FROM GovernmentEmployee WHERE empId = '{}'".format(inp)
        elif(choice == 3):
            query = "SELECT empId, empName, shiftTiming, assignedLocation FROM GovernmentEmployee"
        elif(choice == 4):
            inp1 = input("Enter assigned location : ")
            inp2 = input("Enter employee Id : ")
            query = "UPDATE GovernmentEmployee SET assignedLocation = '{}' WHERE empId = '{}'".format(inp1, inp2)
        elif(choice == 5):
            inp = input("Enter employee Id : ")
            query = "SELECT P.passengerId, P.passengerName FROM Passenger AS P, govtCheck AS GC WHERE P.passengerId = GC.passengerId and GC.empId = '{}'".format(inp)
        elif(choice == 6):
            inp = input("Enter date in YYYY-MM-DD format : ")
            query = "SELECT P.passengerId, P.passengerName FROM Passenger AS P, govtCheck AS GC WHERE P.passengerId = GC.passengerId and GC.checkDate = '{}'".format(inp)
        elif(choice == 7):
            inp1 = input("Enter date in YYYY-MM-DD format : ")
            inp2 = input("Enter Location : ")
            query ="SELECT G.empId, G.empName FROM GovernmentEmployee AS G,(SELECT DISTINCT(empId) FROM GovtCheck WHERE checkDate = '{}') AS T WHERE T.empId = G.empId and G.assignedLocation = '{}'".format(inp1, inp2)
        elif(choice == 8):
            return
        else:
            print("select correct choice")
            continue
        result_dataFrame = pd.read_sql(query, cnx)
        pd.set_option('display.max_rows', result_dataFrame.shape[0]+1)
        print(result_dataFrame)
        cnx.commit()
        c = input("Do you want to continue(y/n) : ")
    return

def airportStaff(mydb):
    c = 'y'
    while(c == 'y' or c == 'Y'):
        print("\n\t\t1) List of airlines on a given day\n");
        print("\t\t2) List of passengers departing/arriving from an airline\n");
        print("\t\t3) Request for cleaning employees\n");
        print("\t\t4) Transport assigned to a particular gate\n");
        print("\t\t5) Assigning shifts\n");
        print("\t\t6) Find information about a particular passenger\n");
        print("\t\t7) Find information about a particular employee\n");
        print("\t\t8) List of passengers with positive result\n");
        print("\t\t9) previous Menu\n")
        choice = int(input("Select the query : "))
        if(choice==1):
          date=input("Enter date in YYYY-MM-DD format : ");
          query1="SELECT * from airlines natural join travelstofrom where trDate='{}'".format(date);
        elif(choice==2):
          fid=input("Enter flight Id : ");
          query1="SELECT * from passenger natural join travellingairline where flightid='{}'".format(fid);
        elif(choice==4):
          gate=int(input("Enter exit gate no : "));
          query1="SELECT * from transport where exitGateNoAssigned='{}'".format(gate);
        elif(choice==6):
          fid=input("enter flight Id : ");
          query1="SELECT * from passenger where passengerID='{}'".format(fid);
        elif(choice==7):
          fid=input("enter flight Id : ");
          query1="SELECT * from airportstaff where empID='{}'".format(fid);
        elif(choice==8):
          query1="SELECT count(passengerID),trFrom from Passenger natural join travellingairline natural join TravelsToFrom where covidTestResult='Positive' group by trFrom";
          result = pd.read_sql(query1, mydb)
          result=result.set_index('count(passengerID)')
          plt.figure(figsize=(100,100))
          plt.title("Positive cases, by arriving Airport")
          sns.barplot(x=result.index, y=result['trFrom'])
          plt.ylabel("Arng Airport");
          plt.show();
        elif(choice == 9):
            return
        else:
            print("select correct choice")
            continue
        result_dataFrame = pd.read_sql(query1, mydb)
        pd.set_option('display.max_rows', result_dataFrame.shape[0]+1)
        print(result_dataFrame)
        mydb.commit()
        c = input("Do you want to continue(y/n) : ")
    return

def cleaningCompany(cnx):
    c = 'y'
    while(c == 'y' or c == 'Y'):
        print("\n\t\t1) Cleaning company employee list in a particular shift\n");
        print("\t\t2) Last cleaned location by employee and its time\n");
        print("\t\t3) Flight departure time\n");
        print("\t\t4) Location that need cleaning\n");
        print("\t\t5) Store and restaurant timings\n");
        print("\t\t6) previous Menu\n");
        choice = int(input("Select the query : "))
        if(choice==1):
            t1=input("Enter Start time of Shift(hh:mm:ss) : ");
            t2=input("Enter end time of Shift(hh:mm:ss) : ");
            query1="SELECT * from CleaningCompany where shiftTiming >= '{}' and shiftTiming <= '{}'".format(t1,t2);
        elif(choice==2):
            fid=input("Enter flight ID : ");
            query1="SELECT * from CleaningCompany where empid='{}'".format(fid);
        elif(choice==3):
            fid=input("Enter flight ID :");
            query1="SELECT * from airlines natural join travelstofrom where flightId='{}'".format(fid);
        elif(choice==5):
            query1="SELECT storeName,openTime, closeTime from StoresAndRestaurants";
        elif(choice == 6):
            return
        else:
            print("select correct choice")
            continue
        result_dataFrame = pd.read_sql(query1, cnx)
        pd.set_option('display.max_rows', result_dataFrame.shape[0]+1)
        print(result_dataFrame)
        cnx.commit()
        c = input("Do you want to continue(y/n) : ")
    return

def Airlines(cnx):
    c = 'y'
    while(c == 'y' or c == 'Y'):
        print("\n\t\t1) View list of passengers travelling in the airline\n")
        print("\t\t2) eparting time at each airport\n")
        print("\t\t3) View Staff on Board\n")
        print("\t\t4) Request for cleaning\n")
        print("\t\t5) Previous Menu\n")
        choice=int(input("Select the query : "))
        if(choice==1):
            flightId = input("Enter the flight Id : ")
            query1 = "SELECT passengerId FROM TravellingAirline WHERE flightId = '{}'".format(flightId)
        elif(choice==2):
            flightId=input("Enter the flight Id : ")
            query1 = "SELECT trTime FROM TravelsToFrom WHERE flightId = '{}'".format(flightId)
        elif(choice==3):
            flightId = input("Enter the flight Id : ")
            query1 = "SELECT * FROM ExternalEmployee WHERE flightId = '{}'".format(flightId)
        elif(choice==4):
            flightId = input("Enter the flight Id : ")
            time = input("Enter Shift time(hh:mm:ss) : ")
            query1 = "UPDATE CleaningCompany SET assignedLocation = '{}', shiftTiming='{}' WHERE assignedLocation = '' LIMIT 2".format(flightId, time)
        elif(choice==5):
            return
        else:
            print("select correct choice")
            continue
        result_dataFrame = pd.read_sql(query1, mydb)
        pd.set_option('display.max_rows', result_dataFrame.shape[0]+1)
        print(result_dataFrame)
        mydb.commit()
        c = input("Do you want to continue(y/n) : ")
    return

def StoresandRestaurants(mydb):
    c = 'y'
    while(c == 'y' or c == 'Y'):
        print("\n\t\t1) View employees currently working in your store\n")
        print("\t\t2) Request for Cleaning of your Store\n")
        print("\t\t3) Previous Menu\n")
        choice=int(input("Select the query : "))
        if(choice == 1):
            storename = input("Enter your Storename : ")
            query1 = "SELECT empid, empName FROM ExternalEmployee WHERE storeName = '{}'".format(storename)
        elif(choice == 2):
            storename = input("Enter your Storename : ")
            time = input("Enter Shift time(hh:mm:ss) : ")
            query1 = "UPDATE CleaningCompany SET assignedLocation = '{}', shiftTiming='{}' WHERE assignedLocation = '' LIMIT 2".format(storename, time)
        elif(choice == 3):
            return
        else:
            print("select correct choice")
            continue
        result_dataFrame = pd.read_sql(query1, mydb)
        pd.set_option('display.max_rows', result_dataFrame.shape[0]+1)
        print(result_dataFrame)
        mydb.commit()

if __name__ == '__main__':
    cnx = mysql.connect(
       host="127.0.0.1",
       user="root",
       passwd="toor",
       database="SkyHigh",
       auth_plugin="mysql_native_password"
    )
    cursor = cnx.cursor()
    while(1):
        print("\n1) Airport Staff\n\n2) Cleaning Company\n\n3) Medical Team\n\n4) Airlines\n\n5) Government Employee\n\n6) Store and Restaurant owners\n\n7) logout\n")
        choice = int(input("Select the User type : "))
        if(choice == 1):
            airportStaff(cnx)
        elif(choice == 2):
            cleaningCompany(cnx)
        elif(choice == 3):
            medicalTeam(cnx)
        elif(choice == 4):
            airlines(cnx)
        elif(choice == 5):
            governmentEmployee(cnx)
        elif(choice == 6):
            storeAndRestaurant(cnx)
        elif(choice == 7):
            break;
        else:
            print("choose correct number")
    cnx.close()
