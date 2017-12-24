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


    finished = False
    bridge = [(0, 0)]
    while not finished:
        print("brige:", bridge)
        current_last_component = bridge[-1]
        if isinstance(current_last_component, list):
            current_connections = [comp[-1] for comp in current_last_component]
        else:
            current_connections = [current_last_component[1]]
        print(current_connections)


        current_next = []
        for current_connection in current_connections:
            for component in components:
                if current_connection == component[0]:
                    current_next.append(component)
                    components.remove(component)
                elif current_connection == component[-1]:
                    current_next.append((component[-1], component[0]))
                    components.remove(component)

            print(current_next)

        if current_next:
            bridge.append(current_next)
        else:
            finished = True

    for i

    print("--".join([str(component) for component in bridge]))
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

