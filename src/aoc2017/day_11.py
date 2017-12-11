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
    steps = np.abs(np.sum(sum_of_directions))
    signs = np.sign(sum_of_directions)
    if signs[0] != signs[1]:
        steps += np.abs(sum_of_directions).min()

    return steps


def hexgrid_2(movements):
    direction_indices = {"n": 0, "ne": 1, "nw": 2,
                       "s": 3, "se": 4, "sw": 5}
    movements = [direction_indices[move] for move in movements.split(",")]

    directions = np.array([(1, 0), (0, 1), (1, -1),
                           (-1, 0), (-1, 1), (0, -1)])

    sum_of_directions = np.cumsum(directions[movements], axis=0)

    steps = np.abs(np.sum(sum_of_directions, axis=1))

    signs = np.sign(sum_of_directions)

    neighbor_signs_equal = signs[:, 0:-1] == signs[:, 1:]

    steps[~neighbor_signs_equal.flatten()] += np.abs(sum_of_directions).min(axis=1)[~neighbor_signs_equal.flatten()]

    return np.max(steps)

@click.command()
def main():
    #input_ = get_input(11)
    input_ = "ne,ne,ne"
    print("Input:\n", repr(input_))
    print("Output", hexgrid_1(input_))
    print("Output", hexgrid_2(input_))


if __name__ == '__main__':
    main()
