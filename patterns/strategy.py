from abc import ABC, abstractmethod

"""
Стратегия (Strategy) - шаблон, который обеспечивает взаимозаменяемость
разных алгоритмов с одинаковым интерфейсом

Калькулятор

Арифметическая операция
Сложить
Вычесть
Умножить
Разделить

"""


class Operation(ABC):

    @abstractmethod
    def execute(self, a, b):
        ...


class Add(Operation):

    def execute(self, a, b):
        return a + b


class Sub(Operation):

    def execute(self, a, b):
        return a - b


class Mult(Operation):

    def execute(self, a, b):
        return a * b


class Div(Operation):

    def execute(self, a, b):
        if b != 0:
            return a / b


class Calculator:

    def __init__(self, operation: Operation):
        self.__operation = operation

    def calculate(self, a, b):
        return self.__operation.execute(a, b)


calc = Calculator(Div())
print(calc.calculate(1, 2))
