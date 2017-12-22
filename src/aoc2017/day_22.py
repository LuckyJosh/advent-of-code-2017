#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def virus_1(start_area):
    start_area = [list(line) for line in start_area.split("\n")]
    return start_area

def virus_2(start_area):
    pass

@click.command()
def main():
    input_ = get_input(22)
    print("Input:\n", input_)
    print("Output", virus_1(input_))
    print("Output", virus_2(input_))


if __name__ == '__main__':
    main()

