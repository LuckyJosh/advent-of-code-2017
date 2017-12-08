#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def register_1(arg):
    pass


def register_2(arg):
    pass

@click.command()
def main():
    #input_ = get_input(8)
    input_ = "b inc 5 if a > 1\na inc 1 if b < 5\nc dec -10 if a >= 1\nc inc -20 if c == 10"
    print("Input:\n", input_)
    print("Output", register_1(input_))
    print("Output", register_2(input_))


if __name__ == '__main__':
    main()

