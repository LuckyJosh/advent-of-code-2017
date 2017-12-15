#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from collections import defaultdict

from .download_input import get_input
from .day_10 import knot_hash_2


def hash_grid_1(key):
    row_keys = [key + "-" + str(i) for i in range(128)]
    row_hashes = [knot_hash_2(row_key) for row_key in row_keys]

    bin_row_hashes = []
    for row_hash in row_hashes:
        bin_row_hash = []
        for char in row_hash:
            bin_char = bin(int(char, 16))[2:]
            missing_leading_bits = 4 - len(bin_char)
            bin_char = "0"*missing_leading_bits + bin_char
            bin_row_hash.append(bin_char)
        bin_row_hashes.append("".join(bin_row_hash))

    bin_rows_string = [int(bit) for bit in "".join(bin_row_hashes)]

    return sum(bin_rows_string)


def hash_grid_2(key):
    row_keys = [key + "-" + str(i) for i in range(128)]
    row_hashes = [knot_hash_2(row_key) for row_key in row_keys]

    bin_row_hashes = []
    for row_hash in row_hashes:
        bin_row_hash = []
        for char in row_hash:
            bin_char = bin(int(char, 16))[2:]
            missing_leading_bits = 4 - len(bin_char)
            bin_char = "0"*missing_leading_bits + bin_char
            bin_row_hash.append(bin_char)
        bin_row_hashes.append("".join(bin_row_hash))

    bin_grid = np.array([list(row) for row in bin_row_hashes], dtype=int).astype(bool)
    cluster_grid = np.zeros_like(bin_grid, dtype=int)


    def find_root_cluster(cluster_value, cluster):
        cluster_size = cluster[cluster_value]
        if cluster_size < 0:
            return find_root_cluster(-1*cluster_size, cluster)
        else:
            return cluster_value

    cluster = defaultdict(int)
    current_cluster = 0
    for i in range(128):
        for j in range(128):
            if bin_grid[i, j]:
                cluster_above = ((i-1) >= 0) and bin_grid[i-1, j]
                cluster_left = ((j-1) >= 0) and bin_grid[i, j-1]

                if cluster_above and cluster_left:
                    cluster_value_above = cluster_grid[i-1, j]
                    cluster_value_left = cluster_grid[i, j-1]
                    cluster_grid[i, j] = cluster_value_above

                    cluster[find_root_cluster(cluster_value_above, cluster)] += 1

                    if find_root_cluster(cluster_value_left, cluster) != find_root_cluster(cluster_value_above, cluster):
                        cluster[find_root_cluster(cluster_value_above, cluster)] += cluster[find_root_cluster(cluster_value_left, cluster)]
                        cluster[find_root_cluster(cluster_value_left, cluster)] = -1 * cluster_value_above


                elif cluster_above:
                    cluster_value = cluster_grid[i-1, j]
                    cluster_grid[i, j] = cluster_value
                    cluster[find_root_cluster(cluster_value, cluster)] += 1

                elif cluster_left:
                    cluster_value = cluster_grid[i, j-1]
                    cluster_grid[i, j] = cluster_value
                    cluster[find_root_cluster(cluster_value, cluster)] += 1

                else:
                    current_cluster += 1
                    cluster_grid[i, j] = current_cluster
                    cluster[current_cluster] += 1


    cluster_list = [key for key, value in cluster.items() if value >= 0]

    return len(cluster_list)



@click.command()
def main():
    #input_ = get_input(14)
    input_ = "flqrgnkx"
    print("Input:\n", input_)
    print("Output", hash_grid_1(input_))
    print("Output", hash_grid_2(input_))


if __name__ == '__main__':
    main()
