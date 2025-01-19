class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # sudoku is valid if there are no repeated numbers
        # on the row, col, or within the sub-boxes
        seen = set()

        for row in range(9):
            for col in range(9):
                if (val := board[row][col]) != ".":
                    row_hash = f"r {row} = {val}"
                    col_hash = f"c {col} = {val}"
                    sub_box_hash = f"b {row // 3}, {col // 3} = {val}"

                    if any(h in seen for h in (row_hash, col_hash, sub_box_hash)):
                        return False

                    seen.add(row_hash)
                    seen.add(col_hash)
                    seen.add(sub_box_hash)

        return True
