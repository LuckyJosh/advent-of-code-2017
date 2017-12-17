#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from tqdm import tqdm

from .download_input import get_input


def spinlock_1(num_steps):
    num_steps = int(num_steps)
    spinlock = [0]
    len_spinlock = 1
    num_iterations = 2017
    current_position = 0

    for it in range(1, num_iterations + 1):
        current_position += num_steps
        current_position %= len_spinlock
        spinlock.insert(current_position + 1, it)
        len_spinlock += 1
        current_position += 1
    print(spinlock)
    return spinlock[(spinlock.index(2017) + 1) % len_spinlock]


def spinlock_2(num_steps):
    num_steps = int(num_steps)
    spinlock = [0]
    len_spinlock = 1
    num_iterations = int(5e6)
    current_position = 0

    for it in tqdm(range(1, num_iterations + 1)):
        current_position += num_steps
        current_position %= len_spinlock
        spinlock.insert(current_position + 1, it)
        len_spinlock += 1
        current_position += 1
    print(spinlock)
    return spinlock[(spinlock.index(0) + 1) % len_spinlock]

@click.command()
def main():
    input_ = get_input(17)
    #input_ = "3"
    print("Input:\n", input_)
    print("Output", spinlock_1(input_))
    print("Output", spinlock_2(input_))


if __name__ == '__main__':
    main()

