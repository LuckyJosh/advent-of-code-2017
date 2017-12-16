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

    def dance(program_positions, num_dances):
        for i in tqdm(range(num_dances)):
            for inst in parsed_instructions:
                program_positions = possible_moves[inst[0]](program_positions, *inst[1])
        return program_positions

    dances = 1000000000
    binary_dances = bin(dances)[2:]
    missing_bits = 32 - len(binary_dances)
    binary_dances = "0" * missing_bits + binary_dances
    print(bin(dances), len(binary_dances))

    num_bits_dances = len(binary_dances)
    dances_mask = np.array([int(bit) for bit in binary_dances[::-1]], dtype=bool)

    program_positions = dance(program_positions, dances)






    return "".join([chr(prog) for prog in program_positions + ascii_offset])

@click.command()
def main():
    input_ = get_input(16)
    #input_ = "s1,x3/4,pe/b"
    print("Input:\n", input_)
    print("Output", permutations_1(input_))
    print("Output", permutations_2(input_))


if __name__ == '__main__':
    main()
