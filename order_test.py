from consts import ORDER_BUY_SIDE, ORDER_SELL_SIDE
from order import Order


def test_order_ordering():
    order1 = Order(1, ORDER_BUY_SIDE, 1, 2, 1)
    order2 = Order(2, ORDER_BUY_SIDE, 1, 1, 2)
    assert order1 < order2
    order1 = Order(1, ORDER_BUY_SIDE, 1, 1, 1)
    order2 = Order(2, ORDER_BUY_SIDE, 1, 1, 2)
    assert order1 < order2
    order1 = Order(1, ORDER_SELL_SIDE, 1, 2, 1)
    order2 = Order(2, ORDER_SELL_SIDE, 1, 1, 2)
    assert order1 > order2
    order1 = Order(1, ORDER_SELL_SIDE, 1, 1, 1)
    order2 = Order(2, ORDER_SELL_SIDE, 1, 1, 2)
    assert order1 < order2
