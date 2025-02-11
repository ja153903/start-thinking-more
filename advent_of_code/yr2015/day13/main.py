from itertools import permutations
import os
import re
from collections import defaultdict

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"

HAPPINESS_REGEX = re.compile(
    r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."
)


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip().splitlines()


def parse_data():
    data = parse_input()
    dd = defaultdict(lambda: defaultdict(int))

    for line in data:
        parts = [part for part in re.split(HAPPINESS_REGEX, line) if part]
        a, wl, n, b = parts
        dd[a][b] = int(n) if wl == "gain" else -int(n)

    return dd


def calculate_happiness(dd, people) -> int:
    happiness = 0
    for i in range(1, len(people)):
        a, b = people[i - 1], people[i]
        happiness += dd[a][b]
        happiness += dd[b][a]

    happiness += dd[people[0]][people[-1]]
    happiness += dd[people[-1]][people[0]]

    return happiness


def part1():
    dd = parse_data()
    people = list(dd.keys())

    return max(
        calculate_happiness(dd, people_perm) for people_perm in permutations(people)
    )


def part2():
    dd = parse_data()
    people = list(dd.keys())

    for person in people:
        dd[person]["me"] = 0
        dd["me"][person] = 0

    people.append("me")

    return max(
        calculate_happiness(dd, people_perm) for people_perm in permutations(people)
    )


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 13")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
