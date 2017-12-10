#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def stream_1(stream):
    in_garbage = False
    after_bang = False
    groups = []
    current_group = []
    for i, char in enumerate(stream):
        if after_bang:
            after_bang = False
        elif char == "!":
            after_bang = True
        elif char == "<":
            in_garbage = True
        elif char == ">":
            in_garbage = False
        elif (not in_garbage) and (char == "{"):
            groups.append([i, 0])
            current_group.append(len(groups) - 1)
        elif (not in_garbage) and (char == "}"):
            groups[current_group.pop()][1] = i

    def get_containment(group):
        group_containment = []
        for group_ in groups:
            if (group_[0] < group[0]) and (group[1] < group_[1]):
                group_containment.append(True)
            else:
                group_containment.append(False)
        return group_containment

    def get_group_score(group):
        containment = get_containment(group)
        return np.cumsum(containment)[-1] + 1

    groups = [tuple(group) for group in groups]
    score_by_group = {group: get_group_score(group) for group in groups}

    return sum(score_by_group.values())


def stream_2(stream):
    in_garbage = False
    after_bang = False
    groups = []
    current_group = []
    garbage_count = 0
    for i, char in enumerate(stream):
        if after_bang:
            after_bang = False
            continue
        elif char == "!":
            after_bang = True
        elif char == "<":
            if in_garbage:
                garbage_count += 1
            in_garbage = True
        elif char == ">":
            in_garbage = False
        elif (not in_garbage) and (char == "{"):
            groups.append([i, 0])
            current_group.append(len(groups) - 1)
        elif (not in_garbage) and (char == "}"):
            groups[current_group.pop()][1] = i
        if in_garbage and not char in ["!", "<"]:
            garbage_count += 1

    return garbage_count

@click.command()
def main():
    #input_ = "{{{}}}"
    #input_ = "{<random characters>}"
    input_ = get_input(9)
    print("Input:\n", input_)
    print("Output", stream_1(input_))
    print("Output", stream_2(input_))


if __name__ == '__main__':
    main()

