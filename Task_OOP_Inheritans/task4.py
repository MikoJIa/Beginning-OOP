# оздайте класс NewInt, который унаследован от целого типа int,
# то есть мы будем унаследовать поведение целых чисел и значит экземплярам нашего класса
# будут поддерживать те же операции, что и целые числа.
# Дополнительно в классе NewInt нужно создать:
# метод repeat, который принимает одно целое положительное число n
# (по умолчанию равное 2), обозначающее сколько раз нужно продублировать данное число.
# Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
# метод to_bin, который возвращает двоичное представление числа в виде числа
# (может пригодиться функция bin)
#
# a = NewInt(9)
# print(a.repeat())  # печатает число 99
# d = NewInt(a + 5)
# print(d.repeat(3)) # печатает число 141414
# b = NewInt(NewInt(7) * NewInt(5))
# print(b.to_bin()) # печатает 100011 - двоичное представление числа 35


class NewInt(int):

    def __init__(self, INT):
        self.INT = INT

    def repeat(self, n=2):
        res = ''
        for i in range(n):
            res += str(self.INT)
        return int(res)

    def to_ben(self):
        return int(f'{self:b}')


s = NewInt(9)
print(s.repeat())
d = NewInt(s + 5)
print(d.repeat(3))
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_ben())
c = NewInt(16)
print(c.to_ben())

assert NewInt(16).to_ben() == 10000

# another solution

class NewInt(int):

    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])


s = NewInt(9)
print(s.repeat())
d = NewInt(s + 5)
print(d.repeat(3))
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())
c = NewInt(16)
print(c.to_bin())

assert NewInt(16).to_bin() == 10000