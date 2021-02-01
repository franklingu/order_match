from consts import ORDER_BUY_SIDE, ORDER_SELL_SIDE, FILL_TYPE_FULL, FILL_TYPE_PARTIAL
from order import Order
from trade import Trade


def test_trade():
    quantity = 10
    price = 10
    aggressive_order = Order(1, ORDER_BUY_SIDE, 0, price, 1)
    resting_order = Order(2, ORDER_SELL_SIDE, 1, price, 2)
    trade = Trade(quantity, price, aggressive_order, resting_order)
    assert trade.price == price
    assert trade.quantity == quantity
    assert trade.aggressive_fill == FILL_TYPE_FULL
    assert trade.aggressive_quantity == 0
    assert trade.aggressive_id == 1
    assert trade.resting_fill == FILL_TYPE_PARTIAL
    assert trade.resting_quantity == 1
    assert trade.resting_id == 2
    aggressive_order = Order(1, ORDER_BUY_SIDE, 1, price, 1)
    resting_order = Order(2, ORDER_SELL_SIDE, 0, price, 2)
    trade = Trade(quantity, price, aggressive_order, resting_order)
    assert trade.price == price
    assert trade.quantity == quantity
    assert trade.aggressive_fill == FILL_TYPE_PARTIAL
    assert trade.aggressive_quantity == 1
    assert trade.aggressive_id == 1
    assert trade.resting_fill == FILL_TYPE_FULL
    assert trade.resting_quantity == 0
    assert trade.resting_id == 2
