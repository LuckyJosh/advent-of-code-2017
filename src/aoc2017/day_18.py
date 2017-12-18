#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from collections import defaultdict

from .download_input import get_input



def duet_1(instructions):
    instructions = instructions.split("\n")
    parsed_instructions = []
    for inst in instructions:
        inst_parts = [part if part.isalpha() else int(part)
                      for part in inst.split(" ")]

        parsed_instructions.append((inst_parts[0], tuple(inst_parts[1:])))

    last_played_frequency = 0
    registers = defaultdict(int)

    def snd(x):
        nonlocal last_played_frequency
        nonlocal registers
        nonlocal i
        if isinstance(x, str):
            x = registers[x]
        last_played_frequency = x
        i += 1

    def set(x, y):
        nonlocal registers
        nonlocal i
        if isinstance(y, str):
            y = registers[y]
        registers[x] = y
        i += 1

    def add(x, y):
        nonlocal registers
        nonlocal i
        if isinstance(y, str):
            y = registers[y]
        registers[x] += y
        i += 1

    def mul(x, y):
        nonlocal registers
        nonlocal i
        if isinstance(y, str):
            y = registers[y]
        registers[x] *= y
        i += 1

    def mod(x, y):
        nonlocal registers
        nonlocal i
        if isinstance(y, str):
            y = registers[y]
        registers[x] %= y
        i += 1

    def rcv(x):
        nonlocal last_played_frequency
        nonlocal registers
        nonlocal i
        if isinstance(x, str):
            x = registers[x]
        i += 1
        if x != 0:
            freq = last_played_frequency
            return freq

    def jgz(x, y):
        nonlocal registers
        nonlocal i
        if isinstance(x, str):
            x = registers[x]
        if x > 0:
            i += y
        else:
            i += 1

    operations = {"snd": snd,
                  "set": set,
                  "add": add,
                  "mul": mul,
                  "mod": mod,
                  "rcv": rcv,
                  "jgz": jgz}

    i = 0
    while 0 <= i < len(parsed_instructions):
        current_inst = parsed_instructions[i]
        print("Current Instruction:", current_inst)
        print(i)
        freq = operations[current_inst[0]](*current_inst[1])
        if freq is not None:
            return freq



def duet_2(instructions):
    pass


@click.command()
def main():
    input_ = "set a 1\nadd a 2\nmul a a\nmod a 5\nsnd a\nset a 0\nrcv a\njgz a -1\nset a 1\njgz a -2"
#    input_ = get_input(18)
    print("Input:\n", input_)
    print("Output", duet_1(input_))
    print("Output", duet_2(input_))


if __name__ == '__main__':
    main()

