# 1.calculator

# try:
#     number1=float(input("Enter first number: "))
#     number2=float(input("Enter second number: "))
# except ValueError:
#     print("Number hal vaneko thauma letter halxas")
#     exit()

# operator=input("Enter the operator(+ ,- ,/ ,*): ")

# if(operator == "+"):
#     print(f"The sum of {number1} and {number2} is {round(number1 + number2,3)}")

# elif(operator == "-"):
#     print(f"The subtraction of {number1} from {number2} is {round(number2 - number1,3)}")

# elif(operator == "*"):
#     print(f"The product of {number1} and {number2} is {round(number1 * number2,3)}")

# elif(operator == "/"):
#     try:
#         print(f"The division of {number1} and {number2} is {round(number1 / number2,3)}")
#     except ZeroDivisionError:
#         print("0 bata kaile ni divide")

# else:
#     print("Invalid Operator")


# 2.weight converter

# print("Welcome to weight converter")
# print("1.Kilograms to pounds.")
# print("2.Pounds to Kilograms.")
# choice=int(input("Enter your choice: "))

# if choice == 1:
#     weigh=float(input("Enter weight in kilograms : "))
#     weigh_in_pounds=weigh * 2.205
#     print(f"{weigh}kg is {round(weigh_in_pounds,3)}lbs")

# elif choice == 2:
#     weigh=float(input("Enter weight in pounds : "))
#     weigh_in_kgs=weigh / 2.205
#     print(f"{weigh}lbs is {round(weigh_in_kgs,3)}kg")

# else:
#     print("Invalid choice")

# 3.temperature converter

# print("Welcome to temperature converter")
# print("1.celcius to fahreinheit.")
# print("2.fahreinheit to celcius.")
# choice=int(input("Enter your choice: "))

# if choice == 1:
#     temperature=float(input("Enter temperature in celcius : "))
#     temperature_in_F=temperature * (9/5) +32
#     print(f"{temperature}C is {round(temperature_in_F,3)}F")

# elif choice == 2:
#     temperature=float(input("Enter temperature in Fahreinheit : "))
#     temperature_in_c=(temperature - 32) *(5/9)
#     print(f"{temperature}F is {round(temperature_in_c,3)}C")

# else:
#     print("Invalid choice")


#4. Email slicer

# email=input("Enter your email: ")

# print(email.index("@"))
# index=email.index("@") #if email is sujan@gmail.com then 5 will be stored at variable index

# username=email[0:index] #index 5 vanda agadiko but not including 5 itself(0 is optional)
# domain=email[index + 1:] #index 5 vanda paxadiko (+1 halyo vanechai @ paxi bata or 6 bata start hunx)

# print(f"Username={username} Domain={domain}")


#5. compound interest calculator

# class InsufficientPrincipalError(Exception):
#     def __init__(self, message="Principal amount cannot be less or equal to zero"):
#         super().__init__(message)

# class InsufficientRateError(Exception):
#     def __init__(self, message="Rate cannot be less than or equal to zero"):
#         super().__init__(message)

# class InsufficientTimeError(Exception):
#     def __init__(self, message="Time cannot be less or equal to zero"):
#         super().__init__(message)

# try:
#     principal = float(input("Enter principal amount: "))
#     if principal <= 0:
#         raise InsufficientPrincipalError()

#     rate = float(input("Enter rate of interest: "))
#     if rate <= 0:
#         raise InsufficientRateError()

#     time = float(input("Enter time in years: "))
#     if time <= 0:
#         raise InsufficientTimeError()

#     # Compound interest formula
#     amount = principal * pow((1 + rate/100), time)
#     print(f"Balance after {time} years = ${round(amount, 2)}")

# except ValueError:
#     print("Invalid input! Please enter numeric values only.")
# except (InsufficientPrincipalError, InsufficientRateError, InsufficientTimeError) as e:
#     print("Error:", e)

# finally:
#     print("Thank you for working with us !!")


# 6. countdown timer 

# import time

