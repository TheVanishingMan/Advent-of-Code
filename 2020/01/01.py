# Copyright © 2020 Alexander L. Hayes


def solution1(data):
    for i, num1 in enumerate(data):
        for j, num2 in enumerate(data):
            if i == j:
                break
            if num1 + num2 == 2020:
                return num1 * num2


def solution2(data):
    for i, num1 in enumerate(data):
        for j, num2 in enumerate(data):
            if i == j:
                break
            for k, num3 in enumerate(data):
                if j == k:
                    break
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3


if __name__ == "__main__":

    with open("input.txt", "r") as _fh:
        data = _fh.read().splitlines()
    data = [int(entry) for entry in data]

    print(solution1(data))
    print(solution2(data))
