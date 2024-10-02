import src.day2 as day2
from utils import read_all_of_file


def test_part_1_examples():
    assert day2.part_1(["2x3x4"]) == 58
    assert day2.part_1(["1x1x10"]) == 43


def test_part_1():
    lines = read_all_of_file("day_2.txt")
    assert day2.part_1(lines) == 1586300


def test_part_2_examples():
    assert day2.part_2(["2x3x4"]) == 34
    assert day2.part_2(["1x1x10"]) == 14


def test_part_2():
    lines = read_all_of_file("day_2.txt")
    assert day2.part_2(lines) == 3737498
