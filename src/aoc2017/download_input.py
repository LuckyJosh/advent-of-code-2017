#! /usr/bin/env python
# encoding: utf-8

import requests
import os
session = os.getenv('AOC_SESSION')

url = 'http://adventofcode.com/2017/day/{}/input'


def get_input(day):
    """Downloads the input for a given day automaticly.
       Taken from: https://github.com/MaxNoe/adventofcode2017/blob/master/adventofcode2017/__init__.py
    """
    r = requests.get(url.format(day), cookies={'session': session})
    r.raise_for_status()

    return r.text.strip()
