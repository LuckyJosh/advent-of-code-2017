#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_24 import brigdes_2


def test_brigdes_2_1():
    input_ = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"
    output = 19
    assert brigdes_2(input_) == output
