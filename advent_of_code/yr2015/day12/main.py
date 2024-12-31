import os
import json
from typing import Any


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as file:
        return file.read().strip()


def recurse_further(data: dict[Any, Any] | list[Any] | int | str) -> int:
    if isinstance(data, int):
        return data

    if isinstance(data, str):
        return 0

    if isinstance(data, list):
        return sum(recurse_further(item) for item in data)

    return sum(recurse_further(value) for value in data.values())


def part1():
    data = json.loads(parse_input())
    return recurse_further(data)


def recurse_further_with_no_red(data: dict[Any, Any] | list[Any] | int | str) -> int:
    if isinstance(data, int):
        return data

    if isinstance(data, str):
        return 0

    if isinstance(data, list):
        return sum(recurse_further_with_no_red(item) for item in data)

    if "red" in data.values():
        return 0

    return sum(recurse_further_with_no_red(value) for value in data.values())


def part2():
    data = json.loads(parse_input())
    return recurse_further_with_no_red(data)


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 12")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
