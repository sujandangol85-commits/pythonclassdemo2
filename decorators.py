#property decorators
class School:
    a=1

    #concept of abstraction and encapsulation
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")

    @property #yo vaneko getter method
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter #mathi define vako nam lai set grne
    def name(self,value):
        self.fname=value.split(" ")[0] #string method split vaneko space vanda agadiko nam lai fname ma haldinx
        self.lname=value.split(" ")[1]

b=School()

b.name="Salmon bhai" #yo nam mathiko name function ma pass hunx
print(b.fname,b.lname)
b.show()