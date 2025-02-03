class Solution:
    def printVertically(self, s: str) -> List[str]:
        st = s.split(" ")
        _max = 0
        for word in st:
            _max = max(len(word), _max)
        ans = []
        for i in range(_max):
            string = []
            for word in st:
                if i < len(word):
                    string.append(word[i])
                else:
                    string.append(" ")
            ans.append("".join(string).rstrip())
        return ans