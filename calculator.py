

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def div(a, b):
        if b != 0:
            return a / b
        raise ZeroDivisionError("Попытка деления на ноль")