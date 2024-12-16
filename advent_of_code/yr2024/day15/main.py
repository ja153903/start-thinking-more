import os


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def pretty_print(grid: list[list[str]]):
    for row in grid:
        print(" ".join(row))


def parse_input(extend: bool = False):
    with open(PATH_TO_FILE, "r") as f:
        grid, instructions = f.read().strip().split("\n\n")

        _instructions = []
        for line in instructions.split("\n"):
            for char in line:
                _instructions.append(char)

        if not extend:
            _grid = [list(line) for line in grid.split("\n")]
        else:
            _grid = []

            for line in grid.split("\n"):
                level = []
                for ch in line:
                    match ch:
                        case "#":
                            level.append("#")
                            level.append("#")
                        case "O":
                            level.append("[")
                            level.append("]")
                        case "@":
                            level.append("@")
                            level.append(".")
                        case ".":
                            level.append(".")
                            level.append(".")
                        case _:
                            raise ValueError("This should never be the case")
                _grid.append(level)

        return (_grid, _instructions)


def find_starting_position(grid: list[list[str]]) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return (i, j)

    raise ValueError("For some reason we could not find the @ sign")


def get_instruction_delta(instruction: str) -> tuple[int, int]:
    match instruction:
        case "^":
            return (-1, 0)
        case "v":
            return (1, 0)
        case "<":
            return (0, -1)
        case _:
            return (0, 1)


def in_bounds(grid: list[list[str]], row: int, col: int):
    return 0 <= row <= len(grid) - 1 and 0 <= col <= len(grid[0]) - 1


def evaluate_instruction(grid: list[list[str]], row: int, col: int, instruction: str):
    dr, dc = get_instruction_delta(instruction)
    nr, nc = row + dr, col + dc

    if not in_bounds(grid, nr, nc) or grid[nr][nc] == "#":
        return None

    if grid[nr][nc] == ".":
        grid[nr][nc], grid[row][col] = grid[row][col], grid[nr][nc]
        return (row, col)

    tuple_to_swap = evaluate_instruction(grid, nr, nc, instruction)

    if tuple_to_swap:
        fr, fc = tuple_to_swap
        grid[fr][fc], grid[row][col] = grid[row][col], grid[fr][fc]
        return (row, col)

    return None


def part1():
    grid, instructions = parse_input()

    for instruction in instructions:
        r, c = find_starting_position(grid)
        _ = evaluate_instruction(grid, r, c, instruction)

    res = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                res += 100 * i + j

    return res


def is_path_clear_for_vertical_move(
    grid: list[list[str]], row: int, col: int, instruction: str
):
    dr, dc = get_instruction_delta(instruction)
    nr, nc = row + dr, col + dc

    if not in_bounds(grid, nr, nc) or grid[nr][nc] == "#":
        return False

    if grid[nr][nc] == ".":
        return True

    offset_r, offset_c = [nr, nc - 1] if grid[nr][nc] == "]" else [nr, nc + 1]

    return is_path_clear_for_vertical_move(
        grid, offset_r, offset_c, instruction
    ) and is_path_clear_for_vertical_move(grid, nr, nc, instruction)


def _vertical_eval_with_expanded_grid(
    grid: list[list[str]], row: int, col: int, instruction: str
):
    dr, dc = get_instruction_delta(instruction)
    nr, nc = row + dr, col + dc

    if not in_bounds(grid, nr, nc) or grid[nr][nc] == "#":
        return None

    if grid[nr][nc] == ".":
        grid[nr][nc], grid[row][col] = grid[row][col], grid[nr][nc]
        return (row, col)

    offset_r, offset_c = [nr, nc - 1] if grid[nr][nc] == "]" else [nr, nc + 1]
    tuple_to_swap = _vertical_eval_with_expanded_grid(grid, nr, nc, instruction)
    another_tuple_to_swap = _vertical_eval_with_expanded_grid(
        grid, offset_r, offset_c, instruction
    )

    if tuple_to_swap and another_tuple_to_swap:
        fr, fc = tuple_to_swap
        grid[fr][fc], grid[row][col] = grid[row][col], grid[fr][fc]
        return (row, col)

    return None


def evaluate_instruction_with_expanded_grid(
    grid: list[list[str]], row: int, col: int, instruction: str
):
    dr, dc = get_instruction_delta(instruction)
    nr, nc = row + dr, col + dc

    if not in_bounds(grid, nr, nc) or grid[nr][nc] == "#":
        return None

    if grid[nr][nc] == ".":
        grid[nr][nc], grid[row][col] = grid[row][col], grid[nr][nc]
        return (row, col)

    match instruction:
        case "<" | ">":
            tuple_to_swap = evaluate_instruction_with_expanded_grid(
                grid, nr, nc, instruction
            )
            if tuple_to_swap:
                fr, fc = tuple_to_swap
                grid[row][col], grid[fr][fc] = grid[fr][fc], grid[row][col]
                return (row, col)

            return None
        case _:
            offset = 1 if grid[nr][nc] == "[" else -1
            if not is_path_clear_for_vertical_move(
                grid, nr, nc, instruction
            ) or not is_path_clear_for_vertical_move(
                grid, nr, nc + offset, instruction
            ):
                return None

            tuple_to_swap = _vertical_eval_with_expanded_grid(grid, nr, nc, instruction)
            another_tuple_to_swap = _vertical_eval_with_expanded_grid(
                grid, nr, nc + offset, instruction
            )

            if tuple_to_swap and another_tuple_to_swap:
                fr, fc = tuple_to_swap
                grid[row][col], grid[fr][fc] = grid[fr][fc], grid[row][col]

                return (row, col)

            return None


def part2():
    grid, instructions = parse_input(extend=True)

    for instruction in instructions:
        r, c = find_starting_position(grid)
        _ = evaluate_instruction_with_expanded_grid(grid, r, c, instruction)

    res = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                res += 100 * i + j

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 15")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
