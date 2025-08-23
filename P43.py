class Polygon:
    def area(self):
        pass

class Rect(Polygon):
    def __init__(self, l, b):
        self.length=l
        self.breadth=b

    def calc(self):
        return self.length*self.breadth
    
class Square(Polygon):
    def __init__(self, s):
        self.side=s

    def calc(self):
        return self.side*self.side

class Triangle(Polygon):
    def __init__(self, b, h):
        self.base=b
        self.height=h

    def calc(self):
        return self.height*self.base * 0.5 

class Circle(Polygon):
    def __init__(self, r):
        self.radius=r

    def calc(self):
        return self.radius*self.radius*3.14
    
def print_area(shape: Polygon):
    print(f"The area of {shape.__class__.__name__} is: {shape.calc():.2f}")

shapes=[
    Rect(10, 5),
    Square(6),
    Circle(3),
    Triangle(6, 7)
]

for shape in shapes:
    print_area(shape)
