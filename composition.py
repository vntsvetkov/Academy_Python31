from copy import copy, deepcopy

"""
        2.2 Композиция. Тип взаимодействия, когда класс владеет объектом
и несет ответственность за его время жизни. (сильная асоциация)

"""


class Engine:

    def __init__(self, power):
        self.__power = power


class PatrolEngine(Engine):
    ...


class GasEngine(Engine):
    ...


class Car:

    def __init__(self):
        self.__engine = Engine(120)

