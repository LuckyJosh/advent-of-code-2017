#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def check_passphrase_1(passphrases):
    pass


def func_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(4)
    print("Input:\n", input_)
    print("Output", check_passphrase_1(input_))
    print("Output", func_2(input_))


if __name__ == '__main__':
    main()

