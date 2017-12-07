#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_7 import towers_2


def test_towers_2_1():
    input_ = "pbga (66)\nxhth (57)\nebii (61)\nhavc (66)\nktlj (57)\nfwft (72) -> ktlj, cntj, xhth\n"
    input_ += "qoyq (66)\npadx (45) -> pbga, havc, qoyq\ntknk (41) -> ugml, padx, fwft\njptl (61)\n"
    input_ += "ugml (68) -> gyxo, ebii, jptl\ngyxo (61)\ncntj (57)"
    output = 60
    assert towers_2(input_) == output
