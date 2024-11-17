class Solution:
    def maxPower(self, s: str) -> int:
        max_power, count = 1, 1
        i = 1
        while i < len(s):
            if s[i] == s[i-1]:
                count +=1
            else:
                count = 1
            i+=1
            max_power = max(max_power, count)
        return max_power 
        
        