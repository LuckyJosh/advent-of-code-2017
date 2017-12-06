#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_6 import infinit_loop_2


def test_infinit_loop_1_2():
    input_ = "0\t2\t7\t0"
    output = 4
    assert infinit_loop_2(input_) == output
