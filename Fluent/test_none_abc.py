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
            discount = self.promotion(self)  # Just call self.promotion
        else:
            discount = 0
        return self.total() - discount

    def __repr__(self):
        fmt = '<Customer: {}  Order total: {:.2f}  due: {:.2f}>'
        return fmt.format(self.customer, self.total(), self.due())


def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.10
    return discount


def large_order_promo(order):
    distint_items = {item.product for item in order.cart}
    return order.total() * 0.07 if len(distint_items) >= 10 else 0


promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    return max((promo(order) for promo in promos))


if __name__ == '__main__':
    joe = Customer('Joe', 0)
    ann = Customer('Ann', 1100)
    # Test fedility
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('radish', 5, 5.0)]
    order1 = Order(joe, cart, fidelity_promo)
    order2 = Order(ann, cart, fidelity_promo)
    print(repr(order1))
    print(repr(order2))

    # Test bulk item
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    order3 = Order(joe, banana_cart, bulk_item_promo)
    print(repr(order3))

    # Test long order
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    order4 = Order(joe, long_order, large_order_promo)
    order5 = Order(ann, long_order, large_order_promo)
    print(repr(order4))
    print(repr(order5))

    # Test best promo
    print(repr(Order(ann, )))
    print(repr())
    print(repr())
