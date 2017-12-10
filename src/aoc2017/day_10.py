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

    return lengths


def knot_hash_2(arg):
    pass

@click.command()
def main():
    #input_ = get_input(10)
    input_ = "3,4,1,5"
    print("Input:\n", input_)
    print("Output", knot_hash_1(input_))
    print("Output", knot_hash_2(input_))


if __name__ == '__main__':
    main()
