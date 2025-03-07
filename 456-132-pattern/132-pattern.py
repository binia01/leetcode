class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        k = float("-inf")
        for x in nums[::-1]:
            if x < k:
                return True
            while stk and stk[-1] < x:
                k = stk.pop()
            stk.append(x)
        return False