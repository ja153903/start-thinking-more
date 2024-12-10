import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return [int(x) for x in list(f.read().strip())]


def part1(): ...
def part2(): ...


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 11")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
