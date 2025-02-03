class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            sr = s.split("@")
            return sr[0][0].lower() + "*****" + sr[0][-1].lower() + "@" + sr[-1].lower()
        else:
            sf = []
            for c in s:
                if c.isdigit():
                    sf.append(c)
            c = "".join(sf[len(sf)-4:])
            if len(sf) == 10:
                return "***-***-" + c
            elif len(sf) == 11:
                return "+*-***-***-" + c
            elif len(sf) == 12:
                return "+**-***-***-" + c
            else:
                return "+***-***-***-" + c

        
        



        