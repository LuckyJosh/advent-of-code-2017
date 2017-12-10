#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_9 import stream_2


def test_stream_2_1():
    input_ = "<>"
    output = 0
    assert stream_2(input_) == output


def test_stream_2_2():
    input_ = "<random characters>"
    output = 17
    assert stream_2(input_) == output


def test_stream_2_3():
    input_ = "<<<<>"
    output = 3
    assert stream_2(input_) == output


def test_stream_2_4():
    input_ = "<{!>}>"
    output = 2
    assert stream_2(input_) == output


def test_stream_2_5():
    input_ = "<!!>"
    output = 0
    assert stream_2(input_) == output


def test_stream_2_6():
    input_ = "<!!!>>"
    output = 0
    assert stream_2(input_) == output


def test_stream_2_7():
    input_ = '<{o"i!a,<{i<a>'
    output = 10
    assert stream_2(input_) == output
