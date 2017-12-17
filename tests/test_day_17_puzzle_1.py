#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_17 import spinlock_1


def test_spinlock_1_1():
    input_ = "3"
    output = 638
    assert spinlock_1(input_) == output
