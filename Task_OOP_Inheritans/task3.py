# Создайте базовый класс  Person, у которого есть:
# конструктор __init__, который должен принимать на вход имя и записывать его в атрибут name
# метод get_name, который возвращает атрибут name;
# метод  is_employee, который возвращает  False
# Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:
# метод  is_employee, который возвращает  True
# emp1 = Person("vasya")
# print(emp1.get_name(), emp1.is_employee()) # vasya False
# emp2 = Employee("gena bukin")
# print(emp2.get_name(), emp2.is_employee())# gena bukin True
# Sample Input:
#
# Sample Output:
#
# Good


class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):

    def is_employee(self):
        return True


emp1 = Person("vasya")
print(emp1.get_name(), emp1.is_employee())  # vasya False

emp2 = Employee("gena bukin")
print(emp2.get_name(), emp2.is_employee())  # gena bukin True
