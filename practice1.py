#practice set
# name=input("Please enter your name: ")
# print("Good Afternoon,",name,"\nHow can I help you?")
#           #OR
# print(f"Good Afternoon, {name}") #fstring

# name=input("Enter your name: ")
# dat=input("Enter date: ")
# print("Dear",name,",\n You are selected !\n",dat)
#           #OR
# problem="""Dear |<Name>|,
#             You are selected
#             <|Date|>"""
# print(problem.replace("|<Name>|","Sujan").replace("<|Date|>","2 July 2008"))

# #detect double spaces
# name="Sujan is a bad boyy!"
# if "  " in name:
#     print("Double spaces detected!")
#          #OR
# print(name.find("  ")) #if there is no double space then return -1, otherwise....return index of space
# print(name.find("o")) #return index of character in parent string

#detect single spaces
name="Sujanis goodboy"
print(name.find(" "))
if " " in name:
    print("Single space detected")
#replace
print(name.replace(" ","  ")) #single space to double
print (name) #name jasta ko testai rahanxa je jati change grda ni (string is immutable)
