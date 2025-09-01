import os
import sqlite3

conn = sqlite3.connect("student.db")

cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS records(
               roll INTEGER PRIMARY KEY,
               name VARCHAR(50),
               age INTEGER,
               address VARCHAR(50)
               )
               ''')
conn.commit()

def addRecords():
    while True:
        rollNumber = int(input("Enter your roll number: "))
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age: "))
        address=input("Enter your address: ")

        try:
            cursor.execute("INSERT INTO records (roll, name, age, address) VALUES (?, ?, ?, ?)",
                           (rollNumber, name, age, address))
            conn.commit()
            print("Record added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Roll number {rollNumber} already exists.")

        choice = input("Do you want to add more records? (Y/N): ")
        if choice.lower() == "n":
            break
    input("press enter key to continue....")
    os.system("cls")

def searchRecords():
    tempRoll=int(input("Enter roll number to search: "))
    cursor.execute("SELECT * FROM records WHERE roll = ?", (tempRoll,))
    result = cursor.fetchone()

    if result:
        print("Record found:")
        print(f"Roll->{result[0]}, Name->{result[1]}, Age->{result[2]}, Address->{result[3]}")
    else:
        print(f"Record with roll number {tempRoll} not found.")

    input("Press Enter to continue...")
    os.system("cls")

def showRecords():
    count=0
    print("The available records are: ")
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    for result in rows:
        count+=1
        print(f"Roll->{result[0]}, Name->{result[1]}, Age->{result[2]}, Address->{result[3]}")
    print(f"Total number of students: {count}")

    input("Press Enter to continue...")
    os.system("cls")

def deleteRecords():
    tempRoll = int(input("Enter the roll number to be deleted: "))
    cursor.execute("DELETE FROM records WHERE roll = ?", (tempRoll,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Record with roll number {tempRoll} deleted successfully.")
    else:
        print(f"No record found with roll number {tempRoll}.")

    input("Press Enter to continue...")
    os.system("cls")

def updateRecords():
    tempRoll = int(input("Enter roll number to update: "))
    cursor.execute("SELECT * FROM records WHERE roll = ?", (tempRoll,))
    result = cursor.fetchone()

    if result:
        newName=input("Enter new name: ").strip()
        newAge=input("Enter new age: ")
        newAddress=input("Enter new address: ")
        cursor.execute("UPDATE records SET name = ?, age = ?, address=? WHERE roll = ?",
                       (newName,newAge,newAddress, tempRoll))
    
        conn.commit()
        print("Record updated successfully.")
    else:
        print(f"Record with roll {tempRoll} not found.")

    input("Press Enter to continue...")
    os.system("cls")

                
def sortRecords():
    cursor.execute("SELECT * FROM records ORDER BY roll ASC")
    rows = cursor.fetchall()

    if not rows:
        print("No records to sort.")
    else:
        print("The below are the sorted records:")
        for roll, name, age, address in rows:
            print(f"Roll->{roll}, Name->{name}, Age->{age}, Address->{address}")

    input("Press Enter to continue...")
    os.system("cls")

#menu
while True:
    print("\t\t\t<---- Welcome to Student Records Management System ---->")
    print("\n Menu")
    print("----------")
    print("1.Add Records")
    print("2.Search for a record")
    print("3.Display available records")
    print("4.Delete a record")
    print("5.Update records")
    print("6.Sort records")
    print("7.Exit Program")

    #input
    choice=int(input("Enter a choice: "))

    if(choice==7):
        print("Exited program successfully..")
        break

    if choice==1:
        addRecords()
    elif choice==2:
        searchRecords()
    elif choice==3:
        showRecords()
    elif choice==4:
        deleteRecords()
    elif choice==5:
        updateRecords()
    elif choice==6:
        sortRecords()
    else:
        print("Invalid choicee")

