#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
import math as m

from .download_input import get_input


def fractral_1(rules, num_iterations=5):
    # flip on y-axis, flip on x-axis, rotate 90°, rotate 180°, rotate 270°
    # flip on y-axis and rotate 90°, flip on x-axis and rotate 90°
    # elements that stay the same are skipped
    # (x, y, z) :
    # permuted.flatten[y] = array.flatten()[x]
    # permuted.flatten[z] = array.flatten()[y]
    # permuted.flatten[x] = array.flatten()[z]

    premutations_2by2 = [((0, 1), (2, 3)), ((0, 2), (1, 3)),
                         ((0, 1, 2, 3),), ((0, 2), (1, 3)), ((0, 2, 3, 1),),
                         ((0, 3),), ((1, 2),)]

    permutations_3by3 = [((0, 2), (3, 5), (6, 8)), ((0, 6), (1, 7), (2, 8)),
                            ((0, 2, 8, 6), (1, 5, 7, 3)), ((0, 8), (1, 7), (2, 6), (3, 5)), ((0, 6, 8, 2), (1, 3, 7, 5)),
                         ((0, 8), (1, 5), (3, 7)), ((1, 3), (5, 7), (2, 6))]

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
        elif len(rule_input) == 9:
            for permutation in permutations_3by3:
                new_input = premute_string(rule_input, permutation, dim=3)
                rules_extension[new_input] = rule_output

    rules.update(rules_extension)
    print(rules)
    #start_pattern = [".#.", "..#", "###"]

    pattern = np.array([[".", "#", "."],
                        [".", ".", "#"],
                        ["#", "#", "#"]])


    def get_tiled_indicies(split_indicies):
        tiled_indicies = []
        for idx0 in split_indicies:
            for idx1 in split_indicies:
                tiled_indicies.append(np.ix_(idx0, idx1))
        return tiled_indicies


    for it in range(num_iterations):
        print(f"Iteration {it}")
        size = len(pattern)
        print("pattern size:", size)
        print("pattern:")
        print(pattern)

        if size % 2 == 0:
            print("Size divisible by 2")
            indices = np.arange(size)

            num_parts = size // 2
            split_indicies = np.split(indices, [2 * (i + 1) for i in range(0, num_parts)])[:-1]

            tiled_indicies = get_tiled_indicies(split_indicies)

            tiled_pattern = [pattern[idx] for idx in tiled_indicies]

            print(f"tiled_patterns:{len(tiled_pattern)}")
            for pat in tiled_pattern:
                print(pat);print()


            new_pattern = np.zeros((num_parts*3, num_parts*3), dtype='<U1')
            indices_new = np.arange(3*num_parts)
            split_indicies_new = np.split(indices_new, [3 * (i + 1) for i in range(0, num_parts)])[:-1]

            tiled_indicies_new = get_tiled_indicies(split_indicies_new)

            for idx_new, tile in zip(tiled_indicies_new, tiled_pattern):

                new_chars = [char for char in rules["".join(tile.flatten())]]

                new_pattern[idx_new] = np.array(new_chars).reshape(3, 3)
            pattern = new_pattern
            print("new pattern")
            print(pattern)

        elif size % 3 == 0:
            print("Size divisible by 3")

            indices = np.arange(size)

            num_parts = size // 3
            split_indicies = np.split(indices, [3 * (i + 1) for i in range(0, num_parts)])[:-1]

            tiled_indicies = get_tiled_indicies(split_indicies)

            tiled_pattern = [pattern[idx] for idx in tiled_indicies]

            print(f"tiled_patterns:{len(tiled_pattern)}")
            for pat in tiled_pattern:
                print(pat);print()

            new_pattern = np.zeros((num_parts*4, num_parts*4), dtype='<U1')
            indices_new = np.arange(4*num_parts)
            split_indicies_new = np.split(indices_new, [4 * (i + 1) for i in range(0, num_parts)])[:-1]
            tiled_indicies_new = get_tiled_indicies(split_indicies_new)

            for idx_new, tile in zip(tiled_indicies_new, tiled_pattern):
                new_chars = [char for char in rules["".join(tile.flatten())]]
                new_pattern[idx_new] = np.array(new_chars).reshape(4, 4)
            pattern = new_pattern
            print("new pattern")
            print(pattern)



    print(pattern)
    return np.sum(pattern == "#")




def fractral_2(rules):
    pass

@click.command()
def main():
    input_ = get_input(21)
    #input_ = "../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#"
    print("Input:\n", input_)
    print("Output\n", fractral_1(input_, num_iterations=5))
    print("Output", fractral_2(input_))


if __name__ == '__main__':
    main()

