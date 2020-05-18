# Exercises 11.3.11


class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        """
        Create a MyTime object initialized to hrs, mins, secs
        Every instance is created with the appropriated attributes
        The values of min and secs may be outside the range 0-59, but
        resulting MyTime object will be normalized
         """

        # Calculate total seconds to represent
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600  # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        """ So it can print MyTime objects nicely """
        return "{}:{}:{}".format(self.hours, self.minutes, self.seconds)

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __add__(self, other):
        """ Adds two MyTime objects and returns a new MyTime object
            that contains their sum
        """
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def increment(self, seconds):
        """ Modifier function that adds seconds to a MyTime object """
        return MyTime(0, 0, self.to_seconds() + seconds)

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        if self.hours > time2.hours:
            return True
        if self.hours < time2.hours:
            return False

        if self.minutes > time2.minutes:  # This will be reaches if the 2 hours are the same
            return True
        if self.minutes < time2.minutes:
            return False
        if self.seconds > time2.seconds:  # Same for the seconds
            return True

        return False

    def better_version_after(self, time2):
        """ Return True if I am strictly greater than time2
            We use the to_second method, which transformed everything
            to seconds and compare it. Way better the version above
        """
        return self.to_seconds() > time2.to_seconds()

    def between(self, start, end):
        return start.to_seconds() <= self.to_seconds() < end.to_seconds()


# Exercise 1
def between(t1, obj, t3):
    return t1.to_seconds() <= obj.to_seconds() < t3.to_seconds()


t1 = MyTime(2, 0, 0)
t2 = MyTime(3, 30, 54)
t3 = MyTime(4, 0, 0)

print(between(t1, t2, t3))

# Exercise 2
print(t1.between(t2, t3))

# Exercise 3
print(t3 > t1)

# Exercise 4
t5 = MyTime(1, 0, 0)
t5.increment(65)  # Does not work I dont know why...
print(t5)
