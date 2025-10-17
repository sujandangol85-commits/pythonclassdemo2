from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def __init__(self,food):
        self.food=food

class Cat(Animal):
    def __init__(self,food):
        self.food=food


class Rat (Animal):
    def __init__(self,food):
        self.food=food

dog=Dog()  #dog is object of class Dog and also be considered as of class Animal bcoz Dog class is inherited from it