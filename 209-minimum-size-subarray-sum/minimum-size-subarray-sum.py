class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        sum = 0
        min_length = float("inf")

        for end in range(n):
            sum += nums[end]

            while sum >= target:
                leng = end - start + 1
                min_length = min(min_length, leng)
                sum -= nums[start]
                start += 1

            
        return min_length if min_length < float('inf') else 0

        