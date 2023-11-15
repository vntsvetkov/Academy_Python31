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

    def __int__(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    @classmethod
    def from_seconds(cls, seconds: int):
        h = seconds // 3600 % 24
        m = seconds // 60 % 60
        s = seconds % 60
        return cls(h, m, s)

    @staticmethod
    def __convert_seconds(seconds: int) -> tuple[int, ...]:
        h = seconds // 3600 % 24
        m = seconds // 60 % 60
        s = seconds % 60
        return h, m, s

    def __neg__(self):
        return -int(self)

    def __add__(self, other):
        if isinstance(other, (Clock, int)):
            return Clock.from_seconds(int(self) + int(other))
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"'Clock' and '{other.__class__.__name__}'")

    def __sub__(self, other):
        if isinstance(other, (Clock, int)):
            s = int(self) - int(other)
            s = s + 86400 if s < 0 else s
            return Clock.from_seconds(s)
        else:
            raise TypeError(f"unsupported operand type(s) for -: "
                            f"'Clock' and '{other.__class__.__name__}'")

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __iadd__(self, other):
        if isinstance(other, (Clock, int)):
            seconds = self.__convert_seconds(int(self) + int(other))
            self.__hour, self.__minute, self.__second = seconds
            return self
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"'Clock' and '{other.__class__.__name__}'")

    def __isub__(self, other):
        if isinstance(other, (Clock, int)):
            s = int(self) - int(other)
            s = s + 86400 if s < 0 else s
            seconds = self.__convert_seconds(s)
            self.__hour, self.__minute, self.__second = seconds
            return self
        else:
            raise TypeError(f"unsupported operand type(s) for -: "
                            f"'Clock' and '{other.__class__.__name__}'")
