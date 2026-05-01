class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        cols_set = [set() for _ in range(9)]
        sub_grid_set = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue

                if value in row_set[row] or value in cols_set[col] or value in sub_grid_set[row//3][col//3]:
                    return False

                row_set[row].add(value)
                cols_set[col].add(value)
                sub_grid_set[row//3][col//3].add(value)

        return True
