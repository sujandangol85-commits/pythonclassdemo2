# #args
# def add_numbers(*args):
#     return sum(args)

# print(f"The sum is {add_numbers(2, 3)}")     
# print(f"The sum is {add_numbers(2, 3, 5, 9, 10,14)}")  #jati ota argument ni pathauna payo

# def greet(*args):
#     for arg in args:
#         print(f"Hello, {arg}")

# greet("sujan","rita","sita","hari")


#kwargs
# def introduce(**kwargs):  #kwargs becomes a dictionary.
#     for key, value in kwargs.items():  #methods of dictionary
#         print(f"{key}: {value}")

# introduce(name="Sujan", age=19, country="Nepal")

#list comprehension

odd_numbers = [num for num in range(1,10) if num%2==1]

print(odd_numbers)

#dictionary comprehenison

square_numbers=[{num:num*num for num in range(2,8)}]

print(square_numbers)



