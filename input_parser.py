"""parse input messages
"""
from exceptions import WrongInputFormatException, WrongMessageTypeException
from order import AddOrder, CancelOrder
from consts import ORDER_BUY_SIDE, ORDER_SELL_SIDE


def _parse_add_order_message(items, ts):
    if len(items) != 5:
        raise WrongInputFormatException
    try:
        order_id = int(items[1])
        if order_id <= 0:
            raise WrongInputFormatException
        if items[2] not in order_sides:
            raise WrongInputFormatException
        order_side = order_sides[items[2]]
        quantity = int(items[3])
        if quantity <= 0:
            raise WrongInputFormatException
        price = float(items[4])
        return AddOrder(order_id, order_side, quantity, price, ts)
    except ValueError:
        raise WrongInputFormatException


def _parse_cancel_order_message(items, _ts):
    if len(items) != 2:
        raise WrongInputFormatException
    try:
        order_id = int(items[1])
        if order_id <= 0:
            raise WrongInputFormatException
        return CancelOrder(order_id)
    except ValueError:
        raise WrongInputFormatException


input_msg_types = {
    '0': _parse_add_order_message,
    '1': _parse_cancel_order_message,
}
order_sides = {
    '0': ORDER_BUY_SIDE,
    '1': ORDER_SELL_SIDE,
}


def parse_input_message(message, ts):
    items = message.split(',')
    if len(items) < 1:
        raise WrongInputFormatException
    if items[0] not in input_msg_types:
        raise WrongMessageTypeException
    return input_msg_types[items[0]](items, ts)
