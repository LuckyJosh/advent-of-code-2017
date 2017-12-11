#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def hexgrid_1(movements):
    direction_indices = {"n": 0, "ne": 1, "nw": 2,
                       "s": 3, "se": 4, "sw": 5}
    movements = [direction_indices[move] for move in movements.split(",")]

    directions = np.array([(1, 0), (0, 1), (1, -1),
                           (-1, 0), (-1, 1), (0, -1)])

    sum_of_directions = np.sum(directions[movements], axis=0)
    max_dir = np.abs(sum_of_directions).max()
    min_dir = np.abs(sum_of_directions).min()
    if max_dir == min_dir:
        steps = max_dir
    else:
        steps = max_dir + min_dir

    return steps


def hexgrid_2(movements):
    pass

@click.command()
def main():
    input_ = get_input(11)
    print("Input:\n", repr(input_))
    print("Output", hexgrid_1(input_))
    print("Output", hexgrid_2(input_))


if __name__ == '__main__':
    main()
