from module import *


def trip(transport: Transport, mileage: int):
    transport.start_engine()
    transport.drive(mileage)
    transport.stop_engine()


def main():

    car = FuelCar('ВАЗ 2109', 60)
    tesla = ElectricCar('Tesla Model X', 500)
    trip(tesla, 10)


if __name__ == "__main__":
    main()
