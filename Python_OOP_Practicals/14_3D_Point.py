import math

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt(
            (self.x - p.x)**2 +
            (self.y - p.y)**2
        )


class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # Override distance method
    def distance(self, p):
        return math.sqrt(
            (self.x - p.x)**2 +
            (self.y - p.y)**2 +
            (self.z - p.z)**2
        )


p1 = Point3D(2, 3, 4)
p2 = Point3D(5, 7, 8)

print("Distance between 3D points:", p1.distance(p2))
