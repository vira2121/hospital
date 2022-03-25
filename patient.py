import sqlite3
con = sqlite3.connect('Hospital.db')

curr = con.cursor()

Create_query = '''CREATE TABLE if not exists patient(
                  PatientCode INTEGER PRIMARY KEY AUTOINCREMENT,
                  Name TEXT NOT NULL,
                  Address TEXT NOT NULL UNIQUE,
                  ContactNo INTEGER NOT NULL UNIQUE ) '''
curr.execute(Create_query)

check = 1
while check:
    c = int(input( "Main menu\n 1) Add new Patient record \n 2) View all Details"))

    if c ==1:
        n = int(input("Enter no of patient "))
        for i in range(n):
            PatientCode = int(input("Enter ID: "))
            Name = input("Enter the name: ")
            Address = input("Enter the Address: ")
            ContactNo = int(input("Enter the phone No: "))
            insert_query = f"insert into patient values({PatientCode},'{Name}','{Address}',{ContactNo})"
            curr.execute(insert_query)
            con.commit()
    elif c ==2:
        select_query = "SELECT * FROM patient"
        curr.execute(select_query)
        result = curr.fetchall()
        for row in result:
            print('patientID:',row[0])
            print('Name of patient:',row[1])
            print('Address of patient :',row[2])
            print('Contact no :',row[3])

            con.commit()
    else :
        print("Exit the program")
        check = 0