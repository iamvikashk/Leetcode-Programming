#1572
def diagonalSum(mat):
    final_list = []
    for i in range(len(mat)):
        final_list.append(mat[i][i])
    k = 0
    for j in range(len(mat)-1, -1, -1):
        final_list.append(mat[k][j])
        k+=1
    if len(mat)%2==0:
        out = sum(final_list)
    else:
        ind = len(mat)//2
        out = sum(final_list) - final_list[ind]
    return out