class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal): # Inherits methods from Mammal class
    def bark(self):
        print("BARK")

class Cat(Mammal):   
    def meow(self):
        print("MEOW") 

Dog = Dog()
Dog.walk()
Dog.bark()