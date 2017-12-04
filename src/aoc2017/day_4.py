#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def check_passphrase_1(passphrases):
    # @documentation: All or parts of the documentation is missing!

    passphrases = passphrases.split("\n")
    passphrases = [phrase.split(" ") for phrase in passphrases]

    results = []
    for passphrase in passphrases:
        for i, word1 in enumerate(passphrase):
            for j, word2 in enumerate(passphrase):
                if (i != j) and (word1 == word2):
                    results.append(False)
                    break
            if not results[-1]:
                break


    return results

def func_2(arg):
    pass

@click.command()
def main():
    input_ = get_input(4)
    print("Input:\n", input_)
    print("Output", check_passphrase_1(input_))
    print("Output", func_2(input_))


if __name__ == '__main__':
    main()

