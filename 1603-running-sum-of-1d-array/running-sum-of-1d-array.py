class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0]
        for i in range(len(nums)):
            ans.append(ans[-1]+nums[i])
        return ans[1:]
        