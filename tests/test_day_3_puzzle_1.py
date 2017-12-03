#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_3 import spiral_memory_steps_1


def test_spiral_memory_steps_1_1():
    input_ = 1
    output = 0
    assert spiral_memory_steps_1(input_) == output


def test_spiral_memory_steps_1_2():
    input_ = 12
    output = 3
    assert spiral_memory_steps_1(input_) == output


def test_spiral_memory_steps_1_3():
    input_ = 23
    output = 2
    assert spiral_memory_steps_1(input_) == output


def test_spiral_memory_steps_1_4():
    input_ = 1024
    output = 31
    assert spiral_memory_steps_1(input_) == output
