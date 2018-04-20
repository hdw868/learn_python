from promo import *
from order import *
Customer = namedtuple('Customer', 'name,fidelity')
ann = Customer('ann', 1000)
ben = Customer('ben', 0)

cart1 = [LineItem('banana', 5, 10),
         LineItem('apple', 20, 3.3),
         LineItem('radish', 10, 2.2)
         ]

order_ann = Order(ann, cart1, fidelity_promo)
print(repr(order_ann))
