import os


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip().splitlines()


def get_inmem_repr(line: str) -> int:
    res = 0

    i = 1

    while i < len(line) - 1:
        if line[i] == "\\":
            # this means that we should look ahead
            if line[i + 1] == "x":
                res += 1
                i += 4
            elif line[i + 1] == '"' or line[i + 1] == "\\":
                res += 1
                i += 2
            else:
                raise ValueError("Invalid item that we're trying to iterate over")
        else:
            res += 1
            i += 1

    return res


def part1():
    lines = parse_input()

    res = 0

    for line in lines:
        res += len(line) - get_inmem_repr(line)

    return res


def get_inflated_repr(line: str) -> int:
    res = 0

    for ch in line:
        if ch == '"' or ch == "\\":
            res += 2
        else:
            res += 1

    return 2 + res


def part2():
    lines = parse_input()

    res = 0

    for line in lines:
        res += get_inflated_repr(line) - len(line)

    return res


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 8")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
