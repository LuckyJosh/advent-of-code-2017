#! /usr/bin/env python
# encoding: utf-8
import click
import numpy as np

from . import get_input

def solve_captcha_puzzle_1(captcha):
    # @documentation: All or parts of the documentation is missing!
    if isinstance(captcha, str):
        captcha = list(captcha)
    if len(captcha) == 0:
        return 0
    cap = np.asarray(captcha, dtype=int)
    mask = cap == np.roll(cap, 1)
    selection = cap[mask]
    return np.sum(selection)

def solve_captcha_puzzle_2(captcha):
    # @documentation: All or parts of the documentation is missing!
    if isinstance(captcha, str):
        captcha = list(captcha)
    if len(captcha) == 0:
        return 0
    cap = np.asarray(captcha, dtype=int)
    mask = cap == np.roll(cap, np.floor_divide(cap.size, 2))
    selection = cap[mask]
    return np.sum(selection)


@click.command()
def main():
    test_input_puzzle_1 = get_input(1)
    print(f"Solution for test input: {solve_captcha_puzzle_1(test_input_puzzle_1)}")

    test_input_puzzle_2 = get_input(1)
    print(f"Solution for test input: {solve_captcha_puzzle_2(test_input_puzzle_2)}")


if __name__ == '__main__':
    main()
