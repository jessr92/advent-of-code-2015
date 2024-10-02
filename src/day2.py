import re
from functools import reduce


def part_1(dimensions: list[str]) -> int:
    return sum(map(wrapping_paper_needed, dimensions))


def wrapping_paper_needed(dimensions: str) -> int:
    dimensions: list[int] = [int(s) for s in re.findall(r'\d+', dimensions)]
    assert len(dimensions) == 3
    area_1: int = dimensions[0] * dimensions[1]
    area_2: int = dimensions[0] * dimensions[2]
    area_3: int = dimensions[1] * dimensions[2]
    smallest_area: int = min(area_1, area_2, area_3)
    return (2 * area_1) + (2 * area_2) + (2 * area_3) + smallest_area


def part_2(dimensions: list[str]) -> int:
    return sum(map(ribbon_needed, dimensions))


def ribbon_needed(dimensions: str) -> int:
    dimensions: list[int] = [int(s) for s in re.findall(r'\d+', dimensions)]
    assert len(dimensions) == 3
    dimensions.sort()
    ribbon_to_wrap = (dimensions[0] * 2) + (dimensions[1]) * 2
    ribbon_for_bow = reduce(lambda a, b: a * b, dimensions)
    return ribbon_to_wrap + ribbon_for_bow
