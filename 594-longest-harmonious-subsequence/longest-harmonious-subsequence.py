class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        n = len(nums)
        ans = 0
        for r in range(n):
            while nums[r] - nums[l] > 1:
                l+=1
            if nums[r] - nums[l] == 1:
                ans = max(ans, r-l+1)
        return ans
        