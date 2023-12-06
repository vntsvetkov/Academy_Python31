import re

"""
Unit-тестирование - проверка кода на регресс.
Регрессионное тестирование - проверка приложения, согласно 
определенному сценарию, с возможностью добавлять новые 
функциональные возможности.

"""


def check_phone(phone: str) -> bool:

    template = r'\+7\([0-9]{3}\) ?[0-9]{3}-[0-9]{2}-[0-9]{2}'
    result = re.match(template, phone)
    return bool(result)


def find_phone(data: str) -> list[str]:
    template = r'\+7\([0-9]{3}\) ?[0-9]{3}-[0-9]{2}-[0-9]{2}'
    result = re.findall(template, data)
    return result