# user_time=int(input("Enter the time in seconds: "))

# for countdown in range(user_time,0,-1): #negative indexing
#     seconds =countdown%60 # if countdown is 68 secs then %60 would be 1 min and 8 secs
#     minutes=int(countdown/60)%60
#     hours=int(countdown/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}") #pads with zero if the number is less than 2 digits
#     time.sleep(1)

# print("TIMES UPP !!!! ")



# 7. clock

# import time

# # Get local time
# local_time = time.localtime()

# # Format time as YYYY-MM-DD HH:MM:SS
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

# print(f"Current local time in Nepal: {formatted_time}")


# 8. shopping cart 

# print("<----- Welcome to Shopping Cart ----->")

# cart = []  # Move outside loop

# while True:
#     print("\n1. Add item")
#     print("2. View Total")
#     print("3. Quit Program")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         food_name = input("Enter food's name: ")
#         food_price = float(input("Enter food's price: "))
#         cart.append([food_name, food_price])
#         print(f"{food_name} added to cart.")

#     elif choice == 2:
#         if not cart:
#             print("Your cart is empty.")
#         else:
#             total = 0
#             print("\nItems in your cart:")
#             for item_name, item_price in cart:
#                 print(f"->{item_name}: ${item_price}")
#                 total += item_price
#             print(f"\nTotal = ${round(total,3)}")

#     elif choice == 3:
#         print("Exiting program... Thank you for shopping!")
#         break

#     else:
#         print("Invalid choice. Please try again.")

# 9.Quiz Game

# print("<------ Welcome to Quiz Game ------>\n")

# questions = ("1.How many elements are there in periodic Table?", #can also use lists
#              "2.Which animal lays the largest eggs?",
#              "3.What is the most abundant gas in the Earth's atmosphere?",
#              "4.How many bones are there in human body?",
#              "5.Which planet in the solar system is the hottest?")

# answers = (("A: 116", "B: 117", "C: 118", "D: 119"),
#            ("A: Whale", "B: Crocodile", "C: Ostrich", "D: Elephants"),
#            ("A: Nitrogen", "B: Oxyegn", "C: Helium", "D: Hydrogen"),
#            ("A: 206", "B: 207", "C: 208", "D: 209"),
#            ("A: Mercury", "B: Venus", "C: Earth", "D: Mars"))

# correct_options = ("C", "C", "A", "A", "B")
# question_num = 0
# score = 0
# guesses = []

# for question in questions:
#     print("------------------------------------")
#     print(question)
#     for answer in answers[question_num]:
#         print(answer)

#     guess = input("Enter your answer (A, B, C, D): ").upper()
#     if guess == correct_options[question_num]:
#         score +=1
#         print("CORRECT ")
#     else:
#         print("INCORRECT")
#         print(f"The correct answer was {correct_options[question_num]}")
#     question_num+=1

# print("Well played Boy !!!")
# print(f"You guessed {score} out of {question_num} correct.")

# 10.Menu program

# print("--------------- Menu ---------------")
# print("------------------------------------")

# menu = {
#     "Popcorn": 3.54,
#     "Cheeseburger": 54.65,
#     "Chilly Pizza": 43.32,
#     "Hotdogs": 90.43,
#     "Lemonade": 45,
#     "Milk Tea": 50,
#     "Americano": 100
# }

# order = []
# total = 0

# # Display menu
# for key, value in menu.items():
#     print(f"{key:25} ${value:.2f}")

# # Take orders
# while True:
#     user_input = input("Select your food (q to quit): ").strip().title() #title function le harek word ko first letter capital garaidinxa
#     if user_input.lower() == "q":
#         break
#     elif user_input in menu:
#         order.append(user_input)
#     else:
#         print("Item not found in menu. Please try again.")

# # Display cart
# print("\n--------------- Your Cart ---------------")
# for item in order:
#     price = menu[item]
#     print(f"- {item:20} ${price:.2f}")
#     total += price

# print("-----------------------------------------")
# print(f"Your total is: ${total:.2f}")


