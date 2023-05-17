#  Создайте класс Date, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: день, месяц и год.
#
# свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
#
# свойство usa_date, которое возвращает строку определенного формата
# "<месяц>-<день>-<год>";
# d1 = Date(5, 10, 2001)
# d2 = Date(15, 3, 999)
#
# print(d1.date) # 05/10/2001
# print(d1.usa_date) # 10-05-2001
# print(d2.date) # 15/03/0999
# print(d2.usa_date) # 03-15-0999
# Обратите внимание, что дни и месяцы занимают 2 символа в выводе, а отображение года- 4
# символа(заполняются нулями спереди до нужной длины).
#
# Sample Input:
#
# Sample Output:
#
# 05/10/2001 10-05-2001
# 15/03/0999 03-15-0999
# 03/05/0003 05-03-0003
from datetime import date


class Date:

    def __init__(self, day, month, year):
        self.dates = f'{day:02}/{month:02}/{year:04}'
        self.dates_usa = f'{month:02}-{day:02}-{year:04}'

    @property
    def date(self):
        return self.dates

    @property
    def usa_date(self):
        return self.dates_usa



d1 = Date(5, 10, 2001)
assert isinstance(d1, Date)
assert d1.date == '05/10/2001'
assert d1.usa_date == '10-05-2001'
assert isinstance(type(d1).date, property), 'Вы не создали property date'
print(d1.date, d1.usa_date)

d2 = Date(15, 3, 999)
assert isinstance(d2, Date)
assert d2.date == '15/03/0999'
assert d2.usa_date == '03-15-0999'
assert isinstance(type(d2).date, property), 'Вы не создали property date'
print(d2.date, d2.usa_date)

d3 = Date(3, 5, 3)
assert d3.date == '03/05/0003'
assert d3.usa_date == '05-03-0003'
print(d3.date, d3.usa_date)


# anotuer solution

# class Date:
#
#     def __init__(self, day, month, year):
#         self.__dates = date(year, month, day)
#
#
#     @property
#     def date(self):
#         return self.__dates.strftime('%d/%m/%Y')
#
#
#     @property
#     def usa_date(self):
#         return self.__dates.strftime('%m-%d-%Y')
#
#
# d1 = Date(5, 10, 2001)
# assert isinstance(d1, Date)
# assert d1.date == '05/10/2001'
# assert d1.usa_date == '10-05-2001'
# assert isinstance(type(d1).date, property), 'Вы не создали property date'
# print(d1.date, d1.usa_date)


# another solution


# class Date:
#     def __init__(self, day, month, year):
#         self.day = str(day).zfill(2)
#         self.month = str(month).zfill(2)
#         self.year = str(year).zfill(4)
#
#     @property
#     def date(self):
#         return f"{self.day}/{self.month}/{self.year}"
#
#     @property
#     def usa_date(self):
#         return f"{self.month}-{self.day}-{self.year}"