class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n &(n-1)) == 0 and (n & 0xAAAAAAAA) == 0
        if n == 1:
            return True
        if n % 4 != 0:
            return False
        else:
            return n > 0 and self.isPowerOfFour(n//4) == 1


        