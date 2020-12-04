# Copyright © 2020 Alexander L. Hayes

import numpy as np


def solution(data, init=(0, 0), right=3, down=1):
    x = init[0]
    y = init[1]
    total = 0

    while True:

        x += down
        y += right

        if x >= len(data):
            break

        # 31 is the length of each line. We could make this more general with
        # y >= len(data[0])
        if y >= 31:
            y = y % 31

        if data[x][y] == "#":
            total += 1

    return total


if __name__ == "__main__":

    with open("input.txt", "r") as _fh:
        data = _fh.read().splitlines()

    data = np.array(data)

    # Solution 1
    print(solution(data))

    # Solution 2
    a = solution(data, right=1, down=1)
    b = solution(data, right=3, down=1)
    c = solution(data, right=5, down=1)
    d = solution(data, right=7, down=1)
    e = solution(data, right=1, down=2)

    print(a * b * c * d * e)
