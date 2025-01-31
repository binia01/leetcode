class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            temp = []
            tnum = num
            while tnum != 0:
                temp.insert(0, tnum%10)
                tnum //= 10            
            ans.extend(temp)
        return ans
        