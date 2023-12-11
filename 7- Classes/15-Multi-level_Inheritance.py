class Animal:

    def eat(self):
        print("eat")


class Bird(Animal):

    def fly(self):
        print("fly")

class Chicken(Bird):
    pass #? Inheritance abuse

#imp 1 or 2 level of inheritance is good beyond that is not a good practice 

# Multiple level inheritance can be problematic

# Employee - Person - LivingCreature - Thing