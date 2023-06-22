class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


x = Point(1, 3)
y = Point(1, 3)
s = Point(3, 6)
print(x == y)
print(y == s)
print(hash(x))
print(hash(y))
print(hash(s))
