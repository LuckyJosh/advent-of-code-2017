#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_2 import checksum_puzzle_1

def test_checksum_puzzle_1():
    input_ = "5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8"
    output = 18
    assert checksum_puzzle_1(input_) == output