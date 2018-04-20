from collections import namedtuple
import promo
Customer = namedtuple('Customer', 'name, fidelity')


class LineItem(object):
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order(object):
    def __init__(self, cart, customer, promotion=None):
        self.cart = cart
        self.customer = customer
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total()for item in self.cart)
        return self.__total

    def due(self):
        discount = self.promotion(self) if self.promotion else 0
        return self.total() - discount

    def __repr__(self):
        return '<Cusomter: {} Total: {:.2f} Due: {:.2f}>'.format(
            self.customer.name, self.total(), self.due())


if __name__ == '__main__':
    ann = Customer('ann', 1000)
    ben = Customer('ben', 0)
    cart1 = [LineItem('banana', 5, 10),
             LineItem('apple', 20, 3.3),
             LineItem('radish', 10, 2.2)
             ]

    order_ann_bulk = Order(cart1, ann, promo.bulk_item_promo)
    print(repr(order_ann_bulk))
    order_ann_fidelity = Order(cart1, ann, promo.fidelity_promo)
    print(repr(order_ann_fidelity))
    order_ann_best = Order(cart1, ann, promo.best_promo)
    print(repr(order_ann_best))
