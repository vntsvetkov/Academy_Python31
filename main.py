from module import *


def trip(transport: Transport):
    transport.start_engine()
    transport.drive(10)
    transport.stop_engine()


def main():

    # rect = Rectangle(1, 2, 5, 6)
    # circle = Circle(0, 0, 10)
    #
    # figure_list = [rect, circle]
    #
    # for figure in figure_list:
    #     print(f"Площадь фигуры {figure.name}: {figure.area()}")

    car = Car("BMW", 60)
    trip(car)


if __name__ == "__main__":
    main()