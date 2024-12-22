class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for winsize in range(l, r+1):
            winsum = sum(nums[:winsize])
            if winsum > 0:
                ans = min(winsum, ans)
            for i in range(winsize, len(nums)):
                winsum -= nums[i-winsize]
                winsum += nums[i]
                if winsum > 0:
                    ans = min(winsum, ans)
        return -1 if ans == float('inf') else ans

 
    
        