#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from tqdm import tqdm
from .download_input import get_input


def permutations_1(instructions, num_programs=16):
    ascii_offset = ord("a")
    instructions = instructions.split(",")

    parsed_instructions = []
    for inst in instructions:
        inst_type = inst[0]
        inst_args = tuple([int(i) if i.isdigit() else (ord(i) - ascii_offset)
                           for i in inst[1:].split("/")])
        parsed_instructions.append((inst_type, inst_args))

    def exchange(positions, ind1, ind2):
        positions[[ind1, ind2]] = positions[[ind2, ind1]]
        return positions

    def partner(positions, ind1, ind2):
        ind1, ind2 = np.argwhere(positions == ind1)[0,0], np.argwhere(positions == ind2)[0,0]
        positions[[ind1, ind2]] = positions[[ind2, ind1]]
        return positions

    def spin(positions, steps):
        positions = np.roll(positions, steps)
        return positions

    program_positions = np.arange(num_programs)

    possible_moves = {"s": spin,
                      "p": partner,
                      "x": exchange}

    for inst in parsed_instructions:

        program_positions = possible_moves[inst[0]](program_positions, *inst[1])

    return "".join([chr(prog) for prog in program_positions + ascii_offset])


def permutations_2(instructions, num_programs=16):
    ascii_offset = ord("a")
    instructions = instructions.split(",")

    parsed_instructions = []
    for inst in instructions:
        inst_type = inst[0]
        inst_args = tuple([int(arg) if arg.isdigit() else ord(arg) - ascii_offset
                           for arg in inst[1:].split("/")])
        parsed_instructions.append((inst_type, inst_args))


    def exchange(positions, ind1, ind2):
        positions[ind1], positions[ind2] = positions[ind2], positions[ind1]
        return positions

    def partner(positions, partner1, partner2):
        ind1 = positions.index(partner1)
        ind2 = positions.index(partner2)
        positions = exchange(positions, ind1, ind2)
        return positions

    def spin(positions, steps):
        positions = positions[-steps:] + positions[:-steps]
        return positions

    program_positions = list(range(num_programs))

    possible_moves = {"s": spin,
                      "p": partner,
                      "x": exchange}


    def alldances(program_positions, num_dances):
        start_positions = program_positions[:]
        for i in tqdm(range(num_dances)):
            for inst in parsed_instructions:
                program_positions = possible_moves[inst[0]](program_positions, *inst[1])

            if program_positions == start_positions:
                break

        necessary_dances = num_dances % (i + 1)

        for i in tqdm(range(necessary_dances)):
            for inst in parsed_instructions:
                start_positions = possible_moves[inst[0]](start_positions, *inst[1])
        return start_positions


    dances = 1_000_000_000

    program_positions = alldances(program_positions, dances)

    return "".join([chr(prog + ascii_offset) for prog in program_positions])




@click.command()
def main():
    input_ = get_input(16)
    #input_ = "s1,x3/4,pe/b"
    print("Input:\n", input_)
    print("Output", permutations_1(input_))
    print("Output", permutations_2(input_))


if __name__ == '__main__':
    main()
