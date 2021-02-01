"""trade
"""
from consts import FILL_TYPE_PARTIAL, FILL_TYPE_FULL


class Trade(object):
    def __init__(self, quantity, price, aggressive_order, resting_order):
        self.quantity = quantity
        self.price = price
        self.aggressive_id = aggressive_order.order_id
        self.aggressive_quantity = aggressive_order.quantity
        if aggressive_order.quantity == 0:
            self.aggressive_fill = FILL_TYPE_FULL
        else:
            self.aggressive_fill = FILL_TYPE_PARTIAL
        self.resting_id = resting_order.order_id
        self.resting_quantity = resting_order.quantity
        if resting_order.quantity == 0:
            self.resting_fill = FILL_TYPE_FULL
        else:
            self.resting_fill = FILL_TYPE_PARTIAL
