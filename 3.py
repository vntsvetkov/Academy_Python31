from abc import ABC, abstractmethod


""" Принцип подстановки Лисков (LSP)
Объекты подклассов должны быть полностью взаимозаменяемыми 
с объектами своих родителей
Реализация полиморфизма
"""

# Пример 1. Класс транспорт.


class Transport(ABC):

    @abstractmethod
    def drive(self):
        ...


class Car(Transport):

    def drive(self):
        ...


class Bus(Transport):

    def drive(self):
        ...


class Truck(Transport):

    def drive(self):
        ...


def trip(transport: Transport):

    transport.drive()


# Пример 2. Класс разработчик

class Task:

    def __init__(self, text):
        self.text = text


class Developer(ABC):

    @abstractmethod
    def write_code(self, task: Task):
        ...


class BackendDeveloper(Developer):

    def write_code(self, task: Task):
        ...


class FrontendDeveloper(Developer):

    def write_code(self, task: Task):
        ...


class FullStackDeveloper(Developer):

    def write_code(self, task: Task):
        ...


def make_task(developer: Developer, task: Task):

    developer.write_code(task)

