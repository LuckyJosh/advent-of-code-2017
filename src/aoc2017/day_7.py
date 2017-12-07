#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from collections import namedtuple


from .download_input import get_input

Node = namedtuple("Node", ["name", "weight", "child_nodes", "parent_node"])


def towers_1(program_info):
    programs = program_info.split("\n")
    parsed_programs = []
    for prog in programs:
        parts = prog.split(" ")
        if "->" in parts:
            next_nodes = [part.rstrip(",") for part in parts[3:]]
        else:
            next_nodes = []

        weight = int(parts[1][1:-1])
        parent_node = []
        node = Node(parts[0], weight, next_nodes, parent_node)
        parsed_programs.append(node)

    for child in parsed_programs:
        for parent in parsed_programs:
            if child.name in parent.child_nodes:
                child.parent_node.append(parent.name)

    for prog in parsed_programs:
        if not prog.parent_node:
            return prog.name




def towers_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(7)
    print("Input:\n", input_)
    print("Output", towers_1(input_))
    print("Output", towers_2(input_))


if __name__ == '__main__':
    main()

