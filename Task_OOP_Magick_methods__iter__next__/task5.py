class InfinityIterator:

    def __init__(self, start=0, step=10):
        self.start = start
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value <= 999:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


num = InfinityIterator()
for i in num:
    print(i)
