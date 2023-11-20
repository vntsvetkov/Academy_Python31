# Онлайн-платеж. Выполнить платеж с смс-подтверждением
from abc import ABC, abstractmethod
import random

class AuthenticationError(Exception):

    def __init__(self, text):
        self.__text = text


class Authentication(ABC):

    @abstractmethod
    def generate_code(self):
        ...

    @abstractmethod
    def send_code(self):
        ...

    @abstractmethod
    def authentication(self):
        ...

    @abstractmethod
    def is_authentication(self):
        ...


class SMSAuthentication(Authentication):

    def __init__(self):
        self.__status = False
        self.__code = None

    def generate_code(self):
        self.__code = "".join([str(random.randint(0, 9)) for _ in range(4)])

    def send_code(self):
        print(f"Ваш код: {self.__code}")

    def authentication(self):
        code = input("Введите код: ")
        self.__status = self.__code == code

    def is_authentication(self):
        return self.__status


class A(ABC):

    @abstractmethod
    def add(self, value):
        ...

    def pay(self, value):
        ...


class Card(A):

    def __init__(self):
        self.__score = 0

    def add(self, value):
        self.__score += value

    def pay(self, value):
        self.__score -= value
        print(f"Совершена оплата на сумму {value}")
        print(f"Текущий остаток {self.__score}")


class Payment:

    def __init__(self, auth: Authentication):
        self.__auth = auth

    def pay(self, card: A, amount: float):
        self.__auth.generate_code()
        self.__auth.send_code()
        self.__auth.authentication()
        if self.__auth.is_authentication():
            print("Код подтверждения принят")
            card.pay(amount)
        else:
            raise AuthenticationError("Неверный код подтверждения...")

