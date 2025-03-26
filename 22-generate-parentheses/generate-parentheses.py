class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []
        op, cp = 0, 0
        def backtrack(x):
            nonlocal op, cp
            if op + cp == 2 * n:
                ans.append("".join(sol[:]))
                return
            
            if op < n:
                sol.append("(")
                op += 1
                backtrack(x+1)
                op -= 1
                sol.pop()
            if cp < op:
                sol.append(")")
                cp += 1
                backtrack(x+1)
                cp -= 1
                sol.pop()

        backtrack(0)
        return ans
        