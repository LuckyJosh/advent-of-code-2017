#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def hexgrid_1(movements):
    direction_indices = {"n": 0, "ne": 1, "nw": 2,
                       "s": 3, "se": 4, "sw": 5}
    movements = [direction_indices[move] for move in movements.split(",")]

    directions = np.array([(1, 0), (1, 1), (1, -1),
                           (-1, 0), (-1, 1), (-1, -1)])

    return directions[movements]


def hexgrid_2(movements):
    pass

@click.command()
def main():
    #input_ = get_input(11)
    input_ = "ne,ne,ne"
    print("Input:\n", repr(input_))
    print("Output", hexgrid_1(input_))
    print("Output", hexgrid_2(input_))


if __name__ == '__main__':
    main()
