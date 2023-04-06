# Классы в Python - это прототип или шаблон для создания объектов!!!

class Home:  # Создан чертёж дома
    '''Создан класс или чертёж нашего дома'''
    count_house = 1  # Атрибут класса

    def __init__(self, color: str, width: int, height: int):
        ''' метод, инициализатор свойств класса, часть конструктора '''
        self.color = color
        self.width = width
        self.height = height

# Home - это класс
# Home() - это объект класса
print(Home)