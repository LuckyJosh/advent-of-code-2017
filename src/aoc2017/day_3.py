#! /usr/bin/env python
# encoding: utf-8

import numpy as np

from .download_input import get_input


def spiral_memory_steps_1(data_location):
    # @documentation: All or parts of the documentation is missing!

    # internally to this function, data location start at 0 not at 1!
    if data_location < 1:
        raise ValueError(f"The data location given has to be a positive number of type int, "
                         "but number given is {data_location}.")
    used_indicies = set()

    indicies = np.zeros(shape=(data_location, 2))

    first_indices = [(0, 0), (1, 0), (1, 1)]

    moves = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

    for loc in range(0, data_location):
        if loc <= 2:
            used_indicies.add(first_indices[loc - 1])
            indicies[loc - 1, :] = first_indices[loc - 1]
        else:
            current_index = indicies[loc-1, :]
            new_indicies = current_index + moves
            not_used = [tuple(idx) not in used_indicies for idx in new_indicies]
            distance_to_center = np.linalg.norm(indicies[0, :] - new_indicies[not_used])
            min_distance = np.argmin(distance_to_center)

            used_indicies.add(tuple(new_indicies[min_distance]))
            indicies[loc - 1, :] = new_indicies[min_distance]

    num_steps = np.sum(np.abs(indicies[-1, :]))

    return num_steps




def main():
    input_ = get_input(3)
    print("Input:\n", input_)
    print("Output:" )


if __name__ == '__main__':
    main()