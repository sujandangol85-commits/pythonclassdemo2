#1. factorial

def factorial(num):
    if(num<=1):
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter a number: "))
if(num<0):
    print("Factorial of negative numbers cannot be calculated!! Don\'t you know?")
else:
    print(f"The factorial of {num} is {factorial(num)}")

