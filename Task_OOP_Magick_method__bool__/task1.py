class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print(f'call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print(f'call __bool__')
        return self.x != 0 or self.y != 0


p1 = Point(1, 0)
if p1:
    print('hello')



class Person:
    def __init__(self, name):
        self.name = name

    def __bool__(self):
        return len(self.name)


p1 = Person('Gena')
print(bool(p1))