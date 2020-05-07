# Exercise 1


class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance(self, target):
        """ Returns the distance between two points"""
        dx = target.x - self.x
        dy = target.y - self.y
        dsquared = dx * dx + dy * dy
        result = dsquared ** 0.5
        return result

    def reflect_x(self):
        """ Returns a point which has the opposite y point """
        return self.x, self.y * (-1)

    def slope_from_origin(self):
        """ Returns the slope between a point and the origin """
        rise = Point().y - self.y
        run = Point().x - self.x
        m = rise / run
        return m

    def get_line_to(self, target):
        """ Returns the line equation between two points """
        rise = target.y - self.y
        run = target.x - self.x
        m = rise / run
        c = self.y - m * self.x
        return m, c

    def midpoint(self, point2, point3):
        """ Returns the point at the middle of the circle """
        dist = 2 * (self.x * (point2.y - point3.y)
                    + point2.x * (point3.y - self.y)
                    + point3.x * (self.y - point2.y))
        rx = ((self.x ** 2 + self.y ** 2) * (point2.y - point3.y)
              + (point2.x ** 2 + point2.y ** 2) * (point3.y - self.x)
              + (point3.x ** 2 + point3.y ** 2) * (self.x - point2.y)) / dist
        ry = ((self.x ** 2 + self.y ** 2) * (point3.x - point2.x)
              + (point2.x ** 2 + point2.y ** 2) * (self.x - point3.x)
              + (point3.x ** 2 + point3.y ** 2) * (point2.x - self.x)) / dist
        return rx, ry


p = Point(3, 4)
q = Point(5, 12)
d = p.distance(q)
print(d)

# Exercise 2
print(p.reflect_x())

# Exercise 3
print(Point(4, 10).slope_from_origin())

# Exercise 4
print(Point(4, 11).get_line_to(Point(6, 15)))
# It will fail if the point "self" is bigger than the point "target"

# Exercise 5
print(Point(4, 11).midpoint(Point(5, 5), Point(7, 3)))
# There is no circle passing through four or more points

# Exercise 6