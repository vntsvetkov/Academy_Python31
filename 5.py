from abc import ABC, abstractmethod

""" Принцип инверсии зависимостей (DIP)
Модули высших уровней не должны зависеть от модулей низших уровней.
И то и другое должно зависеть от абстракций.

"""


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float):
        ...


class Card(Payment):

    def pay(self, amount: float):
        print(f"Оплата совершена по карте на сумму {amount}")


class QRCode(Payment):

    def pay(self, amount: float):
        print(f"Оплата совершена по qr-коду на сумму {amount}")


class Shop:

    def __init__(self, payment: Payment):
        self.payment = payment

    def do_pay(self, amount: float):
        self.payment.pay(amount)


# Пример 2.


class Transport(ABC):

    @abstractmethod
    def drive(self, distance: float):
        ...


class Car(Transport):

    def drive(self, distance: float):
        ...


class Bus(Transport):

    def drive(self, distance: float):
        ...


class Truck(Transport):

    def drive(self, distance: float):
        ...


class Excursion:

    def __init__(self, transport: Transport):
        self.transport = transport

    def do_trip(self, distance: float):
        self.transport.drive(distance)

