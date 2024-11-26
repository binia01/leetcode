import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        stop = math.sqrt(c)

        a,b = 0, int(stop)

        while a<=b:
            comp = a*a + b*b
            if comp == c:
                return True
            elif comp > c:
                b-=1
            else:
                a+=1
        return False

        