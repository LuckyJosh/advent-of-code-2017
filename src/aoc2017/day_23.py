#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from tqdm import tqdm
from .download_input import get_input


def coprocess_1(instructions):
    instructions = instructions.split("\n")
    parsed_instructions = []
    for inst in instructions:
        inst_parts = [part if part.isalpha() else int(part)
                      for part in inst.split(" ")]

        parsed_instructions.append((inst_parts[0], tuple(inst_parts[1:])))

    registers = {char: 0 for char in "abcdefgh"}


    def set(x, y):
        nonlocal registers
        nonlocal i
        nonlocal function_count
        if isinstance(y, str):
            y = registers[y]
        registers[x] = y
        function_count["set"] += 1
        i += 1

    def sub(x, y):
        nonlocal registers
        nonlocal i
        nonlocal function_count
        if isinstance(y, str):
            y = registers[y]
        registers[x] -= y
        function_count["sub"] += 1
        i += 1

    def mul(x, y):
        nonlocal registers
        nonlocal i
        nonlocal function_count
        if isinstance(y, str):
            y = registers[y]
        registers[x] *= y
        function_count["mul"] += 1
        i += 1

    def jnz(x, y):
        nonlocal registers
        nonlocal i
        nonlocal function_count
        if isinstance(x, str):
            x = registers[x]
        if isinstance(y, str):
            y = registers[y]
        if x != 0:
            i += y
            function_count["jnz"] += 1
        else:
            i += 1

    function_count = {"set": 0,
                      "sub": 0,
                      "mul": 0,
                      "jnz": 0}
    operations = {"set": set,
                  "sub": sub,
                  "mul": mul,
                  "jnz": jnz}

    i = 0
    while 0 <= i < len(parsed_instructions):
        current_inst = parsed_instructions[i]
        print("Current Instruction:", current_inst)
        print(i)
        operations[current_inst[0]](*current_inst[1])

    return function_count["mul"]


def coprocess_2(instructions):
    instructions = instructions.split("\n")
    parsed_instructions = []
    for inst in instructions:
        inst_parts = [part if part.isalpha() else int(part)
                      for part in inst.split(" ")]

        parsed_instructions.append((inst_parts[0], tuple(inst_parts[1:])))

    # @stability: @hack: @incomplete: This should be read from input
    init_value_b = 1007900
    init_value_c = init_value_b + 17000
    value_b_change = 17
    value_h = 0
    for b in tqdm(range(init_value_b, init_value_c + 1, value_b_change)):
        for e in tqdm(range(2, b + 1)):
            if b % e == 0:
                value_h += 1
                break

    return value_h


@click.command()
def main():
    input_ = get_input(23)
    print("Input:\n", input_)
    print("Output", coprocess_1(input_))
    print("Output", coprocess_2(input_))


if __name__ == '__main__':
    main()
