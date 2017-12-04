#! /usr/bin/env python
# encoding: utf-8

import click
import numpy as np

from .download_input import get_input


def check_passphrase_1(passphrases):
    # @documentation: All or parts of the documentation is missing!

    passphrases = passphrases.split("\n")
    passphrases = [phrase.split(" ") for phrase in passphrases]

    results = [True] * len(passphrases)
    for i, passphrase in passphrases:
        for j, word1 in enumerate(passphrase):
            for k, word2 in enumerate(passphrase):
                if (j != k) and (word1 == word2):
                    results[i] = False
                    break
            if not results[i]:
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

