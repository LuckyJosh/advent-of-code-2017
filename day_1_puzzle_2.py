#! /usr/bin/env python
# encoding: utf-8
import numpy as np


def solve_captcha(captcha):
    # @documentation: All or parts of the documentation is missing!
    if isinstance(captcha, str):
        captcha = list(captcha)
    if len(captcha) == 0:
        return 0
    cap = np.asarray(captcha, dtype=int)
    mask = cap == np.roll(cap, np.floor_divide(cap.size, 2))
    selection = cap[mask]
    return np.sum(selection)


def test_examples():
    # @documentation: All or parts of the documentation is missing!
    example_inputs = ["1212", "1221", "123425", "123123", "12131415"]
    example_outputs = [6, 0, 4, 12, 4]

    solution = [solve_captcha(example) for example in example_inputs]
    assert solution == example_outputs

def main():
    test_examples()
    test_input = ""
    print(f"Solution for test input: {solve_captcha(test_input)}")

if __name__ == '__main__':
    main()