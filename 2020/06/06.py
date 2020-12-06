# Copyright © 2020 Alexander L. Hayes


def solution1(input_data):
    _questions = []
    for entry in input_data:
        x = [set(m) for m in entry.split()]
        question = x[0]
        for b in x[1:]:
            question = question.union(b)
        _questions.append(len(question))
    return sum(_questions)


def solution2(input_data):
    _questions = []
    for entry in input_data:
        x = [set(m) for m in entry.split()]
        question = x[0]
        for b in x[1:]:
            question = question.intersection(b)
        _questions.append(len(question))
    return sum(_questions)


if __name__ == "__main__":

    with open("input.txt", "r") as _fh:
        data = _fh.read().split("\n\n")

    print(solution1(data))
    print(solution2(data))
