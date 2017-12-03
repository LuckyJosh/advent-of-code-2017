#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from io import BytesIO

from .download_input import get_input

def checksum_puzzle_1(spreadsheet):
    spreadsheet = BytesIO(bytes(spreadsheet))
    sheet = np.genfromtxt(spreadsheet, dtype=int, delimiter="\\t", comments='#')
    print(sheet)


@click.command()
def main():
    print("Input:\n", get_input(2))

if __name__ == '__main__':
    main()