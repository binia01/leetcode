class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        else:
            return n > 0 and self.isPowerOfThree(n//3) == 1
        