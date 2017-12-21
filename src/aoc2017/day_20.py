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

    print(positions)

def particles_2(initials):
    pass

@click.command()
def main():
    input_ = get_input(20)
    print("Input:\n", input_)
    print("Output", particles_1(input_))
    print("Output", particles_2(input_))


if __name__ == '__main__':
    main()

