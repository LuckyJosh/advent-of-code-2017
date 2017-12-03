#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
import numpy.ma as ma
from io import BytesIO

from .download_input import get_input

def checksum_puzzle_1(spreadsheet):
    # @documentation: All or parts of the documentation is missing!
    # The example had a row that was shorter than the other ones
    # this is the workaround for that. The way of reading in the
    # input shown in the solution to the second puzzle would have
    # sufficed for the given test (puzzle) input.
    line_split = spreadsheet.split("\n")
    column_split = [line.split("\t") for line in line_split]
    max_line_length = max([len(line) for line in column_split])
    for line in column_split:
        while len(line) < max_line_length:
            line.append(-1)

    sheet = ma.masked_equal(ma.array(column_split, dtype=int), -1)
    checksum = ma.sum(ma.ptp(sheet, axis=1))
    return checksum


def checksum_puzzle_2(spreadsheet):
    # @documentation: All or parts of the documentation is missing!
    spreadsheet = BytesIO(bytes(spreadsheet, encoding="utf8"))
    sheet = np.genfromtxt(spreadsheet, delimiter="\t", dtype=int)

    devision = sheet[:, :, np.newaxis]/sheet[:, np.newaxis, :]
    result_is_int = devision.astype(int) == devision
    row_results = devision[result_is_int & (devision != 1)].astype(int)
    return np.sum(row_results)

@click.command()
def main():
    test_input = get_input(2)
    print("Input:\n", test_input)
    print("Solution 1:\n", checksum_puzzle_1(test_input))
    print("Solution 2:\n", checksum_puzzle_2(test_input))


if __name__ == '__main__':
    main()