class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                ans += (dct[nums[i] * nums[j]]) * 8
                dct[nums[i] * nums[j]] += 1  
        return ans
        # # for key in dct:
        # #     if dct[key] % 8 == 0:
        # #         ans+= dct[key]
        # return ans

        