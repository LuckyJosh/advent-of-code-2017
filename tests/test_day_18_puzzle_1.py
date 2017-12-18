#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_18 import duet_1


def test_duet_1_1():
    input_ = "set a 1\nadd a 2\nmul a a\nmod a 5\nsnd a\nset a 0\nrcv a\njgz a -1\nset a 1\njgz a -2"
    output = 4
    assert duet_1(input_) == output
