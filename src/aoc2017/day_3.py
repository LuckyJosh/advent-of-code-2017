#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def spiral_memory_steps_1(data_location):
    # @documentation: All or parts of the documentation is missing!
    data_location = int(data_location)

    # internally to this function, data location start at 0 not at 1!
    if data_location < 1:
        raise ValueError(f"The data location given has to be a positive number of type int, "
                         "but number given is {data_location}.")
    used_indicies = set()

    indicies = np.zeros(shape=(data_location, 2), dtype=int)

    first_indices = [(0, 0), (1, 0), (1, 1)]

    moves = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

    for loc in range(0, data_location):
        if loc <= 2:
            used_indicies.add(first_indices[loc])
            indicies[loc, :] = first_indices[loc]
        else:
            current_index = indicies[loc-1, :]
            new_indicies = current_index + moves
            not_used = [tuple(idx) not in used_indicies for idx in new_indicies]
            distance_to_center = np.linalg.norm(indicies[0, :] - new_indicies[not_used], axis=1)
            min_distance = np.argmin(distance_to_center)
            used_indicies.add(tuple(new_indicies[not_used][min_distance]))
            indicies[loc, :] = new_indicies[not_used][min_distance]

    num_steps = np.sum(np.abs(indicies[-1, :]))
    return num_steps


def spiral_memory_steps_2(data):
    data = int(data)

    # internally to this function, data location start at 0 not at 1!

    used_indicies_with_values = {}

    indicies = np.zeros(shape=(data, 2), dtype=int)

    first_indices = [(0, 0), (1, 0), (1, 1)]
    first_values = [1, 1, 2]

    moves = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])

    neighbors = np.concatenate([moves, np.array([[1, 1], [1, -1], [-1, -1], [-1, 1]])])

    for loc in range(0, data):
        if loc <= 2:
            used_indicies_with_values[first_indices[loc]] = first_values[loc]
            indicies[loc, :] = first_indices[loc]
        else:
            current_index = indicies[loc-1, :]
            new_indicies = current_index + moves
            not_used = [tuple(idx) not in used_indicies_with_values.keys() for idx in new_indicies]
            distance_to_center = np.linalg.norm(indicies[0, :] - new_indicies[not_used], axis=1)
            min_distance = np.argmin(distance_to_center)

            new_index = new_indicies[not_used][min_distance]
            new_index_neighbors = new_index + neighbors
            values_of_neighbors = [used_indicies_with_values[idx]
                                   for idx in new_index_neighbors
                                   if idx in used_indicies_with_values]

            used_indicies_with_values[tuple(new_index)] = sum(values_of_neighbors)
            indicies[loc, :] = new_indicies[not_used][min_distance]

        if used_indicies_with_values[tuple(new_index)] > data:
            return used_indicies_with_values[tuple(new_index)]




@click.command()
def main():
    input_ = get_input(3)
    print("Input:\n", input_)
    print("Output:", spiral_memory_steps_1(input_))



if __name__ == '__main__':
    main()