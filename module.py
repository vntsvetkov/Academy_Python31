""" Магические (дандеры) методы """
import time


# Последовательности
class StackIndexError(IndexError):

    def __init__(self, text):
        self.text = text


class Stack(object):
    def __init__(self):
        self._floors = []

    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data

    def __getitem__(self, floor_number):
        if len(self._floors) <= abs(floor_number):
            raise StackIndexError("stack index out of range")
        return self._floors[floor_number]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")
        if len(self._floors) <= abs(key):
            raise StackIndexError("stack index out of range")
        del self._floors[key]

    def __len__(self):
        return len(self._floors)

    def append(self, data):
        self._floors.append(data)

    def __bool__(self):
        return len(self) != 0


# Менеджер контекста
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


class Clock:
    """ Класс, который хранит момент времени """
    operation = None

    def __init__(self, h: int, m: int, s: int):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __repr__(self):
        return f"{self.__hour // 10}{self.__hour % 10}:" \
               f"{self.__minute // 10}{self.__minute % 10}:" \
               f"{self.__second // 10}{self.__second % 10}"

    def __str__(self):
        return f"{self.__hour // 10}{self.__hour % 10}:" \
               f"{self.__minute // 10}{self.__minute % 10}:" \
               f"{self.__second // 10}{self.__second % 10}"

    def to_seconds(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    @staticmethod
    def __validate_obj(other):
        if not isinstance(other, (int, Clock)):
            raise TypeError(f"{Clock.operation} not supported between instances "
                            f"of Clock and {other.__class__.__name__}")
        return other if isinstance(other, int) else other.to_seconds()

    def __lt__(self, other):
        Clock.operation = "<"
        other = Clock.__validate_obj(other)
        return self.to_seconds() < other

    def __le__(self, other):
        if isinstance(other, (Clock, int)):
            if isinstance(other, int):
                return self.to_seconds() <= other
            return self.to_seconds() <= other.to_seconds()
        else:
            raise TypeError(f"'<=' not supported between instances "
                            f"of Clock and {other.__class__.__name__}")

    def __eq__(self, other):
        if isinstance(other, (Clock, int)):
            if isinstance(other, int):
                return self.to_seconds() == other
            return self.__hour == other.__hour and \
                self.__minute == other.__minute and \
                self.__second == other.__second
        else:
            raise TypeError(f"'==' not supported between instances "
                            f"of Clock and {other.__class__.__name__}")

    def __ne__(self, other):
        if isinstance(other, (Clock, int)):
            if isinstance(other, int):
                return self.to_seconds() != other
            return self.to_seconds() != other.to_seconds()
        else:
            raise TypeError(f"'!=' not supported between instances "
                            f"of Clock and {other.__class__.__name__}")

    def __gt__(self, other):
        if isinstance(other, (Clock, int)):
            if isinstance(other, int):
                return self.to_seconds() > other
            return self.to_seconds() > other.to_seconds()
        else:
            raise TypeError(f"'>' not supported between instances "
                            f"of Clock and {other.__class__.__name__}")

    def __ge__(self, other):
        if isinstance(other, (Clock, int)):
            if isinstance(other, int):
                return self.to_seconds() >= other
            return self.to_seconds() >= other.to_seconds()
        else:
            raise TypeError(f"'>=' not supported between instances "
                            f"of Clock and {other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__hour, self.__minute, self.__second))

    def __bool__(self):
        """ Возвращает False если полночь """
        return self.to_seconds() != 0

    def __int__(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

