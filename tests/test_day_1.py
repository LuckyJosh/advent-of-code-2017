from aoc2017.day_1 import solve_captcha_puzzle_1


def test_day_1_puzzle_1_1():
    input_ = "1122"
    output = 3
    assert solve_captcha_puzzle_1(input_) == output
