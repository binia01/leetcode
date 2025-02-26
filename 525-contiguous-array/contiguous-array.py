class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = {0:-1}
        maxlen = 0 
        count = 0
        for i in range(len(nums)):
            count += (1 if nums[i] == 1 else -1)
            if count in counter:
                maxlen = max(maxlen, i - counter[count])
            else:
                counter[count] = i
        return maxlen
              
        