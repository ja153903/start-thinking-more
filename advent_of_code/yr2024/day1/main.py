import os
from collections import Counter

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def get_clean_data() -> tuple[list[int], list[int]]:
    with open(PATH_TO_FILE, "r") as f:
        data = f.readlines()
        lv, rv = [], []
        for line in data:
            l, r = line.strip().split()
            lv.append(int(l))
            rv.append(int(r))

        lv.sort()
        rv.sort()

        return lv, rv


def part1() -> int:
    lv, rv = get_clean_data()
    return sum(abs(l - r) for l, r in zip(lv, rv))


def part2() -> int:
    lv, rv = get_clean_data()
    r_map = Counter(rv)
    return sum(l * r_map[l] for l in lv)


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 1")
    print(f"Part 1 -> {part1()}")
    print(f"Part 2 -> {part2()}")
