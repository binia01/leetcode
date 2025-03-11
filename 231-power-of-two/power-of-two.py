class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        else:
            return n > 0 and self.isPowerOfTwo(n//2) == 1
        