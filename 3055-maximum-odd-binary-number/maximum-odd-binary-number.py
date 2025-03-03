class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        stt = list(s)
        stt.sort()
        l = 0
        r = l + 1
        while l < len(stt)-1 and r < len(stt)-1:
            if stt[l] == "0" and stt[r] == "0":
                r += 1
            else:
                stt[l], stt[r] = stt[r], stt[l]
                l+=1
        return "".join(stt)
            

        
        