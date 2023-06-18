# class BancAccount:
# #
# #     def __init__(self, name, balance):
# #         self.name = name
# #         self.balance = balance
# #
# #     def __repr__(self):
# #         return f'Клиент {self.name} с балансом {self.balance}'
# #
# #     def __add__(self, other):
# #         print('__add__ call')
# #         if isinstance(other, BancAccount):  # Тут мы сложим два баланса двух экземпляров
# #             return self.balance + other.balance
# #         if isinstance(other, (int | float)):
# #             self.balance += other
# #             return self
# #         raise NotImplemented
# #
# #     def __mul__(self, other):
# #         print('__mul__ call')
# #         if isinstance(other, BancAccount):  # Тут мы перемножим два баланса двух экземпляров
# #             return self.balance * other.balance
# #         if isinstance(other, (int | float)):
# #             return self.balance * other
# #         if isinstance(other, str):
# #             return self.name + other
# #         raise NotImplemented
# #
# #
# # b = BancAccount('Nik', 300)
# # b + 200
# # c = BancAccount('Mik', 300)
# # b + c
# # print(b.balance)



class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return MyPoint(2 * self.x + other.x, 2 * self.y + other.y)


p1 = MyPoint(3, 4)
