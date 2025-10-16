# ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉
# decimal to binary

# print(f"\u2080 \u2081 \u2082 \u2083 \u2084 \u2085 \u2086 \u2087 \u2088 \u2089") #subscript
import os

def decimal_to_binary():
    decimal_number = int(input("Enter a decimal number: "))
    print(f"({decimal_number})₁₀ is ", end="")

    binary = []

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary.append(remainder)
        decimal_number //= 2   #or decimal_number = decimal_number // 2

    binary.reverse()
    print("(", end="")
    for bit in binary:
        print(bit, end="")
    print(")₂ in binary", end="")
    print()
    input("\nPress Enter to continue...")
    clear()


def binary_to_decimal():
    binary_number = (input("Enter a binary number: "))
    temp = binary_number
    decimal = 0
    power = 0

    for bit in binary_number[::-1]:
        decimal_number = int(bit) * (2**power)
        decimal += decimal_number
        power +=1

    print(f"({temp})₂ is ({decimal})₁₀ in decimal.")
    input("\nPress Enter to continue...")
    clear()


def decimal_to_octal():
    decimal_number = int(input("Enter a decimal number: "))
    temp = decimal_number
    octal = []

    while decimal_number >0:
        quotient = decimal_number //8
        remainder = decimal_number %8
        decimal_number = quotient
        octal.append(remainder)

    octal.reverse()
    print(f"({temp})₁₀ is (", end="")
    for oct in octal:
        print(f"{oct}", end="")
    print(f")₈ in Octal", end="")
    print()
    input("\nPress Enter to continue ...")
    clear()


def octal_to_decimal():
    octal_number = input("Enter a octal number: ")
    decimal = 0
    power = 0
    for oct in octal_number[::-1]:
        decimal_number = int(oct) * (8 ** power)
        decimal += decimal_number
        power+=1

    print(f"({octal_number})₈ is ({decimal})₁₀ in decimal")
    input("\nPress Enter to continue ...")
    clear()

def decimal_to_hexadecimal():
    decimal_number = int(input("Enter a decimal number: "))
    temp =decimal_number
    hexadecimal = []

    while decimal_number > 0:
        quotient = decimal_number //16
        remainder = decimal_number %16
        decimal_number = quotient
        hexadecimal.append(remainder)

    hexadecimal.reverse()
    print(f"({temp})₁₀ is (", end="")
    for hexa in hexadecimal:
        if hexa == 10:
            hexa = "A"
        elif hexa == 11:
            hexa = "B"
        elif hexa == 12:
            hexa = "C"
        elif hexa == 13:
            hexa = "D"
        elif hexa == 14:
            hexa = "E"
        elif hexa == 15:
            hexa = "F"
        
        print(hexa, end="")

    print(f")₁₆ in Hexadecimal", end="")
    print()
    input("\nPress Enter to continue ...")
    clear()


def hexadecimal_to_decimal():
    hexadecimal_number = input("Enter a hexadecimal number: ")

    decimal = 0
    power = 0

    for hexa in hexadecimal_number[::-1]:
        if hexa == "A":
            hexa = 10
        elif hexa == "B":
            hexa = 11
        elif hexa == "C":
            hexa = 12
        elif hexa == "D":
            hexa = 13
        elif hexa == "E":
            hexa = 14
        elif hexa == "F":
            hexa = 15

        decimal_number = int(hexa) * (16**power)
        decimal +=decimal_number
        power +=1

    print(f"({hexadecimal_number})₁₆ is ({decimal})₁₀ in decimal")
    input("\nPress Enter to continue ...")
    clear()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

print("<--------------- Number Converter --------------->\n")

#menu
while True:
    print("Main Menu")
    print("------------")
    print("1. Decimal to Binary.")
    print("2. Binary to Decimal.")
    print("3. Decimal to Octal.")
    print("4. Octal to Decimal.")
    print("5. Decimal to Hexadecimal.")
    print("6. Hexadecimal to Decimal.")
    print("7.Exit the program.")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        decimal_to_binary()
    elif choice == 2:
        binary_to_decimal()
    elif choice == 3:
        decimal_to_octal()
    elif choice == 4:
        octal_to_decimal()
    elif choice == 5:
        decimal_to_hexadecimal()
    elif choice == 6:
        hexadecimal_to_decimal()
    elif choice == 7:
        break
    else:
        print("Invalid choice, Please choose a valid option !!")

    


