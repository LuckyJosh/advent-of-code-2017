#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from tqdm import tqdm

from .download_input import get_input


def generators_1(seedstring):
    seeds = [int(line.split()[-1]) for line in seedstring.split("\n")]

    factors = [16807, 48271]
    modulus = 2147483647
    def num_generator(seed, a, b):
        while True:
            seed = (a * seed) % b
            yield seed

    generator_1 = num_generator(seeds[0], factors[0], modulus)
    generator_2 = num_generator(seeds[1], factors[1], modulus)

    iterations = 4e7
    lowest_bits_equal = 0
    for gen1, gen2 in tqdm(zip(generator_1, generator_2)):

        bits_1 = bin(gen1)[2:]
        bits_2 = bin(gen2)[2:]
        missing_bits_1 = 16 - len(bits_1)
        missing_bits_2 = 16 - len(bits_2)
        if missing_bits_1 > 0:
            bits_1 = missing_bits_1*"0" + bits_1
        if missing_bits_2 > 0:
            bits_2 = missing_bits_2*"0" + bits_2

        last_bits_1 = bits_1[-16:]
        last_bits_2 = bits_2[-16:]

        if last_bits_1 == last_bits_2:

            lowest_bits_equal += 1

        iterations -= 1
        if iterations == 0:
            break


    return lowest_bits_equal



def generators_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(15)
    #input_ = "Generator A starts with 65\nGenerator B starts with 8921"
    print("Input:\n", input_)
    print("\nOutput", generators_1(input_))
    print("Output", generators_2(input_))


if __name__ == '__main__':
    main()

