#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def knot_hash_1(lengths, list_length=256):
    lengths = lengths.split(",")
    lengths = np.array(lengths, dtype=int)
    List = np.arange(0, list_length)

    skip_sizes = np.arange(0, len(lengths + 1))
    jumps = (lengths + skip_sizes) % list_length

    positions = np.zeros_like(skip_sizes)
    positions[1:] = np.cumsum(jumps[:-1]) % list_length

    ends_of_sublist = lengths + positions

    wrap_around_by = list_length - ends_of_sublist
    wrap_around = (wrap_around_by) < 0

    for i in range(len(lengths)):
        position = positions[i]

        end_of_sublist = ends_of_sublist[i]
        if wrap_around[i]:
            List = np.roll(List, wrap_around_by[i])
            position = position + wrap_around_by[i]
            end_of_sublist = list_length

        List[position:end_of_sublist] = List[position:end_of_sublist][::-1]

        if wrap_around[i]:
            List = np.roll(List, -wrap_around_by[i])

    return List[0]*List[1]


def knot_hash_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(10)
    #input_ = "3,4,1,5"
    print("Input:\n", input_)
    print("Output", knot_hash_1(input_))
    print("Output", knot_hash_2(input_))


if __name__ == '__main__':
    main()
