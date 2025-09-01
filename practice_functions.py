#1. to find greatest

# def greatest(num1,num2,num3):
#     if(num1>num2 and num1>num3):
#         print(f"{num1} is greatest")
#     elif(num2>num1 and num2>num3):
#         print(f"{num2} is greatest")
#     else:
#         print(f"{num3} is greatest")

# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))

# greatest(num1,num2,num3)

#2. to convert c to f

# def converter(temp):
#     return (temp * 9/5) + 32 

# temp=float(input("Enter temprature in celcius: "))
# print(f"The converted temprature is {round(converter(temp),2)}° Fahreinheit ") #round figure decimal value to 2(.2f)

#3.prevent python to print new line

# print("Hello",end="")
# print(",Sujan")

#4. recursive funtion for sum of n natural numbers

# def sum(num):
#     if(num==1):
#         return 1
#     else:
#         return num+ sum(num-1)
    
# num=int(input("Enter the number of terms: "))
# print("The sum is ",sum(num))

#5. pattern 

# def pattern(num):
#     if(num==0):
#         return #yeta yesle kehi return garna ko sato function lai end garidinx
#     else:
#         print("*"*num)
#         pattern(num-1)


# num=int(input("Enter the number of terms: "))
# pattern(num)

#6. to convert inches to cm

# def converter(inch):
#     return inch * 2.54


# inch=float(input("Enter inches: "))
# print(f"centimeter= {round(converter(inch),2)} ") #round figure decimal value to 2(.2f)

#7. remove an item from list and strip() also #strip vannale certain character lai remove garne

# def remove(example_list,text):
#     for item in example_list:
#         example_list.remove(text)
#         return example_list

# example_list=["Sujan","Raju","Kaju","Vaju"]
# print(remove(example_list,"Vaju"))

# def remove(example_list,text):
#     eg_list=[]
#     for item in example_list:
#         if not(item==text):
#             eg_list.append(item.strip(text))
    
#     return eg_list


# example_list=["Sujan","Raju","Kaju","Vaju"]
# print(remove(example_list,"ju")) #ju vako word jati lai hataidine ani naya list ma haleko

#8. multiplication table

def table(num):
    for i in range(1,10+1):
        print(f"{num}*{i}={num*i}")
    

num=int(input("Enter the number: "))
table(num)
    






    

