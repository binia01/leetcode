class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        x = sum(shifts) % 26
        for i,c in enumerate(s):
            index = ord(c)- ord('a')
            ans.append(chr(ord('a') + (index+x)%26))
            x = (x - shifts[i])%26
        return ''.join(ans)
        