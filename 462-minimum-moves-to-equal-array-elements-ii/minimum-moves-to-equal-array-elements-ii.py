class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2 
        total = 0
        for i in range(len(nums)):
            total += (abs(nums[i]- nums[n]))
        return total
            