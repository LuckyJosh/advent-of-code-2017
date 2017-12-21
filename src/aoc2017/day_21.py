#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def fractral_1(rules):
    pass


def fractral_2(rules):
    pass

@click.command()
def main():
    input_ = get_input(21)
    print("Input:\n", input_)
    print("Output", fractral_1(input_))
    print("Output", fractral_2(input_))


if __name__ == '__main__':
    main()

