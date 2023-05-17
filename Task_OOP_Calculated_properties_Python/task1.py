# Создайте класс Rectangle, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: длину и ширину.
# свойство area, которое возвращает площадь прямоугольника;
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
#
# print(r1.area) # 15
# print(r2.area) # 6
# Sample Input:
#
# Sample Output:
#
# Good


class Rectangle:

    def __init__(self, length, width):
        self.area_rectangle = length * width

    @property
    def area(self):
        return self.area_rectangle


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area) # 15
print(r2.area) # 6
