class Point:
    default_color = "blue"

    def __init__(self, x, y):
        self.x = x #? instense attribute 
        self.y = y

    def draw(self):
        print(f"point({self.x},{self.y})")


Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
print(point.x)
print(point.draw())

another = Point(3, 4)

print(another.default_color)
print(another.draw())


#! class level attribute share with all instenses of class if we change the value it will affect all the values