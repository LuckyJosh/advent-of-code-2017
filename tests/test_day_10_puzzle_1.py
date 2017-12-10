#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_10 import knot_hash_1


def test_knot_hash_1_1():
    input_ = ""
    output = 12
    assert knot_hash_1(input_) == output
