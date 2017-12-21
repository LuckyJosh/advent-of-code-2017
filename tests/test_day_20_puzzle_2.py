#! /usr/bin/env python
# encoding: utf-8

from aoc2017.day_20 import particles_2


def test_particles_2_1():
    input_ = "p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>\np=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>\np=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>\np=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"
    output = 1
    assert particles_2(input_) == output




