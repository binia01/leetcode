class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = (1/x)
        if n==0:
            return 1
        half = self.myPow(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x
        