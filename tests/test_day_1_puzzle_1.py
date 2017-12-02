from aoc2017.day_1 import solve_captcha_puzzle_1


def test_day_1_puzzle_1_1():
    input_ = "1122"
    output = 3
    assert solve_captcha_puzzle_1(input_) == output


def test_day_1_puzzle_1_2():
    input_ = "1111"
    output = 4
    assert solve_captcha_puzzle_1(input_) == output


def test_day_1_puzzle_1_3():
    input_ = "1234"
    output = 0
    assert solve_captcha_puzzle_1(input_) == output


def test_day_1_puzzle_1_4():
    input_ = "91212129"
    output = 9
    assert solve_captcha_puzzle_1(input_) == output
