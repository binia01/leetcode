class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = {}
        res = set()
        for num in nums:
            cnt[num] = cnt.get(num,0) + 1
            if cnt[num] > n // 3:
                res.add(num)
        return list(res)
       
        