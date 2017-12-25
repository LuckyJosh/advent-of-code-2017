#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def turing_1(blueprint):
    pass


def turing_2(blueprint):
    pass

@click.command()
def main():
    input_ = get_input(25)
    print("Input:\n", repr(input_))
    print("Output", turing_1(input_))
    print("Output", turing_2(input_))


if __name__ == '__main__':
    main()

