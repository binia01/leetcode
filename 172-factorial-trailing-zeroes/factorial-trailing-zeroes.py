class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else self.trailingZeroes(n//5) + n//5