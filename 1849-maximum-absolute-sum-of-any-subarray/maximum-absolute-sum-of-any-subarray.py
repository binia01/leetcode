class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        ans = 0
        for num in nums:
            max_sum = max(max_sum, 0) + num
            min_sum = min(min_sum,0) + num
            ans = max(ans, max_sum, abs(min_sum))
        return ans