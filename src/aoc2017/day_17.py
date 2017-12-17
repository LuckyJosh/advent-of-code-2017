#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def spinlock_1(arg):
    pass


def spinlock_2(arg):
    pass

@click.command()
def main():
    #input_ = get_input(17)
    input_ = "3"
    print("Input:\n", input_)
    print("Output", spinlock_1(input_))
    print("Output", spinlock_2(input_))


if __name__ == '__main__':
    main()

