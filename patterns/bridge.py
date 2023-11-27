from abc import ABC, abstractmethod

"""
Мост (Bridge) - шаблон, который говорит, что композиция
и агрегация лучше наследование. Отделяет абстракции от реализации 
и делает их независимыми.

"""


class Theme(ABC):

    @abstractmethod
    def get_color(self):
        ...


class DarkTheme(Theme):
    __main_color = "#000000"

    def get_color(self):
        return f"Основной цвет страницы: {self.__main_color}"


class LightTheme(Theme):
    __main_color = "#FFFFFF"

    def get_color(self):
        return f"Основной цвет страницы: {self.__main_color}"


class WebPage(ABC):

    @abstractmethod
    def get_content(self):
        ...

    @abstractmethod
    def get_theme(self):
        ...


class HomePage(WebPage):

    def __init__(self, theme: Theme):
        self.__theme = theme

    def get_content(self):
        print("Домашняя страница")

    def get_theme(self):
        return self.__theme.get_color()


class AboutPage(WebPage):

    def __init__(self, theme: Theme):
        self.__theme = theme

    def get_content(self):
        print("Страница о нас")

    def get_theme(self):
        return self.__theme.get_color()


page = HomePage(DarkTheme())
print(page.get_theme())
