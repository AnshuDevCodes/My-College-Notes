import math

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print("X =", self.x)
        print("Y =", self.y)

    def distance(self, p):
        d = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        return d


p1 = Point2D(2, 3)
p2 = Point2D(5, 7)

print("First Point:")
p1.display()

print("Second Point:")
p2.display()

print("Distance between points:", p1.distance(p2))
