#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def graph_1(graph_list):
    graph_list = graph_list.replace(",", "").split("\n")
    number_of_verticies = len(graph_list)
    graph_list = [entry.split(" ") for entry in graph_list]
    adjacent_verticies = {entry[0]: entry[2:] for entry in graph_list}


    def graph_search(start_vertex, adjacent_verticies):
        # "colors": 0:white, 1:gray, 2:black
        vertex_colors = {str(i): 0 for i in range(number_of_verticies)}

        def search_from_vertex(vertex):
            nonlocal adjacent_verticies
            nonlocal vertex_colors
            if vertex_colors[vertex] == 0:
                vertex_colors[vertex] = 1
                for next_vertex in adjacent_verticies[vertex]:
                    search_from_vertex(next_vertex)
                vertex_colors[vertex] = 2

        search_from_vertex(start_vertex)

        return vertex_colors

    graph_colors = graph_search("0", adjacent_verticies)

    verticies_in_group = [vertex
                          for vertex, color in graph_colors.items()
                          if color == 2]

    return len(verticies_in_group)


def graph_2(graph_list):
    graph_list = graph_list.replace(",", "").split("\n")
    number_of_verticies = len(graph_list)
    graph_list = [entry.split(" ") for entry in graph_list]
    adjacent_verticies = {entry[0]: entry[2:] for entry in graph_list}


    def graph_search(start_vertex, adjacent_verticies):
        # "colors": 0:white, 1:gray, 2:black
        vertex_colors = {str(i): 0 for i in range(number_of_verticies)}

        def search_from_vertex(vertex):
            nonlocal adjacent_verticies
            nonlocal vertex_colors
            if vertex_colors[vertex] == 0:
                vertex_colors[vertex] = 1
                for next_vertex in adjacent_verticies[vertex]:
                    search_from_vertex(next_vertex)
                vertex_colors[vertex] = 2

        search_from_vertex(start_vertex)

        return vertex_colors

    remaining_verticies = set(str(i) for i in range(number_of_verticies))
    number_of_groups = 0
    while len(remaining_verticies) > 0:
        graph_colors = graph_search(remaining_verticies.pop(), adjacent_verticies)

        verticies_in_group = [vertex
                              for vertex, color in graph_colors.items()
                              if color == 2]

        print(verticies_in_group, set(verticies_in_group))
        remaining_verticies -= set(verticies_in_group)
        print(remaining_verticies)
        number_of_groups += 1

    return number_of_groups


@click.command()
def main():
    input_ = get_input(12)
    #input_ = "0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5"
    print("Input:\n", input_)
    print("Output", graph_1(input_))
    print("Output", graph_2(input_))


if __name__ == '__main__':
    main()

