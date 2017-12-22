#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def virus_1(start_area, num_steps):
    start_area = start_area.split("\n")
    area_size = len(start_area)

    infected_positions = set()

    for i in range(area_size):
        for j in range(area_size):
            if start_area[i][j] == "#":
                infected_positions.add((i, j))

    print(infected_positions)

    center = area_size // 2

    directions = {"n": (0, 1), "e": (1, 0), "s": (0, -1), "w": (-1, 0)}
    turn_right = {"n": "e", "e": "s", "s": "w", "w": "n"}
    turn_left = {"n": "w", "e": "n", "s": "e", "w": "s"}
    current_position = center, center
    current_direction = "n"

    for step in range(num_steps):
        xf, yf = directions[current_direction]
        if current_position in infected_positions:
            infected_positions.discard(current_position)
        else:
            infected_positions.add(current_position)



    return start_area

def virus_2(start_area):
    pass


@click.command()
def main():
    #input_ = get_input(22)
    input_ = "..#\n#..\n..."
    print("Input:\n", input_)
    print("Output", virus_1(input_, 7))
    print("Output", virus_2(input_))


if __name__ == '__main__':
    main()

