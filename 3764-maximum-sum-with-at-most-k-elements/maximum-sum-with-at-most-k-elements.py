class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        min_heap = []
        for nums, limit in zip(grid, limits):
            nums.sort()
            for _ in range(limit):
                heappush(min_heap, nums.pop())
                if len(min_heap) > k:
                    heappop(min_heap)
        return sum(min_heap)

        