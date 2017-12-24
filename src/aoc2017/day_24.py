#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def brigdes_1(components):
    pass


def brigdes_2(components):
    pass

@click.command()
def main():
    input_ = get_input(24)
    print("Input:\n", input_)
    print("Output", brigdes_1(input_))
    print("Output", brigdes_2(input_))


if __name__ == '__main__':
    main()

