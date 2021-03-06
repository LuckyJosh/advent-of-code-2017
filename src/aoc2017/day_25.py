#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
import re
from collections import defaultdict
from tqdm import tqdm

regex_header = r"Begin in state (?P<start_state>[A-Z]).\nPerform a diagnostic checksum after (?P<checksum_steps>\d*) steps.\n\n"
regex_rules = regex = r"(?:In state (\w):)?(?:\n\s*If the current value is (\d):\n\s*-\sWrite the value (\d).\n\s*-\sMove one slot to the (\w{4,6}).\n\s*-\sContinue with state (\w).)"




from .download_input import get_input



def turing_1(blueprint):
    used_blueprint = blueprint
    header_match = re.match(regex_header, used_blueprint)
    blueprint_data = header_match.groupdict()
    used_blueprint = used_blueprint[header_match.end():]
    rule_parts = ["value", "direction", "state"]

    blueprint_rules = re.findall(regex_rules, used_blueprint)
    parsed_blueprint_rules = defaultdict(dict)
    for i, rule in enumerate(blueprint_rules):
        rule_state = rule[0] or list(parsed_blueprint_rules.keys())[-1]
        condition_rule = {rule[1]: dict(zip(rule_parts, rule[2:]))}
        parsed_blueprint_rules[rule_state].update(condition_rule)

    def generate_band(one_positions, current_position):
        min_pos = 0
        max_pos = 0
        for pos in one_positions:
            min_pos = min(min_pos, pos)
            max_pos = max(max_pos, pos)
        min_pos = min(min_pos, current_position)
        max_pos = max(max_pos, current_position)


        band = [" 0 "]*(max_pos - min_pos + 1)
        for pos in one_positions:
            band[pos - min_pos] = " 1 "

        if 0 in one_positions:
            band[0 - min_pos] = "(1)"
        else:
            band[0 - min_pos] = "(0)"

        if current_position in one_positions:
            band[current_position - min_pos] = "[1]"
        else:
            band[current_position - min_pos] = "[0]"
        return "".join(band)


    state = blueprint_data["start_state"]
    current_position = 0
    directions = {"left": -1, "right": 1}
    one_positions = set()
    print(generate_band(one_positions, current_position))
    for step in tqdm(range(int(blueprint_data["checksum_steps"]))):
        current_state_rule = parsed_blueprint_rules[state]
        current_value = str(int(current_position in one_positions))
        current_value_rules = current_state_rule[current_value]
        if current_value_rules["value"] == "1":
            one_positions.add(current_position)
        else:
            one_positions.discard(current_position)
        state = current_value_rules["state"]
        current_position += directions[current_value_rules["direction"]]
    print(generate_band(one_positions, current_position))


    return len(one_positions)

def turing_2(blueprint):
    pass

@click.command()
def main():
    input_ = get_input(25)
    #input_ = "Begin in state A.\nPerform a diagnostic checksum after 6 steps.\n\nIn state A:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state B.\n  If the current value is 1:\n    - Write the value 0.\n    - Move one slot to the left.\n    - Continue with state B.\n\nIn state B:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the left.\n    - Continue with state A.\n  If the current value is 1:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state A."
    print("Input:\n", input_)
    print("Input:\n", repr(input_))
    print("Output", turing_1(input_))
    print("Output", turing_2(input_))


if __name__ == '__main__':
    main()

