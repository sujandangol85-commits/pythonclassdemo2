# def sum(): #function definition
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))

#     sum=num1+num2
#     print("Sum=",sum)

# sum() #function call

# def greet():
#     print("K xa khabar")

# press=input("Press any key for surprise!!")
# greet()

#IMPORTANT(funtion with argument)

# def greet(name,salutation): #name->parameter
#     print("K xa khabar,"+name)
#     print(salutation)

# greet("sujan","Thank you") #sujan->argument
# greet("Raj","Thank you") #raj->argument
# greet("grish","Thank you") #grish->argument

#IMPORTANT(funtion with argument) + return value

# def greet(name,salutation): #name->parameter
#     print("K xa khabar,"+name)
#     print(salutation)
#     return "haha"

# a=greet("sujan","Thank you") #sujan->argument
# print (a) #a ma function bata return vyera ako value ayera basxa

# def sum(a,b):
#     return a+b

# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))

# print(f"The sum is {sum(a,b)}")


#ANOTHER IMPORTANT (DEFAULT VALUE OF ARGUMENT AND PARAMETER)

def greet(name,salutation="dhanyabad"): #yeslai default parameter bhanincha (salutation), yedi call bata pass gariyena vne yesko dekhauxa , yedi tala bata pass garyo bhane pass greko wala nai dekhauxa
    print("K xa khabar,",name)
    print(salutation)

greet("sujan") #sujan->argument







