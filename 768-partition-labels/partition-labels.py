class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = {}
        for i, c in enumerate(s):
            occur[c] = i
        ans = []
        mx = 0
        l = 0
        for r in range(len(s)):
            mx = max(mx, occur[s[r]])
            if r == mx:
                ans.append(r-l+1)
                l = r + 1
        return ans

        