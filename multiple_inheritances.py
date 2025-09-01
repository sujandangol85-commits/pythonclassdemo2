# #multiple(a class is derived from multiples classes)
# class Employee:
#     company="Amazon"
#     def show(self,name,salary):
#         self.name=name
#         self.salary=salary
#         print(f"The name is {self.name} and the salary is {self.salary}")

# class Coder:
#     language="javascript"
#     def showLanguage(self):
#         print(f"Your coding language is {self.language}")

# class Programmer(Employee, Coder):
#     company="Microsoft"
#     def printLanguage(self,name):
#         self.name=name
#         print(f"The name is {self.name} and he is good at coding with {self.language}") #mathiko javascriptyesma ayera basxa


# a=Employee()
# b=Programmer()

# b.show("sujan",340000)
# b.showLanguage()
# b.printLanguage("sujan") #parent class ma vako jun pani function access garna milxa


#multi-level inheritance(a class is derived from a class which is also derived from another class)

class School: #yesle afno matrai access pauxa
    a=1

class Staff(School): #yesle mathi euta ko access pauxa
    b=2

class Student(Staff): #yesle mathi duitaiko access pauxa
    c=3

z=Student()
print(z.a)


