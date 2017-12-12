#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_12 import graph_2


def test_graph_2_1():
    input_ = "0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5"
    output = 2
    assert graph_2(input_) == output
