#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
import re


from .download_input import get_input

regex = r"p=<(-?\d*,-?\d*,-?\d*)>, v=<(-?\d*,-?\d*,-?\d*)>, a=<(-?\d*,-?\d*,-?\d*)>"

def particles_1(initials):
    initials = initials.split("\n")
    num_particles = len(initials)

    positions = np.zeros((num_particles, 3), dtype=int)
    velocities = np.zeros((num_particles, 3), dtype=int)
    accelerations = np.zeros((num_particles, 3), dtype=int)

    for i, particle in enumerate(initials):
        match = re.match(regex, particle)
        p, v, a = match.groups()
        positions[i] = p.split(",")
        velocities[i] = v.split(",")
        accelerations[i] = a.split(",")

    closest_index = np.argmin(np.sum(positions, axis=1))

    cycles_without_change = 0
    while cycles_without_change < 100000:

        velocities = velocities + accelerations
        positions = positions + velocities

        new_closest_index = np.argmin(np.sum(np.abs(positions), axis=1))

        if closest_index == new_closest_index:
            cycles_without_change += 1
        else:
            closest_index = new_closest_index
            cycles_without_change = 0


    return closest_index

def particles_2(initials):
    initials = initials.split("\n")
    num_particles = len(initials)

    positions = np.zeros((num_particles, 3), dtype=int)
    velocities = np.zeros((num_particles, 3), dtype=int)
    accelerations = np.zeros((num_particles, 3), dtype=int)

    for i, particle in enumerate(initials):
        match = re.match(regex, particle)
        p, v, a = match.groups()
        positions[i] = p.split(",")
        velocities[i] = v.split(",")
        accelerations[i] = a.split(",")

    closest_index = np.argmin(np.sum(positions, axis=1))

    cycles_without_collision = 0
    while cycles_without_collision < 100:

        velocities = velocities + accelerations
        positions = positions + velocities

        position_comparison = positions[:, :, np.newaxis] == positions
        equal_positions_matrix = np.prod(position_comparison, axis=2)
        collision_indicies = np.argwhere(np.sum(equal_positions_matrix, axis=1) > 1).flatten()

        if collision_indicies:
            cycles_without_collision = 0
            positions[collision_indicies, :] = 0
            velocities[collision_indicies, :] = 0
            accelerations[collision_indicies, :] = 0
        else:
            cycles_without_collision += 1

    non_collided_particles = np.sum(np.sum(positions, axis=1) > 0)
    return non_collided_particles



@click.command()
def main():
    input_ = get_input(20)
    #input_ = "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>\np=<4,0,0>, v=<0,0,0>, a=<-2,0,0> "
    print("Input:\n", input_)
    print("Output", particles_1(input_))
    print("Output", particles_2(input_))


if __name__ == '__main__':
    main()

