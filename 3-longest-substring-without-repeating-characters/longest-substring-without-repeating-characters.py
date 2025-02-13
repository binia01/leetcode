class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = max_length = 0
        char = set()

        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l +=1

            char.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length

        