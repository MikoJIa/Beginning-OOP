# Создайте класс Fruit, который имеет:
#
# метод __init__, который устанавливает значения атрибутов name и price:
# название и цена фрукта
#
# методы сравнения. Здесь вы сами решаете какие магические методы реализовывать,
# главное чтобы фрукты могли сравниваться с числами и другими фруктами по цене.
# Смотрите тесты ниже в коде
# Sample Input:
#
# Sample Output:
#
# Good


class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.price == other
        if isinstance(other, Fruit):
            return self.price == other.price

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.price > other
        if isinstance(other, Fruit):
            return self.price > other.price

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.price < other
        if isinstance(other, Fruit):
            return self.price < other.price

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.price >= other
        if isinstance(other, Fruit):
            return self.price >= other.price

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.price <= other
        if isinstance(other, Fruit):
            return self.price <= other.price


apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')

from functools import total_ordering  # Декоратор класса @total_ordering из модуля fanctools
                                      # который позволяет определить в классе лишь метод __eq__()
                                      # и один из методов __lt__(), __le__(), __gt__() или __ge__().
                                      # Все недостающие методы декоратор определит и реализует самостоятельно.


@total_ordering
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, value):
        return self.price == self.check_value(value)

    def __lt__(self, value):
        return self.price < self.check_value(value)

    @staticmethod
    def check_value(value):
        if type(value) == int or isinstance(value, float):
            return value
        elif isinstance(value, Fruit):
            return value.price