class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")
    
#imp Animal: Parent, Base
#imp Mammal: Child, Sub


class Mammal(Animal):
    #! def eat(self):
    #!     print("eat")
    def walk(self):
        print("walk")

class Fish(Animal):
    #! def eat(self):
    #!     print("eat")

    def swim(self):
        print("swim")

m = Mammal()
print(m.eat())
print(m.age)