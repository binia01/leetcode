class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
            else:
                ans += ones
        return ans
        