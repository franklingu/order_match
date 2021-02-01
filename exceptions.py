"""utilities: exceptions
"""


class WrongInputFormatException(Exception):
    pass


class WrongMessageTypeException(Exception):
    pass


class UnknownOrderException(Exception):
    pass


class DuplicateOrderException(Exception):
    pass


class IllegalComparisonException(Exception):
    pass
