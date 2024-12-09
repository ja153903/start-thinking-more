import os
from typing import TypedDict

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip()


def part1():
    filemap = parse_input()
    id = -1

    repr: list[int | None] = []

    for i, ch in enumerate(filemap):
        if i % 2 == 0:
            id += 1

        value_to_add = id if i % 2 == 0 else None

        for _ in range(int(ch)):
            repr.append(value_to_add)

    i, j = 0, len(repr) - 1

    while i < j:
        if repr[i] is not None:
            i += 1
        elif repr[j] is None:
            j -= 1
        else:
            repr[i], repr[j] = repr[j], repr[i]
            i += 1
            j -= 1

    res = 0
    for i, value in enumerate(repr):
        if value is not None:
            res += value * i

    return res


class ChunkMetadata(TypedDict):
    id: int | None
    start: int
    length: int


def part2():
    filemap = parse_input()
    id = -1
    index = 0

    chunks: list[ChunkMetadata] = []
    free_chunks: list[ChunkMetadata] = []

    for i, ch in enumerate(filemap):
        if i % 2 == 0:
            id += 1
            chunks.append({"id": id, "start": index, "length": int(ch)})
        else:
            free_chunks.append({"id": None, "start": index, "length": int(ch)})

        index += int(ch)

    for chunk in reversed(chunks):
        for free_chunk in free_chunks:
            # we don't want to move the chunk if its already leftmost
            if free_chunk["start"] >= chunk["start"]:
                break

            if free_chunk["length"] >= chunk["length"]:
                chunk["start"] = free_chunk["start"]
                free_chunk["start"] += chunk["length"]
                free_chunk["length"] -= chunk["length"]
                break

    chunks.sort(key=lambda x: x["start"])

    res = 0

    for chunk in chunks:
        for i in range(chunk["length"]):
            if chunk["id"] is not None:
                res += (i + chunk["start"]) * chunk["id"]

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 9")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
