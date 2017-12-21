#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_20 import particles_1


def test_particles_1_1():
    input_ = "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>\np=<4,0,0>, v=<0,0,0>, a=<-2,0,0> "
    output = 0
    assert particles_1(input_) == output




