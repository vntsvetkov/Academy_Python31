from abc import ABC, abstractmethod

"""
Состояние (state) - используется в тех случаях, когда во время выполнения 
программы объект должен менять своё поведение в зависимости от своего состояния.

"""


class DeleteFromEmptyBasketError(Exception):

    def __init__(self, text):
        self.text = text


class BasketState(ABC):

    @staticmethod
    @abstractmethod
    def add(basket, data):
        ...

    @staticmethod
    @abstractmethod
    def remove(basket, data):
        ...


class Basket:

    data = []

    def __init__(self, state: BasketState):
        self.__state = state

    def get_state(self):
        return self.__state.__class__.__name__

    def set_state(self, state: BasketState):
        self.__state = state

    def add(self, data):
        self.__state.add(self, data)

    def remove(self, data):
        self.__state.remove(self, data)

    def __len__(self):
        return len(self.data)


class FullBasket(BasketState):

    @staticmethod
    def add(basket: Basket, data):
        basket.data.append(data)
        print(f"В корзине {len(basket)} товаров")

    @staticmethod
    def remove(basket: Basket, data):
        basket.data.remove(data)
        print(f"В корзине {len(basket)} товаров")
        if len(basket) == 0:
            basket.set_state(EmptyBasket())


class EmptyBasket(BasketState):

    @staticmethod
    def add(basket: Basket, data):
        basket.data.append(data)
        basket.set_state(FullBasket())

    @staticmethod
    def remove(basket: Basket, data):
        raise DeleteFromEmptyBasketError("Невозможно удалить товар из пустой корзины")


basket = Basket(EmptyBasket())
print(basket.get_state())

basket.add("Яблоко")
print(basket.get_state())

basket.add("Слива")
print(basket.get_state())

basket.remove("Яблоко")
print(basket.get_state())

basket.remove("Слива")
print(basket.get_state())

