"""contains order details
"""
from functools import total_ordering

from consts import ORDER_BUY_SIDE, ACTION_TYPE_ADD_ORDER, ACTION_TYPE_CANCEL_ORDER
from exceptions import IllegalComparisonException


@total_ordering
class Order(object):
    def __init__(self, order_id, order_side, quantity, price, ts):
        self.order_id = order_id
        self.order_side = order_side
        self.quantity = quantity
        self.price = price
        self.ts = ts

    def __lt__(self, other):
        if self.order_side != other.order_side:
            raise IllegalComparisonException
        if self.order_side == ORDER_BUY_SIDE:
            if self.price > other.price:
                return True
        else:
            if self.price < other.price:
                return True
        if self.price == other.price:
            return self.ts < other.ts
        return False

    def __eq__(self, other):
        return self.order_id == other.order_id and self.order_side == other.order_side and \
               self.quantity == other.quantity and self.price == other.price and self.ts == other.ts

    def __str__(self):
        return 'Order:{},{},{},{},{}'.format(self.order_id, self.order_side, self.price, self.quantity, self.ts)

    def __repr__(self):
        return str(self)


class AddOrder(object):
    def __init__(self, order_id, order_side, quantity, price, ts):
        self.action_type = ACTION_TYPE_ADD_ORDER
        self.order = Order(order_id, order_side, quantity, price, ts)


class CancelOrder(object):
    def __init__(self, order_id):
        self.action_type = ACTION_TYPE_CANCEL_ORDER
        self.order_id = order_id
