class SetError(Exception):
    def __init__(self, text):
        self.text = text


class LevelSetError(SetError):
    """ Исключение, которое возникает при попытке установить
    неверное значение градации сотрудника IT компании"""
    ...


class ValidateError(Exception):
    def __init__(self, text):
        self.text = text


class ValidateErrorName(ValidateError):
    """ Исключение, которое возникает при попытке проверить
        значение имени сотрудника IT компании"""
    ...


class ITEmployee:

    def __init__(self, name: str, age: int, level: str) -> None:
        self._name = self.__validate_name(name)
        self._age = age
        self.__level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value: str):
        self.__level = value

    def __str__(self) -> str:
        return f"Имя: {self._name} \n" \
               f"Возраст: {self._age} \n" \
               f"Уровень: {self.__level} \n"

    @staticmethod
    def __validate_name(name: str):
        if len(name) == 0:
            raise ValidateErrorName("Имя студента не может пустым")
        return name


class RemoteITEmployee(ITEmployee):
    ...


class OfficeITEmployee(ITEmployee):
    ...


class Tester(ITEmployee):
    """ Класс тестировщик """
    def __init__(self, name: str, age: int, level: str,
                 tool: str) -> None:
        super().__init__(name, age, level)
        self.tool = tool

    @ITEmployee.level.setter
    def level(self, value: str):
        """ Переопределение сеттера """
        if value not in ('Junior', 'Middle', 'Senior'):
            raise LevelSetError("Неверное значение...")
        ITEmployee.level.fset(self, value)
        # super().level = value

    def __str__(self):
        return super().__str__() + \
               f"Инструмент тестирования: {self.tool} \n"

        # return f"Имя: {self._name} \n" \
        #        f"Возраст: {self._age} \n" \
        #        f"Уровень: {self._level} \n" \
        #        f"Инструмент тестирования: {self.tool} \n"


class AutoTester(Tester):
    ...


class AutoMobileTester(AutoTester):
    ...


class AutoWebTester(AutoTester):
    ...


class FunctionalTester(Tester):
    ...


class Programmer(ITEmployee):
    """ Класс программист"""

    def __init__(self, name: str, age: int, level: str,
                 language: str) -> None:
        super().__init__(name, age, level)
        self.language = language

    @ITEmployee.level.getter
    def level(self):
        """ Переопределение сеттера """
        return ITEmployee.level.fget(self)
        # return super().level

    def __str__(self):
        return super().__str__() + \
               f"Язык программирования: {self.language} \n"

        # return f"Имя: {self._name} \n" \
        #        f"Возраст: {self._age} \n" \
        #        f"Уровень: {self._level} \n" \
        #        f"Язык программирования: {self.language} \n"


class FrontendProgrammer(Programmer):
    ...


class BackendProgrammer(Programmer):
    ...


class FullstackProgrammer(Programmer):
    ...

