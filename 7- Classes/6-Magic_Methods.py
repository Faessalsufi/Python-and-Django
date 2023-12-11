class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"string({self.x},{self.y})"

    def draw(self):
        print(f"without point({self.x},{self.y})")


point = Point(1,2)
print(point)
print(str(point))
