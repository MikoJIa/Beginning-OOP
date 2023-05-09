# Создайте класс Employee, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов name, __position,
# __hours_worked и __hourly_rate.
#
# приватный метод calculate_salary, который считает зарплату сотрудника,
# умножая отработанные часы на часовую оплату. Метод должен вернуть посчитанную зарплату.
#
#  защищенный метод _set_position, который принимает название должности и изменяет
#  пользователю значение атрибута __position.
#
#  публичный метод get_position, который возвращает атрибут __position.
#
# публичный метод get_salary, который возвращает результат вызова приватного метода
# calculate_salary.
#
# публичный метод get_employee_details,
# который возвращает информацию о работнике в виде следующий строки
#
# "Name: {name}, Position: {position}, Salary: {salary}"
#
# Здесь значение salary должно рассчитываться при помощи приватного метода
# calculate_salary.
# Sample Input:
#
# Sample Output:
#
# Good

class Employee:

    def __init__(self, name, position, hours_worked, hourly_rate):
        self.name = name
        self.__position = position
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def __calculate_salary(self):
        res = self.__hourly_rate * self.__hours_worked
        return res

    def _set_position(self, pos):
        if pos:
            self.__position = pos
        return self.__position

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__calculate_salary()

    def get_employee_details(self):
        return f'Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}'


employee = Employee("Джеки Чан", 'manager', 20, 40)
assert employee.name == 'Джеки Чан'
assert employee._Employee__hours_worked == 20
assert employee._Employee__hourly_rate == 40
assert employee._Employee__position == 'manager'
assert employee.get_position() == 'manager'
assert employee.get_salary() == 800
assert employee._Employee__calculate_salary() == 800
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
employee._set_position('Director')
assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'

employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
assert employee_2._Employee__calculate_salary() == 1050
assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'

print('Good')