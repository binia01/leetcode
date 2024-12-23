class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        pref = {0:-1}

        for i, num in enumerate(nums):
            prefix += num
            if k != 0:
                prefix %=k
            if prefix in pref:
                if i - pref[prefix] >=2:
                    return True
            else:
                pref[prefix] = i
        return False
        