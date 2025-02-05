class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for key, val in count.items():
            if count[key] > 1:
                ans.append(key)
        return ans
       