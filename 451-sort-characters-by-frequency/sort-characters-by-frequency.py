from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        sorted_char = sorted(count.keys(), key = lambda x: (-count[x], s.index(x)))

        result = ''.join([char * count[char] for char in sorted_char])
        
        return result


        