from typing import List, Optional


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        48. Rotate Image
        Do not return anything, modify matrix in-place instead.
        """
        # 1 reverse the list
        matrix.reverse()
        # 2 get its transpose with swapping
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def spiralOrder(self, matrix):
        """
        54. Spiral Matrix
        """
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])  # recursive method
        res = []
        while matrix:
            # res.extend(matrix.pop(0))
            res += matrix.pop(0)
            matrix = [*zip(*matrix)][::-1]
        return res

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        73. Set Matrix Zeroes
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        for r in rows:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0

        for c in columns:
            for i in range(len(matrix)):
                matrix[i][c] = 0

    def isHappy(self, n: int) -> bool:
        """
        202. Happy Number
        """
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sum((int(i) ** 2 for i in str(n)))  # calculating digits squared
            if n == 1:
                return True
        return False


s = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.rotate(matrix)
print('48. Rotate Image:', matrix)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('54. Spiral Matrix:', s.spiralOrder(m))

m1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s.setZeroes(m1)
print('73. Set Matrix Zeroes:', m1)

n = 19
# n = 2
print('202. Happy Number:', s.isHappy(n))
