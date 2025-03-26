class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) > 12:
            return ans

        def backtrack(i, dots, curIp):
            if dots == 4 and i == len(s):
                ans.append(curIp[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != "0"):
                    backtrack(j+1, dots + 1, curIp + s[i:j+1] + ".")
        backtrack(0, 0, "")
        return ans
                     

        