from module import *


def main():

    circle1 = Circle(1, 2, 3)
    circle2 = Circle(3, 4, 6)

    circle3 = Circle.create_circle_by_diameter(1, 2, 8)
    circle4 = Circle.create_circle_by_diameter(3, 4, 10)

    print(Circle.get_count())

    circle1.obj_set_color('#00FF00')   # Изменить цвет только circle1
    Circle.set_color('#FF0000')   # Изменить цвет всем объектам класса Circle

    print(circle1.__dict__)  # Тут есть параметр color
    print(circle2.__dict__)  # Тут нет параметра color

    # current_sum_rub = 1000
    # ConverterCurrency.dollar_rate = 100
    # print(ConverterCurrency.dollar_rate)
    # current_sum_dollar = ConverterCurrency.rub_to_dollar(current_sum_rub)
    # print(current_sum_dollar)


if __name__ == "__main__":
    main()