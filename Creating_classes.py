# Классы в Python - это прототип или шаблон для создания объектов!!!


# class Home:  # Создан чертёж дома
#     """Создан класс или чертёж нашего дома"""
#
#     # count_house = 1  # Атрибут класса
#
#     def _a(self):
#         return "Hello"
#
#     def __b(self):
#         return "Bye"
#
#     def __init__(self, color: str, width: float | int, height: float | int):
#         """Метод, инициализатор свойств класса, часть конструктора"""
#         self.color = color
#         self.width = width
#         self.height = height
#         self.count_house = 1  # Атрибут класса
#
#     def calc_house(self):
#         return self.width * self.height
#
#
# # Home - это класс
# # Home() - это объект класса
#
#
# home1 = Home("white", 3.5, 4.5)
# # print(home1.width)  # 3.5
# print(home1.__dict__)  # {'color': 'white', 'width': 3.5, 'height': 4.5}
# print(home1.calc_house())
# print(Home.__dict__)


# class Point:
#     color = "red"
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self, x, y):
#         return (self.x, self.y)
#
#
# pt = Point(1, 2)
# pt2 = Point()
# res = Point.get_coords(pt)
# print(res)
# print(pt.set_coords(1, 2))
# print(pt2.get_coords(3, 5))

'''объект - единица информации в памяти
   экземпляр - конкретный объект какогото класса
   класс - чертёж или прототип по созданию объктов
   метод - функция в классе для воздействия на объект
   атрибуты - все имена в классе: переменных и методов
'''

class Purse:

    def __init__(self, valuta, name='unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00  # к этому атрибуту мы теперь сможем получить доступ только из
                             # класса
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Не достаточно средств!!!')
            raise ValueError('Не достаточно средств!!!')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        return self.__money

    def __del__(self):  # Деструктор
        print('Кошелёк удалён')


object1 = Purse('USD')  # Кошелёк 1
object2 = Purse('USD', 'Bill')  # Кошелёк 2
object2.top_up_balance(100)
object1.top_up_balance(object2.top_down_balance(35))
print(object1.info())
print(object2.info())


