class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        col_map = [set() for _ in range(len(matrix))]

        for i in range(len(matrix)):
            rset = set()
            for j in range(len(matrix)):
                rset.add(matrix[i][j])
                col_map[j].add(matrix[i][j])
            if len(rset) != len(matrix):
                return False

        for col in col_map:
            if len(col) != len(matrix):
                return False

        return True
