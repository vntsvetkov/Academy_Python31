""" День 2. Объектно-ориентированное программирование. Методы. Методы объекта """
from copy import deepcopy


class Programmer:

    def __init__(self, name: str, age: int, iq: int, level: str,
                 languages: list[str]) -> None:
        self.name: str = self.__validate_name(name)
        self.age: int = self.__validate_age(age)
        self.iq: int = self.__validate_iq(iq)
        self.level: str = level
        self.languages: list[str] = deepcopy(languages)

    def __str__(self) -> str:
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Уровень: {self.level} \n" \
               f"Языки: {', '.join(self.languages)}"

    @staticmethod
    def __validate_name(name: str):
        if len(name) == 0:
            raise ValueError("Имя программиста не может пустым")
        return name

    @staticmethod
    def __validate_age(age: int) -> int:
        if 0 < age < 18:
            raise ValueError("Возраст программиста не может быть меньше 18")
        if age < 0:
            raise ValueError("Возраст программиста не может быть отрицательным")
        return age

    @staticmethod
    def __validate_iq(iq: int):
        if iq < 0:
            raise ValueError("Параметр IQ не может быть отрицательным")
        return iq

    def add_language(self, lang: str) -> None:
        self.languages.append(lang)


""" Модификаторы доступа. 
public - доступен всем
__private - доступен только в классе
_protected - доступен из родительского класса

"""


class Student:

    def __init__(self, name: str, age: int, group: str, scores: list[int]):
        self.__name = self.__validate_name(name)
        self.__age = self.__validate_age(age)
        self.__group = self.__validate_group(group)
        self.__scores = deepcopy(scores)

    def __str__(self):
        return f"Имя: {self.__name} \n" \
               f"Возраст: {self.__age} \n" \
               f"Группа: {self.__group} \n" \
               f"Средний балл: {self.__calc_avg_score()}"

    @staticmethod
    def __validate_name(name: str):
        if len(name) == 0:
            raise ValueError("Имя студента не может пустым")
        return name

    @staticmethod
    def __validate_age(age: int) -> int:
        if age < 0:
            raise ValueError("Возраст студента не может быть отрицательным")
        return age

    @staticmethod
    def __validate_group(group: str):
        if len(group) == 0:
            raise ValueError("Параметр группы не может пустым")
        return group

    @property
    def avg_score(self):
        return self.__calc_avg_score()

    def __calc_avg_score(self):
        if len(self.__scores) == 0:
            return 0
        return sum(self.__scores) / len(self.__scores)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name) == 0:
            raise ValueError("Имя студента не может пустым")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("Возраст студента не может быть отрицательным")
        self.__age = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value: str):
        if len(value) == 0:
            raise ValueError("Параметр группа не может быть пустым")
        self.__group = value

    def add_score(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Оценка должна быть целым значением")
        if value < 0:
            raise ValueError("Оценка студента не может быть отрицательной")
        if value > 5 or value == 0:
            raise ValueError("Оценка студента должна быть в диапазоне от 1 до 5")
        self.__scores.append(value)
