import math

# -------------------------
# Base Class
# -------------------------
class Shape:
    def area(self):
        return 0


# -------------------------
# Derived Class: Triangle
# -------------------------
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# -------------------------
# Derived Class: Circle
# -------------------------
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# -------------------------
# Derived Class: Rectangle
# -------------------------
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# -------------------------
# Main Program
# -------------------------
print("Area of Triangle, Circle and Rectangle using Inheritance")

# Triangle
t = Triangle(10, 5)
print("Area of Triangle:", t.area())

# Circle
c = Circle(7)
print("Area of Circle:", c.area())

# Rectangle
r = Rectangle(8, 4)
print("Area of Rectangle:", r.area())
