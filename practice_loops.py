#1. multiplication table

# num=int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{num}*{i}=",num*i)

#2. greet person with names "s"

# l=["Sujan","Lisa","harry","Sachin"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello,{name}")

#3. multiplication table(while)

# num=int(input("Enter a number: "))
# i=1
# while(i<=10):
#     print(f"{num}*{i}={num*i}")
#     i+=1

#4. prime or not

# count=0
# num=int(input("Enter a number: "))
# for i in range(1,num +1):
#     if(num%i==0):
#         count+=1

# if(count==2):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not prime number")

    #OR

# num=int(input("Enter a number: "))

# for i in range(2,num):
#     if(num%i==0):
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")

#5. sum of n natural numbers

# i=1
# num=int(input("Enter the number of terms: "))
# sum=0
# while(i<=num):
#     sum+=i
#     i+=1
# print("The sum is",sum)

#6. factorial

# i=1
# fact=1
# num=int(input("Enter the number: "))
# for i in range(1,num+1):
#     fact*=i
# print("Factorial=",fact)

#7. pattern

# n=int(input("Enter the term: "))
# for i in range(1,n+1):
#     print(" "* (n-i), end=" ")  #end=" " print le dine wala new line(bydefault) lai cancel garna ko lagi
#     print("*"* (2*i-1), end=" ") #here * means reppeating the strings(outside bracket wal ) mtlb agadi ko bracket ma vakolai kati choti repeat grne vnera pxadi ko brackeet le vnxa
#     print(" ")

#8 another pattern

# n=int(input("Enter the term: "))

# for i in range(1,n+1):
#     print("*"*(2*i-1),"\n")

#     #OR
# for i in range(1,n+1):
#     print("*"*i,"\n")

#9 another pattern (hyaaaaaaaaaaaaaa!!!)

# n=int(input("Enter the term: "))

# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="") 
#     print("")

#10. multiplication table(reversed)

num=int(input("Enter a number: "))

for i in range(10,0,-1):
    print(f"{num}*{i}=",num*i)



