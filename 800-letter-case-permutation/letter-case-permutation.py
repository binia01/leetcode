class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = [i for i, c in enumerate(s) if c.isalpha()]
        res = []
        n = len(letters)
        for mask in range(1 << n): 
            chars = list(s)
            for j in range(n):
                i = letters[j]
                chars[i] = chars[i].upper() if (mask & (1 << j)) else chars[i].lower()
            res.append(''.join(chars))
        return res
