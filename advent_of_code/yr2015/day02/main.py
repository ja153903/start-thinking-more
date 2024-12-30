import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE) as f:
        return [
            [int(x) for x in line.split("x")] for line in f.read().strip().splitlines()
        ]


def part1():
    res = 0
    dimensions = parse_input()

    for l, w, h in dimensions:  # noqa: E741
        res += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, l * h, w * h)

    return res


def part2():
    res = 0
    dimensions = parse_input()

    for l, w, h in dimensions:  # noqa: E741
        res += l * w * h + min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h)

    return res


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 2")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
