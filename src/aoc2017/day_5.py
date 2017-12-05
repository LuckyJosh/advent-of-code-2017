#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def memory_jumps_1(jumps):
    # @documentation: All or parts of the documentation is missing!
    jumps = [int(jump) for jump in jumps.split("\n")]

    njumps = len(jumps)
    i = 0
    counter = 0
    while i < njumps:
        next_i = i + jumps[i]
        jumps[i] += 1
        i = next_i
        counter += 1

    return counter

def func_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(5)
    print("Input:\n", input_)
    print("Output", memory_jumps_1(input_))
    print("Output", func_2(input_))


if __name__ == '__main__':
    main()

