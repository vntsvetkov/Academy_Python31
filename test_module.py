from module import *


def test_check_phone(phone: str, expected: bool):
    a = check_phone(phone)
    if a != expected:
        print(f"ERROR! Значение {phone} не совпадает с ожидаемым {expected}")
        raise


def test_find_phone(data: str, expected: list[str]):

    assert find_phone(data) == expected, f"ERROR! Значение {data} не совпадает с ожидаемым {expected}"


test_text = "Lorem +7(999) 456-67-99 sit amet, consectetur adipiscing " \
            "sed do +8(999) 456-67-99 ut labore et dolore " \
            "magna aliqua. +7(999)456-67-99 veniam, quis nostrud " \
            "exercitation ullamco laboris nisi ut aliquip ex ea " \
            "commodo consequat +7(999) 4566799."


test_data = [
    ('+7(999) 456-67-99', True),
    ('+7(000) 000-00-00', True),
    ('', False),
    ('+8(999) 456-67-99', False),
    ('+7(999)456-67-99', True),
    ('+7999 456-67-99', False),
    ('+8(999) 456-67-99', False),
    ('7(999) 456-67-99', False),
    ('+7(999) 4566799', False),
]

if __name__ == "__main__":

    # for phone, result in test_data:
    #     test_check_phone(phone, result)

    test_find_phone(test_text, ['+7(999) 456-67-99', '+7(999)456-67-99'])
    test_find_phone('', [])
    test_find_phone('sed do +8(999) 456-67-99 ut labore et dolore', [])
    test_find_phone('exercitation ullamco laboris nisi ut aliquip ex ea', [])
    print("ОК")

