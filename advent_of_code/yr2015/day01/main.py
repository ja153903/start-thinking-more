import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip()


def part1():
    data = parse_input()

    res = 0
    for ch in data:
        match ch:
            case "(":
                res += 1
            case ")":
                res -= 1
            case _:
                continue

    return res


def part2():
    data = parse_input()

    level = 0
    for i, ch in enumerate(data):
        match ch:
            case "(":
                level += 1
            case ")":
                level -= 1
            case _:
                continue

        if level < 0:
            return i + 1

    raise ValueError("Santa never enters the basement")


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 01")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
