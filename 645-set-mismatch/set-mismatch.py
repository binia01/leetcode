class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            while nums[idx] - 1 != idx:
                if nums[idx] == nums[nums[idx] -1]:
                    break
                nums[nums[idx] - 1] , nums[idx] = nums[idx], nums[nums[idx] - 1]
        ans = []
        for idx in range(len(nums)):
            if nums[idx] - 1!= idx:
                ans.extend([nums[idx], idx+1])
        return ans