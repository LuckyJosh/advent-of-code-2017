#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input
from .day_10 import knot_hash_2


def hash_grid_1(key):
    row_keys = [key + "-" + str(i) for i in range(128)]
    row_hashes = [knot_hash_2(row_key) for row_key in row_keys]

    bin_row_hashes = []
    for row_hash in row_hashes:
        bin_row_hash = []
        for char in row_hash:
            bin_char = bin(int(char, 16))[2:]
            missing_leading_bits = 4 - len(bin_char)
            bin_char = "0"*missing_leading_bits + bin_char
            bin_row_hash.append(bin_char)
        bin_row_hashes.append("".join(bin_row_hash))

    bin_rows_string = [int(bit) for bit in "".join(bin_row_hashes)]


    return sum(bin_rows_string)

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
