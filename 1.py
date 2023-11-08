""""""

""" 
Принцип единственной ответственности (SRP) 
Каждый класс должен выполнять только одну возложенную на него задачу
"""

# Пример 1. Класс автомобиль


class Car:

    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"Автомобиль марки: {self.model}"

    def start_engine(self):
        ...

    def stop_engine(self):
        ...

    def check_fuel(self):
        ...

    def drive(self):
        ...


class CarDBManagement:

    @staticmethod
    def save_to_db(car: Car, db_name: str):
        ...

    @staticmethod
    def load_from_db(db_name: str) -> Car:
        ...


# Пример 2. Класс клиент

class Client:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class ClientDBManagement:

    def save_to_db(self, client: Client):
        ...


class MailingSystem:

    def send_message(self, email: str):
        ...

