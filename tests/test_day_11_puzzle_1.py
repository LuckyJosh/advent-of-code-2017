#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_11 import hexgrid_1


def test_hexgrid_1_1():
    input_ = "ne,ne,ne"
    output = 3
    assert hexgrid_1(input_) == output


def test_hexgrid_1_2():
    input_ = "ne,ne,sw,sw"
    output = 0
    assert hexgrid_1(input_) == output


def test_hexgrid_1_3():
    input_ = "ne,ne,s,s"
    output = 2
    assert hexgrid_1(input_) == output


def test_hexgrid_1_4():
    input_ = "se,sw,se,sw,sw"
    output = 3
    assert hexgrid_1(input_) == output
