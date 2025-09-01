import csv
def addExpense():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date","Category","Heading for expense","Expense"])
    while True:
        date=input("Enter the date (YYYY-MM-DD): ")
        category=input("Enter the category(for e.g food, travel etc.): ")
        heading=input("Enter the heading(for e.g lunch, office etc.): ")
        amount=float(input("Enter the amount: "))
        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, heading, amount])
        print("Expense added successfully!")
        ch=input("Do you want to add another expense? (y/n)")
        if(ch=="n" or ch=="N"):
            break
    input("Press Enter to continue...")

def trackExpenses():
    found=0
    with open("expenses.csv", "r") as file:
        reader=csv.DictReader(file)
        category=input("Enter the category you want to track: ")
        for row in reader:
            if row["Category"]==category:
                found=1
                print("\n", row, "\n")
        
        if(found!=1):
            print("\nNo expenses found in this category.\n")

def totalExpenses():
    with open("expenses.csv", "r") as file:
        reader=csv.DictReader(file)
        total=0
        for row in reader:
            total+=float(row["Expense"])
        print("\nTotal Expenses: ", total, "\n")


#menu
print('\t\t\t\t\t\t<------Welcome to the Expense Tracker------>')
while True:
    print("1. Add Expense")
    print("2. Track Expenses by Category")
    print("3. View Total Expenses")
    print("4. Exit")
    choice=int(input("Enter your choice: "))

    if(choice==4):
        print("Thank you for using the Expense Tracker. Goodbye!")
        break

    if(choice==1):
        addExpense()
    elif(choice==2):
        trackExpenses()
    elif(choice==3):
        totalExpenses()
    else:
        print("Invalid choice! Please try again.")


