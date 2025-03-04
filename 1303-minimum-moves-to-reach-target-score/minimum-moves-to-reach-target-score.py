class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1 and maxDoubles:
            ans +=1
            if target % 2 == 1:
                target -= 1
            else:
                maxDoubles -= 1
                target //=2
                
        ans += (target - 1)
        return ans
        