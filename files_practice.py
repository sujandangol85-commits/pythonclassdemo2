#1.
# with open("files_practice.txt","r") as f:
#     content=f.read()
#     if("twinkle" in content.lower()):
#         print("The word 'twinkle' is present in the file")
#     else:
#         print("The word 'twinkle' is not present in the file")

#2.

# import random

# with open("files_practice.txt","r") as f:
#     hi_score=f.read()
#     hi_score=int(hi_score)

# def game():
#     print("Welcome to the game!!")
#     score=random.randint(1,100)
#     print(f"Your score is {score}")
#     if(score> hi_score):
#         f=open("files_practice.txt","w")
#         f.write(str(score))
#         print("The new high score is",score)
#         print("You have won")
#     else:
#         print("You lose !!")

# game()

#3

# with open("files_practice.txt","r") as f:
#     content=f.read()
#     if("donkey" in content):
#         content=content.replace("donkey","monkey")

# with open("files_practice.txt","w") as fp:
#         fp.write(content)

#4

# words=["fuck","motherfucker","bitch","xxx","porn","horny"]
# with open("files_practice.txt","r") as f:
#     content=f.read()


# for word in words:
#     content=content.replace(word, "#" * len(word))

# with open("files_practice.txt","w") as fp:
#       fp.write(content)

#5

# with open("files_practice.txt","r") as f:
#     lines=f.readlines()

# lineno=1
# for line in lines:
#     if("python" in line):
#         print(f"Python is mentioned in line number {lineno}")
#         break
#     lineno+=1
    
# else:
#     print("Python is not mentioned in the file")

#6.
# with open("files_practice.txt","r") as f:
#     content=f.read()

# with open("files_practice1.txt","r") as fp:
#     content1=fp.read()

# if(content==content1):
#     print("Both files are identical")
# else:
#     print("Both files are different")

#7

import os
os.rename("files_practice1.txt","hawa.txt")


        

      
