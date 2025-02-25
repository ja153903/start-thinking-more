import os
import re
from collections import defaultdict


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"

REINDEER_REGEX = (
    r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
)


class State:
    name: str
    dist_travelled: int
    cooldown_timer: int
    tick: int
    delta: int
    duration: int
    rest: int

    def __init__(self, name: str, delta: int, duration: int, rest: int) -> None:
        self.name = name
        self.delta = delta
        self.duration = duration
        self.rest = rest

        self.dist_travelled = 0
        self.cooldown_timer = 0
        self.tick = 0

    def update(self):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1
            return

        self.tick += 1
        self.dist_travelled += self.delta

        if self.tick == self.duration:
            self.tick = 0
            self.cooldown_timer = self.rest


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        lines = f.read().strip().splitlines()
        lines = [
            [part for part in re.split(REINDEER_REGEX, line) if part] for line in lines
        ]
        states = []

        for line in lines:
            name, delta, duration, rest = line
            states.append(State(name, int(delta), int(duration), int(rest)))

        return states


def part1():
    states = parse_input()

    for _ in range(2503):
        for state in states:
            state.update()

    return max(states, key=lambda state: state.dist_travelled).dist_travelled


def part2():
    states = parse_input()

    points_by_name = defaultdict(int)

    for _ in range(2503):
        for state in states:
            state.update()

        winner = max(states, key=lambda state: state.dist_travelled).name
        points_by_name[winner] += 1

    return max(points_by_name.values())


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 14")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
