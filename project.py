import os

def addRecords():
    with open ("records.txt","a") as file:
        while True:
            rollNumber=int(input("Enter your roll number: "))
            name=input("Enter your name: ")
            grade=int(input("Enter your grade: "))
            file.write(f"{rollNumber},{name},{grade}\n")
            print("Records added successfully..")

            choice=input("Do you want to add more records?(Y/N) ")
            if(choice=="n" or choice=="N"):
                break

def searchRecords():
    found=0
    tempRoll=int(input("Enter roll number to find: "))
    with open ("records.txt","r") as file:
        records=file.readlines()
        for record in records:
            rollNumber,name,grade=record.strip().split(",")
            rollNumber=int(rollNumber)
            if(rollNumber == tempRoll):
                found=1
                print(f"Record found:")
                print(f"{'Roll':<10}{'Name':<10}{'Grade':<10}")
                print(f"{tempRoll:<10}{name:<10}{grade:<10}")
                break
        
        if(found!=1):
            print("Record not found.")

    input("Press Enter to continue...")

def showRecords():
    available_records=[]
    with open("records.txt","r") as file:
        records=file.readlines()
        for record in records:
            rollNumber,name,grade=record.strip().split(",")
            rollNumber=int(rollNumber)
            grade=int(grade)
            available_records.append((rollNumber,name,grade))

        print("The available records are:\n")
        print(f"{'Roll':<10}{'Name':<10}{'Grade':<10}")
        for rollNumber,name,grade in available_records:
            print(f"{rollNumber:<10}{name:<10}{grade:<10}")
        input("Press Enter to continue...")

def deleteRecords():
    found=0
    tempRoll=int(input("Enter the roll number to be deleted: "))
    with open("records.txt","r") as file:
        records=file.readlines()
    
    with open("demo.txt","w") as f:
        for record in records:
            rollNumber,name,grade=record.strip().split(",")
            rollNumber=int(rollNumber)
            if(rollNumber==tempRoll):
                found=1
                continue
            f.write(f"{rollNumber},{name},{grade}\n")
        
    if(found==1):
        os.remove("records.txt")
        os.rename("demo.txt", "records.txt")
        print(f"Record with roll number {tempRoll} deleted successfully.")
            
    if(found!=1):
        print(f"Record not found with roll number {tempRoll}")
        os.remove("demo.txt")
    
    input("Press Enter to continue...")

def updateRecords():
    found=0
    tempRoll=int(input("Enter roll number to update: "))
    with open("records.txt","r") as file:
        records=file.readlines()
        
    with open("demo.txt","w") as f:
        for record in records:
            rollNumber,name,grade=record.strip().split(",")
            rollNumber=int(rollNumber)
            if(rollNumber==tempRoll):
                found=1
                name=input("Enter new name: ").strip() #nam ma hune whitespaces hatauna
                grade=int(input("Enter new grade: "))
            f.write(f"{rollNumber},{name},{grade}\n")
            
    if(found==1):
        os.remove("records.txt")
        os.rename("demo.txt","records.txt")
        print("Record updated successfully...")
    
    if(found!=1):
        os.remove("demo.txt")
        print(f"Record with roll {tempRoll} not found.")

    input("Press Enter to continue...")
                
def sortRecords():
    sorted_records=[]
    with open("records.txt","r") as file:
        records=file.readlines()
        print("The below are the sorted records")
        print(f"{'Roll':<10},{'Name':<10},{'Grade':<10}")
        for record in records:
            rollNumber,name,grade=record.strip().split(",")
            rollNumber=int(rollNumber)
            sorted_records.append((rollNumber,name,grade))
        
        sorted_records.sort()
        for rollNumber, name, grade in sorted_records:
            print(f"{rollNumber:<10}{name:<10}{grade:<10}")
        input("press enter to continue....")

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

