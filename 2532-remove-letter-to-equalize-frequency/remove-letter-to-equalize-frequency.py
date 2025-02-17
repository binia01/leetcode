class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        for c in word:
            count[c] -= 1
            seen = set(v for v in count.values() if v)
            if len(seen) == 1:
                return True
            count[c] += 1
        return False
        