class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee,Person):
    pass

m = Manager()

m.greet()


#imp A good example of multiple inheritance 


#? If the classes dont have any similar functions then we can use multiple inheritance 

class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer,Swimmer):
    pass

# Because they dont have any similarity 
