#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_15 import generators_1


def test_generators_1_1():
    input_ = "Generator A starts with 65\nGenerator B starts with 8921"
    output = 588
    assert  generators_1(input_) == output
