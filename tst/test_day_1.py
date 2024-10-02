import src.day1 as day1
from utils import read_all_of_file

def test_part_1_examples():
    assert day1.part_1("(())") == 0
    assert day1.part_1("()()") == 0
    assert day1.part_1("(((") == 3
    assert day1.part_1("(()(()(") == 3
    assert day1.part_1("))(((((") == 3
    assert day1.part_1("())") == -1
    assert day1.part_1("))(") == -1
    assert day1.part_1(")))") == -3
    assert day1.part_1(")())())") == -3

def test_part_1():
    floors = read_all_of_file("day_1.txt")[0]
    assert day1.part_1(floors) == 138

def test_part_2_examples():
    assert day1.part_2(")") == 1
    assert day1.part_2("()())") == 5

def test_part_2():
    floors = read_all_of_file("day_1.txt")[0]
    assert day1.part_2(floors) == 1771
