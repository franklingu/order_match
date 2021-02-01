from consts import TRADE_TYPE, FILL_TYPE_FULL


def output_trade(trade):
    print('{},{},{}'.format(TRADE_TYPE, trade.quantity, trade.price))
    if trade.aggressive_fill == FILL_TYPE_FULL:
        print('{},{}'.format(trade.aggressive_fill, trade.aggressive_id))
    else:
        print('{},{},{}'.format(trade.aggressive_fill, trade.aggressive_id, trade.aggressive_quantity))
    if trade.resting_fill == FILL_TYPE_FULL:
        print('{},{}'.format(trade.resting_fill, trade.resting_id))
    else:
        print('{},{},{}'.format(trade.resting_fill, trade.resting_id, trade.resting_quantity))
