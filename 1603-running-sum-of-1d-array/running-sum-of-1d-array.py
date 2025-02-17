class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            ans.append(_sum)
        return ans
        