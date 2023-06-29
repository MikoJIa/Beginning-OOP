# Создайте класс Addition, у которого необходимо:
# определить метод __call__. Он должен принимать произвольное количество аргументов и
# среди этих аргументов находить числа и их суммировать. Все остальные типы данных н
# еобходимо пропускать. В результате метод __call__ должен вернуть строку в следующем в
# виде:
# Сумма переданных значений = {сумма}
# Sample Input:
#
# Sample Output:
#
# Good


class Addition:

    def __call__(self, *args, **kwargs):
        self.summa = 0
        for i in args:
            if type(i) is int or type(i) is float:
                self.summa += i
            if isinstance(args, str):
                self.summa = 0
        return f'Сумма переданных значений = {self.summa}'



add = Addition()
assert add(10, 20) == "Сумма переданных значений = 30"

assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"


add2 = Addition()
assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
assert add2() == "Сумма переданных значений = 0"
assert add2('hello') == "Сумма переданных значений = 0"

print('Good')


# another solution


class Addition:
    def __init__(self):
        self.summa = 0

    def __call__(self, *args):
        x = list(filter(lambda x: isinstance(x, (int, float)),args))
        self.summa += sum(x)
        print(f"Сумма переданных значений = {self.summa}")
        self.summa = 0