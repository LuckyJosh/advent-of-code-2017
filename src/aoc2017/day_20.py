#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
import re
from tqdm import tqdm


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
    max_without_collision = 1000
    collision_indicies = set()
    with tqdm(total=max_without_collision) as pbar:
        while cycles_without_collision < max_without_collision:

            velocities = velocities + accelerations
            positions = positions + velocities

            position_comparison = positions[:, np.newaxis] == positions[:,:]

            equal_positions_matrix = np.prod(position_comparison, axis=2)
            new_collision_indicies = np.argwhere(np.sum(equal_positions_matrix, axis=1) > 1).flatten()
            new_collision_indicies = [idx
                                      for idx in new_collision_indicies
                                      if idx not in collision_indicies]

            collision_indicies.update(set(new_collision_indicies))

            if len(new_collision_indicies) > 0:
                cycles_without_collision = 0
                positions[new_collision_indicies, :]
                velocities[new_collision_indicies, :]
                accelerations[new_collision_indicies, :]
            else:
                pbar.update(1)
                cycles_without_collision += 1


    return num_particles - len(collision_indicies)



@click.command()
def main():
    input_ = get_input(20)
    #input_ = "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>\np=<4,0,0>, v=<0,0,0>, a=<-2,0,0> "
    #input_ = "p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>\np=<-4,0,0>, v=<2,0,0>, a=<0,0,0>\np=<-2,0,0>, v=<1,0,0>, a=<0,0,0>\np=<3,0,0>, v=<-1,0,0>, a=<0,0,0>"
    print("Input:\n", input_)
    print("Output", particles_1(input_))
    print("Output", particles_2(input_))


if __name__ == '__main__':
    main()

