#! /usr/bin/env python
# encoding: utf-8

import requests
import os
import click
import click_completion

from . import day_1
from . import day_2

click_completion.init()
click_completion.install(shell="fish", prog_name="aoc-2017")
click_completion.install(shell="bash", prog_name="aoc-2017")

session = os.getenv('AOC_SESSION')

url = 'http://adventofcode.com/2017/day/{}/input'


def get_input(day):
    """Downloads the input for a given day automaticly.
       Taken from: https://github.com/MaxNoe/adventofcode2017/blob/master/adventofcode2017/__init__.py
    """
    r = requests.get(url.format(day), cookies={'session': session})
    r.raise_for_status()

    return r.text.strip()




@click.group()
def cli_entry_point():
    if 'AOC_SESSION' not in os.environ:
        raise ValueError("Environment variable AOC_SESSION is missing, "
                         "which is needed to download the test input. ")


cli_entry_point.add_command(day_1.main, name="day-1")
cli_entry_point.add_command(day_2.main, name="day-2")

