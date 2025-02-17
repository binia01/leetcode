class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        ans =[0] * (n+1)
        
        for start, end , step in shifts:
            val = 1 if step == 1 else -1
            ans[start] += val
            ans[end+1] -= val

        for i in range(1, n+1):
            ans[i] += ans[i-1]
        string = list(s)
        for idx, char in enumerate(string):
            char = ord("a") + ((ord(char) - ord("a") + ans[idx]) % 26) 
            string[idx] = chr(char)
        return "".join(string)