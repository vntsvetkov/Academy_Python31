from abc import ABC, abstractmethod


class UnitSet(ABC):
    pass


class Phone(UnitSet):
    pass


class Charger(UnitSet):
    pass


class Headphones(UnitSet):
    pass


class IPhone(Phone):
    pass


class LightingCharger(Charger):
    pass


class Airpods(Headphones):
    pass


class AndroidPhone(Phone):
    pass


class TypeCCharger(Charger):
    pass


class WirelessHeadphones(Headphones):
    pass


class MobilePhoneFactory(ABC):
    @abstractmethod
    def create_phone(self):
        ...

    @abstractmethod
    def create_charger(self):
        ...

    @abstractmethod
    def create_headphones(self):
        ...


class IOSSetFactory(MobilePhoneFactory):
    def create_phone(self):
        return IPhone()

    def create_charger(self):
        return LightingCharger()

    def create_headphones(self):
        return Airpods()


class AndroidSetFactory(MobilePhoneFactory):
    def create_phone(self):
        return AndroidPhone()

    def create_charger(self):
        return TypeCCharger()

    def create_headphones(self):
        return WirelessHeadphones()


class MobileSet:
    __mobile_set = []

    def add(self, unit: UnitSet):
        self.__mobile_set.append(unit)


class Shop:
    @staticmethod
    def create_mobile_set(factory: MobilePhoneFactory):
        mobile_set = MobileSet()
        mobile_set.add(factory.create_phone())
        mobile_set.add(factory.create_charger())
        mobile_set.add(factory.create_headphones())
        return mobile_set


if __name__ == "__main__":
    shop = Shop()
    mobile = shop.create_mobile_set(IOSSetFactory())
    print(mobile)
