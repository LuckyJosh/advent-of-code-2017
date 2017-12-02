#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input

def checksum_puzzle_1(spreadsheet):
    pass


@click.command()
def main():
    print("Input:", get_input(2))

if __name__ == '__main__':
    main()