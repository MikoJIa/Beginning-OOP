# Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:
#
# класс-метод from_diameter, принимающий диаметр круга. Метод from_diameter должен
# возвращать новый экземпляр класса Circle(учитывайте, что экземпляры круга создаются по
# радиусу);
#
# статик-метод is_positive, принимающий одно число. Метод is_positive должен возвращать
# ответ является ли переданное число положительным
#
# статик-метод area, который принимает радиус и возвращает площадь круга.
# Для этого воспользуйтесь формулой
# �
# �
# ∗
# �
# 2
# pi∗r
# 2
#   и в качестве значения pi возьмите 3.14
# Ваша задача только добавить реализацию трех методов в класс Circle
#
# Sample Input:
#
# Sample Output:
#
# circle_1.radius=5.0

from math import pi


class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        r = cls(diameter / 2)
        return r

    @staticmethod
    def is_positive(num: int):
        if num >= 0:
            return True

    @staticmethod
    def area(r):
        area_circle = round(pi, 2) * r ** 2
        return float('{:.2f}'.format(area_circle))


circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 3.14
assert Circle.area(2) == 12.56