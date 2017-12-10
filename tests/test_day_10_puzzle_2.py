#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_10 import knot_hash_2


def test_knot_hash_2_1():
    input_ = ""
    output = "a2582a3a0e66e6e86e3812dcb672a272"
    assert knot_hash_2(input_) == output


def test_knot_hash_2_2():
    input_ = "AoC 2017"
    output = "33efeb34ea91902bb2f59c9920caa6cd"
    assert knot_hash_2(input_) == output


def test_knot_hash_2_3():
    input_ = "1,2,3"
    output = "3efbe78a8d82f29979031a4aa0b16a9d"
    assert knot_hash_2(input_) == output


def test_knot_hash_2_4():
    input_ = "1,2,4"
    output = "63960835bcdc130f0b66d7ff4f6a5a8e"
    assert knot_hash_2(input_) == output
