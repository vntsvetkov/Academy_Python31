from abc import ABC, abstractmethod
import sqlite3
import pandas

"""
Фасад - паттерн, который реализует простой интерфейс для работы 
со сложной библиотекой, модулем или группой связных модулей.

"""


class DBSqliteWorker:

    def connect(self, table_name: str) -> sqlite3.Connection:
        con = sqlite3.connect(table_name)
        return con

    def get_data(self):
        ...

    def insert_data(self):
        ...


class PandasWorker:

    df: pandas.DataFrame

    def create_dataframe(self, data: dict):
        self.df = pandas.DataFrame(data)

    def get_data(self):
        ...

    def insert_data(self):
        ...

    def to_sql(self, table_name: str, conn: sqlite3.Connection):
        self.df.to_sql(table_name, conn)


class DBFacade:

    def __init__(self, db: DBSqliteWorker, pd: PandasWorker):
        self.__pd = pd
        self.__db = db

    def from_dataframe_to_db(self, table_name: str, data: dict):
        """ Считать данные из dataframe в БД"""
        self.__pd.create_dataframe(data)
        conn = self.__db.connect(table_name)
        self.__pd.to_sql(table_name, conn)


facade = DBFacade(DBSqliteWorker(), PandasWorker())
facade.from_dataframe_to_db("user.db", {
    "id": [5, 6],
    "name": ["John", "James"],
    "age": [41, 55]
})
