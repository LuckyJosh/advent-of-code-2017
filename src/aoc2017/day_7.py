#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np
from collections import namedtuple


from .download_input import get_input

Node = namedtuple("Node", ["name", "weight", "child_nodes", "parent_node", "weights_child_trees"])


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
        weights_child_trees = []
        node = Node(parts[0], weight, next_nodes, parent_node, weights_child_trees)
        parsed_programs.append(node)

    for child in parsed_programs:
        for parent in parsed_programs:
            if child.name in parent.child_nodes:
                child.parent_node.append(parent.name)

    for prog in parsed_programs:
        if not prog.parent_node:
            return prog.name


# @hack:  This is horrible but I can not muster the strength to do it nice today
def towers_2(program_info):
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
        weights_child_trees = []
        node = Node(parts[0], weight, next_nodes, parent_node, weights_child_trees)
        parsed_programs.append(node)

    for child in parsed_programs:
        for parent in parsed_programs:
            if child.name in parent.child_nodes:
                child.parent_node.append(parent.name)

    for prog in parsed_programs:
        if not prog.parent_node:
            root_prog_name = prog.name

    name_nodes = {}
    for prog in parsed_programs:
        name_nodes[prog.name] = prog

    def get_tree_weight(root):
        tower_weights = {}

        def get_subtree_weight(node):
            nonlocal tower_weights
            node = name_nodes[node]

            if not node.child_nodes:
                tower_weights[node.name] = node.weight
            else:
                for child in node.child_nodes:
                    get_subtree_weight(child)
                tower_weights[node.name] = node.weight + sum(tower_weights[child] for child in node.child_nodes)

        get_subtree_weight(root)
        return tower_weights

    sub_tree_weights = get_tree_weight(root_prog_name)

    node_balanced = {}
    for prog in parsed_programs:
        child_weights = set(sub_tree_weights[child] for child in prog.child_nodes)
        node_balanced[prog.name] = len(child_weights) < 2

    def get_heavy_node(root):
        root = name_nodes[root]
        if node_balanced[root.name]:
            return root
        else:
            child_sub_tree_weights = [(i, sub_tree_weights[child]) for i, child in enumerate(root.child_nodes)]
            idx = sorted(child_sub_tree_weights, key=lambda x: x[1], reverse=True)[0][0]
            node = get_heavy_node(root.child_nodes[idx])
            return node

    heavy_node = get_heavy_node(root_prog_name)

    parent_heavy = name_nodes[heavy_node.parent_node[0]]
    child_sub_tree_weights = [sub_tree_weights[child] for child in parent_heavy.child_nodes]
    diff = max(child_sub_tree_weights) - min(child_sub_tree_weights)

    return heavy_node.weight - diff







@click.command()
def main():
    input_ = get_input(7)
    print("Input:\n", input_)
    print("Output", towers_1(input_))
    print("Output", towers_2(input_))


if __name__ == '__main__':
    main()

