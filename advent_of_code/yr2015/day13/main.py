import os
import re
from typing import NamedTuple
from collections import defaultdict

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip().splitlines()


HAPPINESS_REGEX = re.compile(
    r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."
)


class Edge(NamedTuple):
    u: str
    v: str
    w: int


def parse_edge(line: str) -> Edge:
    u, sign, w, v = [part for part in re.split(HAPPINESS_REGEX, line) if part]
    return Edge(u, v, -int(w) if sign == "lose" else int(w))


def part1():
    edges = [parse_edge(line) for line in parse_input()]
    edge_mp = defaultdict(int)  # key => (u, v) and (v, u), value => weight
    g = defaultdict(list)

    for edge in edges:
        g[edge.u].append(edge.v)
        g[edge.v].append(edge.u)
        edge_mp[(edge.u, edge.v)] += edge.w
        edge_mp[(edge.v, edge.u)] += edge.w

    return 0


def part2(): ...


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 13")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
