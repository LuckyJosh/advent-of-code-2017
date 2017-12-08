#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_8 import register_2


def test_register_2_1():
    input_ = "b inc 5 if a > 1\na inc 1 if b < 5\nc dec -10 if a >= 1\nc inc -20 if c == 10"
    output = 10
    assert register_2(input_) == output
