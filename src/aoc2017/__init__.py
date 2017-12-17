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
from . import day_7
from . import day_8
from . import day_9
from . import day_10
from . import day_11
from . import day_12
from . import day_13
from . import day_14
from . import day_15
from . import day_16
from . import day_17

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
cli_entry_point.add_command(day_7.main, name="day-7")
cli_entry_point.add_command(day_8.main, name="day-8")
cli_entry_point.add_command(day_9.main, name="day-9")
cli_entry_point.add_command(day_10.main, name="day-10")
cli_entry_point.add_command(day_11.main, name="day-11")
cli_entry_point.add_command(day_12.main, name="day-12")
cli_entry_point.add_command(day_13.main, name="day-13")
cli_entry_point.add_command(day_14.main, name="day-14")
cli_entry_point.add_command(day_15.main, name="day-15")
cli_entry_point.add_command(day_16.main, name="day-16")
cli_entry_point.add_command(day_17.main, name="day-17")
