class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i+=1
            i+=1
        