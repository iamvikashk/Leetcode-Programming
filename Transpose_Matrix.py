"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3], [4, 5, 6]]


class Solution:
    def transpose(self, matrix):
        col = matrix[0]
        final = []
        for i in range(len(col)):
            new = []
            for j in range(len(matrix)):
                new.append(matrix[j][i])
            final.append(new)

        return final


sol = Solution()
print(sol.transpose(matrix))
