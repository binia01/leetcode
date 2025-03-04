class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcount = 0
        rcount = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "L":
                lcount += 1
            elif s[i] == "R":
                rcount += 1
            if lcount == rcount:
                ans+=1
                lcount = 0
                rcount = 0 

        return ans

        