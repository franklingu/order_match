"""order book implementation. contains actual order matching part
"""
from sortedcontainers import SortedList

from exceptions import UnknownOrderException, DuplicateOrderException
from order import ORDER_BUY_SIDE
from trade import Trade


class OrderBook(object):
    def __init__(self):
        self.buy_orders = SortedList()
        self.sell_orders = SortedList()
        self.buy_mapping = {}
        self.sell_mapping = {}

    def add_order(self, order):
        if order.order_id in self.buy_mapping or order.order_id in self.sell_mapping:
            raise DuplicateOrderException
        if order.order_side == ORDER_BUY_SIDE:
            return self._try_buy(order)
        else:
            return self._try_sell(order)

    def cancel_order(self, order_id):
        if order_id in self.buy_mapping:
            order = self.buy_mapping[order_id]
            self.buy_orders.discard(order)
            del self.buy_mapping[order_id]
            return
        if order_id in self.sell_mapping:
            order = self.sell_mapping[order_id]
            self.sell_orders.discard(order)
            del self.sell_mapping[order_id]
            return
        raise UnknownOrderException

    def _try_buy(self, order):
        trades = []
        while self.sell_orders and order.price >= self.sell_orders[0].price and order.quantity > 0:
            resting_order = self.sell_orders[0]
            trades.append(self._trade(order, resting_order))
            if resting_order.quantity == 0:
                self.sell_orders.pop(0)
        if order.quantity > 0:
            self.buy_orders.add(order)
            self.buy_mapping[order.order_id] = order
        return trades

    def _trade(self, order, resting_order):
        quantity = min(resting_order.quantity, order.quantity)
        price = resting_order.price
        resting_order.quantity -= quantity
        order.quantity -= quantity
        return Trade(quantity, price, order, resting_order)

    def _try_sell(self, order):
        trades = []
        while self.buy_orders and order.price <= self.buy_orders[0].price and order.quantity > 0:
            resting_order = self.buy_orders[0]
            trades.append(self._trade(order, resting_order))
            if resting_order.quantity == 0:
                self.buy_orders.pop(0)
        if order.quantity > 0:
            self.sell_orders.add(order)
            self.sell_mapping[order.order_id] = order
        return trades
