class operators:
    def __init__(self,number):
        self.number=number

    def __add__(self,n): #a.__add__(b) 
        return self.number + n.number
    
    def __sub__(self,n):
        return self.number - n.number
    
    def __mul__(self,n):
        return self.number * n.number
    
    def __truediv__(self,n):
        return self.number / n.number
    
    def __floordiv__(self,n):
        return self.number // n.number
    

a=sum(10)
b=sum(4)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

