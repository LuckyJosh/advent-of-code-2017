#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_14 import hash_grid_2


def test_hash_grid_2_1():
    input_ = "flqrgnkx"
    output = 1242
    assert hash_grid_2(input_) == output
