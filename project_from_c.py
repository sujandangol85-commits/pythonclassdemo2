#1. CALCULATOR

# while True:
    # num1 = int(input("Enter first number: "))
    # num2 = int(input("Enter second number: "))
    # operator = input("Enter operator (+, -, *, /): ")

    # if operator == '+':
    #     print(f"Sum of {num1} and {num2} is {num1 + num2}.")
    # elif operator == '-':
    #     print(f"Difference of {num1} and {num2} is {num1 - num2}.")
    # elif operator == '*':
    #     print(f"Product of {num1} and {num2} is {num1 * num2}.")
    # elif operator == '/':
    #     if num2 != 0:
    #         print(f"Quotient of {num1} and {num2} is {num1 / num2}.")
    #     else:
    #         print("Division by zero is not allowed.")
    # else:
    #     print("Invalid operator. Program will exit.")
    #     break  # Exit the loop

    # input("Press Enter to continue...\n")


#2. Armstrong

# num=int(input("Enter a number: "))
# sum=0
# temp=num
# while(num>0):
#     r=num%10
#     sum=sum+(r*r*r)
#     num=num//10 #Double // vneko integer division (float value return gardaina)

# if(sum==temp):
#     print(f"{temp} is an armstrong number.")
# else:
#     print(f"{temp} is not an armstrong number.")

#3. palindrome

# num=int(input("Enter a number: "))
# rev =0
# temp=num
# while(num>0):
#     r=num%10
#     rev=rev*10+r
#     num=num//10 #Double // vneko integer division (float value return gardaina)

# if(rev==temp):
#     print(f"{temp} is a palindrome number.")
# else:
#     print(f"{temp} is not a palindrome number.")

#3. palindrome(strings)

# text = input("Enter a string or number: ")
# if text == text[::-1]:
#     print(f"{text} is a palindrome.")
# else:
#     print(f"{text} is not a palindrome.")

#4. student records(sort):

# l=["sujan","lisa","zayn","alice","border"]

# l.sort()

# print(l)

l=[]

for i in range(1,6):
    name=input(f"Enter student {i} name: ")
    l.append(name)

l.sort()
print(l)








