# 11.2.6 - Exercises
# Exercise 1


class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        """" Other option. Python interpreter will use our code whenever
         it needs to convert a Point to a string """
        return "({0}, {1})".format(self.x, self.y)


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn  # Corner of the rectangle
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})"\
            .format(self.corner, self.width, self.height)

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        return 2 * (self.width + self.height)

    def flip(self):
        """ Changes the height to the width and the other way around """
        self.width, self.height = self.height, self.width

    def contains(self, point):  # IDK why they say the corner its up left, should be down left
        """ Checks if the point given is inside the rectangle """
        inside = True

        if self.corner.x <= point.x < (self.corner.x + self.width) and \
                self.corner.y <= point.y < (self.corner.y + self.height):
            return inside
        else:
            return not inside


r = Rectangle(Point(0, 0), 10, 5)
print(r.area())

# Exercise 2
print(r.perimeter())

# Exercise 3
r.flip()
print(r)

# Exercise 4
r = Rectangle(Point(0, 0), 10, 5)

print(r.contains(Point(0, 0)))
print(r.contains(Point(3, 3)))
print(not r.contains(Point(3, 7)))
print(not r.contains(Point(3, 5)))
print(r.contains(Point(3, 4.99999)))
print(not r.contains(Point(-3, -3)))
