# from car import Car

# car1 = Car("BMW",1992,980000,"SnowWhite",True)
# car2 = Car("MUSTANG",2092,580000,"Black",False)
# car3 = Car("Lamborgini",3022,9800000,"vivid White",True)

# car1.info_car()
# print(f"Owner={Car.owner}") #class variable lai class kai nam vnda call garda ramro rather than calling it from object's name
# print(f"The number of cars are:{Car.num_cars}")
# car3.drive()
# car3.stop()

#important 

# abstract base class (abc)

from abc import ABC,abstractmethod 

class Vehicle(ABC): #abstract class ko directly kunai object banauna mildaina

    @abstractmethod
    def go(self):
        pass #only declare them but not define them

    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def go(self):
        print("You are driving the bike")

    def stop(self):
        print("You are stopping the bike")

class Car(Vehicle):
    def go(self):
        print("You are driving the Car")

    def stop(self):
        print("You are stopping the Car")


bike=Bike()
bike.go()


