class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        summ = 0
        for i in range(len(columnTitle)-1,-1, -1):
            summ += (26 **(len(columnTitle) - i - 1)) * (ord(columnTitle[i])-64)
        return summ

        