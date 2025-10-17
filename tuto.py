# # to know about the data types
# # a=54.6
# # b=54
# # c="Sujan"
# # d=True
# # print(a, "is ", type(a))
# # print(b, "is ", type(b))
# # print(c, "is ", type(c))
# # print(d, "is ", type(d))
# # print(d, "is ", type(d))

# #  shortcut keyss
# #  alt+shift+down key(copy and paste)
# # alt +cursor(To write more at less time)

# # taking inputs
# # input() function is used to take inputs from the user
# # a=input("Enter your name: ")
# # b=input("ENter a number: ")# the input function takes input as a string unless the datatype is defined at front as below
# # c=int(input("Enter a number: "))#b=string, c=int

# # indexing of stringss
# # positive (start from 0), negative(paxadi bata -1)
# # name= "Sujan"
# # sl=(name[1:4])  #indexing start from 1 but exxcluding 4
# # print(sl)
# # sla=(name[-4: -1]) #indexing start from -1(0=-1,1=-2)
# # print(sla)

# # string functions

# name = " Ajjubhai is noob "
# print(len(name))  # Length including whitespaces → Output: 18
# print(name.endswith("on"))  # False → The string ends with " ", not "on"
# print(name.startswith("Aj"))  # False → Because of the leading space
# print(name.capitalize())  # First letter capitalized, rest lower → " ajjubhai is noob "
# print(name.casefold())  # All lowercase → " ajjubhai is noob "
# print(name.lower())  # Same as above → " ajjubhai is noob "
# print(name.upper())  # All uppercase → " AJJUBHAI IS NOOB "
# print(name.strip())  # Removes leading/trailing whitespaces → "Ajjubhai is noob"
# print(name.replace("Ajjubhai", "Amitbhai"))  
# # No effect! Because original string has capital "A" → Use .lower() or match case
# print(name.find("i")) #indexing (whistespace also counts)

# # escape sequance(Formatting)
# # /n-> newline,\t-> tab space
# # intro="Hello welcome\nback to my youtube channel"
# # print(intro)
# # #\"\" -> to print double qoute on screen
# # name="SUjan is a \"cool\" boy"
# # print(name)
# # # \\ to print backslash
# # ex="Path: C:\\Users"
# # print(ex) 
# # sentence="Ram said to sita \"I am going to marry you\" "
# # print(sentence)
# #         #OR
# # sentence1='Ram said to sita "I am going to marry you" '
# # print(sentence1)


# list2=[1,3,4,"teacher",2,5]

# print(list2.index("teacher"))


for i in range(1,5):
    print(i)