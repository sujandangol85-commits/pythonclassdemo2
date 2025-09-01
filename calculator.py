def add(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1 + num2}")

def subtract(num1, num2):
    print(f"The subtraction of {num1} and {num2} is {num1 - num2}")

def product(num1, num2):
    print(f"The product of {num1} and {num2} is {num1 * num2}")

def division(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The division of {num1} by {num2} is {num1 / num2}")

print("Welcome to calculator\n")

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        add(num1, num2)
    elif choice == 2:
        subtract(num1, num2)
    elif choice == 3:
        product(num1, num2)
    elif choice == 4:
        division(num1, num2)
    else:
        print("Invalid choice")
