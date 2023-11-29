from abc import ABC, abstractmethod

"""
Компоновщик (Composite) - шаблон, который упрощает работу с 
контейнерными объектами, предоставляя контейнерам и объектам 
содержимого общий интерфейс.

Что такое контейнерный тип?

"""


class SystemObject(ABC):
    type = "Объект системы"

    @abstractmethod
    def get_name(self):
        ...

    @abstractmethod
    def get_size(self):
        ...

    @abstractmethod
    def get_data(self):
        ...


class File(SystemObject):
    type = "Файл"

    def __init__(self, name: str, size: int):
        self.__name = name
        self.__size = size

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_data(self):
        ...


class Directory(SystemObject):
    type = "Директория"

    def __init__(self, name: str):
        self.__name = name
        self.__files: list[SystemObject] = []

    def get_name(self):
        return self.__name

    def add(self, data: SystemObject):
        self.__files.append(data)

    def remove(self, data: SystemObject):
        self.__files.remove(data)

    def get_size(self):
        size = 0
        for element in self.__files:
            size += element.get_size()
        return size


file1 = File("Документ 1", 116)
file2 = File("Документ 2", 118)
file3 = File("Документ 3", 100)

directory1 = Directory("Папка 1")
directory2 = Directory("Папка 2")

directory1.add(file1)
directory2.add(file2)
directory2.add(directory1)
directory2.add(file3)

print(directory2.get_size())
