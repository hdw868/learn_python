promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity_promo(order):
    return order.total()*0.05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item_promo(order):
    discount = 0
    for line_item in order.cart:
        if line_item.quantity >= 20:
            discount += line_item.total() * 0.10
    return discount


@promotion
def large_order_promo(order):
    distinct_items = {line_item.product for line_item in order.cart}
    return order.total()*0.07 if len(distinct_items) >= 10 else 0


def best_promo(order):
    return max(promo(order) for promo in promos)
