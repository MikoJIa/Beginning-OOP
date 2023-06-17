class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)

class Section:

    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)  # self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)


b = Section(9, 8)
c = Section(3, 9)
print(len(b))
print(len(c))