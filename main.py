from module import *


def trip(transport: Transport, mileage: int):
    transport.start_engine()
    transport.drive(mileage)
    transport.stop_engine()


def main():

    car = FuelCar('ВАЗ 2109', 60)
    tesla = ElectricCar('Tesla Model X', 500)

    # Загрузили в прицеп 50 кг
    tesla.add_cargo(50)

    # Включить радио на частоте 103.5
    tesla.turn_radio(103.5)

    # Отправиться в путешествие на 10 км
    trip(tesla, 10)


if __name__ == "__main__":
    main()
