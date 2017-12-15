#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_15 import generators_2


def test_generators_2_1():
    input_ = "Generator A starts with 65\nGenerator B starts with 8921"
    output = 309
    assert  generators_2(input_) == output
