from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        d = SortedList()
        l = 0
        ans = 0
        for r in range(len(nums)):
            d.add(nums[r])
            while d[-1] - d[0] > limit:
                d.remove(nums[l])
                l+=1
            ans = max(ans, r-l+1)
        return ans

        