#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def fractral_1(rules):
    # flip on y-axis, flip on x-axis, rotate 90°, rotate 180°, rotate 270°
    # elements that stay the same are skipped
    # (x, y, z) :
    # permuted.flatten[y] = array.flatten()[x]
    # permuted.flatten[z] = array.flatten()[y]
    # permuted.flatten[x] = array.flatten()[z]

    premutations_2by2 = [((0, 1), (2, 3)), ((0, 2), (1, 3)),
                         ((0, 1, 2, 3),), ((0, 2), (1, 3)), ((0, 2, 3, 1))]

    permutation_3by3 = [((0, 2), (3, 5), (6, 8)), ((0, 6), (1, 7), (2, 8)),
                        ((0, 2, 8, 6), (1, 5, 7, 3)), ((0, 8), (1, 7), (2, 6), (3, 5)), ((0, 6, 8, 2), (1, 3, 7, 5))]

    flattend_index_2by2 = [(0, 0), (0, 1),
                           (1, 0), (1, 1)]

    flattend_index_3by3 = [(0, 0), (0, 1), (0, 2),
                           (1, 0), (1, 1), (1, 2),
                           (2, 0), (2, 1), (2, 2)]
    rules = rules.replace("/","").split("\n")
    print(rules)




def fractral_2(rules):
    pass

@click.command()
def main():
    #input_ = get_input(21)
    input_ = "../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#"
    print("Input:\n", input_)
    print("Output", fractral_1(input_))
    print("Output", fractral_2(input_))


if __name__ == '__main__':
    main()

