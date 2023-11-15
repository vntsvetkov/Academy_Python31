class Fraction:
    """ Класс для хранения обыкновенной дроби """
    def __init__(self, m: int, n: int):
        self.__m = m
        self.__n = n


a = Fraction(1, 2)  # 1/2
b = Fraction(3, 4)  # 3/4

# a + b
# a + 5
# 5 + a
# a - b
# a * b
# a / b


class Number:

    def __init__(self, value: str, system: int):
        self.__value = value
        self.__system = system


class SystemCalculate:
    @staticmethod
    def add(n: Number, m: Number) -> Number:
        """ Возвращает результат в CC числа n"""
        return n + m

    @staticmethod
    def sub(n: Number, m: Number) -> Number:
        """ Метод, который вычитает из большего меньшее
        и возвращает ответ в СС числа n
        """
        return n - m


c = Number("10", 2)
d = Number("9", 10)

SystemCalculate.add(c, d)
SystemCalculate.sub(c, d)

