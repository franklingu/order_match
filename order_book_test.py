import pytest

from consts import ORDER_BUY_SIDE, ORDER_SELL_SIDE, FILL_TYPE_PARTIAL, FILL_TYPE_FULL
from exceptions import UnknownOrderException, DuplicateOrderException
from order import Order
from order_book import OrderBook


def test_order_book():
    order_book = OrderBook()
    assert len(order_book.sell_orders) == 0
    assert len(order_book.buy_orders) == 0
    trades = order_book.add_order(Order(100000, ORDER_SELL_SIDE, 1, 1075, 1))
    assert len(trades) == 0
    assert len(order_book.sell_orders) == 1
    assert len(order_book.buy_orders) == 0
    assert order_book.sell_orders[0].order_id == 100000
    trades = order_book.add_order(Order(100001, ORDER_BUY_SIDE, 9, 1000, 2))
    assert len(trades) == 0
    assert len(order_book.sell_orders) == 1
    assert len(order_book.buy_orders) == 1
    assert order_book.sell_orders[0].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    trades = order_book.add_order(Order(100002, ORDER_BUY_SIDE, 30, 975, 3))
    assert len(trades) == 0
    assert len(order_book.sell_orders) == 1
    assert len(order_book.buy_orders) == 2
    assert order_book.sell_orders[0].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100002
    trades = order_book.add_order(Order(100003, ORDER_SELL_SIDE, 10, 1050, 3))
    assert len(trades) == 0
    assert len(order_book.sell_orders) == 2
    assert len(order_book.buy_orders) == 2
    assert order_book.sell_orders[0].order_id == 100003
    assert order_book.sell_orders[1].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100002
    trades = order_book.add_order(Order(100004, ORDER_BUY_SIDE, 10, 950, 4))
    assert len(trades) == 0
    assert len(order_book.sell_orders) == 2
    assert len(order_book.buy_orders) == 3
    assert order_book.sell_orders[0].order_id == 100003
    assert order_book.sell_orders[1].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100002
    assert order_book.buy_orders[2].order_id == 100004
    trades = order_book.add_order(Order(100005, ORDER_SELL_SIDE, 2, 1025, 5))
    assert len(trades) == 0
    assert len(order_book.sell_orders) == 3
    assert len(order_book.buy_orders) == 3
    assert order_book.sell_orders[0].order_id == 100005
    assert order_book.sell_orders[1].order_id == 100003
    assert order_book.sell_orders[2].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100002
    assert order_book.buy_orders[2].order_id == 100004
    trades = order_book.add_order(Order(100006, ORDER_BUY_SIDE, 1, 1000, 6))
    assert len(trades) == 0
    assert len(order_book.sell_orders) == 3
    assert len(order_book.buy_orders) == 4
    assert order_book.sell_orders[0].order_id == 100005
    assert order_book.sell_orders[1].order_id == 100003
    assert order_book.sell_orders[2].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100006
    assert order_book.buy_orders[2].order_id == 100002
    assert order_book.buy_orders[3].order_id == 100004
    order_book.cancel_order(100004)
    assert len(order_book.sell_orders) == 3
    assert len(order_book.buy_orders) == 3
    assert order_book.sell_orders[0].order_id == 100005
    assert order_book.sell_orders[1].order_id == 100003
    assert order_book.sell_orders[2].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100006
    assert order_book.buy_orders[2].order_id == 100002
    trades = order_book.add_order(Order(100007, ORDER_SELL_SIDE, 5, 1025, 8))
    assert len(trades) == 0
    assert order_book.sell_orders[0].order_id == 100005
    assert order_book.sell_orders[1].order_id == 100007
    assert order_book.sell_orders[2].order_id == 100003
    assert order_book.sell_orders[3].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100006
    assert order_book.buy_orders[2].order_id == 100002
    trades = order_book.add_order(Order(100008, ORDER_BUY_SIDE, 3, 1050, 9))
    assert len(trades) == 2
    assert trades[0].quantity == 2
    assert trades[0].price == 1025
    assert trades[0].aggressive_fill == FILL_TYPE_PARTIAL
    assert trades[0].aggressive_quantity == 1
    assert trades[0].aggressive_id == 100008
    assert trades[0].resting_fill == FILL_TYPE_FULL
    assert trades[0].resting_id == 100005
    assert trades[1].quantity == 1
    assert trades[1].price == 1025
    assert trades[1].aggressive_fill == FILL_TYPE_FULL
    assert trades[1].aggressive_id == 100008
    assert trades[1].resting_fill == FILL_TYPE_PARTIAL
    assert trades[1].resting_id == 100007
    assert trades[1].resting_quantity == 4
    assert order_book.sell_orders[0].order_id == 100007
    assert order_book.sell_orders[1].order_id == 100003
    assert order_book.sell_orders[2].order_id == 100000
    assert order_book.buy_orders[0].order_id == 100001
    assert order_book.buy_orders[1].order_id == 100006
    assert order_book.buy_orders[2].order_id == 100002
    with pytest.raises(UnknownOrderException):
        order_book.cancel_order(1000004)
    with pytest.raises(DuplicateOrderException):
        order_book.add_order(Order(100007, ORDER_SELL_SIDE, 5, 1025, 11))
