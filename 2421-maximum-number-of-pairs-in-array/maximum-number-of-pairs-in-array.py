class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = 0
        left = 0
        for val in count.values():
            ans +=(val//2)
            left += (val%2)
        return [ans, left]