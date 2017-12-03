#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_2 import checksum_puzzle_2


def test_checksum_puzzle_2():
    input_ = "5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5"
    output = 9
    assert checksum_puzzle_2(input_) == output