#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_4 import check_passphrase_2


def test_check_passphrase_2_1():
    input_ = "abcde fghij"
    output = 1
    assert check_passphrase_2(input_) == output


def test_check_passphrase_2_2():
    input_ = "abcde xyz ecdab"
    output = 0
    assert check_passphrase_2(input_) == output


def test_check_passphrase_2_3():
    input_ = "a ab abc abd abf abj"
    output = 1
    assert check_passphrase_2(input_) == output


def test_check_passphrase_2_4():
    input_ = "iiii oiii ooii oooi oooo"
    output = 1
    assert check_passphrase_2(input_) == output


def test_check_passphrase_2_5():
    input_ = "oiii ioii iioi iiio"
    output = 0
    assert check_passphrase_2(input_) == output


def test_check_passphrase_2_6():
    input_ = "abcde fghij\nabcde xyz ecdab\na ab abc abd abf abj\niiii oiii ooii oooi oooo\noiii ioii iioi iiio"
    output = None
    assert check_passphrase_2(input_) == output
