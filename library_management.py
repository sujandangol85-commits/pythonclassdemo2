import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Works on Windows (cls) and macOS/Linux (clear)

def librarian_new():
    pass

def customer_new():
    pass

def login_page():
    print(" --------------- Login Page ---------------")
    (" \t-----------------------------------------")

def create_new_page():
    print(" --------------- New Account Registration Page ---------------")
    print(" \t-----------------------------------------")
    while True:
        print("Are you a:")
        print("1. Librarian")
        print("\tor")
        print("2. Customer")
        print("3. Back to main menu")
        try:
            choice = int(input("Enter your answer(1-2): "))

            if choice == 1:
                librarian_new()
            elif choice == 2:
                customer_new()
            elif choice == 3:
                break
            else:
                print("Please enter valid choice. (1 - 3)\n")
        except ValueError:
            print("Please enter between 1-3, no letters allowed.\n")

    

print(" --------------- LIBRARY MANAGEMENT SYSTEM ---------------")
print(" \t-----------------------------------------")

while True:
    print("\n1. Login into existing account")
    print("2. Create a new account")
    print("3. Exit the system")

    try:
        user_choice = int(input("Enter your choice(1-3): "))
        if user_choice == 1:
            login_page()
        elif user_choice == 2:
            create_new_page()
        elif user_choice == 3:
            print("Thank you for using this service !!")
            break
        else:
            print("Please enter valid choice (1-3).\n")
    except ValueError:
        print("Only choose between (1-3) , no letters allowed.\n")
input()
clear()

