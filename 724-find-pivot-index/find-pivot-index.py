class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l,r =0,0
        for i in range(len(nums)):
            r = total - nums[i] - l
            if  l == r:
                return i
            else:
                l += nums[i]
        return -1