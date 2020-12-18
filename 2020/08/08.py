# Copyright © 2020 Alexander L. Hayes

from copy import deepcopy
import time


class VirtualMachine:
    def __init__(self):
        self.counter = 0
        self.accumulator = 0
        self.stack = None
        self.visited = set()

    def load(self, instruction_list, parse=False):
        if parse:
            self.stack = [Instruction(inst) for inst in instruction_list]
        else:
            self.stack = instruction_list

    def fetch(self):
        return self.stack[self.counter]

    def execute(self, instruction):
        op = instruction.opcode
        va = instruction.value

        if op == "jmp":
            self.counter += va
        if op == "acc":
            self.accumulator += va
            self.counter += 1
        if op == "nop":
            self.counter += 1

        _current = len(self.visited)
        self.visited.add(self.counter)
        if len(self.visited) == _current:
            raise ValueError("Infinite Loop!")

    def run(self):
        while True:
            self.execute(self.fetch())


class Instruction:
    def __init__(self, instruction_string):
        _instruction = instruction_string.split()
        self.opcode = _instruction[0]
        self.value = int(_instruction[1])

    def __repr__(self):
        return self.opcode + " " + str(self.value)


if __name__ == "__main__":

    _input = "input.txt"

    with open(_input, "r") as _fh:
        machine_instructions = _fh.read().splitlines()

    try:
        vm = VirtualMachine()
        vm.load(machine_instructions, parse=True)
        vm.run()
    except ValueError:
        print("Infinite Loop, accumulator:", vm.accumulator)
        pass

    instructions = [Instruction(a) for a in machine_instructions]

    for i in range(len(instructions)):

        if instructions[i].opcode == 'acc':
            pass

        local_instructions = deepcopy(instructions)

        if instructions[i].opcode == "nop":
            local_instructions[i].opcode = "jmp"
        elif instructions[i].opcode == "jmp":
            local_instructions[i].opcode = "nop"

        try:
            vm = VirtualMachine()
            vm.load(local_instructions)
            vm.run()
        except ValueError:
            pass
        except IndexError:
            print("Found a fix, accumulator:", vm.accumulator)
            with open("fixed_input.txt", "w") as _fh:
                _fh.writelines([str(inst) + "\n" for inst in local_instructions])
            with open("origi_input.txt", "w") as _fh:
                _fh.writelines([str(inst) + "\n" for inst in instructions])
            break
