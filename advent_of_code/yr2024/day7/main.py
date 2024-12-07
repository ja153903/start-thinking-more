import os
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
                {"test_value": int(res), "numbers": [int(x) for x in rest.split(" ")]}
            )

        return result


def backtrack(current: int, numbers: list[int], index: int, target: int) -> bool:
    if index == len(numbers):
        return current == target

    return backtrack(current + numbers[index], numbers, index + 1, target) or backtrack(
        current * numbers[index], numbers, index + 1, target
    )


def part1():
    equations = parse_input()

    res = 0
    for equation in equations:
        if backtrack(0, equation["numbers"], 0, equation["test_value"]):
            res += equation["test_value"]

    return res


def backtrack_with_concat(
    current: int, numbers: list[int], index: int, target: int
) -> bool:
    if index == len(numbers):
        return current == target

    return (
        backtrack_with_concat(current + numbers[index], numbers, index + 1, target)
        or backtrack_with_concat(current * numbers[index], numbers, index + 1, target)
        or backtrack_with_concat(
            int(f"{current}{numbers[index]}"), numbers, index + 1, target
        )
    )


def part2():
    equations = parse_input()

    res = 0
    for equation in equations:
        if backtrack_with_concat(0, equation["numbers"], 0, equation["test_value"]):
            res += equation["test_value"]

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 7")

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
