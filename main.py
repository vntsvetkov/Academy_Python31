from module import *


def main():
    # Создание собственной последовательности
    # stack = Stack()
    # stack.append(1)
    # stack.append(2)
    # print(len(stack))

    # Пример использования контекстного менеджера
    # with Timer() as timer:
        # Ваш блок кода
        # time.sleep(1)

    # Создать список моментов времени и упорядочить их по возрастанию

    clock1 = Clock(0, 10, 0)
    clock2 = Clock(0, 8, 0)
    clock3 = Clock(0, 9, 0)

    clocks = [clock1, clock2, clock3]
    clocks = sorted(clocks, reverse=True)
    print(clocks)

    # clock = {
    #     clock1: "Полдень",
    #     clock2: "Полдень",
    # }
    # print(clock)


if __name__ == "__main__":
    main()