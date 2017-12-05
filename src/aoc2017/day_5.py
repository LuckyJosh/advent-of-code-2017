#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def memory_jumps_1(arg):
    pass


def func_2(arg):
    pass

@click.command()
def main():
    input_ = get_input()
    print("Input:\n", input_)
    print("Output", memory_jumps_1(input_))
    print("Output", func_2(input_))


if __name__ == '__main__':
    main()

