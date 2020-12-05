# Copyright © 2020 Alexander L. Hayes


class DecodeTicket:
    def __init__(self, representation):
        self.row_coded = representation[:7]
        self.col_coded = representation[7:]
        self.row = self.decode(self.row_coded, 127, "F")
        self.col = self.decode(self.col_coded, 7, "L")
        self.id = (self.row * 8) + self.col

    @staticmethod
    def decode(entry, upper_number, lower_symbol):
        lower = 0
        upper = upper_number
        for letter in entry:
            if letter == lower_symbol:
                upper = (lower + upper) // 2
            else:
                lower = ((lower + upper) // 2) + 1
        return min(lower, upper)

    def __repr__(self):
        return "row:{0}, col:{1}, id:{2}".format(self.row, self.col, self.id)


if __name__ == "__main__":

    with open("input.txt", "r") as _fh:
        data = _fh.read().splitlines()

    # Problem One:
    print(max([entry.id for entry in [DecodeTicket(row) for row in data]]))

    # Problem Two:
    found_ids = set([entry.id for entry in [DecodeTicket(row) for row in data]])
    possible_ids = set(range(min(found_ids), max(found_ids)))
    print(possible_ids - found_ids)
