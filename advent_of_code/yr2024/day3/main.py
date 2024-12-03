import os
import re

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        input = f.read()
        results = re.findall(r"mul\((?P<l>\d+),(?P<r>\d+)\)", input)
        return [(int(l), int(r)) for l, r in results]


def part1():
    data = parse_input()
    return sum(l * r for l, r in data)


def parse_input_pt2():
    with open(PATH_TO_FILE, "r") as f:
        input = f.read()
        return re.findall(r"(mul\((?P<l>\d+),(?P<r>\d+)\)|don\'t\(\)|do\(\))", input)


def part2():
    data = parse_input_pt2()
    res = 0

    add = True

    for patt, l, r in data:
        if patt.startswith("mul") and add:
            res += int(l) * int(r)
        elif patt.startswith("don't"):
            add = False
        elif patt.startswith("do"):
            add = True

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 3")
    print(f"Part 1 -> {part1()}")
    print(f"Part 2 -> {part2()}")
