class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if not isinstance(other, (int, ChessPlayer)):
            return f'Невозможно выполнить сравнение'
        if isinstance(other, int) and self.rating == other:
            return True
        if isinstance(other, ChessPlayer) and self.rating == other.rating:
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, (int, ChessPlayer)):
            return f'Невозможно выполнить сравнение'
        if isinstance(other, int) and self.rating > other:
            return True
        if isinstance(other, ChessPlayer) and self.rating > other.rating:
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, (int, ChessPlayer)):
            return f'Невозможно выполнить сравнение'
        if isinstance(other, int) and self.rating < other:
            return True
        if isinstance(other, ChessPlayer) and self.rating < other.rating:
            return True
        return False


magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000) # False
print(ian == 2789) # True
print(magnus == ian) # False
print(magnus > ian) # True
print(magnus < ian) # False
print(magnus < [1, 2]) # печатает "Невозможно выполнить сравнениe"


# another solution

class ChessPlayer:

    def __init__(self,name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayer) or isinstance(other,int):
            if self.rating == other:
                return True
            else:
                return False
        else:
            return f"Невозможно выполнить сравнение"

    def __gt__(self, other):
        if isinstance(other, ChessPlayer) or isinstance(other,int):
            if self.rating > other:
                return True
            else:
                return False
        else:
            return f"Невозможно выполнить сравнение"

    def __lt__(self, other):
        if isinstance(other, ChessPlayer) or isinstance(other,int):
            if self.rating < other:
                return True
            else:
                return False
        else:
            return f"Невозможно выполнить сравнение"