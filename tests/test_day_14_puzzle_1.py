#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_14 import hash_grid_1


def test_hash_grid_1_1():
    input_ = "flqrgnkx"
    output = 8108
    assert hash_grid_1(input_) == output
