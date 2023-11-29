from abc import ABC, abstractmethod

"""
Заместитель (Proxy) - шаблон, который предоставляет объект, 
который в свою очередь контролирует доступ к другому объекту.

"""


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float):
        ...

    @abstractmethod
    def replenish(self, amount: float):
        ...

    @abstractmethod
    def get_balance(self):
        ...


class BankAccount(Payment):
    __balance = 0

    def pay(self, amount: float):
        if self.__balance < amount:
            print("Недостаточно средств на счёте")
        else:
            self.__balance -= amount
            print(f"Совершена оплата на сумму {amount}")

    def replenish(self, amount: float):
        self.__balance += amount

    def get_balance(self):
        return f"Остаток: {self.__balance}"


class Card(Payment):

    def __init__(self, account: Payment):
        self.__account = account
        self.__code = 1234

    def pay(self, amount: float):
        code = int(input("Ведите пин-код: "))
        if code == self.__code:
            self.__account.pay(amount)
        else:
            print("Пин-код введён неверно")

    def replenish(self, amount: float):
        self.__account.replenish(amount)

    def get_balance(self):
        return self.__account.get_balance()


bank_account = BankAccount()
card = Card(bank_account)
card.replenish(1000)
card.pay(2000)
print(card.get_balance())
