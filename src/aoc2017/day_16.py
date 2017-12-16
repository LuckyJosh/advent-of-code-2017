#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def permutations_1(arg):
    pass


def permutations_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(16)
    print("Input:\n", input_)
    print("Output", permutations_1(input_))
    print("Output", permutations_2(input_))


if __name__ == '__main__':
    main()

