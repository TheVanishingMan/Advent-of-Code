# Copyright © 2020 Alexander L. Hayes

import re


def solution1(entry):
    total = 0
    for passport in entry:
        try:
            assert "byr" in passport
            assert "iyr" in passport
            assert "eyr" in passport
            assert "hgt" in passport
            assert "hcl" in passport
            assert "ecl" in passport
            assert "pid" in passport
            total += 1
        except AssertionError:
            pass
    return total


def solution2(entry):
    total = 0
    for passport in entry:
        try:
            assert 1920 <= int(passport["byr"]) <= 2002
            assert 2010 <= int(passport["iyr"]) <= 2020
            assert 2020 <= int(passport["eyr"]) <= 2030

            # hgt
            height = passport["hgt"]
            assert ("cm" in height) or ("in" in height)
            if "cm" in height:
                assert 150 <= int(height.replace("cm", "")) <= 193
            elif "in" in height:
                assert 59 <= int(height.replace("in", "")) <= 76

            assert re.match("#([0-9]|[a-f]){6}", passport["hcl"])
            assert passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            assert len(passport["pid"]) == 9

            total += 1
        except (AssertionError, KeyError):
            # Any kind of exception raised is considered an error in validation.
            pass
    return total


if __name__ == "__main__":

    with open("input.txt", "r") as _fh:
        data = _fh.read().split("\n\n")

    cleaned = [
        {entry.split(":")[0]: entry.split(":")[1] for entry in passport.split()}
        for passport in data
    ]

    print(solution1(cleaned))
    print(solution2(cleaned))
