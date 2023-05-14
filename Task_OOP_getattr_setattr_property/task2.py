# Создайте класс UserMail, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес.
# Их необходимо сохранить в экземпляр, как атрибуты login и __email
# (обратите внимание, защищенный атрибут).
# метод геттер get_email, который возвращает защищенный атрибут __email.
#
# метод сеттер set_email, который принимает в виде строки новую почту.
# Метод должен проверять, что в новой почте есть только один символ @ и
# после нее есть точка. Если данные условия выполняются, новая почта сохраняется в атрибут
# __email, в противном случае выведите сообщение "ErrorMail:<почта>".
# создайте свойство email, у которого геттером будет метод get_email,
# а сеттером  метод set_email.
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
# k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait
# 🚀Разбор🚀
# Sample Input:
#
# Sample Output:
#
# ErrorMail:[1, 2, 3]
# ErrorMail:hello@@re.ee
# ErrorMail:{1, 2, 3}
# ErrorMail:prince@still@.wait
# ErrorMail:prince@stillwait
# ErrorMail:pri.nce@stillwait


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return getattr(self, "_UserMail__email")

    def set_email(self, value):
        if (
            isinstance(value, str)
            and value.count("@") == 1
            and "." in value[value.index("@"):]
        ):
            self.__email = value
        else:
            print(f"ErrorMail:{value}")

    email = property(fget=get_email, fset=set_email)


jim = UserMail("aka47", "hello@com.org")
assert jim.login == "aka47"
assert jim._UserMail__email == "hello@com.org"
assert isinstance(jim, UserMail)
assert isinstance(type(jim).email, property), "Вы не создали property email"

jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
jim.email = "hello@@re.ee"  # печатает ErrorMail:hello@@re.ee
jim.email = "hello@re.w3"
assert jim.email == "hello@re.w3"

k = UserMail("belosnezhka", "prince@wait.you")
assert k.email == "prince@wait.you"
assert k.login == "belosnezhka"
assert isinstance(k, UserMail)

k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
k.email = "prince@still@.wait"  # печатает ErrorMail:prince@still@.wait
k.email = "prince@stillwait"  # печатает ErrorMail:prince@stillwait
k.email = "prince@still.wait"
assert k.get_email() == "prince@still.wait"
k.email = "pri.nce@stillwait"  # печатает ErrorMail:pri.nce@stillwait
assert k.email == "prince@still.wait"
