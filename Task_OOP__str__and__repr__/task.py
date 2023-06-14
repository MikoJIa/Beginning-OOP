# Создайте класс Person, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: name, surname, gender.
# Атрибут gender может принимать только 2 значения: "male" и "female",
# по умолчанию "male". Если в атрибут gender передается любое другое значение,
# печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить
# атрибут gender значением "male"
# переопределить метод __str__ следующим образом:
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>"
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>"
# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду?
# Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"
# Click and drag to move
# Sample Input:
#
# Sample Output:
#
# Не знаю, что вы имели ввиду? Пусть это будет мальчик!
# Гражданин Norris Chuck
# Гражданин Кеноби Оби-Ван
# Гражданка Kunis Mila


class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender == 'male' or gender == 'female':
            self.gender = gender
        else:
            print(f'Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        if self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
assert p1.name == 'Chuck'
assert p1.surname == 'Norris'
assert p1.gender == 'male'
assert isinstance(p1, Person)
assert str(p1) == 'Гражданин Norris Chuck'

p2 = Person('Оби-Ван', 'Кеноби', True) #  нужно распечатать предупреждение из условия

assert str(p2) == 'Гражданин Кеноби Оби-Ван'
assert p2.__dict__ == {'name': 'Оби-Ван', 'surname': 'Кеноби', 'gender': 'male'}
assert isinstance(p2, Person)

p3 = Person('Mila', 'Kunis', 'female')

assert isinstance(p3, Person)
assert str(p3) == 'Гражданка Kunis Mila'

print(p1)
print(p2)
print(p3)