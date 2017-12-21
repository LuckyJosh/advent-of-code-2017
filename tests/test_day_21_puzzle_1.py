#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_21 import fractral_1


def test_fractral_1_():
    input_ = "../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#"
    output = 12
    assert fractral_1(input_, num_iterations=2) == output
