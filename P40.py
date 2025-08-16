from abc import ABC, abstractmethod
import math

class Polygon(ABC):

    @abstractmethod
    def area(self):
        pass

class Rect(Polygon):
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5 * self.base*self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return math.pi * self.radius * self.radius

class Square(Polygon):
    def __init__(self, side):
        self.side=side

    def area(self):
        return self.side*self.side

shapes=[Rect(10,5), Triangle(4, 6), Circle(7), Square(3)]
for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area(): .2f}")                