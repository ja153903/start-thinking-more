import os
from functools import lru_cache
from typing import TypedDict


class Equation(TypedDict):
    test_value: int
    numbers: list[int]


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input() -> list[Equation]:
    with open(PATH_TO_FILE, "r") as f:
        lines = [line.strip() for line in f.readlines()]

        result: list[Equation] = []

        for line in lines:
            res, rest = line.split(": ")

            result.append(
                {"test_value": int(res), "numbers": [int(x) for x in rest.split()]}
            )

        return result


def backtrack(numbers: list[int], target: int) -> bool:
    @lru_cache
    def _rec(current: int, index: int) -> bool:
        if index == len(numbers):
            return current == target

        return _rec(current + numbers[index], index + 1) or _rec(
            current * numbers[index], index + 1
        )

    return _rec(0, 0)


def part1():
    equations = parse_input()

    res = 0
    for equation in equations:
        if backtrack(equation["numbers"], equation["test_value"]):
            res += equation["test_value"]

    return res


def backtrack_with_concat(numbers: list[int], target: int) -> bool:
    @lru_cache
    def _rec(current: int, index: int) -> bool:
        if index == len(numbers):
            return current == target

        return (
            _rec(current + numbers[index], index + 1)
            or _rec(current * numbers[index], index + 1)
            or _rec(int(f"{current}{numbers[index]}"), index + 1)
        )

    return _rec(0, 0)


def part2():
    equations = parse_input()

    res = 0
    for equation in equations:
        if backtrack_with_concat(equation["numbers"], equation["test_value"]):
            res += equation["test_value"]

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 7")

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
