class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        b = list(s)
        count = []
        for i in range(len(b)):
            count.append([b[i], indices[i]])
        print(count)
        count.sort(key = lambda x: x[1])
        ans = ""
        for word in count:
            ans += word[0]
        return ans
        

        