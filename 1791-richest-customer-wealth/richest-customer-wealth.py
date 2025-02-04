class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        for num in accounts:
            ans.append(sum(num))
        return max(ans)
        