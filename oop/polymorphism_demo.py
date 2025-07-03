# polymorphism_demo.py

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override area() method.")

class Rectangle(Shape):
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage (can be removed or commented out if not needed)
if __name__ == "__main__":
    shapes = [
        Rectangle(5, 3),
        Circle(4)
    ]
    for shape in shapes:
        print(f"The area is: {shape.area()}")
