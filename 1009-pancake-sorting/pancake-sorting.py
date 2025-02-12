class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            i = 0
            while i < k//2:
                arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
                i+=1
            # return arr
            
        ans = [] 
        val = len(arr)
        while val > 0:
            idx = arr.index(val)
            if idx != val -1:
                if idx != 0:
                    ans.append(idx+1)
                    flip(arr, idx + 1)
                ans.append(val)
                flip(arr, val)
            val -=1
        return ans
            

