#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def virus_1(start_area, num_steps):
    start_area = start_area.split("\n")
    area_size = len(start_area)

    center = area_size // 2

    infected_positions = set()
    for i in range(area_size):
        for j in range(area_size):
            if start_area[i][j] == "#":
                infected_positions.add((i, j))

    print(infected_positions)



    directions = {"n": (0, 1), "e": (1, 0), "s": (0, -1), "w": (-1, 0)}
    turn_right = {"n": "e", "e": "s", "s": "w", "w": "n"}
    turn_left = {"n": "w", "e": "n", "s": "e", "w": "s"}
    current_position = center, center
    current_direction = "n"

    infection_counter = 0
    for step in range(num_steps):

        if current_position in infected_positions:
            current_direction = turn_right[current_direction]
            infected_positions.discard(current_position)
        else:
            infection_counter += 1
            current_direction = turn_left[current_direction]
            infected_positions.add(current_position)

        dx, dy = directions[current_direction]
        current_position = current_position[0] + dy, current_position[1] + dx

    print(f"{infection_counter}/{num_steps}")
    return infection_counter

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

