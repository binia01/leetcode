class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        count = 0
        for i in range(n):
            if citations[i] >= n - i:
                count = max(count, n - i)
        return count
        
        