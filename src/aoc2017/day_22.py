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
        grid = []
        for i in range(size):
            line = []
            for j in range(size):
                char = " . " if (i + ymin, j + xmin) != current_position else "(.)"
                line.append(char)
            grid.append(line)
        for y, x in infected_positions:
            grid[y - ymin][x - xmin] = " # " if (y, x) != current_position else "(#)"
        return grid

    def plot_grid(infected_positions, current_direction):
        grid = build_gird(infected_positions, current_position)
        size = len(grid)
        print("---"*size)
        for line in grid:
            print("".join(line))
        print("---"*size)
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


def virus_2(start_area, num_steps):
    start_area = start_area.split("\n")
    area_size = len(start_area)

    center = area_size // 2

    def build_gird(infected_positions, weakend_positions,
                   flagged_positions, current_position):
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
        grid = []
        for i in range(size):
            line = []
            for j in range(size):
                char = " . " if (i + ymin, j + xmin) != current_position else "(.)"
                line.append(char)
            grid.append(line)

        for y in range(size):
            for x in range(size):
                if (y, x) in infected_positions:
                    grid[y - ymin][x - xmin] = " # " if (y, x) != current_position else "(#)"
                elif (y, x) in weakend_positions:
                    grid[y - ymin][x - xmin] = " W " if (y, x) != current_position else "(W)"
                elif (y, x) in flagged_positions:
                    grid[y - ymin][x - xmin] = " F " if (y, x) != current_position else "(F)"
        return grid

    def plot_grid(infected_positions, current_direction):
        grid = build_gird(infected_positions, current_position)
        size = len(grid)
        print("---"*size)
        for line in grid:
            print("".join(line))
        print("---"*size)
        print()

    infected_positions = set()
    for i in range(area_size):
        for j in range(area_size):
            if start_area[i][j] == "#":
                infected_positions.add((i, j))
    weakend_positions = set()
    flagged_positions = set()


    directions = {"n": (0, -1), "e": (1, 0), "s": (0, 1), "w": (-1, 0)}
    turn_right = {"n": "e", "e": "s", "s": "w", "w": "n"}
    turn_left = {"n": "w", "e": "n", "s": "e", "w": "s"}
    turn_back = {"n": "s", "e": "w", "s": "n", "w": "e"}
    current_position = center, center
    current_direction = "n"

    plot_grid(infected_positions, weakend_positions, flagged_positions, current_position)

    infection_counter = 0
    for step in range(num_steps):

        if current_direction in flagged_positions:
            current_direction = turn_back[current_direction]
            flagged_positions.discard(current_position)

        elif current_position in infected_positions:
            current_direction = turn_right[current_direction]
            infected_positions.discard(current_position)
            flagged_positions.add(current_position)

        elif current_position in weakend_positions:
            # current_direction = current_direction
            weakend_positions.discard(current_position)
            infected_positions.add(current_position)
        else:
            current_direction = turn_left[current_direction]
            weakend_positions.add(current_position)

        dx, dy = directions[current_direction]
        current_position = current_position[0] + dy, current_position[1] + dx

    plot_grid(infected_positions, weakend_positions, flagged_positions, current_position)


    print(f"{infection_counter}/{num_steps}")
    return infection_counter


@click.command()
def main():
    input_ = get_input(22)
    #input_ = "..#\n#..\n..."
    print("Input:\n", input_)
    print("Output", virus_1(input_, 10000))
    print("Output", virus_2(input_), 5)


if __name__ == '__main__':
    main()

