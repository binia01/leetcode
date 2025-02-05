class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        temp = "`".join(source)
        ans = []
        j = 0
        # print(ans)
        while j < len(temp):
            if j < len(temp)-1 and temp[j] == "/" and temp[j+1] =="*":
                j+=2
                while temp[j] + temp[j+1] != "*/":
                    j+=1
                j += 2
            elif j < len(temp)-1 and temp[j] + temp[j+1] == "//":
                j += 1
                while j < len(temp) and temp[j] != "`":
                    j+=1
                # j += 1
            else:
                ans.append(temp[j])
                j+=1
        res = []
        x = "".join(ans)
        y = x.split("`")
        for ch in y:
            if len(ch) != 0:
                res.append(ch)
        return res
                

       