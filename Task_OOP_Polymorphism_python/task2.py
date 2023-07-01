# Создайте класс UnitedKingdom, у которого необходимо реализовать:
#
# статический метод get_capital, который печатает строку "London is the capital of Great Britain."
# статический метод get_language, который печатает строку "English is the primary language of Great Britain."
# Создайте класс Spain, у которого необходимо реализовать:
#
# статический метод get_capital, который печатает строку "Madrid is the capital of Spain."
# статический метод get_language, который печатает строку "Spanish is the primary language of Spain."


class UnitedKingdom:

    @staticmethod
    def get_capital():
        print(f'London is the capital of Great Britain.')

    @staticmethod
    def get_language():
        print(f'English is the primary language of Great Britain.')


class Spain:

    @staticmethod
    def get_capital():
        print(f'Madrit is the capital of Spain.')


    @staticmethod
    def get_language():
        print(f'Spanish is the primary language of Spain.')


obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.get_capital()
    country.get_language()