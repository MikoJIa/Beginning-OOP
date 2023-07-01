import math
from math import pi


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Прямоугольник: {self.a}x{self.b} равен -'

    def get_area(self):
        return self.a * self.b


class Square:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Квадрат: {self.a}x{self.a} равен -'

    def get_area(self):
        return self.a ** 2


class Cirecl:

    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Круг: с радиусом {self.r} равен -'

    def get_area(self):
        return math.pi * self.r ** 2
