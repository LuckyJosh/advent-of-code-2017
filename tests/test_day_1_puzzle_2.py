from aoc2017.day_1 import solve_captcha_puzzle_2


def test_day_1_puzzle_2_1():
    input_ = "1212"
    output = 6
    assert solve_captcha_puzzle_2(input_) == output


def test_day_1_puzzle_2_2():
    input_ = "1221"
    output = 0
    assert solve_captcha_puzzle_2(input_) == output


def test_day_1_puzzle_2_3():
    input_ = "123425"
    output = 4
    assert solve_captcha_puzzle_2(input_) == output


def test_day_1_puzzle_2_4():
    input_ = "123123"
    output = 12
    assert solve_captcha_puzzle_2(input_) == output


def test_day_1_puzzle_2_5():
    input_ = "12131415"
    output = 4
    assert solve_captcha_puzzle_2(input_) == output
