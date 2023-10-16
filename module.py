""" День 1. Объектно-ориентированное программирование """
from copy import deepcopy
"""
Классы и объекты

"""


class Programmer:

    def __init__(self, name: str, age: int, iq: int, level: str,
                 languages: list[str]) -> None:
        self.name = name
        if age < 18:
            raise ValueError("Возраст программиста не может быть меньше 18")
        self.age = age
        self.iq = iq
        self.level = level
        self.languages = deepcopy(languages)

    def __str__(self) -> str:
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Уровень: {self.level}"


class Address:

    def __init__(self, city: str, street: str, home: int):
        self.city = city
        self.street = street
        self.home = home

    def __str__(self):
        return f"г. {self.city}, ул. {self.street}, д. {self.home}"


class ITCompany:

    def __init__(self, name: str, address: Address) -> None:

        self.name: str = name
        self.address: Address = deepcopy(address)
        self.programmers: list[Programmer] = []

    def __str__(self):
        return f"Название компании: {self.name} \n" \
               f"Адрес компании: {self.address}"
