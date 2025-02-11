class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in ans:
                ans[sorted_nums[i]] = i
        print(ans)

        return [ans[key] for key in nums]
        

        