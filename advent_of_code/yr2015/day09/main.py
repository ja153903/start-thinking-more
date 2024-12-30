import os
import re
from collections import defaultdict, deque
from typing import NamedTuple


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip().splitlines()


EDGE_REGEX = re.compile(r"(\w+) to (\w+) = (\d+)")


class Edge(NamedTuple):
    u: str
    v: str
    w: int


def parse_edge(line: str) -> Edge:
    u, v, w = [part for part in re.split(EDGE_REGEX, line) if part]
    return Edge(u, v, int(w))


def part1():
    # we want to make sure that we visit all possible nodes
    # we want to find the shortest path to do so
    edges = [parse_edge(line) for line in parse_input()]
    weight = {}
    g = defaultdict(list)

    for u, v, w in edges:
        g[u].append(v)
        g[v].append(u)

        weight[(u, v)] = w
        weight[(v, u)] = w

    res = float("inf")

    for node in g.keys():
        # use each one as a starting node
        queue = deque()
        queue.append((node, 0, set()))

        while queue:
            n, w, visited = queue.popleft()

            visited.add(n)

            if len(visited) == len(g.keys()):
                res = min(res, w)
                continue

            for child in g[n]:
                if child not in visited:
                    queue.append((child, w + weight[(n, child)], visited.copy()))

    return res


def part2():
    # we want to make sure that we visit all possible nodes
    # we want to find the shortest path to do so
    edges = [parse_edge(line) for line in parse_input()]
    weight = {}
    g = defaultdict(list)

    for u, v, w in edges:
        g[u].append(v)
        g[v].append(u)

        weight[(u, v)] = w
        weight[(v, u)] = w

    res = -float("inf")

    for node in g.keys():
        # use each one as a starting node
        queue = deque()
        queue.append((node, 0, set()))

        while queue:
            n, w, visited = queue.popleft()

            visited.add(n)

            if len(visited) == len(g.keys()):
                res = max(res, w)
                continue

            for child in g[n]:
                if child not in visited:
                    queue.append((child, w + weight[(n, child)], visited.copy()))

    return res


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 9")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
