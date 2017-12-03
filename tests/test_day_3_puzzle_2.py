#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_3 import spiral_memory_steps_2

def test_spiral_memory_steps_2_1():
    input_ = "1"
    output = 2
    assert spiral_memory_steps_2(input_) == output


def test_spiral_memory_steps_2_2():
    input_ = "2"
    output = 4
    assert spiral_memory_steps_2(input_) == output


def test_spiral_memory_steps_2_3():
    input_ = "3"
    output = 4
    assert spiral_memory_steps_2(input_) == output


def test_spiral_memory_steps_2_4():
    input_ = "4"
    output = 5
    assert spiral_memory_steps_2(input_) == output


def test_spiral_memory_steps_2_5():
    input_ = "5"
    output = 10
    assert spiral_memory_steps_2(input_) == output


def test_spiral_memory_steps_2_6():
    input_ = "11"
    output = 23
    assert spiral_memory_steps_2(input_) == output
