from module import *


def main():

    # rect = Rectangle(1, 2, 5, 6)
    # circle = Circle(0, 0, 10)
    #
    # figure_list = [rect, circle]
    #
    # for figure in figure_list:
    #     print(f"Площадь фигуры {figure.name}: {figure.area()}")

    car = Car("BMW", 60)

    car.start_engine()
    car.drive(10)
    car.stop_engine()


if __name__ == "__main__":
    main()