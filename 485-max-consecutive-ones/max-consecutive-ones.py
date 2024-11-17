class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ctr , max_num = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ctr +=1
            else:
                ctr = 0
            max_num = max(ctr, max_num)
        return max_num

        