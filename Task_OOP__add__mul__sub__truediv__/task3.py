# Создайте класс  Order, который имеет следующие методы:
# метод __init__, который устанавливает значения атрибутов cart и customer:
# список покупок и имя покупателя
#
# магический метод __add__, который описывает добавления товара в список покупок.
# Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из
# старого заказа и в конец добавляется новый товар. Покупатель в заказе остается прежним
#
# магический метод __radd__, который описывает добавления товара в список покупок при
# правостороннем сложении. Результатом такого сложения должен быть новый заказ,
# в котором все покупки берутся из старого заказа и в начало списка покупок добавляется
# новый товар. Покупатель в заказе остается прежним
#  магический метод __sub__, который описывает исключение товара из списка покупок.
#  Результатом вычитания должен быть новый заказ
# магический метод __rsub__, который описывает исключение товара из списка покупок при
# правостороннем вычитании. Результатом должен быть таким же как и при __sub__
#
# Sample Input:
#
# Sample Output:
#
# Good

class Order:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        if isinstance(other, str):
            return Order(self.cart + other.split(','), self.customer)

    def __radd__(self, other):
        return Order(other.split(',') + self.cart, self.customer)

    def in_list(self, other):
        if isinstance(self, Order):
            if other in self.cart:
                return True
            return False

    def __sub__(self, other):
        if self.in_list(other):
            self.cart.remove(other)
            return Order(self.cart, self.customer)
        else:
            return Order(self.cart, self.customer)

    def __rsub__(self, other):
        if self.in_list(other):
            self.cart.remove(other)
            return Order(self.cart, self.customer)
        else:
            return Order(self.cart, self.customer)



order = Order(['banana', 'apple'], 'Гена Букин')
order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')

# another solution

class Order:
    def __init__(self, cart: list, customer: str):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        return Order(self.cart + [other], self.customer)

    def __radd__(self, other):
        return Order([other] + self.cart, self.customer)

    def __sub__(self, other):
        if other in self.cart:
            self.cart.remove(other)
        return self

    def __rsub__(self, other):
        return self - other


order = Order(['banana', 'apple'], 'Гена Букин')
order_2 = order + 'orange'
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

order = order - 'banana'
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')