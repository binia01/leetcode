class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        arr = [0] * n
        for _, v in edges:
            arr[v] += 1
        return -1 if arr.count(0) != 1 else arr.index(0) 
        
        