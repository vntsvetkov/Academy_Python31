""" День 1. Объектно-ориентированное программирование. Классы и объекты"""
from copy import deepcopy


class Programmer:

    def __init__(self, name: str, age: int, iq: int, level: str,
                 languages: list[str]) -> None:
        self.name: str = name
        if age < 18:
            raise ValueError("Возраст программиста не может быть меньше 18")
        self.age: int = age
        self.iq: int = iq
        self.level: str = level
        self.languages: list[str] = deepcopy(languages)

    def __str__(self) -> str:
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Уровень: {self.level}"


class Address:

    def __init__(self, city: str, street: str, home: int):
        self.city: str = city
        self.street: str = street
        self.home: int = home

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
