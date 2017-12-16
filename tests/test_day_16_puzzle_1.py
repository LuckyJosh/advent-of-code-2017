#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_16 import permutations_1


def test_permutations_1_1():
    input_ = "s1,x3/4,pe/b"
    output = "baedc"
    assert permutations_1(input_, num_programs=5) == output
