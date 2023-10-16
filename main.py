from module import Programmer, Address, ITCompany


def main():
    # Пример 1. Класс программист
    languages = ["Python", "SQL"]
    programmer = Programmer(name="Иван", age=20, iq=156, level="Middle+", languages=languages)

    print(programmer)

    # Пример 2. Класс Адрес
    address = Address(city="Ярославль", street="Свободы", home=1)

    print(address)

    # Пример 3. Класс IT компания
    company = ITCompany(name="Яндекс", address=address)

    print(company)


if __name__ == "__main__":
    main()

