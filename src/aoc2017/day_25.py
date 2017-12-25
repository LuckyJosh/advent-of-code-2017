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
    #input_ = get_input(25)
    input_ = "Begin in state A.\nPerform a diagnostic checksum after 6 steps.\n\nIn state A:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state B.\n  If the current value is 1:\n    - Write the value 0.\n    - Move one slot to the left.\n    - Continue with state B.\n\nIn state B:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the left.\n    - Continue with state A.\n  If the current value is 1:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state A."
    print("Input:\n", input_)
    print("Input:\n", repr(input_))
    print("Output", turing_1(input_))
    print("Output", turing_2(input_))


if __name__ == '__main__':
    main()

