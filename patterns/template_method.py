from abc import ABC, abstractmethod

"""
Шаблонный метод (Template method) - шаблон, который описывает порядок
алгоритма, перекладывая ответственность за реализацию на наследников

"""


class DataParser:

    def parse(self):
        self.open_file()
        self.get_data()
        self.parse_data()
        self.save_data()
        self.close_file()

    @abstractmethod
    def open_file(self):
        ...

    @abstractmethod
    def get_data(self):
        ...

    @abstractmethod
    def parse_data(self):
        ...

    @abstractmethod
    def save_data(self):
        ...

    @abstractmethod
    def close_file(self):
        ...


class WordDocParser(DataParser):

    def open_file(self):
        print("Открыли файл с расширением .docx ")

    def get_data(self):
        print("Получили данные ")

    def parse_data(self):
        print("Распарсили данные ")

    def save_data(self):
        print("Сохранили данные ")

    def close_file(self):
        print("Закрыли файл с расширением .docx ")


class PDFParser(DataParser):
    
    def open_file(self):
        print("Открыли файл с расширением .pdf ")

    def get_data(self):
        print("Получили данные ")

    def parse_data(self):
        print("Распарсили данные ")

    def save_data(self):
        print("Сохранили данные ")

    def close_file(self):
        print("Закрыли файл с расширением .docx ")


parser = PDFParser()
parser.parse()



