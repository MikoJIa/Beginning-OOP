class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print(f'init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Our instance was called {self.counter} times')

    def average(self):
        return self.summa / self.length


b = Counter()
b(3, 4, 5, 6, 7)
b(1, 2, 3)
print(b.length)
print(b.average())
#
# from time import perf_counter
#
#
# class Timer:
#
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, *args, **kwargs):
#         start = perf_counter()
#         print(f'was called function {self.fn.__name__}')
#         result = self.fn(*args, **kwargs)
#         finish = perf_counter()
#         print(f'function worked out {finish - start}')
#         return result

# @Timer
# def factorial(n):
#     pr = 1
#     for i in range(1, n + 1):
#         pr *= i
#     return pr
#
#
# print(factorial(3))

# def fibb(n):
#     if n <= 2:
#         return 1
#     return fibb(n - 1) + fibb(n - 2)
#
# print(Timer(fibb)(7))





# class Adder:
#     def __init__(self, x):
#         self.x = x
#
#     def __call__(self, y):
#         return self.x + y
#
#
# a = Adder(10)
# b = Adder(20)
# c = a(5) + b(5)
# print(c)