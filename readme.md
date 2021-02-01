# order match

## program structure
main.py: driver of the whole trade engine
engine.py: trade engine. parse input and produces output
order_book.py: keeps buy and sell orders. produces trades if any
order.py: order
trade.py: trade

## instruction
`pip install -r requirements.txt` to install the requirements
`python main.py` to start running the program and Ctrl+C to exit.
`pytest` to run all the tests

## performance
order_book.py contains the most important part for the whole trade matching algorithm. it is using both dictionary and sorted list from sorted container package.
when adding an order, adding order to sorted list is O(log n) on average; removing resting order is O(log n) as well. so in total O(log n).
when removing an order, removing the order from sorted list if O(log n).

## reference
http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedlist
