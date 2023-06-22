# Создайте класс Rectangle, который имеет следующие методы:
# метод __init__, который устанавливает значения атрибутов width и height:
# ширина и высота прямоугольника
# магический метод __add__, который описывает сложение двух прямоугольников.
# Результатом такого сложения должен быть новый прямоугольник, в котором ширина и высота
# получились в результате сложения исходных прямоугольников. Новый прямоугольник нужно
# вернуть в качестве результата вызова метода __add__. Сложения с другими типами данных
# реализовывать не нужно
#  магический метод __str__, который возвращает строковое представление  прямоугольника в
#  следующем виде:
# Rectangle({width}x{height})
# Sample Input:
#
# Sample Output:
#
# Rectangle(5x10)
# Rectangle(20x5)
# Rectangle(25x15)

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        raise TypeError

    def __str__(self):
        return f'Rectangle({self.width}x{self.height})'


r1 = Rectangle(5, 10)
assert r1.width == 5
assert r1.height == 10
print(r1)

r2 = Rectangle(20, 5)
assert r2.width == 20
assert r2.height == 5
print(r2)

r3 = r2 + r1
assert isinstance(r3, Rectangle)
assert r3.width == 25
assert r3.height == 15
print(r3)