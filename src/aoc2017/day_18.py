#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def duet_1(instructions):
    pass


def duet_2(instructions):
    pass

@click.command()
def main():
    input_ = get_input(18)
    print("Input:\n", input_)
    print("Output", duet_1(input_))
    print("Output", duet_2(input_))


if __name__ == '__main__':
    main()

