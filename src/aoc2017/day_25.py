#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
import re

regex_header = r"Begin in state (?P<start_state>[A-Z]).\nPerform a diagnostic checksum after (?P<checksum_steps>\d) steps.\n\n"
regex_rules = regex = r"(?:In state (\w):)?(?:\n\s*If the current value is (\d):\n\s*-\sWrite the value (\d).\n\s*-\sMove one slot to the (\w{4,6}).\n\s*-\sContinue with state (\w).)"




from .download_input import get_input


def turing_1(blueprint):
    used_blueprint = blueprint
    header_match = re.match(regex_header, used_blueprint)
    blueprint_data = header_match.groupdict()
    used_blueprint = used_blueprint[header_match.end():]
    rule_parts = ["current_state", "condition", "new_value", "move_direction", "new_state"]

    blueprint_rules = re.findall(regex_rules, used_blueprint)
    parsed_blueprint_rules = {}


    return blueprint_data, blueprint_rules

def turing_2(blueprint):
    pass

@click.command()
def main():
    #input_ = get_input(25)
    input_ = "Begin in state A.\nPerform a diagnostic checksum after 6 steps.\n\nIn state A:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state B.\n  If the current value is 1:\n    - Write the value 0.\n    - Move one slot to the left.\n    - Continue with state B.\n\nIn state B:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the left.\n    - Continue with state A.\n  If the current value is 1:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state A."
    print("Input:\n", input_)
    print("Input:\n", repr(input_))
    print("Output", turing_1(input_))
    print("Output", turing_2(input_))


if __name__ == '__main__':
    main()

