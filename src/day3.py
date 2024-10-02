from collections import Counter
from operator import concat


def part_1(directions: str) -> int:
    deliveries: list[tuple[int, int]] = []
    position: tuple[int, int] = (0, 0)
    deliveries.append(position)
    for direction in directions:
        position = update_position(direction, position)
        deliveries.append(position)
    return len(set(deliveries))


def update_position(direction, position):
    if direction == '^':
        position = (position[0], position[1] + 1)
    elif direction == '>':
        position = (position[0] + 1, position[1])
    elif direction == '<':
        position = (position[0] - 1, position[1])
    else:
        position = (position[0], position[1] - 1)
    return position


def part_2(directions: str) -> int:
    deliveries: list[tuple[int, int]] = []

    santa_position: tuple[int, int] = (0, 0)
    deliveries.append(santa_position)

    robot_position: tuple[int, int] = (0, 0)
    deliveries.append(robot_position)

    santa_move = True
    for direction in directions:
        if santa_move:
            santa_position = update_position(direction, santa_position)
            deliveries.append(santa_position)
        else:
            robot_position = update_position(direction, robot_position)
            deliveries.append(robot_position)
        santa_move = not santa_move
    return len(set(deliveries))
