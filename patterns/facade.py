from abc import ABC, abstractmethod
import sqlite3
import pandas

"""
Фасад - паттерн, который реализует простой интерфейс для работы 
со сложной библиотекой, модулем или группой связных модулей.

"""


class DBSqliteWorker:

    def connect(self) -> sqlite3.Connection:
        ...

    def get_data(self):
        ...

    def insert_data(self):
        ...


class PandasWorker:

    def create_dataframe(self, data: dict) -> pandas.DataFrame:
        ...

    def get_data(self):
        ...

    def insert_data(self):
        ...

    def to_sql(self, conn: sqlite3.Connection):
        ...


class DBFacade:

    def __init__(self, db: DBSqliteWorker, pd: PandasWorker):
        self.__pd = pd
        self.__db = db

    def from_dataframe_to_db(self, data: dict):
        """ Считать данные из dataframe в БД"""
        self.__pd.create_dataframe(data)
        conn = self.__db.connect()
        self.__pd.to_sql(conn)


facade = DBFacade(DBSqliteWorker(), PandasWorker())
facade.from_dataframe_to_db({
    "id": [5, 6],
    "name": ["John", "James"],
    "age": [41, 55]
})
