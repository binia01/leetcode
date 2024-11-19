class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        summ = 0
        max_sum = 0
        count = {}
        
        for r in range(n):

            count[nums[r]] = count.get(nums[r], 0 )+1
            summ += nums[r]

            while len(count) < r-l +1 or r-l+1 > k:
                count[nums[l]]-= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                summ -=nums[l]
                l+=1

            if r - l + 1 == k:
                max_sum = max(max_sum, summ)

        return max_sum