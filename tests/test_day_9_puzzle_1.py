#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_9 import stream_1


def test_stream_1_1():
    input_ = "{}"
    output = 1
    assert stream_1(input_) == output


def test_stream_1_2():
    input_ = "{{{}}}"
    output = 6
    assert stream_1(input_) == output


def test_stream_1_3():
    input_ = "{{},{}}"
    output = 5
    assert stream_1(input_) == output


def test_stream_1_4():
    input_ = "{{{},{},{{}}}}"
    output = 16
    assert stream_1(input_) == output


def test_stream_1_5():
    input_ = "{<a>,<a>,<a>,<a>}"
    output = 1
    assert stream_1(input_) == output


def test_stream_1_6():
    input_ = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
    output = 9
    assert stream_1(input_) == output


def test_stream_1_7():
    input_ = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
    output = 9
    assert stream_1(input_) == output


def test_stream_1_8():
    input_ = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
    output = 3
    assert stream_1(input_) == output


def test_stream_1_8():
    input_ = "{{<a!>},{<a!>},\n{<a!>},{<ab>}}"
    output = 3
    assert stream_1(input_) == output


def test_stream_1_9():
    input_ = "{{},\n{}}"
    output = 5
    assert stream_1(input_) == output
