#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def permutations_1(instructions):
    instructions = instructions.split(",")

    parsed_instructions = []
    for inst in instructions:
        inst_type = inst[0]
        inst_args = tuple([int(i) for i in inst[1:].split("/")])
        parsed_instructions.append((inst_type, inst_args))

    return  parsed_instructions

def permutations_2(instructions):
    pass

@click.command()
def main():
    #input_ = get_input(16)
    input_ = "s1,x3/4,pe/b"
    print("Input:\n", input_)
    print("Output", permutations_1(input_))
    print("Output", permutations_2(input_))


if __name__ == '__main__':
    main()
