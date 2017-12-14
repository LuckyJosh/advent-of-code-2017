#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def hash_grid_1(arg):
    pass


def hash_grid_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(14)
    print("Input:\n", input_)
    print("Output", hash_grid_1(input_))
    print("Output", hash_grid_2(input_))


if __name__ == '__main__':
    main()

