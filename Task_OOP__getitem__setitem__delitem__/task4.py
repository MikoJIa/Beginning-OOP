# В этой задаче мы создадим аналог корзины покупок и для этого нам понадобиться
# реализовать класс ShoppingCart. В нем
# должно содержаться следующее:
# метод __init__. , который создает в экземпляре атрибут items.
# Изначально должен быть пустым словарем, в нем будут содержаться покупки;
# метод __getitem__ , который возвращает по названию товара его текущее количество или 0,
# если товар отсутствует в корзине
# метод __setitem__ , который проставляет по названию товара его количество в корзине.
# Если товар отсутствовал, его необходимо добавить, если присутствовал - нужно проставить ему новое количество
# метод __delitem__ , который удаляет товар из корзины
# метод add_item, который добавляет товар к текущим. Это значит, что если товар уже
# присутствовал в корзине, то необходимо увеличить его количество. Если товар отсутствовал
# , нужно его добавить. Данный метод принимает обязательно название товара и необязательно
# его количество (по умолчанию количество равно 1).
# метод remove_item, который удаляет некоторое количество товара из корзины. Если хотят
# удалить из корзины столько же товара, чем там имеется или больше, необходимо удалить
# его из корзины.  В остальных случаях уменьшаем количество товара на переденное
# количество. Данный метод принимает обязательно название товара и необязательно его
# количество (по умолчанию количество равно 1). Предусмотрите ситуацию, когда удаляемый
# товар отсутствует в корзине
# Sample Input:
#
# Sample Output:
#
# Shopping Cart:
# Apple: 3
# Banana: 2
# Orange: 10
# Updated Shopping Cart:
# Apple: 5
# Banana: 7
# Orange: 10
# Kivi: 11
# Updated Shopping Cart:
# Orange: 10
# Kivi: 11


class ShoppingCart:

    def __init__(self):
        self.items = dict()

    def __getitem__(self, item):
        if item not in self.items:
            return 0
        return self.items[item]

    def __setitem__(self, key, value):
        if key not in self.items:
            self.items[key] = value
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]

    def add_item(self, item, count=1):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += count

    def remove_item(self, item, count=1):
        if item not in self.items:
            return self.items
        if count >= 1:
            self.items[item] -= count
            if self.items[item] >= 0:
                return self.items
            self.items[item] = 0
        if self.items[item] <= 0:
            self.__delitem__(item)


cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)

assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")