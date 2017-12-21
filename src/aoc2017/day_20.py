#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def particles_1(initials):
    pass


def particles_2(initials):
    pass

@click.command()
def main():
    input_ = get_input(20)
    print("Input:\n", input_)
    print("Output", particles_1(input_))
    print("Output", particles_2(input_))


if __name__ == '__main__':
    main()

