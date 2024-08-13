class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                wmp_idx = "w" + str(j) + str(board[i][j])
                hmp_idx = "h" + str(i) + str(board[i][j])
                bmp_idx = "b" + str(i // 3) + str(j // 3) + str(board[i][j])

                if wmp_idx in m or hmp_idx in m or bmp_idx in m:
                    return False
                else:
                    m[wmp_idx] = 1
                    m[hmp_idx] = 1
                    m[bmp_idx] = 1

        return True
