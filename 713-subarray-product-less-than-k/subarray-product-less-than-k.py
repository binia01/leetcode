class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = 0
        r = 0
        prod = 1
        count = 0
        while r < len(nums):
            prod *=nums[r]
            while prod >= k:
                prod //= nums[l]
                l +=1
            count += 1 + (r - l) 
            r+=1
        return count
        