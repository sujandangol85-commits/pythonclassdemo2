# class Programmer:
#     company="Microsoft"

#     def __init__(self,name,address,salary):
#         self.name=name
#         self.address=address
#         self.salary=salary

# programmer1=Programmer("Ram","Khokana",30000)
# print(programmer1.company,programmer1.name,programmer1.address,programmer1.salary)
# programmer2=Programmer("Shyam","Bungamati",304000)
# print(programmer2.company,programmer2.name,programmer2.address,programmer2.salary)
# programmer3=Programmer("Budha","Jhamsikhel",303000)
# print(programmer3.company,programmer3.name,programmer3.address,programmer3.salary)


# class Calculator:

#     @staticmethod
#     def greet():
#         print("Hello")

#     def __init__(self,number):
#         self.number=number

#     def square(self):
#         print(f"The square of {self.number} is {self.number*self.number}")

#     def cube(self):
#         print(f"The cube of {self.number} is {self.number*self.number*self.number}")

#     def root(self):
#         print(f"The squareroot of {self.number} is {self.number**0.5}")

# num1=Calculator(int(input("Enter a number: ")))
# num1.greet()
# num1.square()
# num1.cube()
# num1.root()

# class random:
#     a="goa"


# j=random()
# j.a="o"
# print(j.a)


from random import randint
class Train:
    company="Indian Railways"
    seats=40
    fare=450

    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self, fro, to):
        print(f"Ticket is booked for train number{self.trainNo} from {fro} to {to}")

    def getStatus(oii):  #self ko satta j lekhda ni hunx
        print(f"Train number {oii.trainNo} is operating successfully")

    def getFare(self,fro,to):
        print(f"ticket fare in train number{self.trainNo} from {fro} to {to} is {randint(450,4500)}")



p=Train(input("Enter train number: "))
p.book("Pokhara","Kathmandu")
p.getStatus()
p.getFare("Jamal","Jawalakhel")


    


