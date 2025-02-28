class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res = [0] * 1001
        for i,x,y in trips:
            res[x] += i
            if y < 1000:
                res[y] -= i

        return all(numpass <= capacity for numpass in accumulate(res))
        