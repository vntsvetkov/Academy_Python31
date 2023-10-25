from module import *


def main():

    tester = Tester("Пётр", 34, "Senior", "Selenium")
    # tester.level = "TeamLead"
    print(tester.level)
    programmer = Programmer("Сергей", 26, "Junior", "Python")
    programmer.level = "Middle"
    print(programmer)


if __name__ == "__main__":
    main()
