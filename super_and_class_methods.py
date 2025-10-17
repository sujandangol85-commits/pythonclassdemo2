# #super method
# class School:
#     def __init__(self):
#         print("Constructor of School")

# class Staff(School):
#     def __init__(self):
#         super().__init__() #yesko super class ko constructor pani sangai run hunx
#         print("Constructor of Staff")

# class Student(Staff):
#     def __init__(self):
#         super().__init__() #yesko super class ko constructor pani sangai run hunx
#         print("Constructor of Student")

class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

    def des(self):
        print(f'It is {self.color} and status={self.filled}')


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius=radius

    def info(self):
        print(f"The color of circle is {self.color} and radius is {self.radius}. Status={self.filled} the area is {3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, color, filled, length):
        super().__init__(color,filled)
        self.length=length
        
    def info(self):
        print(f"The color of square is {self.color} and length is {self.length}. Status={self.filled}  the area is {self.length * self.length}")
class Triangle(Shape):
    def __init__(self, color, filled, length, width):
        super().__init__(color,filled)
        self.length=length
        self.width=width
    
    def info(self):
        print(f"The color of triangle is {self.color}, width is {self.width} and length is {self.length}. Status={self.filled}  the area is {self.length *self.width}")
circle= Circle(color="Blue",filled=True,radius=3.1490)
square=Square(color="Red",filled=False,length=8.1490)
triangle= Triangle(color="White",filled=True,length=4.90,width=56)

circle.info()
circle.des()
square.info()
square.des()
triangle.info()

# z=Student()


# # class method

# class Employee:
#     a=1
#     @classmethod #yo rakhena vane chai show function le 90 dekhauxa 
#     def show(cls): #classmethod rakhda self ko thauma cls rakhne
#         print(f"The value of a is {cls.a}")

# e=Employee()
# e.a=90
# e.show() 

