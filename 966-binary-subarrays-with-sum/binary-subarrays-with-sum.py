class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = {0:1}
        total = 0
        count = 0

        for num in nums:
            total += num
            if total - goal in counter:
                count += counter[total-goal]
            counter[total] = counter.get(total,0) + 1
        return count


        