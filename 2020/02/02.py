# Copyright © 2020 Alexander L. Hayes


class Policy0:
    def __init__(self, policy, letter, password):
        self.first_num = int(policy.split("-")[0])
        self.second_num = int(policy.split("-")[1])
        self.letter = letter[0]
        self.password = password

    def check_valid(self):
        raise NotImplementedError


class Policy1(Policy0):
    def __init__(self, policy, letter, password):
        super().__init__(policy, letter, password)

    def check_valid(self):
        observed = 0
        for entry in self.password:
            if entry == self.letter:
                observed += 1
        if self.first_num <= observed <= self.second_num:
            return 1
        return 0


class Policy2(Policy1):
    def __init__(self, policy, letter, password):
        super().__init__(policy, letter, password)

    def check_valid(self):
        observed = 0
        if self.password[self.first_num - 1] == self.letter:
            observed += 1
        if self.password[self.second_num - 1] == self.letter:
            observed += 1
        if observed == 1:
            return 1
        return 0


if __name__ == "__main__":

    with open("input.txt", "r") as _fh:
        data = _fh.read().splitlines()

    total = 0
    for entry in data:
        total += Policy1(*entry.split(" ")).check_valid()
    print(total)

    total = 0
    for entry in data:
        total += Policy2(*entry.split(" ")).check_valid()
    print(total)
