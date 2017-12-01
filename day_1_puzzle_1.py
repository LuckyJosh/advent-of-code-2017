#! /usr/bin/env python
# encoding: utf-8
import numpy as np


def solve_captcha(captcha):
    if isinstance(captcha, str):
        captcha = list(captcha)
    if len(captcha) == 0:
        return 0
    cap = np.asarray(captcha, dtype=int)
    mask = np.zeros_like(cap, dtype=bool)
    mask[:-1] = cap[:-1] == cap[1:]
    mask[-1] = cap[0] == cap[-1]
    selection = cap[mask]
    return np.sum(selection)


def test_examples():
    example_inputs = ["1122", "1111", "1234", "91212129"]
    example_outputs = [3, 4, 0, 9]

    solution = [solve_captcha(example) for example in example_inputs]
    assert solution == example_outputs

def main():
    test_examples()

if __name__ == '__main__':
    main()