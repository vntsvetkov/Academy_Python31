from abc import ABC, abstractmethod

""" Принцип разделения интерфейса (ISP)
Ни один класс не должен зависеть от методов которые он не использует

"""


class Developer(ABC):

    @abstractmethod
    def write_code(self):
        ...


class Backend(ABC):

    @abstractmethod
    def create_db(self):
        ...


class Frontend(ABC):

    @abstractmethod
    def build_web_page(self):
        ...


class BackendDeveloper(Developer, Backend):

    def write_code(self):
        ...

    def create_db(self):
        ...


class FrontendDeveloper(Developer, Frontend):

    def write_code(self):
        ...

    def build_web_page(self):
        ...


class FullStackDeveloper(Developer, Backend, Frontend):

    def write_code(self):
        ...

    def create_db(self):
        ...

    def build_web_page(self):
        ...
