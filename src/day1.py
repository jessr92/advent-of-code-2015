def part_1(floors: str) -> int:
    return floors.count('(') - floors.count(')')

def part_2(floors: str) -> int:
    floor_number = 0
    position = 1
    for floor in floors:
        floor_number = floor_number + 1  if floor == "("  else floor_number - 1
        if floor_number < 0:
            break
        position += 1
    return position
