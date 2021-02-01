"""driver of the program
"""
from engine import Engine


def main():
    engine = Engine()
    while True:
        try:
            message = input()
            if not message:  # simply ignore empty input line
                continue
            engine.execute(message)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
