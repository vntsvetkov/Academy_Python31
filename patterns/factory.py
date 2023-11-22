from abc import ABC, abstractmethod

"""
Фабрика (фабричный метод) - шаблон, который используется для 
создания объектов общего интерфейса.

"""


class Transport(ABC):

    @abstractmethod
    def deliver(self):
        ...


class Truck(Transport):

    def deliver(self):
        print("Доставка груза наземным транспортом")


class Airplane(Transport):

    def deliver(self):
        print("Доставка груза воздушным транспортом")


class Delivery:

    @abstractmethod
    def create_transport(self, id_transport):
        ...


class GroundDelivery(Delivery):

    t = {1: Truck()}

    def create_transport(self, id_transport) -> Transport:
        return self.t.get(id_transport)


class FlyDelivery(Delivery):

    def create_transport(self, id_transport) -> Transport:
        return Airplane()


transport = GroundDelivery().create_transport(1)
