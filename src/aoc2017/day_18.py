#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np


from .download_input import get_input



def duet_1(instructions):
    instructions = instructions.split("\n")
    parsed_instructions = []
    for inst in instructions:
        inst_parts = [part if part.isalpha() else int(part)
                      for part in inst.split(" ")]

        parsed_instructions.append((inst_parts[0], tuple(inst_parts[1:])))

    return parsed_instructions


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

