import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        print(f'{self.height * self.width:.2f}')

    def diagonal(self):
        print(round(math.sqrt(self.height ** 2 + self.width ** 2), 2))


rectangle1 = Rectangle(height=5, width=6)
rectangle1.area()
rectangle1.diagonal()

rectangle2 = Rectangle(height=3, width=3)
rectangle2.area()
rectangle2.diagonal()
