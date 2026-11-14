class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        s=0
        d1,d2=0,0
        for i in range(len(mat)):
            d1+=mat[i][i]
            d2+=mat[i][len(mat)-1-i]
        n=len(mat)
        if n%2!=0:
            d2-=mat[n//2][n//2]
        return d1+d2    
