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
                             ((0, 1, 2, 3),), ((0, 2), (1, 3)), ((0, 2, 3, 1),)]

    permutation_3by3 = [((0, 2), (3, 5), (6, 8)), ((0, 6), (1, 7), (2, 8)),
                            ((0, 2, 8, 6), (1, 5, 7, 3)), ((0, 8), (1, 7), (2, 6), (3, 5)), ((0, 6, 8, 2), (1, 3, 7, 5))]

    flattend_index_2by2 = [(0, 0), (0, 1),
                               (1, 0), (1, 1)]

    flattend_index_3by3 = [(0, 0), (0, 1), (0, 2),
                           (1, 0), (1, 1), (1, 2),
                           (2, 0), (2, 1), (2, 2)]
    def premute_string(string, permutation, dim):
        string_list = [char for char in string]
        new_string_list = string_list.copy()

        for step in permutation:
            step = list(step)
            step += [step[0]]
            for i in range(0, len(step)-1):
                old_idx, new_idx = step[i], step[i+1]
                new_string_list[new_idx] = string_list[old_idx]


        string_list = new_string_list
        return "".join(string_list)

    rules = rules.replace("/","").replace(" ", "").split("\n")
    rules = {rule.split("=>")[0]: rule.split("=>")[1] for rule in rules}

    rules_extension = {}
    for rule_input, rule_output in rules.items():
        new_input = ""
        if len(rule_input) == 4:
            for permutation in premutations_2by2:
                new_input = premute_string(rule_input, permutation, dim=2)
                rules_extension[new_input] = rule_output

    rules.update(rules_extension)


    return rules




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

