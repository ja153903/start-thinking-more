from functools import cache
import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        data = f.read().strip()
        patterns, designs = data.split("\n\n")
        return patterns.split(", "), designs.split("\n")


# NOTE: Inspired by the Word Break LeetCode problem
def can_create_design(design: str, uniq: set[str]):
    dp = [False for _ in range(len(design) + 1)]
    dp[0] = True

    for i in range(1, len(design) + 1):
        for j in range(i):
            if dp[j] and design[j:i] in uniq:
                dp[i] = True
                break

    return dp[-1]


def part1():
    patterns, designs = parse_input()
    patterns = set(patterns)

    res = 0

    for design in designs:
        if can_create_design(design, patterns):
            res += 1

    return res


def get_number_of_possible_ways_to_create_design(
    design: str, patterns: list[str]
) -> int:
    @cache
    def inner(start: int, path: str):
        if start > len(design):
            return 0

        if start == len(design):
            return 1 if path == design else 0

        res = 0

        for pattern in patterns:
            if start + len(pattern) <= len(design) and design[start:].startswith(
                pattern
            ):
                res += inner(start + len(pattern), f"{path}{pattern}")

        return res

    return inner(0, "")


def part2():
    patterns, designs = parse_input()

    res = 0

    for design in designs:
        res += get_number_of_possible_ways_to_create_design(design, patterns)

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 19")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
