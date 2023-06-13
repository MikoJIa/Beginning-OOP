# Создание класса для проверки пароля

from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'abracadabra'

    @property
    def password(self):
        print('Property getter')
        return self.__password

    # создадим статикфункцию которая будет проверять переменную на число
    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def dict_password(password):
        with open('password.txt', 'r', encoding='utf-8') as file:
            if password in file.read():
                return False
            else:
                return True

    @property
    def secret(self):
        user_input = input('Введите пароль')
        if user_input == self.password:
            return self.__secret
        else:
            raise ValueError("Доступ закрыт")

    @password.setter
    def password(self, value):
        print('Property setter')
        if not isinstance(value, str):
            raise TypeError('The password must be a string!')
        if len(value) < 5:
            raise ValueError(
                'The password length is too small, the min length must be 4 simbol')
        if len(value) > 12:
            raise ValueError(
                'The password length is too big, the max length must be 12 simbol')
        if self.is_include_number(value) is False:
            raise ValueError('The Password must contain at least 1 digit!')
        if not self.dict_password(value):
            raise ValueError("Пароль слишком слабый!")
        self.__password = value