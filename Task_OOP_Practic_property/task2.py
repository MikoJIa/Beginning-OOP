# Создать класс, модули и свойства для проверки пароля
from string import digits


class Registration:

    def __init__(self, log, passw):
        self.login = log
        self.__password = passw

    @staticmethod
    def is_include_number(passw):
        for digit in digits:
            if digit in passw:
                return True
        return False

    @staticmethod
    def is_include_all_register(passw):
        if passw.islower():
            return False
        elif passw.isupper():
            return False
        return True

    @staticmethod
    def is_include_only_latin(passw):
        if passw.isascii() and passw.isupper():
            return False
        if passw.isascii() and passw.islower():
            return False
        return True

    @staticmethod
    def check_password_dictionary(passw):
        with open('easy_passwords.txt', 'r', encoding='utf-8') as file:
            if passw in file.read():
                return False
            return True


    @property
    def password(self):
        return self.__password

    @property
    def login(self):
        return self.__login

    @password.setter
    def password(self, passw):
        if not isinstance(passw, str):
            raise TypeError("Пароль должен быть строкой")
        if len(passw) < 5 and len(passw) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_number(passw):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(passw):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(passw):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(passw):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = passw

    @login.setter
    def login(self, log):
        if not isinstance(log, str):
            raise TypeError
        if not log.count('@', 1):
            raise ValueError
        if not log.count('.') or log.index('.') < log.index('@'):
            raise ValueError
        self.__login = log



try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")


try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')
# try:
#     result = Registration("fga")
# except ValueError as error:
#     print("Логин fga должен содержать один символ '@'")
#
# try:
#     result = Registration(1234)
# except TypeError as error:
#     print("Пароль должен быть строкой")
#
# try:
#     result = Registration("f@ga@")
# except ValueError as error:
#     print("Логин f@ga@ должен содержать только один символ '@'")
#
# try:
#     result = Registration("fg@a")
# except ValueError as error:
#     print("В логине fg@a должен быть символ '.' после символа '@'")
#
# try:
#     result = Registration("fg.@a")
# except ValueError as error:
#     print("В логине fg.@a должна быть '.' после символа '@'")
#
# result = Registration("translate@gmail.com")
# assert result.login == "translate@gmail.com"
# assert result._Registration__login == "translate@gmail.com"
#
# try:
#     result.login = "asdsa12asd."
# except ValueError as error:
#     print("Логин asdsa12asd. должен содержать один символ '@'")
#
# try:
#     result.login = "asdsa12@asd"
# except ValueError as error:
#     print("asdsa12@asd должен быть символ '.' после символа '@'")
#
# result.login = "alligator13@how.do"
# assert result.login == "alligator13@how.do"
# assert result._Registration__login == "alligator13@how.do"