class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 0, max(candies)

        while l < r:
            mid = (l+r+1) // 2
            cnt = sum(candy//mid for candy in candies)

            if cnt >= k:
                l = mid
            else:
                r = mid - 1
        return l
        