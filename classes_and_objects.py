class Staff:
    salary=1200000 #this is an class attribute
    address="khokana"

eg_object=Staff()
print(eg_object.salary,eg_object.address)

Ram=Staff()
Ram.name="Ram Shyam Hari Dev" #this is an instance attribute
Ram.address="Lagankhel" #class attribute lai vanda badi object attribute le priority pauxa
print(Ram.name,Ram.salary,Ram.address)

print(type(Staff),type(eg_object))

# Here name is object attribute and salary and address are class attributes as they directly belong to class.
# In the above code, we have created two objects.




# important (SELF)

class Staff:
    salary=1200000 #this is an class attribute
    address="khokana"

    def getInfo(self): #self vannale object ko reference garne yaniki Ram
        print(f"The salary is {self.salary}. The address is {self.address}.")

    def greet(self):
        print("Hello, I am a staff member.")

    @staticmethod
    def intro():
        print("Static wala bina self ko nai run hunx")

Ram=Staff()
Ram.name="Ram Shyam Hari Dev" #this is an instance attribute
Ram.address="Lagankhel" #class attribute lai vanda badi object attribute le priority pauxa
Ram.getInfo()
#OR
# Staff.getInfo(Ram) #yo pass vako ram lai self le accept garxa mathiko bata ni ram pass hunx tara dekhidaina
Ram.greet()
Ram.intro() 

# important (init)

class Staff:
    salary=1200000 #this is an class attribute
    address="khokana"

    def __init__(self,name,salary,address): #dunder method which is automatically called
        print("I am creating an object")
        self.name=name # yo vaneko Ram.name vaneko ho
        self.salary=salary
        self.address=address

    def getInfo(self): #self vannale object ko reference garne yaniki Ram
        print(f"The salary is {self.salary}. The address is {self.address}.")

    def greet(self):
        print("Hello, I am a staff member.")

Ram=Staff("Sujan",1300000,"Lagankhel")
print(Ram.name,Ram.salary,Ram.address)
