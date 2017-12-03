#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
import numpy.ma as ma

from .download_input import get_input

def checksum_puzzle_1(spreadsheet):
    line_split = spreadsheet.split("\n")
    column_split = [line.split("\t") for line in line_split]
    max_line_length = max([len(line) for line in column_split])
    for line in column_split:
        while len(line) < max_line_length:
            line.append(-1)

    sheet = ma.masked_equal(ma.array(column_split, dtype=int), -1)
    checksum = ma.sum(ma.ptp(sheet, axis=1))
    return checksum



@click.command()
def main():
    print("Input:\n", get_input(2))

if __name__ == '__main__':
    main()