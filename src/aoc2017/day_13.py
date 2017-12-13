#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def firewall_1(depth_range):

    depth_range = {int(line[0]): int(line[-1])
                   for line in depth_range.replace(":", "").split("\n")}

    depth_range_ = []

    for i in range(max(depth_range) + 1):
        if i in depth_range:
            depth_range_.append(depth_range[i])
        else:
            depth_range_.append(-1)

    depth_range = np.array(depth_range_)

    max_depth = len(depth_range)
    max_range = max(depth_range)

    def pyramid_range(max_num, num_repeats=0, cutoff=None):
        num_elements = max_num + max_num - 1
        if num_repeats == 0 and cutoff is not None:
            num_repeats = cutoff//num_elements

        pyramid_range = np.full(num_elements, max_num - 1)
        indicies = np.arange(max_num - 1)
        pyramid_range[indicies] = indicies
        pyramid_range[indicies+max_num] = indicies[::-1]
        num_total_elements = num_elements + (num_elements - 1) * num_repeats
        repeated_pyramid_range = np.zeros(shape=num_total_elements, dtype=int)

        if num_repeats > 0:
            repeated_pyramid_range[:-num_elements] = np.tile(pyramid_range[:-1], num_repeats)

        repeated_pyramid_range[-num_elements:] = pyramid_range
        if cutoff is not None:
            repeated_pyramid_range = repeated_pyramid_range[:cutoff]

        return repeated_pyramid_range



    depth_index = np.arange(max_depth)
    layers = []
    for range_ in depth_range:
        if range_ != -1:
            layers.append(pyramid_range(range_, cutoff=max_depth))
        else:
            layers.append(np.full(max_depth, range_))

    positions_in_time = np.column_stack(layers)

    caught_indices = np.argwhere(np.diag(positions_in_time) == 0).flatten()

    return np.sum(caught_indices * depth_range[caught_indices])



def firewall_2(arg):
    pass

@click.command()
def main():
    #input_ = get_input(13)
    input_ = "0: 3\n1: 2\n4: 4\n6: 4"
    print("Input:\n", input_)
    print("Output", firewall_1(input_))
    print("Output", firewall_2(input_))


if __name__ == '__main__':
    main()

