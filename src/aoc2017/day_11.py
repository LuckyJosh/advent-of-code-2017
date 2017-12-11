#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def hexgrid_1(movements):
    pass


def hexgrid_2(movements):
    pass

@click.command()
def main():
    input_ = get_input(11)
    print("Input:\n", input_)
    print("Output", hexgrid_1(input_))
    print("Output", hexgrid_2(input_))


if __name__ == '__main__':
    main()

