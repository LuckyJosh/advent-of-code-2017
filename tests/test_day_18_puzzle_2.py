#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_18 import duet_2


def test_duet_2_1():
    input_ = "snd 1\nsnd 2\nsnd p\nrcv a\nrcv b\nrcv c\nrcv d"
    output = 3
    assert duet_2(input_) == output