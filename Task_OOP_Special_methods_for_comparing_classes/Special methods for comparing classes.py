# Магтческие методы сравнения
# __eq__ -- '=='
# __ne__ -- '!='
# __lt__ -- '<'
# __le__ -- '<='
# __gt__ -- '>'
# __ge__ -- '>='

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print(f'__eq__ call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print(f'__lt__ call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        print(f'__le__ call')
        return self == other or self < other


a = Rectangle(1, 2)
b = Rectangle(1, 2)
print(a > b)
