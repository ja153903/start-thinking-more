import os
from collections import Counter

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input() -> tuple[list[int], list[int]]:
    with open(PATH_TO_FILE, "r") as f:
        data = f.readlines()
        lv, rv = [], []
        for line in data:
            left, right = line.strip().split()
            lv.append(int(left))
            rv.append(int(right))

        lv.sort()
        rv.sort()

        return lv, rv


lv, rv = parse_input()


def part1() -> int:
    return sum(abs(left - right) for left, right in zip(lv, rv))


def part2() -> int:
    r_map = Counter(rv)
    return sum(left * r_map[left] for left in lv)


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 1")
    print(f"Part 1 -> {part1()}")
    print(f"Part 2 -> {part2()}")
