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
    instructions = instructions.split("\n")
    parsed_instructions = []
    for inst in instructions:
        inst_parts = [part if part.isalpha() else int(part)
                      for part in inst.split(" ")]

        parsed_instructions.append((inst_parts[0], tuple(inst_parts[1:])))

    both_registers = [defaultdict(int), defaultdict(int)]
    both_sending_queues = [[], []]
    for i, registers in enumerate(both_registers):
        registers["p"] = i


    def set(x, y, id, instruction, registers, both_sending_queues):
        if isinstance(y, str):
            y = registers[y]
        registers[x] = y
        instruction += 1
        return instruction, registers, both_sending_queues

    def add(x, y, id, instruction, registers, both_sending_queues):
        if isinstance(y, str):
            y = registers[y]
        registers[x] += y
        instruction += 1
        return instruction, registers, both_sending_queues


    def mul(x, y, id, instruction, registers, both_sending_queues):
        if isinstance(y, str):
            y = registers[y]
        registers[x] *= y
        instruction += 1
        return instruction, registers, both_sending_queues

    def mod(x, y, id, instruction, registers, both_sending_queues):
        if isinstance(y, str):
            y = registers[y]
        registers[x] %= y
        instruction += 1
        return instruction, registers, both_sending_queues


    def jgz(x, y, id, instruction, registers, both_sending_queues):
        if isinstance(x, str):
            x = registers[x]
        if x > 0:
            instruction += y
        else:
            instruction += 1
        return instruction, registers, both_sending_queues


    def snd(x, id, instruction, registers, both_sending_queues):
        if isinstance(x, str):
            x = registers[x]
        if id == 1:
            nonlocal send_count_1
            send_count_1 += 1

        both_sending_queues[(id + 1) % 2].append(x)
        instruction += 1
        return instruction, registers, both_sending_queues

    def rcv(x, id, instruction, registers, both_sending_queues):

        if both_sending_queues[id]:
            registers[x] = both_sending_queues[id].pop(0)
            instruction += 1

        return instruction, registers, both_sending_queues



    operations = {"snd": snd,
                  "set": set,
                  "add": add,
                  "mul": mul,
                  "mod": mod,
                  "rcv": rcv,
                  "jgz": jgz}

    send_count_1 = 0
    terminated_0 = False
    terminated_1 = False
    waiting_0 = False
    waiting_1 = False
    i_0 = 0
    i_1 = 0
    while not (terminated_0 and terminated_1):

        if not terminated_0:
            Id = 0
            current_inst = parsed_instructions[i_0]
            i_0_, registers, both_sending_queues = operations[current_inst[0]](*current_inst[1], Id, i_0, both_registers[Id], both_sending_queues)

            if i_0_ == i_0:
                weighting_0 = True
            else:
                weighting_0 = False
                i_0 = i_0_

            both_registers[Id] = registers

            if not (0 <= i_0 < len(instructions)):
                terminated_0 = True

        if not terminated_1:
            Id = 1
            current_inst = parsed_instructions[i_1]
            i_1_, registers, both_sending_queues = operations[current_inst[0]](*current_inst[1], Id, i_1, both_registers[Id], both_sending_queues)

            if i_1_ == i_1:
                weighting_1 = True
            else:
                weighting_1 = False
                i_1 = i_1_

            both_registers[Id] = registers

            if not (0 <= i_1 < len(instructions)):
                terminated_1 = True

        if weighting_0 and weighting_1:
            terminated_0 = terminated_1 = True

    return send_count_1




@click.command()
def main():
    input_ = "set a 1\nadd a 2\nmul a a\nmod a 5\nsnd a\nset a 0\nrcv a\njgz a -1\nset a 1\njgz a -2"
#    input_ = get_input(18)
    print("Input:\n", input_)
    print("Output", duet_1(input_))
    print("Output", duet_2(input_))


if __name__ == '__main__':
    main()

