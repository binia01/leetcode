class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans , sol = [], []

        def backtrack(i):
            if len(sol) == len(nums[0]):
                ans.append("".join(sol[:]))
                return

            for i in range(2):
                sol.append(str(i))
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        res = [a for a in ans if a not in nums]
        return res[0]

        