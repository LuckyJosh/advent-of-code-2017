#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from collections import namedtuple
from collections import defaultdict
import operator

from .download_input import get_input


Instruction = namedtuple("instruction",
                         ["register", "operation", "value", "condition_start",
                          "condition_register", "condition_operator", "condition_value"])


def register_1(instructions):
    instructions = instructions.split("\n")
    instructions = [Instruction(*instruction.split(" ")) for instruction in instructions]
    registers = defaultdict(int)
    operations = {"dec": operator.sub, "inc": operator.add}
    for inst in instructions:
        query = f"{registers[inst.condition_register]}{inst.condition_operator}{inst.condition_value}"
        if eval(query):
            registers[inst.register] = operations[inst.operation](registers[inst.register], int(inst.value))

    return max(registers.values())


def register_2(instructions):
    instructions = instructions.split("\n")
    instructions = [Instruction(*instruction.split(" ")) for instruction in instructions]
    registers = defaultdict(int)
    operations = {"dec": operator.sub, "inc": operator.add}
    highest_register_value = 0
    for inst in instructions:
        query = f"{registers[inst.condition_register]}{inst.condition_operator}{inst.condition_value}"
        if eval(query):
            registers[inst.register] = operations[inst.operation](registers[inst.register], int(inst.value))
            highest_register_value = max(registers[inst.register], highest_register_value)

    return highest_register_value


@click.command()
def main():
    input_ = get_input(8)
    #input_ = "b inc 5 if a > 1\na inc 1 if b < 5\nc dec -10 if a >= 1\nc inc -20 if c == 10"
    print("Input:\n", input_)
    print("Output", register_1(input_))
    print("Output", register_2(input_))


if __name__ == '__main__':
    main()

