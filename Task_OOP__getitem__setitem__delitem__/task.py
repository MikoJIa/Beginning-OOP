class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)
    # Для того что бы мы могли обратиться к индексу списка values, необходимо реализовать
    # магически й метод __getitem__

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):
            return self.values[item-1]
        else:
            raise IndexError('Такого индекса в коллекции не существует')

    def __setitem__(self, key, value):
        if 1 <= key <= len(self.values):
            self.values[key-1] = value
            return self.values
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff)
            self.values[key-1] = value
            for i in range(1, len(self.values)):
                if self.values[i-1] != i:
                    self.values[i-1] = i
            return self.values
        else:
            raise IndexError(f'Такого индекса в коллекции нет')

    def __delitem__(self, key):
        if 1 <= key <= len(self.values):
            del self.values[key-1]
            return self.values
        else:
            raise IndexError(f'Такого индекса в коллекции нет')


v1 = Vector(1, 2, 3, 4, 5)
print(v1[3])
v1[2] = 100
print(v1[2])
print(v1.values)
del v1[2]
print(v1.values)
v1[6] = 6
print(v1.values)

