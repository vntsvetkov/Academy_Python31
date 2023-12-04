from collections.abc import Iterable, Iterator, Generator


def get_even_numbers(n: int) -> Generator:

    for i in range(0, n, 2):
        yield i


class EvenNumbers(Iterable):

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return EvenIterator(self)


class EvenIterator(Iterator):

    def __init__(self, container):
        self.container = container
        self.start = 0

    def __next__(self):
        self.start += 2
        if self.start > self.container.limit:
            raise StopIteration()
        return self.start

    def __iter__(self):
        return self


iterable = EvenNumbers(11)
iterator = EvenIterator(iterable)

a = [1, 2, 3, 4, 5]
b = iter(a)

