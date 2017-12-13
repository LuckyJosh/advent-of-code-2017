#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_13 import firewall_1


def test_firewall_1_1():
    input_ = "0: 3\n1: 2\n4: 4\n6: 4"
    output = 24
    assert firewall_1(input_) == output
