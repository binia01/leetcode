class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = set(Counter(s).values())
        return len(count) == 1