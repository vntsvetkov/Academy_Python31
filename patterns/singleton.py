""" Singleton """

"""
Одиночка (singleton) - механизм создания одного и только одного 
экземпляра объекта и предоставления к нему глобальной точки доступа

"""


class DBWorker:

    __data = []

    def add_data(self, value):
        self.__data.append(value)

    def pop_data(self):
        self.__data.pop()

    def print_data(self):
        print(self.__data)


class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = DBWorker()
        return cls.__instance


a = Singleton.get_instance()
b = Singleton.get_instance()

print(a)
print(b)

a.add_data(1)
a.print_data()
b.pop_data()
a.print_data()