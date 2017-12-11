#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_11 import hexgrid_2


def test_hexgrid_2_1():
    input_ = "ne,ne,ne"
    output = 3
    assert hexgrid_2(input_) == output


def test_hexgrid_2_2():
    input_ = "ne,ne,sw,sw"
    output = 2
    assert hexgrid_2(input_) == output


def test_hexgrid_2_3():
    input_ = "ne,ne,s,s"
    output = 2
    assert hexgrid_2(input_) == output


def test_hexgrid_2_4():
    input_ = "se,sw,se,sw,sw"
    output = 3
    assert hexgrid_2(input_) == output
