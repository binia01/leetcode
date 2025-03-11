class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n-1)
        x = factorial(n)
        count = 0
        while n > 0:
            dig = x % 10
            x //= 10
            if dig == 0:
                count +=1
            else:
                break
        return count