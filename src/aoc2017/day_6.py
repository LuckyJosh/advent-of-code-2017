#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def infinit_loop_1(blocks):
    blocks = [int(block) for block in blocks.split("\t")]
    blocks = np.array(blocks)
    blocks_change = np.zeros_like(blocks)
    num_banks = blocks.size
    past_configs = set()
    num_redistributions = 0
    while num_redistributions == len(past_configs):
        num_redistributions += 1
        past_configs.add(tuple(blocks.tolist()))
        max_arg = np.argmax(blocks)
        max_value = blocks[max_arg]
        fill_value, rest = divmod(max_value, num_banks)
        blocks_change.fill(fill_value)
        blocks_change[:rest] += 1
        blocks_change = np.roll(blocks_change, max_arg + 1)
        blocks_change[max_arg] -= max_value
        blocks += blocks_change

    return num_redistributions - 1


def infinit_loop_2(blocks):
    blocks = [int(block) for block in blocks.split("\t")]
    blocks = np.array(blocks)
    blocks_change = np.zeros_like(blocks)
    num_banks = blocks.size
    past_configs = dict()
    num_redistributions = 0

    while True:
        if tuple(blocks.tolist()) not in past_configs:
            past_configs[tuple(blocks.tolist())] = num_redistributions
        else:
            break

        num_redistributions += 1
        max_arg = np.argmax(blocks)
        max_value = blocks[max_arg]
        fill_value, rest = divmod(max_value, num_banks)
        blocks_change.fill(fill_value)
        blocks_change[:rest] += 1
        blocks_change = np.roll(blocks_change, max_arg + 1)
        blocks_change[max_arg] -= max_value
        blocks += blocks_change

    return num_redistributions - past_configs[tuple(blocks.tolist())]


@click.command()
def main():
    input_ = get_input(6)
    print("Input:\n", input_)
    print("Output", infinit_loop_1(input_))
    print("Output", infinit_loop_2(input_))


if __name__ == '__main__':
    main()

