#1. while loop
# i=1
# while(i<=50):
#     print(i)
#     i +=1 #(i=i+1) #note: i++,i-- (Increment/decrement doesn't exist in python)

# example_list=[1,2,3,"Sujan","jake","paul",False]
# i=0

# while(i<len(example_list)):
#     print(example_list[i])
#     i=i+1

# example_tuple=(1,2,3,"Sujan","jake","paul",False)
# i=0

# while(i<len(example_tuple)):
#     print(example_tuple[i])
#     i=i+1


#2.for loop

# for i in range(1,6): #range(start, stop, step) 1 dekhi 5 smma janx last value ko -1, just like indexing
#     print(i)

# ✅ Parameters of range(start, stop, step)
# Parameter	Description
# start->	The beginning value (default is 0)
# stop->	The loop runs until just before this value
# step->	The amount by which the value increases or decreases

#for odd
# for i in range(1,100,2):
#     print(i)
# #for even
# for i in range(2,100,2):
#     print(i)

#third wala chai thyakka difference xuttauna (slicing)

# example_list=[1,2,3,"Sujan","jake","paul",False]

# for i in range(len(example_list)):
#     print(example_list[i])

#     #OR
# for i in example_list:
#     print(i)

# name="Sujan"

# for i in name:
#     print(i)

#important ones

#for loop with else

# example_list=[1,2,3,"Sujan","jake","paul",False]

# for i in example_list:
#     print(i)
# else:
#     print("The list item has ended") #loop sakepxi last ma else execute hunx

#break 

# for i in range(50):
#     if(i==27):
#         break #exit loop right after this
#     print(i)

#continue

# for i in range(50):
#     if(i==27):
#         continue #thyakka jun vneko xa tyo wala lai skip garera agadi badne
#     print(i)

#pass

for i in range(50):
    pass #instructs the program to do nothing for loop ko kei kam hudaina siddhai tala ko code execute huna janx

name="sujan"
print(name)





