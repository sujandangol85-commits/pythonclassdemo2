# class Employee:
#     company="Amazon"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

# # class Programmer:
# #     company="Microsoft"
# #     def show(self):
# #         print(f"The name is {self.name} and the salary is {self.salary}")

# #     def showLanguage(self):
# #         print(f"The name is {self.name} and he is good at coding with {self.language}")

# class Programmer(Employee): #class programmer is inherited from class employee
#     company="Microsoft"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good at coding with {self.language}")


# a=Employee()
# b=Programmer()
# print(a.company,b.company)


class Animal:
    def __init__(self, name, breed, price):
        self.name = name
        self.breed = breed
        self.price = price

    def sound(self):
        print("woof woof")

    def information(self):
        print(f"Name={self.name} Breed={self.breed} Price={self.price}")

class Dog(Animal):
    def __init__(self, name, breed, price):
        super().__init__(name, breed, price)
        print("Hey, it's the constructor of Dog.")

class Cat(Animal):
    pass

class Cow(Animal):
    pass

dog_object = Dog("Jacky", "German Shepherd", 3500)
dog_object.sound()
dog_object.information()