# 11. number guessing game

# from random import randint

# class NotNumberError(Exception):
#     def __init__(self, message="Please enter a valid number"):
#         super().__init__(message)

# highest_num=100
# lowest_num=1
# print("Welcome to number guessing game !!")
# answer = randint(lowest_num , highest_num)
# guesses = 0

# print(f"The number is between {lowest_num} and {highest_num}")
# while True:
#     try:
#         try:
#             guess = int(input("\nMake your guess: "))
#             guesses +=1
#         except ValueError:
#             raise NotNumberError()
#     except NotNumberError as e:
#         print(e)
#         continue
    
#     if(guess > answer):
#         print("INCORRECT, Too high !!")
#     elif guess <answer:
#         print("INCORRECT, Too low!!")
#     else:
#         print("CORRECT, CONGRATSS !!")
#         break

# print("The correct answer is ",answer)
# print(f"You took total {guesses} guesses. ")
    

# # 12. rock scissor paper game

# import random


# options = ("rock", "paper", "scissor")

# print("Welcome to Rock, Scissors, Paper Game\n")

# while True:
#     user=input("Make your move:(rock,scissor,paper): ").lower()
#     while user not in options:
#         user=input("Please make your move correctly:(rock,scissor,paper): ").lower()

#     bot = random.choice(options)
#     print(f"Computer Choice: {bot:>18}")
#     print(f"Player Choice: {user:>20}")

#     if user == bot:
#         print("Draw !!")
#     elif user == "paper" and bot == "rock":
#         print("You win !!")
#     elif user == "scissor" and bot == "paper":
#         print("You win !!")
#     elif user == "rock" and bot == "scissor":
#         print("You win !!")
#     else:
#         print("You lose !!")

#     once_again=input("Do you wanna play again(y/n): ").lower()
#     if(once_again !="y"):
#         print("Thanks for playing!!")
#         break

# 13.dice roller program

# import random

# # Dice faces using ASCII art
# dice_art = {
#     1: (
#         "┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘",
#     ),
#     2: (
#         "┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘",
#     ),
#     3: (
#         "┌─────────┐",
#         "│ ●       │",
#         "│    ●    │",
#         "│       ● │",
#         "└─────────┘",
#     ),
#     4: (
#         "┌─────────┐",
#         "│ ●     ● │",
#         "│         │",
#         "│ ●     ● │",
#         "└─────────┘",
#     ),
#     5: (
#         "┌─────────┐",
#         "│ ●     ● │",
#         "│    ●    │",
#         "│ ●     ● │",
#         "└─────────┘",
#     ),
#     6: (
#         "┌─────────┐",
#         "│ ●     ● │",
#         "│ ●     ● │",
#         "│ ●     ● │",
#         "└─────────┘",
#     ),
# }

# # --- Input section ---
# while True:
#     try:
#         num_dice = int(input("How many dice do you want to roll? "))
#         if num_dice <= 0:
#             print("Please enter a positive number.")
#             continue
#         break
#     except ValueError:
#         print("Enter a valid number.")

# # --- Rolling dice ---
# dice_values = [random.randint(1, 6) for i in range(num_dice)]

# # for i in range(user): #vertical
# #    for j in dice_art.get(dice[i]):
# #       print(f"{j}",end="")

# # --- Printing dice horizontally ---
# print("\nYour dice:\n")
# for line in range(5):  # each die has 5 lines of art
#     for value in dice_values:
#         print(dice_art[value][line], end="  ")  # two spaces between dice
#     print()

# # --- Display results ---
# total = sum(dice_values)
# print(f"\nYou rolled: {dice_values}")
# print(f"Your total is: {total}")

# 14. password generator

import string
import random

somewords =string.digits + string.punctuation + string.ascii_letters

spacing = int(input("Enter the length of password: "))
password = []
for i in range(spacing):
    fake=random.choice(somewords)
    password.append(fake)

print(f"Password:",end="")
for pas in password:
    print(pas,end="")
print()












    







