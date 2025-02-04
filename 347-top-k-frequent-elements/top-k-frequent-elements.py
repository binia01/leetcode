from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        count = sorted(list(s.items()), key = lambda x: x[1], reverse = True)
        t = []
        for i in range(k):
            t.append(count[i][0])
        return t




           
            


        