#! /usr/bin/env python
# encoding: utf-8

import click
import click_completion

from . import day_1

click_completion.init()
click_completion.install(shell="fish", prog_name="aoc-2017")
click_completion.install(shell="bash", prog_name="aoc-2017")

@click.group()
def cli_entry_point():
    pass


cli_entry_point.add_command(day_1.main, name="day1")