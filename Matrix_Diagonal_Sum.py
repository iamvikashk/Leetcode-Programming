class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumof = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i==j:
                    sumof.append(mat[i][j])
            if i!=len(mat)-i-1:
                sumof.append(mat[i][len(mat)-i-1])

        return sum(sumof)