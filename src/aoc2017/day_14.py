#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input
from day_10 import knot_hash_2


def hash_grid_1(key):
    row_keys = [key + "-" + str(i) for i in range(128)]
    row_hashes = [knot_hash_2(row_key) for row_key in row_keys]

    return row_hashes

def hash_grid_2(arg):
    pass

@click.command()
def main():
    #input_ = get_input(14)
    input_ = "flqrgnkx"
    print("Input:\n", input_)
    print("Output", hash_grid_1(input_))
    print("Output", hash_grid_2(input_))


if __name__ == '__main__':
    main()
