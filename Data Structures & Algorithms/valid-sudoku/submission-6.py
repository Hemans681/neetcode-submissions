class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == '.':
                    continue
                # col_str=f'{val} in row {c}' 
                # row_str=f'{val} in col {r}'
                # box_str=f'{val} in {r//3}-{c//3}'
                col_str = (val, "row", r)
                row_str = (val, "col", c)
                box_str = (val, "row", r//3, c//3)
                if row_str in seen or col_str in seen or box_str in seen:
                    return False
                else:
                    seen.add(col_str)
                    seen.add(row_str)
                    seen.add(box_str)
        return True
