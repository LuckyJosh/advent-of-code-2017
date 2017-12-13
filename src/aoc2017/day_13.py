#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def firewall_1(arg):
    pass


def firewall_2(arg):
    pass

@click.command()
def main():
    #input_ = get_input(13)
    input_ = "0: 3\n1: 2\n4: 4\n6: 4"
    print("Input:\n", input_)
    print("Output", firewall_1(input_))
    print("Output", firewall_2(input_))


if __name__ == '__main__':
    main()

