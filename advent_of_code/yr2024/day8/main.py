import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        return lines


def part1(): ...


def part2(): ...


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 8")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
