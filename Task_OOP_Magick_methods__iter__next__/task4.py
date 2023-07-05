# Создайте класс PowerTwo, который возвращает следующую степень двойки,
# начиная с нулевой степени (20=1). Внутри класса реализуйте:
# метод __init__. Он должен принимать одно положительное число - степень двойки,
# до которой нужно итеририроваться включительно (см пример ниже)
# методы __iter__ и __next__ для итерирования по степеням двойки
# for i in PowerTwo(4): # итерируемся до 4й степени двойки
#     print(i)
# # Цикл выше печатает следующие числа
# 1
# 2
# 4
# 8
# 16
# numbers = PowerTwo(2)
#
# iterator = iter(numbers)
#
# print(next(iterator)) # печатает 1
# print(next(iterator)) # печатает 2
# print(next(iterator)) # печатает 4
# print(next(iterator)) # исключение StopIteration
# Sample Input:
#
# Sample Output:
#
# Элементы итератора PowerTwo(2)
# 1
# 2
# 4
# ---------------
# Элементы итератора PowerTwo(20)
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256
# 512
# 1024
# 2048
# 4096
# 8192
# 16384
# 32768
# 65536
# 131072
# 262144
# 524288
# 1048576


class PowerTwo:

    def __init__(self, number: int) -> int:
        self.number = number
        self.res = []
        for i in range(0, number + 1):
            self.res.append(2 ** i)

    def __iter__(self):
        return iter(self.res)

    def __next__(self):
        return self.res


numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)


# another solution

class PowerTwo:
    def __init__(self, power):
        self.pow_gen = (2 ** p for p in range(power + 1))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.pow_gen)