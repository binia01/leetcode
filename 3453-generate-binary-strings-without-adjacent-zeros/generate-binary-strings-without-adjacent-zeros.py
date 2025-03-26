class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans, sol = [], []
        def backtrack(x):
            if len(sol) == n:
                ans.append("".join(sol[:]))
                return

            for i in range(2):
                if (i == 0 and (x == 0 or sol[x-1] == "1")) or i == 1:
                    sol.append(str(i))
                    backtrack(x+1)
                    sol.pop()
                    
        backtrack(0)
        return ans
            

        