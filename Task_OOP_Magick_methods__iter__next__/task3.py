# Создайте класс Countdown, который должен принимать начальное значение и вести обратный
# отсчет до нуля, возвращая каждое значение в последовательности каждый раз,
# когда вызывается __next__. Когда обратный отсчет достигает нуля, итератор должен вызвать
# исключение StopIteration. Для этого вам понадобиться реализовать:
# метод __init__. Он должен принимать одно положительное число - начало отсчета
# методы __iter__ и __next__ для итерирования по значениям класса Countdown.
# for i in Countdown(3):
#     print(i)
# # Цикл выше должен печатать следующие числа
# 3
# 2
# 1
# 0
# Sample Input:
# Sample Output:
# Элементы итератора Countdown(7)
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# ----------
# Элементы итератора Countdown(10)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0


class Countdown:

    def __init__(self, num):
        self.num = num + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num != 0:
            self.num -= 1
            return self.num
        raise StopIteration


count = Countdown(2)

for i in count:
    print(i)


# another solution


class Countdown:
    def __init__(self, number):
        self.number = [i for i in range(number + 1)][::-1]

    def __iter__(self):
        return iter(self.number)

    def __next__(self):
        return self.number