#super method
class School:
    def __init__(self):
        print("Constructor of School")

class Staff(School):
    def __init__(self):
        super().__init__() #yesko super class ko constructor pani sangai run hunx
        print("Constructor of Staff")

class Student(Staff):
    def __init__(self):
        super().__init__() #yesko super class ko constructor pani sangai run hunx
        print("Constructor of Student")

z=Student()


# class method

class Employee:
    a=1
    @classmethod #yo rakhena vane chai show function le 90 dekhauxa 
    def show(cls): #classmethod rakhda self ko thauma cls rakhne
        print(f"The value of a is {cls.a}")

e=Employee()
e.a=90
e.show() 

