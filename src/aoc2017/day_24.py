#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def brigdes_1(components):
    components = [component.split("/") for component in components.split("\n")]

    return components


def brigdes_2(components):
    pass

@click.command()
def main():
    #input_ = get_input(24)
    input_ = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"
    print("Input:\n", input_)
    print("Output", brigdes_1(input_))
    print("Output", brigdes_2(input_))


if __name__ == '__main__':
    main()

