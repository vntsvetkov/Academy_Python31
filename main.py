from module import *


def main():

    clock1 = Clock(2, 0, 0)
    clock2 = Clock(1, 0, 0)

    # clock3 = clock1 + clock2
    # print(clock3)
    # clock4 = clock1 + (-clock2) + 3600
    # print(clock4)
    # clock5 = 3600 + clock1
    # print(clock5)
    # clock2 += clock1
    # print(clock2)
    # clock1 += 3600
    # print(clock1)

    clock3 = clock1 - clock2
    print(clock3)
    clock4 = clock1 - (-clock2)
    clock5 = 3600 - clock1
    clock6 = clock1 - 3600
    clock2 -= clock1
    clock2 -= 3600


if __name__ == "__main__":
    main()