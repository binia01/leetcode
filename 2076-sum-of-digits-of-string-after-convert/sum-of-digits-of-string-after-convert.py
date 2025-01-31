class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ls = list(s)
        for i in range(len(ls)):
            ls[i] = ord(ls[i]) - 96
        for i in range(len(ls)):
            ls[i] = sum(map(int, list(str(ls[i]))))
        
        _sum = sum(ls)
        def evaluate(_sum):
            _sum = map(int, list(str(_sum)))
            return sum(_sum)
        while k != 1:
           _sum = evaluate(_sum)
           k-=1
        return _sum

            

