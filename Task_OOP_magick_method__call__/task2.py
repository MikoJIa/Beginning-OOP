# Помните из школы это потрясающее уравнение?
# Давайте воссоздадим эту формулу в виде класса QuadraticFunction, в котором есть:
# метод __init__. Он должен сохранять в экземпляр класса три атрибута: a , b и c.
# метод __call__ , который принимает аргумент x, подставляет его в формулу выше, находит
# значение и возвращает его в качестве результата
# Sample Input:
#
# Sample Output:
#
# Good


class QuadraticFunction:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        res = self.a * x ** 2 + self.b * x + self.c
        return res


f = QuadraticFunction(2, 5, 7)
assert f(1) == 14
assert f(-3) == 10
assert f(2) == 25
assert f(5) == 82

f_2 = QuadraticFunction(-1, 2, 4)
assert f_2(5) == -11
assert f_2(2) == 4
assert f_2(-3) == -11
assert f_2(1) == 5
print('Good')