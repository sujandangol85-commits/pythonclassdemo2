# age = int(input("Enter your age nalle: "))
# elif(age>=18):
#     print("badda horaha he tu\nCongrats")
# elelif(age>18 and age<=60):
#     print("Kam karne ki umar he teri")
# else:
#     print("Chal nikal budde")

#practice 1

# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
# num3=int(input("Enter third number"))
# num4=int(input("Enter fourth number"))

# elif(num1>num2 and num1>num3 and num1>num4):
#     print(f"{num1} is greatest among all")
# elelif(num2>num1 and num2>num3 and num2>num4):
#     print(f"{num2} is greatest among all")
# elelif(num3>num1 and num3>num2 and num3>num4):
#     print(f"{num3} is greatest among all")
# else:
#     print(num4,"is greatest among ALL")

    #OR

# One-liner version using max()
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))

# greatest = max(num1, num2, num3, num4)
# print(f"{greatest} is the greatest among all.")

#2

# marks1=int(input("Enter your marks in sub1: "))
# marks2=int(input("Enter your marks in sub2: "))
# marks3=int(input("Enter your marks in sub3: "))

# total_marks=marks1+marks2+marks3
# percentage=total_marks/300*100

# elif(percentage >=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("Congratulations !! You have passed in every subject!! ")
#     print(f"Your total percentage:{percentage}")
# else:
#     print("Better luck next time!! ")
#     print(f"Your total percentage:{percentage}")

# print("Keep grinding")

#3

# spam_words=[""Make a lot of money"","buy now","Subscribe this","click this"]

# comment=input("Enter comment: ")

# elif(comment in spam_words):
#     print("Spammer")
# else:
#     print("Not spam")

    #OR

# spam1="make a lot of money"
# spam2="buy now"
# spam3="subscribe this"
# spam4="click this"

# comment=input("Enter comment: ").lower()

# elif((spam1 in comment) or (spam2 in comment) or (spam3 in comment) or (spam4 in comment)):
#     print(f"{comment} is a Spam comment")
# else:
#     print(f"{comment} is not spam")

#4

# name=input("Enter your name: ")
# length=len(name)

# elif(length<10):
#     print("Yes,it contains less than 10 characters!! ")
# else:
#     print("NO")

#5

# example_list=[1,5,43,65,23,65,23,65,234,65,87,76]

# user_input=int(input("Enter a number to check: "))

# elif(user_input in example_list):
#     print("Yees")
# else:
#     print("no")

#6

# total_marks=int(input("Enter your total marks: "))
# if(total_marks>90 and total_marks<=100):
#     print("Your grade is excellent.")
# elif(total_marks>80 and total_marks<=90):
#     print("Your grade is A.")
# elif(total_marks>70 and total_marks<=80):
#     print("Your grade is B.")
# elif(total_marks>60 and total_marks<=70):
#     print("Your grade is C.")
# elif(total_marks>50 and total_marks<=60):
#     print("Your grade is D.")
# else:
#     print("Your grade is F.")

#7

post="Oii sujaan , k xa halkhabar sab thik xa?"

if("sujan" in post):
    print("Yes")
else:
    print("No")

