class Car:

    owner="sujan" #class variable can be accessed by all objects ,created outside of constructor

    num_cars=0

    def __init__(self,model,year,price,color,for_sale): #instance variable ho yo sab
        self.model=model
        self.year=year
        self.price=price
        self.color=color
        self.for_sale=for_sale
        Car.num_cars+=1 #instance variable ko lagi self, class variable ko lagi class ko nam

    def drive(self):
        print(f"You are driving {self.color} colored {self.model}.")

    def stop(self):
        print(f"You stopped driving {self.color} colored {self.model}.")

    def info_car(self):
        print(f"Model Number={self.model}, Year={self.year}, price={self.price}, Color={self.color}, Sale={self.for_sale}")