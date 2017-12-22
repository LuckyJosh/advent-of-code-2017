#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_22 import virus_1


def test_virus_1_1():
    input_ = ("..#\n#..\n...", 7)
    output = 5
    assert virus_1(*input_) == output


def test_virus_1_2():
    input_ = ("..#\n#..\n...", 70)
    output = 41
    assert virus_1(*input_) == output


def test_virus_1_3():
    input_ = ("..#\n#..\n...", 10000)
    output = 5587
    assert virus_1(*input_) == output
