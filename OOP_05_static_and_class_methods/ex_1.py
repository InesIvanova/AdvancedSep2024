from functools import reduce


class Calculator:
    @staticmethod
    def add(*args) -> float:
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args) -> float:
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args) -> float:
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args) -> float:
        return reduce(lambda x, y: x - y, args)
