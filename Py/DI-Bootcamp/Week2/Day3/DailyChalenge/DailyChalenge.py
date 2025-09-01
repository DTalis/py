import math

class Circle:
    def __init__(self, *, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=7)

print(c1)  # Circle(radius=5.00, diameter=10.00, area=78.54)
print(c2)  # Circle(radius=5.00, diameter=10.00, area=78.54)

# Area
print(f"Area of c3: {c3.area:.2f}")

# Addition
c4 = c1 + c3
print(c4)  # Circle with combined radius

# Comparisons
print(c1 == c2)  # True
print(c1 > c3)   # False

# Sort circles
circles = [c1, c2, c3, c4]
circles.sort()
print(circles)
