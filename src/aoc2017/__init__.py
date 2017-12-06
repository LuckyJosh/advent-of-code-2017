#! /usr/bin/env python
# encoding: utf-8
import os
import click
import click_completion

from . import day_1
from . import day_2
from . import day_3
from . import day_4
from . import day_5
from . import day_6

click_completion.init()
click_completion.install(shell="fish", prog_name="aoc-2017")
click_completion.install(shell="bash", prog_name="aoc-2017")


@click.group()
def cli_entry_point():
    if 'AOC_SESSION' not in os.environ:
        raise ValueError("Environment variable AOC_SESSION is missing, "
                         "which is needed to download the test input. ")


cli_entry_point.add_command(day_1.main, name="day-1")
cli_entry_point.add_command(day_2.main, name="day-2")
cli_entry_point.add_command(day_3.main, name="day-3")
cli_entry_point.add_command(day_4.main, name="day-4")
cli_entry_point.add_command(day_5.main, name="day-5")
cli_entry_point.add_command(day_6.main, name="day-6")
