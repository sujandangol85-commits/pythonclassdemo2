# randomText="Hello who are you to tell me that i am chatgpt !!"
# fptr=open("file.txt","w")
# fptr.write(randomText + "\n")
# fptr.close()

# fptr=open("file.txt","r")
# reading=fptr.read()
# print(reading)
# fptr.close()

# fptr=open("file.txt","a")
# name=input("Enter your username: ")
# fptr.write(name  + "\n")
# password=input("Enter your password: ")
# fptr.write(password  + "\n")
# fptr.close()


#reading lines
# fptr=open("file.txt","r")
# lines=fptr.readlines() #list ma return garxa, sabai ekaichoti
# print(lines , type(lines))
# fptr.close()

# fptr=open("file.txt","r")
# line1=fptr.readline() #string ma return garxa, ekchoti ma euta matra line
# print(line1 , type(line1))
# line2=fptr.readline() #string ma return garxa, ekchoti ma euta matra line
# print(line2 , type(line2))
# line3=fptr.readline() #string ma return garxa, ekchoti ma euta matra line
# print(line3 , type(line3))
# fptr.close()

#OR
# fptr=open("file.txt","r")
# line=fptr.readline()
# while(line != ""): #file ko item skexi empty string return hunx tesaile
#     print(line)
#     line=fptr.readline()
# fptr.close()



#v.v.v.v.v.v. imp (With statement) close() nalekhda ni hunx yo use garepxi

# with open("file.txt","r") as fptr:
#     print(fptr.read()) #aba close nagarda ni hunx

import csv
with open("demo.csv", "w", newline="") as file:
    writer=csv.writer(file)
    writer.writerow([["Name","Age","Grade","Address"],["John", 25, "A", "New York"],["Jane", 30, "B", "Los Angeles"]])
          