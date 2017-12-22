#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_22 import virus_2


def test_virus_2_1():
    input_ = ("..#\n#..\n...", 100)
    output = 26
    assert virus_2(*input_) == output


def test_virus_2_2():
    input_ = ("..#\n#..\n...", 10000000)
    output = 2511944
    assert virus_2(*input_) == output

