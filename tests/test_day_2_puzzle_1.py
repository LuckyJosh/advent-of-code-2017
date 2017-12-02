from aoc2017.day_2 import checksum_puzzle_1

def test_checksum_puzzle_1():
    input_ = """5 1 9 5
                7 5 3
                2 4 6 8"""
    output = 18
    assert checksum_puzzle_1(input_) == output