from module import Programmer, Student


def main():
    languages = ["Python", "SQL"]
    programmer = None
    try:
        programmer = Programmer(name="Иван",
                                age=20,
                                iq=156,
                                level="Middle+",
                                languages=languages)
    except ValueError as e:
        print(e)

    print(programmer)
    programmer.add_language("Java Script")
    print(programmer)

    student = Student("Иван", 22, "41D", [])
    student.name = "Сергей"
    student.age = 21
    student.group = "43G"
    student.add_score(5)
    student.add_score(4)
    student.add_score(3)
    student.add_score(3)
    print(student.avg_score)


if __name__ == "__main__":
    main()