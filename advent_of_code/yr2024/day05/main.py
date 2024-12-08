from typing import TypedDict
from collections import defaultdict
import os


class Input(TypedDict):
    prerequisites: defaultdict[str, set[str]]
    updates: list[list[str]]


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input() -> Input:
    with open(PATH_TO_FILE, "r") as f:
        data = f.read().strip()
        ordering, updates = data.split("\n\n")

        ordering = [o.strip().split("|") for o in ordering.split("\n")]

        prerequisites: defaultdict[str, set[str]] = defaultdict(set)

        for u, v in ordering:
            prerequisites[v].add(u)

        return {
            "prerequisites": prerequisites,
            "updates": [u.strip().split(",") for u in updates.split("\n")],
        }


def part1():
    params = parse_input()
    prerequisites = params["prerequisites"]
    updates = params["updates"]

    res = 0

    for update in updates:
        is_legal_update = True
        for i in range(1, len(update)):
            if update[i - 1] not in prerequisites[update[i]]:
                is_legal_update = False
                break

        if is_legal_update:
            res += int(update[len(update) // 2])

    return res


def sort_update(update: list[str], prerequisites: defaultdict[str, set[str]]):
    for i in range(1, len(update)):
        j = i

        while j > 0 and update[j] in prerequisites[update[j - 1]]:
            update[j], update[j - 1] = update[j - 1], update[j]
            j -= 1


def part2():
    params = parse_input()
    prerequisites = params["prerequisites"]
    updates = params["updates"]

    res = 0

    for update in updates:
        is_legal_update = True

        for i in range(1, len(update)):
            if update[i - 1] not in prerequisites[update[i]]:
                is_legal_update = False
                break

        if not is_legal_update:
            sort_update(update, prerequisites)
            res += int(update[len(update) // 2])

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 5")

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
