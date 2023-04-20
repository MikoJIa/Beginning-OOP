# В вашем распоряжении класс Person, у которого имеется 7 атрибутов.
# Программа будет принимать на вход произвольное количество слов в одну строку,
# разделенных пробелом. Ваша задача проверить, является ли каждое из введенных слов
# названием атрибута. Регистр слов значения не имеет.
# Нужно вывести в каждой отдельной строке введенные слова по порядку и напротив через
# дефис
# указать, нашлось ли свойство с таким именем или нет (вывести YES или NO)
# Sample Input 1:
# age date address
#
# Sample Output 1:
# age-YES
# date-NO
# address-YES
# Sample Input 2:
#
# Email banana
# Sample Output 2:
#
# Email-YES
# banana-NO
# Sample Input 3:
#
# NAME GeNdEr work hobby
# Sample Output 3:
#
# NAME-YES
# GeNdEr-YES
# work-NO
# hobby-NO

class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


lst = list(map(str, input().split()))
for i in lst:
    if i.lower() in Person.__dict__:
        print(f'{i}-YES')
    else:
        print(f'{i}-NO')


# another solution

for i in input().split():
    if hasattr(Person, i.lower()):
        print(i, 'YES', sep='-')
    else:
        print(i, 'NO', sep='-')