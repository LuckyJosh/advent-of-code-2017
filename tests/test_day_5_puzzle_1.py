#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_5 import memory_jumps_1


def test_memory_jumps_1_1():
    input_ = "0\n3\n0\n1\n-3"
    output = 5
    assert memory_jumps_1(input_) == output
