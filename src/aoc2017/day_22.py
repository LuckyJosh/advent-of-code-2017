#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def virus_1(start_area, num_steps):
    start_area = start_area.split("\n")
    area_size = len(start_area)

    center = area_size // 2

    def build_gird(infected_positions, current_position):
        xmax = 0
        xmin = 0
        ymax = 0
        ymin = 0
        for y, x in infected_positions:
            xmax = max(xmax, x)
            xmin = min(xmin, x)
            ymax = max(ymax, y)
            ymin = min(ymin, y)

        size = max(xmax - xmin, ymax - ymin) + 1
        print(size)
        grid = []
        for i in range(size):
            line = []
            for j in range(size):
                char = " . " if (i, j) != current_position else "(.)"
                line.append(char)
            grid.append(line)
        for y, x in infected_positions:
            print(y - ymin, x - xmin )
            grid[y - ymin][x - xmin] = " # " if (y, x) != current_position else "(#)"
        return grid

    def plot_grid(infected_positions, current_direction):
        grid = build_gird(infected_positions, current_position)
        for line in grid:
            print(line)
        print()

    infected_positions = set()
    for i in range(area_size):
        for j in range(area_size):
            if start_area[i][j] == "#":
                infected_positions.add((i, j))


    print(infected_positions)

    directions = {"n": (0, -1), "e": (1, 0), "s": (0, 1), "w": (-1, 0)}
    turn_right = {"n": "e", "e": "s", "s": "w", "w": "n"}
    turn_left = {"n": "w", "e": "n", "s": "e", "w": "s"}
    current_position = center, center
    current_direction = "n"

    plot_grid(infected_positions, current_position)

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

        plot_grid(infected_positions, current_direction)


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

