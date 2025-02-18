class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2 if len(nums)%2 != 0 else ((len(nums)//2)+((len(nums)//2)+1))//2
        total = 0
        for i in range(len(nums)):
            total += (abs(nums[i]- nums[n]))
        return total
            