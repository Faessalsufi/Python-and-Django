class Animal:
    def __init__(self):
        self.age = 1
        print("Animal constructor ")

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor ")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print("Weight: ",m.weight)
print("Age: ",m.age)
