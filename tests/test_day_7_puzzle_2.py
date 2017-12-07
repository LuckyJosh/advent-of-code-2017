#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_7 import towers_2


def test_towers_2_1():
    input_ = "pbga (66)\nxhth (57)\nebii (61)\nhavc (66)\nktlj (57)\nfwft (72) -> ktlj, cntj, xhth\n"
    input_ += "qoyq (66)\npadx (45) -> pbga, havc, qoyq\ntknk (41) -> ugml, padx, fwft\njptl (61)\n"
    input_ += "ugml (68) -> gyxo, ebii, jptl\ngyxo (61)\ncntj (57)"
    output = 60
    assert towers_2(input_) == output

def test_towers_2_2():
    input_ = "h (3)\nm (1)\nf (2)\ni (3)\nk (1)\nd (9) -> k, l, m\n"
    input_ += "j (3)\nc (3) -> h, i, j\na (5) -> b, c, d\ng (2)\n"
    input_ += "b (6) -> e, f, g\ne (3)\nl (1)"
    output = 2
    assert towers_2(input_) == output
