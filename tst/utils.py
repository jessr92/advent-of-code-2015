def read_all_of_file(filename: str) -> list[str]:
    file = open(filename, "r")
    lines = []
    for line in file:
        lines.append(line)
    return lines
