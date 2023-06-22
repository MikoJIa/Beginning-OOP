# class Vector:
#
#     def __init__(self, *args):
#         self.values = sorted([i for i in args if type(i) == int])
#
#     def __str__(self):
#         if self.values:
#             return f'Вектор{tuple(self.values)}'
#         return f'Пустой вектор'
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Vector)):
#             return [print(f'Вектор нельзя сложить с {other}')]
#         if isinstance(other, int):
#             res = [self.values[i] + other for i in range(len(self.values))]
#             return Vector(*res)
#         if isinstance(other, (int, Vector)):
#             res = [self.values[i] + other.values[i] for i in range(len(self.values))]
#             return Vector(*res)
#         if isinstance(other, (int, Vector)) and len(self.values) != len(other.values):
#             return f'Сложение векторов разной длины недопустимо'
#
#     def __mul__(self, other):
#         if isinstance(other, (str, bool, float)):
#             return f'Вектор нельзя умножать с {other}'
#         if isinstance(other, (int)):
#             res = [self.values[i] * other for i in range(len(self.values))]
#             return Vector(*res)
#         if isinstance(other, (int, Vector)):
#             res = [self.values[i] * other.values[i] for i in range(len(self.values))]
#             return Vector(*res)
#         if isinstance(other, (int, Vector)) and len(self.values) != len(other.values):
#             return f'Умножение векторов разной длины недопустимо'
#
#
# v1 = Vector(1, 2, 3)
# print(v1) # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3,4,5)
# print(v2) # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3) # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4) # печатает "Вектор(9, 11, 13)"
# v5 = v1 * 2
# print(v5) # печатает "Вектор(2, 4, 6)"
# v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
# v6 = v5 + v1  # 3, 6, 9
# print(v6) # 3, 6, 9
# v7 = v6 * 3
# print(v7)


class Vector:

    def __init__(self, *args: int) -> None:
        self.values = sorted([i for i in args if type(i) == int])

    def __str__(self):
        return f'Вектор{tuple(self.values)}' if self.values else f'Пустой вектор'

    def __add__(self, other: int) -> ['Vector']:
        if isinstance(other, int):
            new_vector = [i + other for i in self.values]
            return Vector(*new_vector)
        elif isinstance(other, Vector):
            if not len(other) == len(self.values):
                return [print(f'Сложение векторов разной длины недопустимо')]
            new_vector = [sum(i) for i in zip(self.values, other.values)]
            return Vector(*new_vector)
        else:
            return [print(f'Вектор нельзя сложить с {other}')]

    def __mul__(self, other: int) -> ['Vector']:
        if isinstance(other, int):
            new_vector = [i * other for i in self.values]
            return Vector(*new_vector)
        elif isinstance(other, Vector):
            if not len(other) == len(self.values):
                return [print(f'Сложение векторов разной длины недопустимо')]
            new_vector = (i * j for i, j in zip(self.values, other.values))
            return Vector(*new_vector)
        else:
            return [print(f'Вектор нельзя умножать с {other}')]

    def __len__(self) -> int:
        return len(self.values)


v1 = Vector(1, 2, 3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
v6 = v5 + v1  # 3, 6, 9
print(v6) # 3, 6, 9
v7 = v6 * 3
print(v7)