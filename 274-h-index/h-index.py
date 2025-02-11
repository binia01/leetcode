class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 0
        citations.sort()
        for i, num in enumerate(citations):
            if num >= len(citations) - i:
                count = max(len(citations) - i, count)
                return count
        return count


        
        