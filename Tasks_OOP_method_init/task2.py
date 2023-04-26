# Создайте класс Zebra, внутри которого есть метод which_stripe, который поочередно
# печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"
#
# Пример работы с классом Zebra
#
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"


class Zebra:
    def __init__(self):
        self.color_strip = 'Полоска белая'
        self.color_strip2 = 'Полоска черная'

    def which_stripe(self):
        print(self.color_strip)
        self.color_strip, self.color_strip2 = self.color_strip2, self.color_strip
        return self.color_strip


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()
z2.which_stripe()
z2.which_stripe()


class Zebra2:
    count = 0

    def __init__(self):
        self.color_strip = 'Полоска белая'
        self.color_strip2 = 'Полоска черная'

    def func(self):
        if self.count % 2 == 0:
            print(self.color_strip)
        else:
            print(self.color_strip2)
        self.count += 1


z1 = Zebra2()
z1.func()
z1.func()
z1.func()

z2 = Zebra2()
z2.func()
z2.func()
z2.func()