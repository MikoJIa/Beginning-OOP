# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
# В классе Counter нужно определить:
# Метод start_from, который принимает один необязательный аргумент. Значение, с которого
# начинается подсчет, по умолчанию равно 0.
# Метод increment, который увеличивает счетчик на 1.
# Метод display, который печатает фразу "Текущее значение счетчика = <value>".
# Метод reset, который обнуляет накопившееся значение счетчика.
# Sample Input:
# Sample Output:
# Текущее значение счетчика = 46
# Текущее значение счетчика = 47
# Текущее значение счетчика = 0
# Текущее значение счетчика = 1
# Текущее значение счетчика = 0
# Текущее значение счетчика = 1


class Counter:
    def start_from(self, num=0):
        self.num = num
        return self.num

    def increment(self):
        self.num = self.num + 1
        return self.num

    def display(self):
        print(f'Текущее значение счетчика = {self.num}')

    def reset(self, num=0):
        self.num = num
        return self.num

# Ниже код для проверки класса Counter

c1 = Counter()
c2 = Counter()

assert isinstance(c1, Counter)
assert isinstance(c2, Counter)
assert c1.__dict__ == {}
assert c2.__dict__ == {}

c1.start_from(45)
assert len(c1.__dict__) == 1
c1.increment()
c1.display()  # печатает 46
c1.increment()
c1.display()  # печатает 47

c2.start_from()
c2.display()  # печатает 0
c2.increment()
c2.display()  # печатает 1

c1.reset()  # обнулили с1, но с2 не должен меняться
c1.display()  # печатает 0

c2.display()  # попрежнему печатает 1