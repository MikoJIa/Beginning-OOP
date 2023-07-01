# Необходимо создать класс декоратор Time
import time

class Timer:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        getting_started = time.time()
        self.func()
        finish_time = time.time()
        res = finish_time - getting_started
        return f'Время работы программы - {res} sec'

@Timer
def calculate():
    for i in range(10000000):
        2 ** 100

print(calculate())

