class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m,Mammal))
print(isinstance(m,Animal))
print(isinstance(m,object)) #imp Indirectly inherit the object class by default which gives the magic methods

print(issubclass(Mammal,Animal))
print(issubclass(Mammal,object))
print(issubclass(Animal,object))
#? Every class is a sub-class of object class