class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        idx = 0
        for i in range(len(nums)):
            if nums[i] > k:
                idx = i
                break
        ans = 0
        while len(nums) >= 2:
            if nums[0] < k:
                ans+=1
                res1 = heapq.heappop(nums)
                res2 = heapq.heappop(nums)
                new = min(res1, res2)*2 + max(res1, res2)
                heapq.heappush(nums, new)
            else:
                break
        return ans
            


        