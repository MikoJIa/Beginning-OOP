# Создайте класс Hero, который имеет следующие методы:
# метод __len__, который возвращает количество атрибутов экземпляра
# приватный метод __str__, который возвращает строковое представление героя.
# Для этого нужно перечислить все атрибуты в алфавитном порядке на отдельной строке,
# напротив каждого атрибута указать его значение. Вот такой формат должен получится:
# атрибут_1: значение_атрибут_1
# атрибут_2: значение_атрибут_2
# ...
# атрибут_N: значение_атрибут_N
#
# Если у экземпляра нету атрибутов, необходимо вернуть пустую строку
# Sample Input:
#
# Sample Output:
#
# damage: 10
# health: 50
# skill: Некромант
# weapon: ['sword', ' bow']
# armor: 25
# level: 15
# skill: Боец


class Hero:

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        res = ""
        for k, v in sorted(self.__dict__.items()):
            res += f"{k}: {str(v)}\n"
        res = res.rstrip('\n')
        return res


hero = Hero()
assert len(hero) == 0
hero.health = 50
hero.damage = 10
assert len(hero) == 2
assert str(hero) == '''damage: 10
health: 50'''
print(hero)
hero.weapon = ['sword', ' bow']
hero.skill = 'Некромант'
assert str(hero) == '''damage: 10
health: 50
skill: Некромант
weapon: ['sword', ' bow']'''
print(hero)