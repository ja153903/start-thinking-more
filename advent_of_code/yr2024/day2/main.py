import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input() -> list[list[int]]:
    with open(PATH_TO_FILE, "r") as f:
        data = f.readlines()
        reports: list[list[int]] = []
        for line in data:
            reports.append([int(x) for x in line.split()])

        return reports


def is_mono_increasing(lst: list[int]) -> bool:
    return all(x < y for x, y in zip(lst, lst[1:]))


def is_mono_decreasing(lst: list[int]) -> bool:
    return all(x > y for x, y in zip(lst, lst[1:]))


def is_diff_within_thresh(lst: list[int]) -> bool:
    for i in range(1, len(lst)):
        diff = abs(lst[i] - lst[i - 1])
        if diff < 0 or diff > 3:
            return False
    return True


def validate_report(report: list[int]) -> bool:
    return (
        is_mono_increasing(report) or is_mono_decreasing(report)
    ) and is_diff_within_thresh(report)


def part1() -> int:
    reports = parse_input()
    res = 0

    for report in reports:
        if validate_report(report):
            res += 1

    return res


def part2():
    reports = parse_input()
    res = 0

    for report in reports:
        if validate_report(report):
            res += 1
        else:
            for i in range(len(report)):
                without_i = report[:i] + report[i + 1 :]
                if validate_report(without_i):
                    res += 1
                    break

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 2")
    print(f"Part 1 -> {part1()}")
    print(f"Part 2 -> {part2()}")
