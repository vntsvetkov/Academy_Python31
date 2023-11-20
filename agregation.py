from copy import copy, deepcopy

"""
Взаимодействие между классами.
Есть 3 способа:
    1. Наследование. Класс-наследник имеет все поля и методы 
    родителя и добавляет какой-то новый функционал.
    Описывается словом "является". 
    
    2. Ассоциация. Класс в качестве полей использует другой класс
    
    class Engine: ...
    class Car:
        engine: Engine
        
    Описывается словом "имеет". Автомобиль имеет двигатель.
    
    class Car(Engine): - миксины
        ...
        
        2.1 Агрегация ("Слабая ассоциация"). Тип взаимодействия, когда 
        зависимая структура может существовать отдельно от родительской.

"""


class Book:

    def __init__(self, name: str):
        self.__name = name


class Reader:

    def __init__(self, name: str, number: str):
        self.__name = name
        self.__number = number
        self.__books: list[Book] = []

    def add_book(self, b: Book):
        self.__books.append(b)


class Library:

    def __init__(self):
        self.__books: list[Book] = []
        self.__readers: list[Reader] = []

    def add_book(self, b: Book):
        self.__books.append(b)

    def give_book(self, b: Book, r: Reader):
        if b in self.__books:
            if r in self.__readers:
                r.add_book(b)  # выдать читателю книгу
                self.__books.remove(b)  # удалить книгу из библиотеки


book = Book("Самоучитель по Python")
library = Library()
library.add_book(book)

"""
Между классами Library и Book возникает слабая ассоциация, т.е. 
класс Library позаимствовал объект класса Book, в т.ч. класс Reader
также позаимствовал объект класса Book.

"""


class Engine:
    __status = False

    def __init__(self, power: int):
        self.__power = power

    def get_status(self):
        return self.__status

    def on(self):
        self.__status = True

    def off(self):
        self.__status = False


class Car:

    def __init__(self, engine: Engine):
        self.__engine = engine

    def start(self):
        if self.__engine.get_status():
            print("Двигатель уже заведен, можно ехать")
        else:
            self.__engine.on()
            print("Двигатель заведен, поехали...")


engine = Engine(120)
car = Car(engine)
car.start()

"""
Агрегация - это когда экземпляр класса engine был создан где-то извне
и передается в конструктор класса Car в качестве параметра.

"""

"""
Принцип внедрения зависимостей (dependency injection)

Способ 1. Внедрение через метод инициализации. 
class Car:

    def __init__(self, engine: Engine):
        self.__engine = engine

Способ 2. Внедрение через методы. (Method injection)

class Car:
    __engine: Engine
    
    def set_engine(self, engine: Engine):
        self.__engine = engine
    
Способ 3. Внедрение через метод установки. (Field injection)

class Car:
    __engine: Engine

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine: Engine):
        self.__engine = engine

"""