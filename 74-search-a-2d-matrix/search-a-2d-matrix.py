class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in matrix:
            for j in i:
                res.append(j)

        return True if target in res else False
        
        