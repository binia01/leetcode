class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        bs = []
        for key in s:
            if s[key] > 1:
                bs.append(key)
        return bs 

        