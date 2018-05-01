from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


class Order(object):
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion:
            discount = self.promotion.discount(self)
        else:
            discount = 0
        return self.total() - discount

    def __repr__(self):
        fmt = '<Customer: {}  Order total: {:.2f}  due: {:.2f}>'
        return fmt.format(self.customer, self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return discount as a postive dollar amount"""


class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total * 0.10
        return discount


class LargeOrderPromo(Promotion):
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        return order.total() * 0.07 if len(distinct_items) >= 10 else 0


if __name__ == '__main__':
    joe = Customer('Joe', 0)
    ann = Customer('Ann', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('radish', 5, 5.0)]
    order1 = Order(joe, cart, FidelityPromo())
    order2 = Order(ann, cart, FidelityPromo())
    print(repr(order1))
    print(repr(order2))
