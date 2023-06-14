# Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
# конструктор __init__, принимающий произвольное количество аргументов.
# Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в
# атрибут values в виде списка;
# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим
# образом:
# «Вектор(<value1>, <value2>, <value3>, ...)», если вектор не пустой.
# При этом значения должны быть упорядочены по возрастанию (будьте аккуратнее с пробелами,
# они стоят только после запятых, см. пример ниже);
# «Пустой вектор», если наш вектор не хранит в себе значения
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2) # печатает "Пустой вектор"
# Sample Input:
#
# Sample Output:
#
# Вектор(1, 2, 3)
# Пустой вектор
# Вектор(1, 2, 3)
# Пустой вектор


class Vector:

    def __init__(self, *args):
        self.values = []
        for i in args:
            if not isinstance(i, (float, bool, str, list)):
                self.values.append(i)

    def check_values(self):
        if len(self.values) > 0:
            self.values = tuple(sorted(self.values))
            return True
        return False

    def __str__(self):
        if Vector.check_values(self) is True:
            return str(f'Вектор{self.values}')
        return str('Пустой вектор')


v1 = Vector(1, 2, 3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector()
assert isinstance(v2, Vector)
assert str(v2) == 'Пустой вектор'

v3 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
assert isinstance(v3, Vector)
assert sorted(v3.values) == [1, 2, 3]
assert str(v3) == 'Вектор(1, 2, 3)'

v4 = Vector([4, 5], 'hello')
assert str(v2) == 'Пустой вектор'
assert v2.values == []

v5 = Vector(1, 2, True)
assert isinstance(v5, Vector)
assert str(v5) == 'Вектор(1, 2)'

print(v1)
print(v2)
print(v3)
print(v4)


# another solution

class Vector:

    def __init__(self, *args: int) -> None:
        self.values = Vector.is_integer(*args)

    @staticmethod
    def is_integer(*args: int) -> list:
        return sorted([i for i in args if type(i) == int])

    def __str__(self):
        return f'Вектор{tuple(self.values)}' if self.values else 'Пустой вектор'
