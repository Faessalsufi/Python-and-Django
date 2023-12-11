class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def Zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"point({self.x},{self.y})")


# imp point = Point(0,0)
point = Point.Zero()
print(point.draw())
