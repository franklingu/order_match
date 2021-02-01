"""trade engine
"""
import sys

from exceptions import WrongInputFormatException, WrongMessageTypeException, UnknownOrderException, \
    DuplicateOrderException
from input_parser import parse_input_message
from consts import ACTION_TYPE_ADD_ORDER, ACTION_TYPE_CANCEL_ORDER
from order_book import OrderBook
from output_formatter import output_trade


class Engine(object):
    def __init__(self):
        self.order_book = OrderBook()
        self.ts = 0

    def execute(self, message):
        self.ts += 1
        try:
            order_action = parse_input_message(message, self.ts)
            if order_action.action_type == ACTION_TYPE_ADD_ORDER:
                trades = self.order_book.add_order(order_action.order)
                for trade in trades:
                    output_trade(trade)
            elif order_action.action_type == ACTION_TYPE_CANCEL_ORDER:
                self.order_book.cancel_order(order_action.order_id)
        except WrongInputFormatException:
            sys.stderr.write('Wrong input format: {}\n'.format(message))
        except WrongMessageTypeException:
            sys.stderr.write('Wrong message type: {}\n'.format(message))
        except UnknownOrderException:
            sys.stderr.write('Unknown order: {}\n'.format(message))
        except DuplicateOrderException:
            sys.stderr.write('Duplicate order: {}\n'.format(message))
