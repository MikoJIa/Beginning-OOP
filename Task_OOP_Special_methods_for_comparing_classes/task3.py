# Создайте класс Rectangle, который имеет:
# метод __init__, который устанавливает значения атрибутов width и height:
# ширина и высота прямоугольника
# свойство area, возвращающее площадь прямоугольника
#
# методы сравнения. Здесь вы сами решаете какие магические методы реализовывать,
# главное чтобы прямоугольники могли сравниваться с числами и между собой по значению
# площади. Используйте декоратор  @total_ordering
# Sample Input:
# Sample Output:
# Good

from functools import total_ordering

@total_ordering
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        if isinstance(self.width, (str, bool, float)):
            raise TypeError(f'не корректно введены данные')
        if isinstance(self.height, (str, bool, float)):
            raise TypeError(f'не корректно введены данные')
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        if isinstance(other, int):
            return self.area == other

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        if isinstance(other, int):
            return self.area < other


r1 = Rectangle(3, 4)
assert r1.width == 3
assert r1.height == 4
assert r1.area == 12
assert isinstance(type(r1).area, property), 'Вы не создали property area'

assert r1 > 11
assert not r1 > 12
assert r1 >= 12
assert r1 <= 12
assert not r1 > 13
assert not r1 == 13
assert r1 != 13
assert r1 == 12

r2 = Rectangle(2, 6)
assert r1 == r2
assert not r1 != r2
assert not r1 > r2
assert not r1 < r2
assert r1 >= r2
assert r1 <= r2

r3 = Rectangle(5, 2)
assert not r2 == r3
assert r2 != r3
assert r2 > r3
assert not r2 < r3
assert r2 >= r3
assert not r2 <= r3
print('Good')