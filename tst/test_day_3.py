import src.day3 as day3
from utils import read_all_of_file


def test_part_1_examples():
    assert day3.part_1(">") == 2
    assert day3.part_1("^>v<") == 4
    assert day3.part_1("^v^v^v^v^v") == 2


def test_part_1():
    line = read_all_of_file("day_3.txt")[0]
    assert day3.part_1(line) == 2081


def test_part_2_examples():
    assert day3.part_2("^v") == 3
    assert day3.part_2("^>v<") == 3
    assert day3.part_2("^v^v^v^v^v") == 11


def test_part_2():
    line = read_all_of_file("day_3.txt")[0]
    assert day3.part_2(line) == 2341
