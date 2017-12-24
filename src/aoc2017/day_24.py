#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def brigdes_1(components):
    components = [tuple(
                  [int(part)
                   for part in component.split("/")])
                  for component in components.split("\n")]

    def flatten(nested_form):
        flat_form = []
        for elem in nested_form:
            if hasattr(elem, "__iter__"):
                for e in flatten(elem):
                    flat_form.append(e)
            else:
                flat_form.append(elem)

        return flat_form

    def build_bridges(current_bridge, current_components):
        current_last_component = current_bridge[-1]
        current_connection = current_last_component[-1]
        possible_next_components = []
        possible_next_component_isflipped = []
        for component in current_components:
                if current_connection == component[0]:
                    possible_next_components.append(component)
                    possible_next_component_isflipped.append(False)
                elif current_connection == component[-1]:
                    possible_next_components.append((component[-1], component[0]))
                    possible_next_component_isflipped.append(True)
        if not possible_next_components:
            return [current_bridge]
        else:
            bridge_ends = []
            for i, next_component in enumerate(possible_next_components):
                current_components_ = current_components[:]

                if possible_next_component_isflipped[i]:
                    current_components_.remove((next_component[-1], next_component[0]))
                else:
                    current_components_.remove(next_component)

                bridge_ends.append(build_bridges(current_bridge + [next_component], current_components_))
            return [current_bridge + bridge_end for bridge_end in bridge_ends]


    finished = False
    bridge = [(0, 0)]

    print(build_bridges(bridge, components))



    #print("--".join([str(component) for component in bridge]))
    return sum(flatten(bridge))


def brigdes_2(components):
    pass

@click.command()
def main():
    #input_ = get_input(24)
    input_ = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"
    print("Input:\n", input_)
    print("Output", brigdes_1(input_))
    print("Output", brigdes_2(input_))


if __name__ == '__main__':
    main()

