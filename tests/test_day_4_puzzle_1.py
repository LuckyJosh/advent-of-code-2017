#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_4 import check_passphrase_1


def test_check_passphrase_1_1():
    input_ = "aa bb cc dd ee"
    output = 1
    assert check_passphrase_1(input_) == output


def test_check_passphrase_1_2():
    input_ = "aa bb cc dd aa"
    output = 0
    assert check_passphrase_1(input_) == output


def test_check_passphrase_1_3():
    input_ = "aa bb cc dd aaa"
    output = 1
    assert check_passphrase_1(input_) == output


def test_check_passphrase_1_4():
    input_ = "aa bb cc dd ee\naa bb cc dd aa\naa bb cc dd aaa"
    output = 2
    assert check_passphrase_1(input_) == output
