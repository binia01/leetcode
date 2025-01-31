class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = nums[i]
            elif nums[i] > 0:
                var = i + nums[i] if i + nums[i] < len(nums) else (i + nums[i]) - len(nums)
                result[i] = nums[var % len(nums)]
            else:
                var = i + nums[i] if i + nums[i] >= 0 else len(nums)+ i + nums[i]
                result[i] = nums[var % len(nums)]
        return result      