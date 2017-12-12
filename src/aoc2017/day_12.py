#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def graph_1(arg):
    pass


def graph_2(arg):
    pass


@click.command()
def main():
    input_ = get_input(12)
    print("Input:\n", input_)
    print("Output", graph_1(input_))
    print("Output", graph_2(input_))


if __name__ == '__main__':
    main()

