class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        n = len(nums)
        res= [0] * (n+1)
        for s,e in requests:
            res[s] +=1
            res[e+1] -=1
        res = sorted(accumulate(res))
        ans =[l*r for l,r in zip(nums, res[1:])]
        return sum(ans)%((10**9) + 7)
        