class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref_sum = 0
        max_num = float("-inf")
        for i in range(len(nums)):
            pref_sum += nums[i] 
            max_num = max(max_num, pref_sum)              
            if pref_sum < 0:   
                pref_sum = 0
                
        return max_num
        