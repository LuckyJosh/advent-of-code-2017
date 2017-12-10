#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_10 import knot_hash_1


def test_knot_hash_1_1():
    input_ = "3,4,1,5"
    output = 12
    assert knot_hash_1(input_, list_length=5) == output
