from abc import ABC, abstractmethod
import json

"""
Адаптер - шаблон, который объединяет два несовместимых интерфейса

"""


class Person:
    def __init__(self, name: str, surname: str, year: int):
        self.name = name
        self.surname = surname
        self.year = year

    def __str__(self):
        return f"{self.name} {self.surname} {self.year}"


class JSONPersonAdapter:

    @staticmethod
    def dumps(obj: Person) -> str:
        if isinstance(obj, Person):
            return json.dumps({
                "name": obj.name,
                "surname": obj.surname,
                "year": obj.year,
            })
            # return json.dumps(obj.__dict__)

    @staticmethod
    def loads(data: str) -> Person:
        data = json.loads(data)
        try:
            obj = Person(data["name"], data["surname"], data["year"])
        except AttributeError as e:
            print(e)
        else:
            return obj


person = Person("Иван", "Иванов", 1980)
json_obj = JSONPersonAdapter.dumps(person)
print(json_obj)
person_obj = JSONPersonAdapter.loads(json_obj)
print(person_obj)
