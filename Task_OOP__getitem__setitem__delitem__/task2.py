# Для этого в классе Building должно быть реализованы
#
# метод __init__, который принимает количество этажей в здании
# метод __setitem__, который закрепляет за определенным этажом компанию.
# Если этаж был занят другой компанией, нужно заменить название другой компанией
# метод __getitem__, который возвращает название компании с этого этажа.
# В случае, если этаж пустует, следует вернуть None
# метод __delitem__, который высвобождает этаж
# В этом задании вы сами решаете какие атрибуты создавать внутри класса,
# главное реализовать магические методы из списка выше


class Building:

    def __init__(self, *args):
        self.floors = list(args)
        self.company = dict()

    def __setitem__(self, key, value):
        if key is not self.company:
            self.company[key] = value
        self.company[key] = value

    def __getitem__(self, item):
        if item in self.company:
            return self.company[item]
        return None

    def __delitem__(self, key):
        if key in self.company:
            del self.company[key]


iron_building = Building(22)  # Создаем здание с 22 этажами
print(iron_building.floors)
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building.company)
print(iron_building[2])
del iron_building[2]
print(iron_building[2])

val = '123456789'
val1 = '987654321'



