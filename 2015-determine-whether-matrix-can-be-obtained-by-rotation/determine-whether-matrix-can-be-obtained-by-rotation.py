class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if mat == target:
                return True
            mat = [[mat[n-j-1][i] for j in range(n)] for i in range(n)]
        return False            


        
        